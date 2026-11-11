# Humane Dev Rules

A free, plain-English set of rules for building websites, apps, software and AI that treat people well.

There are 60 short rules and a 24-point checklist you run before each release. You can use them, copy them and change them for your own work.

## Why this exists

I wanted one list I could follow on my own projects.

The advice on building things properly is spread over a lot of places: security standards, privacy laws in different countries, accessibility guidelines, and writing on ethics and design. Each one is useful. But nobody has time to read all of them before every project, and most small teams and solo developers never do.

So I went through them and turned them into one list. Each rule is a sentence or two. It says when it applies and what to do. Where a rule comes from a law or a standard, the [sources page](SOURCES.md) links to it.

## Why it matters

A lot of apps today are built to keep people hooked. Feeds that never end, pop-ups that guilt you into staying, cookie banners where "Reject" is hidden behind three clicks. These choices wear people down, and more and more of them now break the law in the EU, the UK and parts of the US.

Security has changed too. Attackers now go after the accounts, packages and tools developers use, not just the finished site. A small site with a weak admin login can still leak every customer's details.

AI makes both problems bigger. It writes code quickly, but it also repeats the same old mistakes and tricks, just faster.

You don't need a big team to avoid this. Most of it comes down to a few good habits, done every time. That's what these rules are.

## New to humane technology?

Start here. You don't need to know anything else first.

Humane technology means building things that respect people's time, attention, privacy and wellbeing, instead of using them up. The idea is pushed most by the [Center for Humane Technology](https://www.humanetech.com/), a non-profit started by people who used to work in big tech.

A simple way to think about it: if your users knew exactly how your product works and why it's designed that way, would they still be happy using it? If yes, you're probably on the right track. If you'd rather they didn't know, that's a warning sign.

These rules turn that idea into things you can actually check, along with the security, privacy and accessibility basics every product needs anyway.

If you want to read a bit more first:

- The Center for Humane Technology's [design principles](https://www.humanetech.com/humane-product-design) and their free [Foundations of Humane Technology course](https://www.humanetech.com/course).
- [Deceptive Patterns](https://deceptive.design/), a catalogue of the tricks to avoid, with real examples.
- The [glossary](GLOSSARY.md) in this repo, which explains every technical word used in the rules.

## How to use it

You don't need AI or any special tools. You need about ten minutes for the first read.

1. **Answer the [intake questions](INTAKE.md).** There are ten yes-or-no questions about your project, like "Do we collect personal data?" Your answers tell you which rules apply to you.
2. **Read the [rules](RULES.md) that apply.** Rules marked "Always" apply to every project. Rules marked "Only if" apply when your answers switch them on. A small brochure site follows around 30 rules. An app with accounts, payments and AI follows most of them.
3. **Keep them open while you build.** Check a section when you get to it, for example the privacy section when you add a contact form.
4. **Run the [checklist](CHECKLIST.md) before every release.** Copy it into your release notes, tick what's done and fix what isn't.

[How to use these rules](GUIDE.md) walks through each step with a real example, a small booking site, and there's a [project template](TEMPLATE.md) you can copy for your own projects.

## Using AI tools?

If you use an AI coding assistant such as Claude Code, Cursor or GitHub Copilot, you can give it these rules so it follows them while it writes code and warns you before it breaks one.

[Using these rules with AI tools](AI-TOOLS.md) has copy-and-paste setup for the common tools and some useful prompts. The checklist still needs a person to sign it off.

## What's in this repo

- [GUIDE.md](GUIDE.md): how to use the rules, step by step, with an example.
- [RULES.md](RULES.md): the 60 rules, in ten sections from "Starting a project" to "Healthy engagement".
- [INTAKE.md](INTAKE.md): the ten intake questions and which rules each one switches on.
- [CHECKLIST.md](CHECKLIST.md): the release checklist, ready to paste into a pull request.
- [TEMPLATE.md](TEMPLATE.md): a project template for your answers, risks, data and plans.
- [AI-TOOLS.md](AI-TOOLS.md): how to use the rules with AI coding assistants.
- [GLOSSARY.md](GLOSSARY.md): plain explanations of the technical words.
- [SOURCES.md](SOURCES.md): the standards, laws and research behind the rules.
- [CONTRIBUTING.md](CONTRIBUTING.md): how to suggest a fix or a new rule.

The same content is on the website: https://abuturab840.github.io/humane-dev-rules/

## Please note

This is a practical guide, not legal advice. Laws are different in each country and they change often. Some dates here come from law-firm summaries rather than the official texts. If you're launching in a regulated area like health, finance or children's products, check with a lawyer.

The fix times in rule 49 are a suggested policy based on common practice, not a legal rule.

Last reviewed: November 2026.

## Licence

[CC BY 4.0](LICENSE). You can share and change this work for any purpose, including paid work, as long as you give credit. For example:

> Based on "Humane Dev Rules" by abuturab840, https://github.com/abuturab840/humane-dev-rules, licensed under CC BY 4.0.

Found a mistake or have an idea? Please [open an issue](https://github.com/abuturab840/humane-dev-rules/issues).
