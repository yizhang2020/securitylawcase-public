# Board Pack (FTC v. Drizly 2022)

> Use this to brief executives and counsel.

---

## Purpose

This board brief provides decision-useful context for FTC v. Drizly 2022: the July 2020 incident, the October 2022 consent order, root causes in IAM and secure development, and specific oversight decisions requested from directors. It is designed to help the board evaluate governance adequacy, remediation priority, and reporting cadence across legal, technical, and operational dimensions.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the FTC October 2022 consent order after the July 2020 Drizly breach **(time)**, the Chief Information Security Officer **(role)** prepares a board security brief **(type)** for Board Audit Committee **(audience)**.

<div class="writing-example-formal">

<p><strong>MEMORANDUM</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Board Audit Committee<br>
<strong>From: </strong>Chief Information Security Officer<br>
<strong>Date: </strong>November 15, 2022<br>
<strong>Subject: </strong>Board Security Brief — July 2020 Data Breach; FTC Decision and Order (Docket No. 2023185); Remediation Plan</p>
</div>

<p>This memorandum summarizes the July 2020 cybersecurity incident affecting approximately 2.5 million consumers, the Federal Trade Commission’s complaint and Decision and Order accepted October 24, 2022 (<em>In the Matter of Drizly, LLC, and James Cory Rellas</em>, FTC Docket No. 2023185), and the Company’s remediation and compliance program. The FTC did not impose a civil money penalty in this action; obligations are primarily injunctive and program-based, with individual duties on the CEO in future covered roles.</p>

<p><strong>Incident Summary: </strong>In July 2020, an attacker compromised an executive’s GitHub account through credential reuse from an unrelated breach. The executive retained access after a short-term need, without multifactor authentication. The attacker accessed repositories containing cloud and database credentials, entered the production environment, and exfiltrated a user table with personal information for more than 2.5 million consumers. The Company did not detect the breach internally initially; we learned of it from external reporting that data was offered for sale.
<br>
The FTC alleged unfair security practices and deception regarding safeguards described in public statements.</p>

<p><strong>Regulatory and Legal Outcomes: </strong>The consent order requires a comprehensive written information security program (coordinator, risk assessment, access controls, secure development, monitoring, vendor oversight), a published data retention schedule and minimization discipline, biennial independent assessments, and recordkeeping. CEO-specific obligations apply if he serves in a leadership role at another company meeting the order’s coverage thresholds. Management coordinates implementation with legal and compliance.</p>

<p><strong>Control Failures and Root Causes: </strong>The FTC’s complaint and our internal review identified:</p>

<ol>
  <li>Storage of cloud and database credentials in source repositories;</li>
  <li>Failure to enforce MFA and strong credential hygiene for GitHub and production administration paths;</li>
  <li>Failure to revoke or monitor temporary elevated access after the one-day event;</li>
  <li>Insufficient monitoring and detection for exfiltration and anomalous access;</li>
  <li>Absence of a formal minimization and retention program aligned to actual collection practices;</li>
  <li>Prior 2018 GitHub exposure of credentials without adequate sustained remediation.</li>
</ol>

<p>These areas are the focus of our remediation plan.</p>

<p><strong>Remediation and Order Compliance: </strong>The Company is implementing MFA for privileged and sensitive paths, secret scanning and pipeline blocking, access reviews and offboarding discipline, centralized logging with retention targets, detection engineering for crown-jewel data flows, a published retention schedule with deletion jobs, and biennial assessment procurement with FTC-ready reporting.</p>

<p><strong>Approval and Endorsement Requests: </strong>Management requests the Committee’s approval of the written program framework and retention schedule for publication; approval of budget for SIEM, secret-management tooling, and independent assessments; and endorsement of executive accountability metrics on MFA coverage, mean time to revoke access, and retention compliance sampling.</p>

<p>
Please let me know if additional information or further detail would be helpful.
</p>

<p>Respectfully submitted,</p>
Chief Information Security Officer
</div>

**Document-type guide:** [Board Security Brief](../../../../document-types/executive-board/board-security-brief.md)

**Writing tips:** [Writing best practices — Board Security Brief](../../../../studio/writing-best-practices.md#board-security-brief)
