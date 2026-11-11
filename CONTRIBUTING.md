# Contributing

Suggestions are welcome, especially:

- **Law changes.** A date moved, a new law passed, or a summary that's wrong. Please link the official source.
- **Clearer wording.** Rules should be short, plain and testable.
- **Better tools or standards** behind a rule.
- **Translations.**

## How

1. Open an issue describing the change and why, with a source link if it's about law or a standard.
2. Or send a pull request. Keep each pull request to one topic.

## Style

- One rule, one idea. Aim for a single sentence.
- Mark every rule **Always** or **Only if**, with the condition.
- Plain English. Explain any acronym the first time it appears.
- No product endorsements unless the tool is free or a recognised standard.

## The website

The website in the `docs` folder is built from the Markdown files in this repo, so please edit the `.md` files, not the HTML. To rebuild it:

```bash
python3 -m venv .venv
.venv/bin/pip install -r tools/requirements.txt
.venv/bin/python tools/build_site.py
```

By contributing, you agree your contribution is licensed under [CC BY 4.0](LICENSE).
