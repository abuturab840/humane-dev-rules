# Glossary

Plain explanations of the technical words in the rules. Each one says which rules use it. On the website, point at a rule number to see the rule.

**Accessibility statement** (rule 45). A page on your site saying how accessible it is, what you know doesn't work yet, and how people can contact you about problems.

**Argon2 and bcrypt** (rule 26). Ways of scrambling passwords before you store them, so that even if your database leaks, the real passwords can't easily be worked out.

**ASVS** (rule 22). The OWASP Application Security Verification Standard. A list of security checks for web apps, split into levels. Level 1 is the basics every app needs. Level 2 is for apps that hold personal or sensitive data.

**C2PA Content Credentials** (rule 37). A label stored inside an image, audio or video file that shows it was made or changed by AI.

**Consent banner** (rules 15 and 16). The pop-up asking visitors if they accept optional cookies. In the EU and UK, optional cookies can't load until the visitor says yes.

**Consequence Scan** (rule 2). A short meeting, or a quiet 15 minutes on your own, where you think through who your product could hurt and how, before you build it.

**Cookie scan** (rules 20 and 33). A check of every cookie and tracking script your site loads, so you know nothing runs without permission.

**Dark pattern** (rule 10). A design trick that pushes people into doing something they didn't mean to, like a hidden "Cancel" button or a pre-ticked box. Also called a deceptive pattern.

**DAST** (rule 33). Dynamic application security testing. A tool that attacks your live site the way a hacker would, to find holes. ZAP is a free example.

**Dependency** (rule 28). Code written by someone else that your project uses, like a library, package or WordPress plugin.

**DPIA** (rule 3). Data protection impact assessment. A written check of the privacy risks in a project, required by GDPR when you handle risky data.

**GPC (Global Privacy Control)** (rules 17 and 18). A setting in some browsers that tells websites "don't sell or share my data". Several US states require sites to respect it.

**"Do Not Sell or Share"** (rule 17). A link US privacy laws require on sites that sell or share personal data, so visitors can opt out.

**Lockfile** (rule 28). A file that records the exact version of every dependency, so your project doesn't silently pick up a new, possibly broken or malicious, version.

**Manipulation Matrix** (rule 55). Nir Eyal's test for habit-forming products. Ask two questions: would I use this myself, and does it really improve people's lives? Only build it if both answers are yes.

**MASVS** (rule 22). The OWASP Mobile Application Security Verification Standard. Like ASVS, but for mobile apps.

**MFA, passkeys and security keys** (rule 24). MFA means logging in with something more than a password. Passkeys and security keys are the strongest kind, because they can't be tricked by fake login pages.

**NIST SSDF** (rule 21). The US Secure Software Development Framework. A set of good habits for building software securely, from planning to release.

**OWASP** (rules 22 and 38). The Open Worldwide Application Security Project. A non-profit that publishes free security standards and guides.

**OWASP LLM Top 10** (rule 38). OWASP's list of the ten biggest security risks in apps that use AI language models, like prompt injection.

**Penetration test** (rule 34). Paying or asking a security expert to try to break into your product, so you can fix what they find.

**Red-team** (rule 42). Deliberately trying to make your AI misbehave, say harmful things or leak data, before real users do.

**Regret test** (rule 56). Nir Eyal's question: if people understood exactly how this feature works, would they regret using it? If yes, change it or remove it.

**SAST** (rule 32). Static application security testing. A tool that reads your code and flags common security mistakes. Semgrep is a free example.

**SBOM** (rule 29). Software bill of materials. A list of every dependency in a release and its version, like an ingredients label. CycloneDX and SPDX are the two common formats.

**SCA** (rule 32). Software composition analysis. A tool that checks your dependencies for known security holes. GitHub's Dependabot is a free example.

**Secrets manager** (rule 25). A safe place to store passwords and API keys, instead of writing them into your code.

**security.txt** (rule 46). A small file on your site at `/.well-known/security.txt` that tells security researchers how to report a problem to you.

**Session replay** (rule 18). A tool that records what visitors do on your site, like mouse movements and clicks, so you can watch it back. It can capture personal details, so it needs consent.

**Signature (signed release)** (rule 29). A digital stamp on a release that proves it came from you and wasn't changed along the way.

**Strictly necessary cookies** (rule 15). Cookies a site can't work without, like keeping someone logged in or remembering their basket. These don't need consent.

**Threat model** (rule 4). A simple list of what an attacker might want from your product, how they'd try to get it, and how you'll stop them.

**TLS** (rule 26). The encryption behind the padlock in the browser's address bar. It keeps data private on its way between the user and your server.

**WCAG 2.2 AA** (rule 44). The Web Content Accessibility Guidelines, the main standard for making sites usable by disabled people. AA is the level most laws ask for.

**Wellbeing measure** (rules 5 and 52). One number that shows your product is really helping people, like "tasks finished" or "problems solved", instead of time spent.
