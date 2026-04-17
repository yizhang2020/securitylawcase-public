# Board Pack (SEC v. SolarWinds Corp. et al.)

> Use this to brief executives and counsel.

---

## Purpose

This board brief provides decision-useful context for the SUNBURST supply-chain incident, SEC enforcement alleging disclosure and controls issues, subsequent motion practice and stipulated dismissal, and ongoing technical and governance lessons. It is designed to help the board evaluate governance adequacy, remediation priority, and reporting cadence across legal, technical, and operational dimensions.

## Hallucinated writing examples

**Scenario:** In an illustrative period after the SEC filed its October 2023 complaint and after later dismissal on stipulated terms **(time)**, the Chief Information Security Officer **(role)** prepares a board security brief **(type)** for Board Audit Committee **(audience)**.

<div class="writing-example-formal">

<p><strong>MEMORANDUM</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Board Audit Committee<br>
<strong>From: </strong>Chief Information Security Officer<br>
<strong>Date: </strong>January 15, 2025<br>
<strong>Subject: </strong>Board Security Brief — SUNBURST; SEC Civil Action; Stipulated Dismissal (LR-26423); Build Integrity and Disclosure Discipline</p>
</div>

<p>This memorandum summarizes the December 2020 public disclosure of the SUNBURST campaign affecting Orion customers, the SEC’s October 30, 2023 civil enforcement action against SolarWinds and related individuals alleging fraud and controls failures tied to cybersecurity disclosures, subsequent district court motion practice (including a reported decision at 741 F. Supp. 3d 37), and the parties’ stipulated dismissal with prejudice reflected in SEC Litigation Release LR-26423 (2025). Dismissal ends this enforcement action but does not eliminate operational lessons for build security and investor communications.</p>

<p><strong>Incident Summary: </strong>SUNBURST involved compromise of the software build and distribution chain, enabling insertion of malicious code into Orion updates and affecting numerous customers globally. The incident triggered intense customer incident response, government coordination, and scrutiny of development environment security and integrity controls.
<br>
Enforcement theories (as alleged) emphasized gaps between internal security assessments and public statements about cybersecurity risk and program maturity.</p>

<p><strong>Regulatory and Legal Outcomes: </strong>The SEC action sought injunctive and other relief under the federal securities laws. After motion practice, the action was dismissed with prejudice on stipulated terms in 2025. Customer litigation, contractual indemnity, and reputational effects may persist. Management continues to invest in pipeline security, customer trust programs, and disclosure control testing under counsel guidance.</p>

<p><strong>Control Failures and Root Causes: </strong>Allegations and public postmortems have emphasized themes including:</p>

<ol>
  <li>Insufficient segregation and monitoring of build and release infrastructure;</li>
  <li>Weaknesses in secure SDLC, artifact signing, and tamper detection for distributed software;</li>
  <li>Risk that internal vulnerability or assessment information was not adequately reflected in public disclosures;</li>
  <li>Challenges coordinating technical facts with Finance and Legal for periodic reports during a fast-moving supply-chain crisis.</li>
</ol>

<p>These areas are the focus of our remediation plan.</p>

<p><strong>Remediation and Oversight Program: </strong>The Company is implementing SLSA-style build attestations, expanded PAM and MFA for build systems, secret and key management hardening, anomaly detection on publishing pipelines, SBOM practices for releases, customer-facing incident playbooks, and recurring disclosure-control tests with documented remediation of exceptions.</p>

<p><strong>Approval and Endorsement Requests: </strong>Management requests the Committee’s approval of capital for pipeline security engineering and signing infrastructure; endorsement of a policy that security assessment results route through disclosure review when material to public statements; and confirmation of quarterly metrics on build attestation coverage, build-system patch latency, and disclosure test exceptions.</p>

<p>
Please let me know if additional information or further detail would be helpful.
</p>

<p>Respectfully submitted,</p>
Chief Information Security Officer
</div>

**Document-type guide:** [Board Security Brief](../../../../document-types/executive-board/board-security-brief.md)

**Writing tips:** [Writing best practices — Board Security Brief](../../../../studio/writing-best-practices.md#board-security-brief)
