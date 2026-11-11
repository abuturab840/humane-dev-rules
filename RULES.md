# The rules

Every rule has one of two labels:

- **Always** rules apply to every project, even a small one.
- **Only if** rules apply when the condition is true for your project. The [intake questions](INTAKE.md) help you work out which ones those are.

Some rules have an "Always" part and an "Only if" part. For example, rule 22 asks every project for the basic security level, and a higher level only if you hold personal data.

If a word is new to you, the [glossary](GLOSSARY.md) explains it. If you're not sure how to start, read [how to use these rules](GUIDE.md) first. This isn't legal advice.

## A. Starting a project

Do these before you design anything. They take less time than you think and they save you from building the wrong thing.

1. **Always.** Answer the ten [intake questions](INTAKE.md) before you start. They ask things like "Does your product collect personal data?", "Could children use it?" and "Does it use AI?". Your answers show which "Only if" rules apply to you.
2. **Always.** Before you design anything, think through who your product could harm and how. This is called a Consequence Scan. Fifteen minutes is enough for a small site or feature. Give it up to an hour if the product handles personal data, could be used by children or uses AI. Write down the biggest risks and how you'll deal with each one.
3. **Only if** you handle personal data, especially health, biometric or payment data: write down the privacy risks and how you'll reduce them before you build. This is called a privacy risk assessment (DPIA).
4. **Always.** Make a simple threat model. Write down what an attacker might want from your product, like customer data or admin access, and how you'll stop them.
5. **Always.** Pick one number that shows your product is really helping people, and track it. "Time spent in the app" is never the goal.

## B. Humane design

How the product treats people's attention and choices.

6. **Only if** your product sends notifications: keep them off by default, except essential ones like security alerts or booking reminders. Never use red badges to push marketing.
7. **Only if** your product plays video or audio: don't play it automatically unless the user turns that on.
8. **Only if** your product has a feed: give it natural stopping points, like "You're all caught up". Never use endless scrolling for anyone under 18.
9. **Always.** Make leaving as easy as joining. Cancelling, saying no and deleting an account should take no more effort than signing up, saying yes or creating one.
10. **Always.** Don't use dark patterns, the design tricks that push people into things they didn't mean to do, and don't use guilt-trip wording like "No thanks, I don't like saving money". Check your screens against the examples at deceptive.design.
11. **Only if** your product ranks or recommends posts: reward the helpful ones, not the ones that make people angry.

## C. Privacy and cookies

What data you collect, how long you keep it, and how you ask for consent.

12. **Always.** Only collect the data you really need, and decide when each type of data will be deleted.
13. **Only if** users have accounts: set every privacy option to the most private choice by default.
14. **Only if** you hold personal data: let people see their data, download it and delete it.
15. **Only if** you have visitors from the EU or UK and use optional cookies or tracking tags: don't load anything optional until the visitor says yes.
16. **Only if** you show a cookie banner: put "Reject all" and "Accept all" side by side on the first screen, looking exactly the same.
17. **Only if** you have visitors from the US and you sell or share their data or run targeted ads: respect Global Privacy Control, a browser setting that says "don't sell my data", and show a "Do Not Sell or Share" link.
18. **Only if** you have visitors from the US and use tracking: ad and analytics pixels follow rule 17. But never record visitors' screens (session replay) or chats without telling them and asking first, and never put ad pixels on sensitive pages, like health, money, children's or account pages.
19. **Only if** you use optional cookies: put a cookie settings link in every footer, and remember each visitor's choice for six months.
20. **Only if** you use optional cookies or tags: check every cookie your site sets every three months, and again whenever you add a plugin or tag.

## D. Security

How you protect your users, your code and your accounts.

21. **Always.** Follow the good habits in NIST's Secure Software Development Framework (SSDF), a free US guide to building software securely.
22. **Always.** Meet level 1 of OWASP's security checklist for apps (ASVS). **Only if** you hold personal, health or payment data: meet level 2. **Only if** it's a mobile app: also meet OWASP's mobile checklist (MASVS).
23. **Only if** users log in: check on the server, every time, that the person is allowed to do what they're asking. When in doubt, the answer is no.
24. **Always.** Protect every account that touches your code, hosting or packages with a login that can't be phished, like passkeys or security keys.
25. **Always.** Never put passwords, keys or other secrets in your code or logs. Keep them in a secrets manager and use tokens that expire quickly.
26. **Always.** Encrypt all traffic with TLS 1.2 or newer, the padlock in the browser. **Only if** you store passwords or sensitive data: scramble passwords with Argon2 or bcrypt, and encrypt the data you store.
27. **Always.** Make the safe setting the default: debug mode off, security headers on, and any features you don't use switched off.
28. **Always.** Use as few outside packages and plugins as you can, pick well-maintained ones, and lock their versions in a lockfile.
29. **Always.** Give every release an SBOM, a list of everything inside it in CycloneDX or SPDX format, and a digital signature.
30. **Always.** Lock down how you build and deploy. Build in a clean, separate environment, and have a person approve every release to production.
31. **Only if** you take payments: never store card details yourself. Use a payment provider.

