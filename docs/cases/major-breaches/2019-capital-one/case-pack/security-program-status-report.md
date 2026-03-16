# Security Program Status Report (Capital One 2019)

> Use this to report program health, key metrics, and progress to leadership; supports board and regulator questions on program maturity.

---

## Hallucinated writing examples

**Scenario.** In November 2019, approximately four months after the July 2019 breach disclosure and arrest of Paige Thompson **(time)**, the Lead Security Engineer **(role)** is required to submit a security program status report **(type)** to the Security Director and CISO **(audience)**. The report will be used for internal leadership and for early discussions with regulators. It must document what has been done since the incident, current metrics, and remaining gaps—all in the context of the Capital One AWS environment and the upcoming OCC examination.

<div class="writing-example-formal">

<p><strong>SECURITY PROGRAM STATUS REPORT</strong></p>

<div class="doc-meta">
<p><strong>To:</strong> Security Director, Chief Information Security Officer<br>
<strong>From:</strong> Lead Security Engineer, Cloud Security<br>
<strong>Date:</strong> November 15, 2019<br>
<strong>Reporting period:</strong> Post-incident remediation (July 2019–November 2019)</p>
</div>

<p><strong>Overview.</strong> This report summarizes the security program status following the July 2019 cybersecurity incident involving unauthorized access to customer data in our AWS-hosted infrastructure. The incident was disclosed on July 29, 2019; the individual responsible was arrested the same day (<em>United States v. Paige A. Thompson</em>, U.S. District Court, W.D. Wash.). This report covers remediation actions, current control state, and remaining work in the areas of cloud perimeter configuration, identity and access management (IAM), and logging and retention, which were identified as root causes or contributing factors.</p>

<p><strong>Incident context.</strong> The actor exploited a misconfiguration in a web application firewall (WAF) protecting our AWS environment, obtained credentials, and accessed data stored in our cloud storage. We have since fixed the vulnerable configuration, implemented additional monitoring, and preserved forensic evidence for law enforcement and potential regulatory or legal proceedings. Federal and state regulators have begun inquiries into our cybersecurity practices.</p>

<p><strong>Metrics and progress.</strong> Since July 2019 we have: (1) Enforced a mandatory peer-review workflow for all perimeter and WAF changes affecting production; approximately 78% of such changes in the reporting period went through the workflow (target 90% by Q1 2020). (2) Initiated an IAM least-privilege review; we have reduced the number of roles with broad or wildcard permissions by roughly 25% and are continuing the review. (3) Deployed centralized logging for designated AWS workloads and defined a 90-day retention standard for security-relevant logs. (4) Mapped control domains to evidence artifacts so we can produce an audit packet on short notice. Open high-risk findings from our internal review: 12 (down from 18 at the start of the period).</p>

<p><strong>Issues and next period.</strong> Drift detection for perimeter configuration is not yet fully deployed across all critical assets; we expect completion in Q1 2020. One control domain still lacks complete evidence mapping. Priorities for the next period: complete the IAM review, achieve 90% of perimeter changes via the approved workflow, close evidence gaps, and engage independent testing for control effectiveness. This report is prepared for internal use and in anticipation of regulatory and legal process.</p>

</div>

---

## Official document (program-level reporting)

There is no single public “security program status report” for Capital One; the **OCC consent order** and **10-K** describe required program elements and how the company reports on them. Consent orders often mandate periodic reporting to the board and regulator.

- **OCC Consent Order (2020):** [OCC Consent Order and Civil Money Penalty against Capital One](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html) — required board reporting, risk management, and control improvements; progress is reported to the OCC.
- **Capital One 10-K:** [Capital One 10-K](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000927628&type=10-K&dateb=&owner=include&count=40) — Item 1C describes governance, risk management, and program elements that align with status reporting.
- **NIST / CMMC:** Program status reports often map to framework maturity (e.g., NIST CSF, CMMC) for auditors and regulators.

*Program status reports are usually internal; consent orders and 10-K show what “program health” means to regulators and the board.*

---

## Writing analysis

**How program status reports are typically structured**

- **Overview** — Program mission and scope; reporting period.
- **Metrics** — KPIs/KRIs (e.g., incidents, vulnerabilities, control coverage, training).
- **Progress** — Initiatives completed, in progress, and planned.
- **Issues and blockers** — What is at risk and what is needed.
- **Next period** — Priorities and milestones.
- **Appendix** — Optional charts, framework alignment, or roadmap.

**What to emulate**

- Tie every metric to a data source (ticketing, assessments, audits) so the report is defensible.
- Show trend over time (e.g., open findings, control coverage) so leadership sees direction.
- Call out decisions needed (resources, scope, timeline) so the report drives action.

**What to improve**

- Avoid vanity metrics; prefer metrics that reflect control effectiveness and evidence readiness.
- Link “progress” to risk register and audit findings so regulators and counsel see a clear thread.

