# Executive Security Risk Summary (FTC v. Drizly 2022)

> Consolidated security risks and mitigation for executives following the FTC consent order.

---

## Purpose

A one- to two-page summary for the CEO and leadership that distills material security risks, root causes from the breach and FTC findings, and mitigation status. Use when briefing executives on consent order compliance and program priorities.

**Risks to highlight (aligned with FTC complaint and order):** (1) Access control and credential management — inadequate MFA, credentials in code, stale access. (2) Monitoring and detection — failure to detect exfiltration and anomalous access. (3) Data minimization — retention of personal information beyond necessity. (4) Security program maturity — lack of written program, designated ownership, and follow-through after prior incident.

**Mitigation summary:** Implement written program with designated coordinator; enforce MFA and eliminate credentials from repositories; deploy monitoring and retention schedule; complete biennial independent assessment and report to FTC.

---

## Hallucinated writing examples

**Scenario:** In December 2022, following the FTC’s consent order **(time)**, the Security Director **(role)** provides an executive security risk summary **(type)** to the Board Audit Committee **(audience)**. The summary focuses on the material control gaps alleged by the FTC and the remediation plan and evidence required for compliance.

<div class="writing-example-formal">

<p><strong>EXECUTIVE SECURITY RISK SUMMARY</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Board Audit Committee<br>
<strong>From: </strong>Security Director<br>
<strong>Date: </strong>December 5, 2022<br>
<strong>Subject: </strong>Security Risk Summary — FTC Consent Order Compliance and Residual Risk</p>
</div>

<p>This summary identifies the Company’s principal cybersecurity risks and remediation status following the FTC’s Decision and Order accepted on October 24, 2022. The scenario described below is illustrative; the underlying facts and obligations are based on the FTC Complaint and Decision and Order in FTC Docket No. 2023185.</p>

<p><strong>Top Risks (Current): </strong></p>
<p>1. <strong>Identity and Access Management (IAM): </strong>Elevated risk from weak authentication practices for source code and credentialed access (e.g., missing MFA, weak/reused credentials, incomplete access revocation).<br>
2. <strong>Secrets and Credential Management: </strong>Elevated risk if credentials are stored in repositories or otherwise insufficiently controlled, enabling rapid escalation from developer access to production access.<br>
3. <strong>Detection and Response: </strong>Elevated risk from incomplete monitoring for anomalous access and data exfiltration, with delayed discovery driven by external reporting.<br>
4. <strong>Data Minimization and Retention: </strong>Elevated risk from retaining personal information beyond necessity and lacking an enforced retention schedule, increasing breach impact and compliance exposure.<br>
5. <strong>Program Governance and Assurance: </strong>Elevated risk from insufficiently documented program ownership, risk assessment, and independent validation, which are required for compliance.</p>

<p><strong>Mitigation Status and Near-Term Commitments (90 Days): </strong></p>
<p>- Implement and operate a documented information security program with a designated coordinator, risk assessment, safeguards, and training.<br>
- Enforce MFA for accounts with access to source code and production credentials; complete access reviews and timely offboarding.<br>
- Eliminate credentials from source repositories and maintain continuous scanning and remediation.<br>
- Operate a retention schedule with deletion or de-identification evidence for personal information that is no longer necessary.<br>
- Engage an independent assessor and establish a remediation closure process for any findings.</p>

<p><strong>Board Oversight Requests: </strong>Approve the program framework and assessment budget, and require quarterly reporting on MFA coverage, secret-scanning results, retention schedule compliance, and assessment readiness.</p>

</div>

**Document-type guide:** [Executive Security Risk Summary](../../../../document-types/executive-board/executive-security-risk-summary.md)

**Writing tips:** [Writing best practices — Executive Security Risk Summary](../../../../studio/writing-best-practices.md#executive-security-risk-summary)
