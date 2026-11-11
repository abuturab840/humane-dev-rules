# The rules

60 rules for building safe, secure, private, accessible and humane software, apps, websites and AI.

- **Always** rules apply to every project.
- **Only if** rules switch on when the [intake questions](INTAKE.md) say they apply.

New here? Start with the [README](README.md). Not legal advice: see the [disclaimer](README.md#disclaimer).

## A. Starting a project
1. **Always.** Answer the intake questions: personal data? EU/UK users? US users? children? AI? payments? user posts? tracking? mobile app? sold in the EU?
2. **Always.** Consequence Scan before design: 15 minutes for small sites and features, up to an hour for products with personal data, children or AI. Write down the top risks and how each will be handled.
3. **Only if** we handle personal, health, biometric or payment data: do a privacy risk assessment (DPIA).
4. **Always.** Make a simple threat model: what attackers could target and how we'll block it.
5. **Always.** Choose one wellbeing measure per project. "Time spent" is never a goal.

## B. Humane design
6. **Only if** it sends notifications: off by default except essential ones; no red badges for marketing.
7. **Only if** it plays video or audio: no autoplay unless the user turns it on.
8. **Only if** it has a feed: natural stopping points; no infinite scroll for under-18s.
9. **Always.** Leaving is as easy as joining: cancel, reject and delete take the same effort as sign-up, accept and create.
10. **Always.** No dark patterns and no guilt-trip wording. Check screens against the Deceptive Patterns catalogue (deceptive.design).
11. **Only if** we rank content: reward helpful posts, not outrage.

## C. Privacy and cookies
12. **Always.** Collect only the data we need. Every data type gets a delete date.
13. **Only if** users have accounts: privacy settings are on by default.
14. **Only if** we hold personal data: users can access, export and delete it.
15. **Only if** there are EU/UK visitors and optional cookies or tags: nothing optional runs before consent.
16. **Only if** we show a consent banner: "Reject all" and "Accept all" sit side by side on the first screen and look the same.
17. **Only if** there are US visitors and we sell or share data or run targeted ads: honour Global Privacy Control and show "Do Not Sell or Share".
18. **Only if** there are US visitors and tracking: ad and analytics pixels follow rule 17. But there's no session replay or chat recording without notice and consent, and no ad pixels on sensitive pages (health, money, children's content, account areas).
19. **Only if** there are optional cookies: a settings link goes in every footer; each choice is remembered for 6 months.
20. **Only if** there are optional cookies or tags: run a cookie scan every quarter and after every new plugin or tag.

## D. Security
21. **Always.** Work to NIST's Secure Software Development Framework (SSDF, SP 800-218).
22. **Always.** Meet OWASP ASVS Level 1. **Only if** there's personal, health or payment data: Level 2. **Only if** it's a mobile app: also OWASP MASVS.
23. **Only if** users log in: check permissions on the server for every request, with access denied by default.
24. **Always.** Phishing-resistant MFA (passkeys or security keys) on all code, cloud and package accounts.
25. **Always.** No secrets in code or logs. Use a secrets manager and short-lived tokens.
26. **Always.** TLS 1.2+ everywhere. **Only if** we store passwords or sensitive data: hash with Argon2 or bcrypt, and encrypt at rest.
27. **Always.** Secure defaults: debug off, security headers on, unused features off.
28. **Always.** Few, well-maintained dependencies, with versions pinned in lockfiles.
29. **Always.** Every release gets an SBOM (CycloneDX or SPDX) and a signature.
30. **Always.** Lock down the build pipeline: isolated builds and manual approval for production.
31. **Only if** it takes payments: never store card data; use a payment provider.

## E. Testing
32. **Always.** Every code change is automatically scanned: code (SAST), dependencies (SCA), secrets and configuration.
33. **Always.** Every release gets a live security scan (DAST), an accessibility audit and a dark pattern review. **Only if** users log in: access control tests. **Only if** there's tracking: a cookie scan.
34. **Only if** it's a major launch, or a product has been live a year: a penetration test, a threat model review and a backup restore drill.
35. **Always.** Nothing ships with an open critical or high finding. Any exception needs a reason and an expiry date.

## F. AI features
36a. **Only if** users chat with AI or read replies it writes: show a small "AI" label, unless AI is already obvious (for example a "Generate with AI" button).
36b. **Only if** the AI has a human form (avatar, human name or voice): say clearly at the start that it's AI, make no "I feel" claims, and remind users during long chats.
37. **Only if** AI makes images, audio or video: label them with C2PA Content Credentials.
38. **Only if** there's AI: treat all AI input as untrusted; guard against the OWASP LLM Top 10.
39. **Only if** AI can take actions: give it the least power possible; a human approves spending, sending or deleting.
40. **Only if** AI affects money, health, jobs or legal matters: a person reviews its output.
41. **Only if** there's AI: no mood profiling and no emotional pressure to keep users engaged.
42. **Only if** there's AI: red-team it before launch and after major changes.

## G. Children and accessibility
43. **Only if** children might use it: the strictest defaults. No profiling, location off, parental consent where required, no addictive features.
44. **Always.** WCAG 2.2 AA, tested with keyboard and screen reader.

## H. Launch
45. **Always.** An accessibility statement. **Only if** there's personal data: a privacy notice. **Only if** there are cookies: a cookie policy. **Only if** there are accounts or payments: terms with clear cancellation.
46. **Always.** A security.txt file and a vulnerability disclosure policy.
47. **Only if** it's an app or software product (not just a website): state how long we'll provide security updates.
48. **Always.** The release owner goes through the [release checklist](CHECKLIST.md) and saves the result with the release. For major launches, a second person reviews it (working solo? re-check it the next day with fresh eyes).

## I. After launch
49. **Always.** Fix actively exploited flaws within 72 hours, critical within 7 days, high within 30, medium within 90.
50. **Always.** Keep an incident plan. **Only if** there's personal data: keep a breach plan (72h).
51. **Only if** there's personal data: answer data requests within 1 month. **Only if** there are user posts: remove reported intimate images within 48 hours.
52. **Always.** Check the wellbeing measure every month and fix whatever is hurting users.
53. **Always.** Every quarter, review access and remove old accounts and keys. Every year, refresh the risk notes and threat model, and run an incident drill and a law check.
54. **Always.** After any incident, write a short note covering what happened, why, and what changed, and track each fix until it's done.

## J. Healthy engagement
55. **Always.** Pass the Manipulation Matrix: only build what we'd use ourselves and what truly improves users' lives.
56. **Always.** Apply the regret test in every dark pattern review. If users would regret a feature once they understood it, remove it.
57. **Only if** it has rewards or gamification: rewards are earned and predictable; no random rewards designed to compel use.
58. **Only if** users can invite others: they choose each person; never send automatic invites from uploaded contacts; rate-limit invites.
59. **Only if** it's used regularly: give users controls such as quiet hours, a daily limit, snooze and optional usage summaries.
60. **Only if** we show numbers or reviews: only real, current figures and genuine reviews; no fake urgency or scarcity.
