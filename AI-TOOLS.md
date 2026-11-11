# Using these rules with AI tools

AI coding assistants read instruction files in your project. If you put these rules in one of those files, the assistant follows them while it writes code and can warn you before it breaks one.

This page shows you how to set that up for the common tools. If you don't use AI, you can skip it. The rules work the same way without it, as [how to use these rules](GUIDE.md) explains.

## Two things to know first

- **The AI can still get it wrong.** It may miss a rule or say something passes when it doesn't. A person still goes through the checklist and signs off each release.
- **Never paste secrets or personal data into an AI chat.** That means passwords, API keys, or your users' details (rule 25).

## Step 1: Put a copy of the rules in your project

Save [RULES.md](RULES.md) into your project, for example as `docs/humane-dev-rules.md`. You can download it from GitHub, or run this in your project folder:

```bash
mkdir -p docs
curl -o docs/humane-dev-rules.md https://raw.githubusercontent.com/abuturab840/humane-dev-rules/main/RULES.md
```

Your copy won't update by itself. Check back here now and then for changes.

## Step 2: Point your AI tool at it

Each tool reads a different file. Pick yours.

### Claude Code

Create a file called `CLAUDE.md` in your project's main folder (or open it if it's already there) and add:

```
@docs/humane-dev-rules.md
```

The `@` line tells Claude Code to read the rules file. To use the rules on every project on your computer, put the same line in `~/.claude/CLAUDE.md` instead, with the full path to your copy.

### Cursor

Create a file at `.cursor/rules/humane-dev-rules.mdc` with this at the top, then paste the rules underneath:

```
---
description: Humane Dev Rules
alwaysApply: true
---
```

### GitHub Copilot

Create a file at `.github/copilot-instructions.md` and paste the rules into it. Copilot reads this file for chat and code suggestions in that repository.

### Other tools

Many other assistants, including OpenAI's Codex, read a file called `AGENTS.md` in your project's main folder. Paste the rules in there. If your tool uses a different file, its documentation will say which.

### Chat assistants (Claude, ChatGPT and others)

If you plan in a chat app rather than in your code editor, add the rules file to a project's files or knowledge, so every chat in that project can see it. Or paste the rules at the start of a new chat.

## Step 3: Tell it how to use them

The rules alone aren't enough. Tell the assistant what to do with them. Paste this under the rules, in the same file:

```
How to use these rules:
- At the start of a new project or a big new feature, ask me the intake questions and tell me which "Only if" rules apply.
- If something I ask for would break a rule, tell me which rule and why, and ask me before you do it.
- Before a release, go through the release checklist. Mark each item pass, fail or n/a, with a short reason.
- Never put secrets in code or logs.
```

## Prompts you can use

Copy these into your assistant when you need them:

- "Answer the intake questions for this project from the code. Ask me about anything you can't tell."
- "Fill in the project template (TEMPLATE.md) for this project from the code. Leave a question for anything you can't tell."
- "Do a 15-minute Consequence Scan of this feature with me. What could go wrong, and for whom?"
- "Check this sign-up and cancel flow against rules 9, 10 and 56. Point out anything that could be a dark pattern."
- "Check our cookie banner against rules 15, 16 and 19."
- "Review this change for security problems. Check permissions (rule 23), secrets (rule 25) and dependencies (rule 28)."
- "Go through the release checklist for this release. Mark each item pass, fail or n/a, and explain any fail."

## If you're adding AI to your own product

That's a different thing from using AI to write code. If your product has AI features, such as a chatbot or AI-written replies, section F of the rules applies. It covers labelling AI, treating its input as untrusted, limiting what it can do, and testing it before launch (rules 36a to 42).
