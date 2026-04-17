# Board Pack (Capital One 2019)

> Use this to brief executives and counsel.

---

## Purpose

This board brief provides decision-useful context for Capital One 2019: incident and legal background, current security posture, material risk themes, and specific oversight decisions requested from directors. It is designed to help the board evaluate governance adequacy, remediation priority, and reporting cadence across legal, technical, and operational dimensions.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the 2019 Capital One cloud breach and related enforcement and litigation tracks **(time)**, the Chief Information Security Officer **(role)** prepares a board security brief **(type)** for Board Audit Committee **(audience)**.

<div class="writing-example-formal">

<p><strong>MEMORANDUM</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Board Audit Committee<br>
<strong>From: </strong>Chief Information Security Officer<br>
<strong>Date: </strong>September 10, 2020<br>
<strong>Subject: </strong>Board Security Brief — July 2019 Cybersecurity Incident; OCC Consent Order and Remediation Status</p>
</div>

<p>This memorandum provides a summary of the cybersecurity incident publicly disclosed on July 29, 2019, including its root causes, regulatory and legal outcomes, and the Company’s remediation and compliance status in response to the Consent Order issued by the Office of the Comptroller of the Currency (“OCC”) on August 6, 2020 (the “Consent Order”).</p>

<p><strong>Incident Summary: </strong>Between March and July 2019, an external actor exploited a misconfiguration in a web application firewall (WAF) protecting the Company’s AWS-hosted infrastructure. The actor obtained credentials and accessed customer data stored in the Company’s cloud environment.
<br>
The Company was notified by a security researcher on July 17, 2019, and confirmed unauthorized access on July 19, 2019. It secured the vulnerability, preserved forensic evidence, and notified federal law enforcement. An individual was arrested by the Federal Bureau of Investigation on July 29, 2019. The Company publicly disclosed the incident the same day, reporting that approximately 106 million individuals in the United States and Canada were affected.</p>

<p><strong>Regulatory and Legal Outcomes: </strong>The OCC investigated our cybersecurity and cloud governance practices and, on August 6, 2020, issued a Consent Order and imposed an $80 million civil money penalty. The Consent Order requires the Bank to strengthen risk management, board and management reporting, cloud security controls, and third-party risk management, and to report progress to the OCC. 
<br>
In addition, consumer class-action litigation was resolved by a settlement approved by the U.S. District Court for the Eastern District of Virginia in 2022 in the amount of $190 million, including consumer benefits and claims process.</p>

<p><strong>Control Failures and Root Causes: </strong>The OCC’s findings and our internal review identified the following control deficiencies:</p>

<ol>
  <li>Cloud perimeter and WAF configurations were not consistently managed as code with mandatory peer review, allowing misconfigurations to persist;</li>
  <li>Identity and access management (IAM) roles were over-permissioned, which enabled lateral movement following initial access;</li>
  <li>Logging and retention controls were insufficient to support timely detection and forensic readiness;</li>
  <li>Risk governance and board reporting did not meet the heightened supervisory expectations of the OCC.</li>
</ol>

<p>These areas are the focus of our remediation plan.</p>

<p><strong>Remediation and Consent Order Compliance: </strong>The Company has implemented, or is implementing, remediation measures to address these control gaps. Key actions include establishing configuration-as-code controls with drift detection for cloud boundaries, and conducting a comprehensive least-privilege review of identity and access management (IAM) roles. The Company is also implementing centralized logging with defined retention standards and introducing independent testing and validation of key controls. Progress against Consent Order requirements is tracked and reported to the OCC in accordance with the prescribed cadence.</p>

<p><strong>Approval and Endorsement Requests: </strong>In connection with these efforts, management requests the Committee’s approval of baseline control standards for cloud boundary security and identity and access management, approval of funding for logging infrastructure and drift detection capabilities, and endorsement of a governance requirement that all risk acceptances include defined review dates and formal mitigation tracking.</p>

<p>
Please let me know if additional information or further detail would be helpful.
</p>

<p>Respectfully submitted,</p>
Chief Information Security Officer
</div>

**Document-type guide:** [Board Security Brief](../../../../document-types/executive-board/board-security-brief.md)

**Writing tips:** [Writing best practices — Board Security Brief](../../../../studio/writing-best-practices.md#board-security-brief)
