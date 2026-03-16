# Board Pack (Capital One 2019)

> Use this to brief executives and counsel.

---

## Hallucinated writing examples

**Scenario.** One month after the Office of the Comptroller of the Currency (OCC) issued its Consent Order and $80 million civil money penalty (August 6, 2020) **(time)**, the Chief Information Security Officer **(role)** is required to deliver a board security brief **(type)** to the Board Audit Committee **(audience)**. The brief must summarize the July 2019 cybersecurity incident, root causes, regulatory and legal outcomes, and progress against consent order commitments. The audience is the same board that will report to shareholders and the OCC.

<div class="writing-example-formal">

<p><strong>MEMORANDUM</strong></p>

<div class="doc-meta">
<p><strong>To:</strong> Board Audit Committee<br>
<strong>From:</strong> Chief Information Security Officer<br>
<strong>Date:</strong> September 10, 2020<br>
<strong>Subject:</strong> Board Security Brief — July 2019 Cybersecurity Incident; OCC Consent Order and Remediation Status</p>
</div>

<p>This brief summarizes the cybersecurity incident publicly disclosed on July 29, 2019, its root causes, the resulting regulatory and legal actions, and the Company’s remediation and compliance status in light of the Consent Order issued by the Office of the Comptroller of the Currency on August 6, 2020 (the “Consent Order”). References: OCC News Release NR 2020-98 (Aug. 6, 2020); <em>United States v. Paige A. Thompson</em>, U.S. District Court, W.D. Wash.; <em>In re Capital One Consumer Data Security Breach Litigation</em>, E.D. Va.</p>

<p><strong>Incident summary.</strong> Between March and July 2019, an external actor exploited a misconfiguration in a web application firewall (WAF) that secured our AWS-hosted infrastructure. The actor obtained credentials and accessed customer data stored in our cloud environment. On July 17, 2019, we were notified by a security researcher who had discovered references to the data online. We confirmed unauthorized access on July 19, 2019, secured the vulnerability, preserved forensic evidence, and notified federal law enforcement. On July 29, 2019, the Federal Bureau of Investigation arrested Paige Thompson in Seattle in connection with the breach. That same day, the Company publicly disclosed the incident, affecting approximately 106 million individuals in the United States and Canada.</p>

<p><strong>Regulatory and legal outcomes.</strong> The OCC investigated our cybersecurity and cloud governance practices and, on August 6, 2020, issued a Consent Order and imposed an $80 million civil money penalty. The Consent Order requires the Bank to strengthen risk management, board and management reporting, cloud security controls, and third-party risk management, and to report progress to the OCC. Consumer class-action litigation was resolved by a settlement approved by the U.S. District Court for the Eastern District of Virginia in 2022 in the amount of $190 million, including consumer benefits and claims process.</p>

<p><strong>Root causes and control gaps.</strong> The OCC’s findings and our internal review identified the following: (1) cloud perimeter and WAF configuration was not fully managed as code with mandatory peer review, allowing a misconfiguration to persist; (2) identity and access management (IAM) roles were over-permissioned, enabling lateral movement once initial access was obtained; (3) logging and retention were insufficient for timely detection and forensic readiness; (4) risk governance and board reporting did not meet the heightened standards expected by the OCC. These areas are the focus of our remediation plan.</p>

<p><strong>Remediation and consent order compliance.</strong> We have implemented or are implementing config-as-code and drift detection for perimeter controls, a least-privilege IAM review and reduction of over-permissioned roles, centralized logging with defined retention, and independent control testing. Consent order milestones are tracked and reported to the OCC on the required cadence. We request the Committee’s approval of baseline control standards for cloud boundaries and IAM, approval of funding for logging and drift detection, and a requirement that risk acceptances include revisit dates and mitigation tracking.</p>

</div>

---

## Official document (board-level security disclosure)

**SEC 10-K Item 1C — Cybersecurity** disclosures are the closest public analogue to a board security brief: they describe risk management, governance, and material risks for investors and are reviewed by the board.

- **Capital One 10-K (post-breach):** [Capital One Financial Corporation 10-K (2020)](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000927628&type=10-K&dateb=&owner=include&count=40) — open the latest 10-K and search for "Item 1C" or "Cybersecurity."
- **SEC guidance:** [SEC Disclosure Guidance on Cybersecurity](https://www.sec.gov/divisions/corpfin/guidance/cfguidance-topic2.htm) — how the SEC expects material cyber risks and incidents to be disclosed.

*Many companies do not publish standalone “board security briefs”; 10-K and proxy disclosures are the main public source of board-level security narrative.*

---

## Writing analysis

**How board-level security disclosure is typically structured (e.g. 10-K Item 1C)**

- **Risk management and strategy** — How the company identifies, assesses, and manages material cyber risks; use of frameworks (e.g. NIST); third-party and incident response programs.
- **Governance** — Board oversight (e.g. audit committee); who in management is responsible (CISO/CIO); frequency of reporting.
- **Material incidents** — If applicable, description of significant incidents, impact, and remediation.
- **Program elements** — Defense in depth, monitoring, identity/access, business continuity, third-party reviews, testing.

**What to emulate**

- One-page (or one-screen) summary for the board: incident + why it matters + key gaps + what we’re doing + how we’ll measure + decisions requested.
- Talk track so the presenter can stay consistent and on message.
- Explicit “decisions requested” so the board knows what is being asked.

**What to improve**

- Avoid jargon in the one-slide summary; use plain-language risk and metrics.
- Tie every “what we’re doing” to a measurable outcome or artifact (e.g. “PR-reviewed changes %” not just “config-as-code”).

---

## Sample rewrite

*Below is a board-pack style brief for the Capital One 2019 case: one-slide summary, talk track, and decisions requested. Use it as a template for your own briefings.*

---

## One-slide summary
- **Incident:** Major cloud-era breach with downstream regulatory enforcement and civil settlement impact.
- **Why it matters:** High scrutiny on *program effectiveness*, cloud configuration governance, and evidence readiness.
- **Key gaps to prevent:** boundary drift, over-permissioned IAM, insufficient logging/retention, weak risk governance.
- **What we’re doing:** config-as-code + drift detection + least privilege + centralized logging + independent testing.
- **How we’ll measure:** PR-reviewed changes %, drift MTTR, IAM wildcard count, log coverage %, audit finding closure time.

## Talk track (3 minutes)
1. This case shows outcomes depend on governance + proof, not only exploit mechanics.
2. Our focus is preventing boundary drift and proving control effectiveness continuously.
3. We will report quarterly metrics tied to evidence readiness and independent testing.

## Decisions requested
- Approve baseline control standards for cloud boundaries + IAM
- Fund logging/retention and drift detection improvements
- Require risk acceptance to include revisit dates and mitigation tracking

---

*End of sample rewrite. Adapt to your own context and get appropriate legal and leadership review before use.*
