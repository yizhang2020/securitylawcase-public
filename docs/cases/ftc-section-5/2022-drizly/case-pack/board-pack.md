# Board Pack (FTC v. Drizly 2022)

> Use this to brief executives and counsel.

---

## Purpose

Brief the board on the July 2020 breach, FTC Section 5 findings, and the October 2022 consent order: incident summary, root causes, program and retention obligations, and decisions on budget, assessments, and reporting. Supports oversight of consent-order compliance and residual risk.

---

## Hallucinated writing examples

**Scenario:** In November 2022, shortly after the Federal Trade Commission accepted the consent order in *In the Matter of Drizly, LLC, and James Cory Rellas* **(time)**, the Chief Information Security Officer **(role)** delivers a board security brief **(type)** to the Board Audit Committee **(audience)**. The brief summarizes the July 2020 data breach, root causes, the FTC’s findings, and the company’s plan to comply with the consent order. The audience is the board responsible for oversight of risk and compliance.

<div class="writing-example-formal">

<p><strong>MEMORANDUM</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Board Audit Committee<br>
<strong>From: </strong>Chief Information Security Officer<br>
<strong>Date: </strong>November 15, 2022<br>
<strong>Subject: </strong>Board Security Brief — July 2020 Data Breach; FTC Consent Order and Remediation Plan</p>
</div>

<p>This brief summarizes the cybersecurity incident that resulted in unauthorized access to and exfiltration of personal information of approximately 2.5 million consumers in July 2020, the root causes identified by the Federal Trade Commission and our internal review, the consent order accepted by the FTC on October 24, 2022, and the Company’s remediation and compliance plan. References: FTC Complaint and Decision and Order, <em>In the Matter of Drizly, LLC, and James Cory Rellas</em>, FTC Docket No. 2023185 (Oct. 24, 2022).</p>

<p><strong>Incident Summary: </strong>In July 2020, an attacker obtained access to an executive’s GitHub account through credential reuse (credentials from an unrelated breach). The executive had been granted access to the Company’s GitHub repositories for a one-day event; that access had not been revoked, and the account did not use multifactor authentication. The attacker used the compromised account to access repositories containing AWS and database credentials stored in source code. The attacker then accessed our production environment and exfiltrated the User Table containing more than 2.5 million consumer records. The Company did not detect the breach internally; we learned of it from external reports that customer data was offered for sale on dark web forums.</p>

<p><strong>Regulatory Outcome: </strong>The FTC investigated and alleged that our security practices were unfair and that certain public statements about security were deceptive under Section 5 of the FTC Act. The FTC did not impose a monetary penalty. The consent order requires us to implement a comprehensive information security program, publish and adhere to a data retention schedule, limit collection and retention of personal information, obtain biennial independent security assessments, and maintain specified reporting and recordkeeping. The order also imposes obligations on the CEO individually if he moves to another company that collects consumer data above a specified threshold.</p>

<p><strong>Root Causes and Control Gaps: </strong>The FTC’s complaint and our internal review identified: (1) storage of AWS and database credentials in GitHub repositories; (2) lack of multifactor authentication and strong password requirements for access to source code and production credentials; (3) failure to revoke or monitor access after the one-day event; (4) insufficient monitoring and detection of exfiltration and anomalous access; (5) no formal data retention schedule or deletion practice for unnecessary personal information; (6) prior incident in 2018 involving exposed credentials on GitHub without adequate follow-up controls. These areas are the focus of our remediation plan.</p>

<p><strong>Remediation and Consent Order Compliance: </strong>We are implementing or have implemented: (1) a written information security program with designated coordinator, risk assessment, access control and credential management (including MFA for all privileged and sensitive access), secure development practices (no credentials in code; repository scanning), monitoring and testing, and vendor oversight; (2) a published data retention schedule and process to delete or de-identify personal information when no longer necessary; (3) biennial independent third-party assessments and submission of reports to the FTC upon request. We request the Committee’s approval of the program framework, retention schedule, and budget for assessments and monitoring enhancements.</p>

</div>

**Document-type guide:** [Board Security Brief](../../../../document-types/executive-board/board-security-brief.md)

**Writing tips:** [Writing best practices — Board Security Brief](../../../../studio/writing-best-practices.md#board-security-brief)
