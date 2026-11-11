"""Build the Humane Dev Rules website into docs/ from the Markdown files.

Usage (from the repo root):
    python3 -m venv .venv
    .venv/bin/pip install -r tools/requirements.txt
    .venv/bin/python tools/build_site.py
"""
import html
import pathlib
import re
import shutil

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
REPO = "https://github.com/abuturab840/humane-dev-rules"
SITE = "https://abuturab840.github.io/humane-dev-rules/"

# (source, output, nav label, kicker, lead). A lead of None takes the first paragraph.
PAGES = [
    ("README.md", "index.html", "Home", "A free starting guide", None),
    ("GUIDE.md", "guide.html", "How to use", "Start here", "A step-by-step guide for anyone, with or without AI, and a worked example."),
    ("RULES.md", "rules.html", "Rules", "60 rules in ten sections", "Short rules for building websites, apps, software and AI that treat people well."),
    ("INTAKE.md", "intake.html", "Intake", "Step 1", "Ten yes-or-no questions that tell you which rules apply to your project."),
    ("CHECKLIST.md", "checklist.html", "Checklist", "Before every release", "24 checks to run before you ship. Copy them into your release notes."),
    ("TEMPLATE.md", "template.html", "Template", "Copy and fill in", "One place to record your answers, risks, data and plans for each project."),
    ("AI-TOOLS.md", "ai-tools.html", "AI tools", "For AI users", "How to give these rules to Claude Code, Cursor, GitHub Copilot and other assistants."),
    ("GLOSSARY.md", "glossary.html", "Glossary", "Words explained", "Plain explanations of every technical word in the rules."),
    ("SOURCES.md", "sources.html", "Sources", "Where the rules come from", "The standards, laws and research behind each rule."),
    ("CONTRIBUTING.md", "contributing.html", None, "Help improve it", "How to suggest a fix, a new rule or a translation."),
    ("ACCESSIBILITY.md", "accessibility.html", None, "About this site", "How this site meets the accessibility rules it asks of everyone else."),
]
LINKS = {src: out for src, out, *_ in PAGES}
LINKS["LICENSE"] = REPO + "/blob/main/LICENSE"

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='8' fill='%23E2262D'/%3E"
           "%3Ctext x='16' y='23' font-family='Arial Black,Arial,sans-serif' font-size='19' font-weight='900' "
           "text-anchor='middle' fill='white'%3EH%3C/text%3E%3C/svg%3E")


def load_rules():
    """Map each rule number to its plain text, for the hover popups."""
    rules = {}
    for line in (ROOT / "RULES.md").read_text().splitlines():
        m = re.match(r"^(\d+[ab]?)\. (.*)$", line)
        if m:
            text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", m.group(2))
            rules[m.group(1)] = re.sub(r"\*\*|\*", "", text)
    return rules


RULES = load_rules()
SKIP_TAGS = {"a", "pre", "code", "h1", "h2", "h3", "title", "script", "style"}


def add_rule_refs(body):
    """Turn "rule 14" in running text into a link with a small popup showing the rule."""
    counter = [0]

    def chip(num):
        if num not in RULES:
            return num
        counter[0] += 1
        tid = f"tip-{counter[0]}"
        return (f'<span class="ref"><a href="rules.html#rule-{num}" aria-describedby="{tid}">{num}</a>'
                f'<span class="tip" role="tooltip" id="{tid}"><b>Rule {num}.</b> {html.escape(RULES[num])}</span></span>')

    def refs(m):
        return m.group(1) + " " + re.sub(r"\d+[ab]?", lambda n: chip(n.group(0)), m.group(2))

    pattern = re.compile(r"\b([Rr]ules?) (\d+[ab]?(?:(?:, | and | to | or )\d+[ab]?)*)")
    out, depth = [], 0
    for part in re.split(r"(<[^>]+>)", body):
        tag = re.match(r"<(/?)([a-zA-Z0-9]+)", part)
        if tag and tag.group(2).lower() in SKIP_TAGS:
            depth += -1 if tag.group(1) else 1
        elif not part.startswith("<") and depth == 0:
            part = pattern.sub(refs, part)
        out.append(part)
    return "".join(out)


def fix_links(body):
    def repl(m):
        target, frag = m.group(1), m.group(2) or ""
        return f'href="{LINKS[target]}{frag}"' if target in LINKS else m.group(0)
    return re.sub(r'href="([A-Za-z-]+\.md|LICENSE)(#[^"]*)?"', repl, body)


def rules_list(md_text):
    """Turn numbered rule lines into one HTML list per section, with tag pills."""
    out, buf = [], []

    def flush():
        if buf:
            items = []
            for num, text in buf:
                inner = markdown.markdown(text).removeprefix("<p>").removesuffix("</p>")
                items.append(f'<li id="rule-{num}"><span class="rn" aria-hidden="true">{num}</span><div><span class="sr">Rule&#160;{num}. </span>{inner}</div></li>')
            out.append('<ol class="rules">\n' + "\n".join(items) + "\n</ol>\n")
            buf.clear()

    for line in md_text.splitlines():
        m = re.match(r"^(\d+[ab]?)\. (.*)$", line)
        if m:
            buf.append(m.groups())
        else:
            flush()
            out.append(line + "\n")
    flush()
    return "".join(out)


