# Controls -> Evidence Map (FTC v. Drizly 2022)

## Purpose

Provide a technical control-to-evidence appendix that a Lead Security Engineer can submit to the CISO (and that the CISO can attach to FTC or auditor responses) to demonstrate implementation status, operating effectiveness, and evidence readiness against the consent order in FTC Docket No. 2023185.

## Hallucinated writing examples

**Scenario:** In January 2023, during initial implementation of the FTC Decision and Order **(time)**, a Senior Lead Security Engineer **(role)** submits a Controls -> Evidence Map **(type)** to the CISO and compliance leadership **(audience)** for use as a technical appendix supporting consent order compliance and examination readiness. The document emphasizes implementation proof: required control state, evidence artifacts, and measurable verification signals aligned with the complaint and order.

<div class="writing-example-formal">

<p><strong>CONTROLS -> EVIDENCE MAP (TECHNICAL APPENDIX)</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Chief Information Security Officer; Compliance Program Owner<br>
<strong>From: </strong>Senior Lead Security Engineer<br>
<strong>Date: </strong>January 18, 2023<br>
<strong>Subject: </strong>Control Implementation and Evidence Readiness Appendix — FTC Consent Order (Docket No. 2023185)</p>
</div>

<p><strong>Technical Objective: </strong>This appendix maps required control state to evidence artifacts and verification signals for domains addressed in the FTC complaint and Decision and Order. It is written for technical and compliance stakeholders who need substantiation of operating effectiveness, not policy statements alone.</p>

<p><strong>Scope: </strong>Access control and credential management; monitoring and detection; data minimization and retention; program governance and biennial independent assessment.</p>

<p><strong>1) Access Control and Credential Management: </strong></p>
<p><strong>Required Control State: </strong>Multifactor authentication for all accounts with access to source code or production credentials; no long-lived credentials stored in source repositories; role-based access with timely offboarding; strong password or equivalent authentication policy for in-scope accounts.<br>
<strong>Evidence Artifacts: </strong>MFA enrollment and enforcement logs; access review attestations; repository secret-scanning reports with remediation closure; offboarding checklists with access revocation timestamps; authentication policy version and distribution records.<br>
<strong>Verification Signals: </strong>Percentage of privileged and source-code-access accounts with MFA; count of credentials detected in repositories (target zero); median time from offboarding trigger to access revocation.</p>

<p><strong>2) Monitoring and Detection: </strong></p>
<p><strong>Required Control State: </strong>Logging and monitoring for anomalous access and data exfiltration; documented alert thresholds; regular assessment of protection measures; investigation workflow with retained outcomes.<br>
<strong>Evidence Artifacts: </strong>Log source inventory and retention configuration exports; detection rule catalog and change history; sample investigation tickets with timeline, containment actions, and closure rationale; internal or third-party assessment reports with remediation tracking.<br>
<strong>Verification Signals: </strong>Log coverage for critical systems; mean time to detect anomalous access or exfiltration patterns; percentage of high-severity alerts triaged within SLA; assessment finding closure rate.</p>

<p><strong>3) Data Minimization and Retention: </strong></p>
<p><strong>Required Control State: </strong>Published data retention schedule; process to delete or de-identify personal information when no longer necessary for specified purposes; collection and use limited to necessity.<br>
<strong>Evidence Artifacts: </strong>Retention schedule (public or internal, per order); data inventory by purpose and retention period; deletion or de-identification logs; periodic compliance review records.<br>
<strong>Verification Signals: </strong>Retention schedule adherence rate; volume of data deleted or de-identified per reporting period; count of exceptions with documented business justification and approval.</p>

<p><strong>4) Program Governance and Assessment: </strong></p>
<p><strong>Required Control State: </strong>Written information security program; designated program coordinator; risk assessment; training; testing and monitoring; service provider oversight; biennial independent third-party security assessment with report available to the FTC upon request.<br>
<strong>Evidence Artifacts: </strong>Approved program document and version history; coordinator designation and reporting line; risk assessment outputs; training completion records; testing reports; vendor oversight evidence; biennial assessor statement of work and final report with remediation plan.<br>
<strong>Verification Signals: </strong>Program document last approved date; risk review cadence met; training coverage percentage for in-scope roles; biennial assessment completion date and scope; open high findings aging.</p>

<p><strong>Submission Note: </strong>This appendix is technical by design and intended to accompany executive or regulator-facing narrative documents as implementation proof for consent order obligations.</p>

</div>

**Document-type guide:** [Security Control Implementation Explanation](../../../../document-types/regulatory-compliance/security-control-implementation-explanation.md)

**Writing tips:** [Writing best practices — Compliance Justification Document](../../../../studio/writing-best-practices.md#compliance-justification-document)
