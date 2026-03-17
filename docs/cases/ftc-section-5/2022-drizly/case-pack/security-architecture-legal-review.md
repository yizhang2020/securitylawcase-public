# Security Architecture Explanation for Legal Review (FTC v. Drizly 2022)

> Explain architecture and controls for counsel in connection with FTC order compliance or litigation.

---

## Purpose

A technical memo for General Counsel or outside counsel that explains: (1) architecture relevant to the breach (e.g., GitHub, AWS, production database); (2) how the attacker gained access (credential reuse, repository access, credentials in code); (3) controls now in place (MFA, no secrets in repos, monitoring, retention); (4) evidence available for regulator or discovery. Use precise, non-jargon language where possible; cite the FTC complaint and order for factual and remedial context.

---

## Hallucinated writing examples

**Scenario.** In November 2022, after the FTC accepted the consent order **(time)**, a Lead Security Engineer **(role)** provides a security architecture explanation for legal review **(type)** to the CISO **(audience)** to support counsel review, evidence readiness, and order compliance planning.

<div class="writing-example-formal">

<p><strong>MEMORANDUM</strong></p>

<div class="doc-meta">
<p><strong>To:</strong> Chief Information Security Officer<br>
<strong>From:</strong> Lead Security Engineer<br>
<strong>Date:</strong> November 18, 2022<br>
<strong>Subject:</strong> Security Architecture and Control Narrative — Incident Attack Path and Remediation Evidence</p>
</div>

<p>This memorandum summarizes the architecture implicated by the July 2020 incident, the attack path described in the FTC’s complaint, and the control and evidence changes required by the FTC’s Decision and Order (FTC Docket No. 2023185). The scenario is illustrative; the underlying facts and obligations are grounded in the FTC Complaint and Decision and Order.</p>

<p><strong>Architecture in scope.</strong> Drizly’s source code and configuration were maintained in GitHub repositories. Production services and data stores were hosted in Amazon Web Services, including a production database (e.g., Amazon RDS). Access to these environments was mediated through credentials and security settings managed in GitHub and AWS.</p>

<p><strong>Attack path (condensed).</strong> The FTC alleged that an attacker accessed an executive’s GitHub account using reused credentials, used that access to reach company repositories, obtained AWS and database credentials stored in those repositories, modified AWS security settings, and then accessed and exfiltrated the User Table containing personal information of approximately 2.5 million consumers. Drizly allegedly did not detect the breach internally and learned of it from external reporting.</p>

<p><strong>Control objectives and evidence (Order-driven).</strong><br>
1. <strong>IAM:</strong> enforce MFA and strong authentication for accounts with access to source code and production credentials; maintain access reviews and revocation records.<br>
2. <strong>Secrets management:</strong> prohibit secrets in repositories; continuous scanning; documented remediation and rotation workflows.<br>
3. <strong>Monitoring:</strong> logging coverage, retention, and detection for anomalous access and data exfiltration; investigation ticketing and outcomes.<br>
4. <strong>Data minimization:</strong> retention schedule publication; deletion or de-identification evidence for data no longer necessary.<br>
5. <strong>Program governance:</strong> documented program coordinator designation, written information security program, and assessment readiness.</p>

<p><strong>Evidence readiness.</strong> Evidence artifacts should include MFA enforcement logs, access review reports, secret scanning findings and closure, AWS security setting change records, log source inventories and retention configurations, retention schedule and deletion logs, and independent assessment engagement documentation.</p>

</div>

## Primary sources

- **FTC Complaint:** [In the Matter of Drizly, LLC, and James Cory Rellas](https://www.ftc.gov/system/files/ftc_gov/pdf/202-3185-Drizly-Complaint.pdf), FTC Docket No. 2023185 (Oct. 24, 2022).
- **FTC Decision and Order:** [Decision and Order](https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf), FTC Docket No. 2023185 (Oct. 24, 2022).