def decorate(body, src):
    # Tag pills for Always / Only if.
    body = re.sub(r"<strong>Always\.?</strong>", '<span class="tag t-always">Always</span>', body)
    body = re.sub(r"<strong>Only if</strong>", '<span class="tag t-onlyif">Only if</span>', body)
    # Checklist items become real checkboxes (nothing is saved).
    if "[ ] " in body:
        body = re.sub(r"<ul>\n(<li>\[ \] )", r'<ul class="check">\n\1', body)
        body = re.sub(r"<li>\[ \] (.*?)</li>", r'<li><label><input type="checkbox"> <span>\1</span></label></li>', body)
    # Tables scroll inside their own box on small screens.
    body = body.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    # Section pills: "A. Title" and "Step 1: Title" get a pill; otherwise number them, or a red bar on step pages.
    has_steps = bool(re.search(r"<h2[^>]*>Step \d+:", body))
    count = 0

    def h2(m):
        nonlocal count
        attrs, text = m.group(1), m.group(2)
        letter = re.match(r"([A-J])\. (.*)", text)
        step = re.match(r"Step (\d+): (.*)", text)
        if letter:
            return f'<span class="pill" aria-hidden="true">{letter.group(1)}</span>\n<h2{attrs}><span class="sr">{letter.group(1)}. </span>{letter.group(2)}</h2>'
        if step:
            return f'<span class="pill" aria-hidden="true">Step {step.group(1)}</span>\n<h2{attrs}><span class="sr">Step {step.group(1)}: </span>{step.group(2)}</h2>'
        if has_steps:
            return f'<span class="bar" aria-hidden="true"></span>\n<h2{attrs}>{text}</h2>'
        count += 1
        return f'<span class="pill" aria-hidden="true">{count:02d}</span>\n<h2{attrs}>{text}</h2>'

    body = re.sub(r"<h2([^>]*)>(.*?)</h2>", h2, body)
    # The paragraph right after a rules section heading is its intro.
    if src == "RULES.md":
        body = re.sub(r"(</h2>\n)<p>", r'\1<p class="intro">', body)
    return body


def page(src, out_name, kicker, lead):
    text = (ROOT / src).read_text()
    title = re.match(r"# (.+)", text).group(1)
    text = re.sub(r"\A# .+\n+", "", text)
    if lead is None:
        first, text = text.split("\n\n", 1)
        lead = re.sub(r"\*\*|\*", "", first)
    if src == "RULES.md":
        text = rules_list(text)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"])
    body = add_rule_refs(decorate(fix_links(md.convert(text)), src))

    nav = []
    for s, o, label, *_ in PAGES:
        if label:
            cur = ' aria-current="page"' if o == out_name else ""
            nav.append(f'<li><a href="{o}"{cur}>{label}</a></li>')
    page_title = "Humane Dev Rules" if out_name == "index.html" else f"{title} | Humane Dev Rules"
    canonical = SITE if out_name == "index.html" else SITE + out_name
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{html.escape(page_title)}</title>
<meta name="description" content="{html.escape(lead)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(page_title)}">
<meta property="og:description" content="{html.escape(lead)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="assets/site.css">
<script src="assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="cover">
  <div class="inner">
    <div class="topbar">
      <a class="wordmark" href="index.html">Humane Dev Rules</a>
      <nav aria-label="Main"><ul>{"".join(nav)}</ul></nav>
    </div>
    <p class="kicker">{html.escape(kicker)}</p>
    <h1>{html.escape(title)}</h1>
    <p class="lead">{html.escape(lead)}</p>
    <div class="slit"></div>
  </div>
</header>
<main class="wrap" id="main">
{body}
</main>
<footer class="foot">
  <div class="inner">
    <a class="wordmark" href="index.html">Humane Dev Rules</a>
    <p>By abuturab840. Free to reuse under <a href="{LINKS['LICENSE']}">CC BY 4.0</a>. Not legal advice. Last reviewed November 2026.</p>
    <p><a href="{REPO}">View on GitHub</a> &middot; <a href="contributing.html">Contribute</a> &middot; <a href="accessibility.html">Accessibility</a> &middot; <a href="{REPO}/issues">Report a problem</a></p>
    <p>This site uses no cookies and no tracking.</p>
  </div>
</footer>
</body>
</html>
"""


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets" / "fonts").mkdir(parents=True)
    (OUT / ".well-known").mkdir()
    shutil.copy(ROOT / "tools" / "site.css", OUT / "assets" / "site.css")
    shutil.copy(ROOT / "tools" / "site.js", OUT / "assets" / "site.js")
    for f in (ROOT / "tools" / "fonts").iterdir():
        shutil.copy(f, OUT / "assets" / "fonts" / f.name)
    (OUT / ".nojekyll").write_text("")
    (OUT / ".well-known" / "security.txt").write_text(
        f"Contact: {REPO}/issues\nExpires: 2027-11-01T00:00:00.000Z\nPreferred-Languages: en\n"
        f"Canonical: {SITE}.well-known/security.txt\n")
    for src, out_name, _label, kicker, lead in PAGES:
        result = page(src, out_name, kicker, lead)
        assert "—" not in result, f"em dash in {src}"
        (OUT / out_name).write_text(result)
        print("built", out_name)


if __name__ == "__main__":
    main()
