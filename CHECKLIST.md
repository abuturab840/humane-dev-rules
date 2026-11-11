# Release checklist

Copy this list into your release notes or pull request and tick every item that applies (rule 48 in [RULES.md](RULES.md)). Nothing ships with an unticked item that applies.


**Humane**
- [ ] Consequence Scan done and top risks handled.
- [ ] Success measured by user benefit, not time spent.
- [ ] Non-essential notifications off; no autoplay; stopping points in feeds.
- [ ] Manipulation Matrix and regret test passed.
- [ ] Rewards earned and predictable; invites chosen by users; user controls in place; only real numbers and reviews.

**Private**
- [ ] Only necessary data collected; delete dates set.
- [ ] Cookie scan clean; "Reject all" equal to "Accept all" and working; GPC honoured where required.
- [ ] Users can access, export and delete their data.
- [ ] Privacy notice and cookie policy published.

**Secure**
- [ ] ASVS (or MASVS) level met; no open critical or high findings.
- [ ] Automatic scans passed: code, dependencies, secrets, configuration.
- [ ] Access control tested for every role.
- [ ] SBOM generated and release signed.
- [ ] security.txt live; incident and breach plans ready.
- [ ] Pen test done if this is a major launch.

**Fair and accessible**
- [ ] No dark patterns; cancel and delete as easy as sign-up.
- [ ] WCAG 2.2 AA passed, including keyboard and screen reader.
- [ ] Children's defaults on, if children may use it.

**Accountable**
- [ ] AI labelled where rule 36a/36b applies; AI media labelled.
- [ ] OWASP LLM checks and AI red-team passed.
- [ ] A person reviews AI decisions on money, health, jobs or legal matters.
- [ ] Reporting contacts live (illegal content, takedowns).
- [ ] Support period for updates stated.
- [ ] Release signed off by the release owner (and a second reviewer for major launches); result saved with the release.