## E. Testing

The checks that prove the rules above are actually working.

32. **Always.** Scan every code change automatically: the code itself (SAST), the packages it uses (SCA), and for leaked secrets and unsafe settings.
33. **Always.** Before every release, run a security scan on the live site (DAST), an accessibility check and a dark pattern review. **Only if** users log in: also test that each type of user can only reach what they should. **Only if** you use tracking: also check your cookies.
34. **Only if** it's a big launch, or the product has been live for a year: get a penetration test, where an expert tries to break in. Also review your threat model and practise restoring from a backup.
35. **Always.** Never ship with a known critical or high security problem. If you really must make an exception, write down why and the date it runs out.

## F. AI features

Only for products that use AI. Skip this section if yours doesn't.

36a. **Only if** users chat with AI or read replies it writes: show a small "AI" label, unless that's already obvious, for example on a "Generate with AI" button.
36b. **Only if** your AI has a human form, like a face, a human name or a voice: say clearly at the start that it's AI, never let it claim to have feelings, and remind users during long chats.
37. **Only if** your AI makes images, audio or video: label them with C2PA Content Credentials, a tag inside the file that shows AI made it.
38. **Only if** you use AI: treat everything that goes into the AI as untrusted, and guard against the risks in OWASP's Top 10 for AI apps (the LLM Top 10).
39. **Only if** your AI can take actions: give it as little power as possible, and have a person approve anything that spends money, sends messages or deletes things.
40. **Only if** your AI's answers affect money, health, jobs or legal matters: have a person check them.
41. **Only if** you use AI: don't track people's moods, and don't use emotional pressure to keep them using it.
42. **Only if** you use AI: try hard to make it misbehave before launch and after any big change. This is called red-teaming.

## G. Children and accessibility

Making sure the product is safe for young people and usable by everyone, including disabled people.

43. **Only if** children might use it: use the safest settings by default. No profiling, location off, parental consent where the law needs it, and no addictive features.
44. **Always.** Meet the WCAG 2.2 AA accessibility standard, and test it using only a keyboard and with a screen reader.

## H. Launch

What needs to be in place on the day you go live.

45. **Always.** Publish an accessibility statement. **Only if** you hold personal data: publish a privacy notice. **Only if** you use cookies: publish a cookie policy. **Only if** you have accounts or payments: publish terms that explain clearly how to cancel.
46. **Always.** Publish a security.txt file and a short page explaining how people can report security problems to you.
47. **Only if** it's an app or software people install, not just a website: say how long you'll keep releasing security updates.
48. **Always.** The person doing the release goes through the [release checklist](CHECKLIST.md) and saves the result with the release. For big launches, a second person checks it too. Working alone? Check it again the next day with fresh eyes.

## I. After launch

Keeping the product safe once people are using it.

49. **Always.** Fix security problems quickly: within 72 hours if they're being actively attacked, 7 days if critical, 30 days if high and 90 days if medium.
50. **Always.** Have a plan for security incidents. **Only if** you hold personal data: also have a plan for data breaches, including reporting them within 72 hours where the law requires it.
51. **Only if** you hold personal data: answer people's requests about their data within a month. **Only if** users can post content: remove reported intimate images within 48 hours.
52. **Always.** Check your wellbeing number from rule 5 every month, and fix whatever is hurting people.
53. **Always.** Every three months, check who has access and remove old accounts and keys. Every year, update your risk notes and threat model, practise your incident plan and check for new laws.
54. **Always.** After any incident, write a short note covering what happened, why, and what you changed. Track each fix until it's done.

## J. Healthy engagement

How to make a product people want to come back to, without hooking them. Rules 55 and 56 come from Nir Eyal's own ethics tests in *Hooked*.

55. **Always.** Pass the Manipulation Matrix: only build something if you'd use it yourself and it truly makes people's lives better.
56. **Always.** In every dark pattern review, ask the regret test question: would people regret using this feature if they understood how it works? If yes, remove it.
57. **Only if** your product has rewards, points or badges: make rewards earned and predictable. No random rewards designed to keep people hooked.
58. **Only if** users can invite others: let them choose each person. Never send automatic invites from uploaded contact lists, and limit how many invites can be sent.
59. **Only if** people use your product regularly: give them controls like quiet hours, a daily limit, snooze and optional usage summaries.
60. **Only if** you show numbers or reviews: show only real, current figures and genuine reviews. No fake urgency like "Only 2 left!" unless it's true.
