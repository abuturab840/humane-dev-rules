# Humane Dev Rules

**60 practical rules and a 24-point release checklist for building software, apps, websites and AI that are safe, secure, private, accessible and humane.**

Free to use, copy and adapt under [CC BY 4.0](LICENSE).

## Why this exists

Good engineering, good ethics and the law now point the same way:

- **Ethics.** The [Center for Humane Technology](https://www.humanetech.com/) warns that products built to grab attention end up harming the people who use them, and that AI is repeating the pattern.
- **Law.** Regulators are turning those ideas into rules: the EU's GDPR, Digital Services Act, AI Act and Cyber Resilience Act, US FTC enforcement and COPPA, and a growing list of US state privacy and AI laws.
- **Security.** Attackers now go after how software is built, not just the finished product. The 2025 OWASP Top 10 added software supply chain failures at number three.

These rules turn all of that into a short list a team can actually follow.

## The five pillars

| Pillar | What it means |
|---|---|
| **Humane** | Respect attention and psychology. Measure success by real benefit, not time spent. |
| **Private** | Collect the least data, keep privacy on by default, ask for real consent. |
| **Secure** | Secure by design and by default, kept secure for the product's whole life. |
| **Fair and accessible** | No tricks. Usable by everyone, including disabled people. Extra care for children. |
| **Accountable** | Say when it's AI. Keep humans in charge of big decisions. Own the harm we cause. |

## How to use it

1. **Start a project with the [intake questions](INTAKE.md).** Each "yes" switches on the rules that apply, so a small static site doesn't carry the rules for AI or children's products.
2. **Follow the [rules](RULES.md)** while you design, build and test.
3. **Tick the [release checklist](CHECKLIST.md)** before every release.
4. **Keep going after launch.** The last section of the rules covers patching, incidents and monthly checks.

You can also hand the rules to an AI coding assistant. For example, add `RULES.md` to your project's instructions file so the assistant follows them.

## What's inside

| File | What it is |
|---|---|
| [RULES.md](RULES.md) | The 60 rules, grouped A to J, each marked **Always** or **Only if** |
| [INTAKE.md](INTAKE.md) | Ten intake questions and the rules each one switches on |
| [CHECKLIST.md](CHECKLIST.md) | The 24-point release checklist, ready to paste into a pull request |
| [SOURCES.md](SOURCES.md) | The standards, laws and research the rules are based on |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to suggest fixes and improvements |

## A taste of the rules

- **9.** Leaving is as easy as joining: cancel, reject and delete take the same effort as sign-up, accept and create.
- **16.** "Reject all" and "Accept all" sit side by side on the first screen and look the same.
- **24.** Phishing-resistant MFA (passkeys or security keys) on all code, cloud and package accounts.
- **29.** Every release gets an SBOM and a signature.
- **36a.** Users who chat with AI see a small "AI" label.
- **56.** If users would regret a feature once they understood it, remove it.
- **49.** Fix actively exploited flaws within 72 hours, critical within 7 days.

## Disclaimer

This is a practical guide, **not legal advice**. Laws differ by country and change often; several dates here come from law-firm summaries rather than official texts. Check with a qualified lawyer before launching products in regulated markets. Fix-time targets (rule 49) are a suggested policy based on common industry practice, not a legal rule.

Last reviewed: November 2026.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may share and adapt this work for any purpose, including commercial use, as long as you give credit:

> Based on "Humane Dev Rules" by abuturab840, https://github.com/abuturab840/humane-dev-rules, licensed under CC BY 4.0.
