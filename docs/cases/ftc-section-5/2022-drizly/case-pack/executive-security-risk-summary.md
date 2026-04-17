# Executive Security Risk Summary (FTC v. Drizly 2022)

> Use this to present a consolidated view of security risks and mitigation to executives; supports risk acceptance and resource decisions after an FTC consent order.

---

## Purpose

This executive summary consolidates the highest-priority security and legal risks arising from FTC v. Drizly 2022, with impact framing, mitigation status, and near-term decision points for senior leadership. It supports cross-functional alignment among security, legal, finance, and operations on risk treatment and accountability.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the FTC October 2022 consent order after the July 2020 Drizly breach **(time)**, the Security Director, Technology Risk **(role)** prepares an executive security risk summary **(type)** for Chief Executive Officer, Chief Risk Officer **(audience)**.

<div class="writing-example-formal">

<p><strong>EXECUTIVE SECURITY RISK SUMMARY</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Chief Executive Officer, Chief Risk Officer<br>
<strong>From: </strong>Security Director, Technology Risk<br>
<strong>Date: </strong>December 5, 2022<br>
<strong>Subject: </strong>Consolidated Security Risk Summary — FTC Decision and Order (Docket No. 2023185); Post–July 2020 Incident</p>
</div>

<p><strong>Executive Summary: </strong>Cyber risk posture remains elevated following the July 2020 incident affecting approximately 2.5 million consumers and the Decision and Order accepted by the Federal Trade Commission on October 24, 2022 (<em>In the Matter of Drizly, LLC, and James Cory Rellas</em>, FTC Docket No. 2023185). The FTC alleged unfair practices (failure to implement reasonable security) and deception (misrepresentations regarding safeguards). The order requires a comprehensive information security program, data minimization and a retention schedule, biennial independent assessments, and—for the CEO—individual obligations in future roles at covered companies. Top risks below are explicitly tied to the complaint’s themes and to root causes emphasized in public materials (credential reuse, secrets in repositories, weak MFA, delayed detection).</p>

<p><strong>Risk Landscape: </strong>Our risk categories align to the consent order’s program elements and to the technical failure mode in the incident: (1) Identity, access, and credential management—MFA, offboarding, and privileged access to source and production. (2) Secrets and secure development—eliminating credentials in repositories and continuous scanning. (3) Detection and response—monitoring for anomalous access and exfiltration; the company initially learned of the breach from external reporting. (4) Data minimization and retention—limiting collection and deleting unnecessary personal information. (5) Assurance—biennial independent assessments and evidence of operation.</p>

<p><strong>Top Risks (Abbreviated): </strong>(1) <em>IAM and MFA gaps for developer and cloud administration paths.</em> High impact; enabled account takeover and rapid escalation to production. Mitigation: enforce MFA, access reviews, and PAM patterns; target coverage milestones per quarterly reporting. (2) <em>Secrets in source repositories.</em> High impact; directly implicated in the attack path. Mitigation: pipeline blocking, secret scanning, exception governance with expiry. (3) <em>Detection latency.</em> Medium–high; external discovery increases regulatory and litigation narrative risk. Mitigation: detection engineering backlog tied to crown-jewel data flows. (4) <em>Retention and minimization noncompliance.</em> Medium–high; order mandates a published schedule and deletion discipline. Mitigation: data inventory, retention jobs with evidence.</p>

<p><strong>Gaps and Initiatives: </strong>Key gaps: independent validation of control operating effectiveness; closure discipline for assessment findings; alignment of risk register to order milestones. Initiatives: executive dashboard for MFA coverage, secret-scanning open issues, and assessment readiness. We request risk acceptance for limited-duration vendor access exceptions with revisit March 2023, budget approval for SIEM and assessment line items per the approved remediation plan, and metrics for the next executive review on MFA enrollment, mean time to revoke access, and retention-schedule compliance sampling.</p>

</div>

**Document-type guide:** [Executive Security Risk Summary](../../../../document-types/executive-board/executive-security-risk-summary.md)

**Writing tips:** [Writing best practices — Executive Security Risk Summary](../../../../studio/writing-best-practices.md#executive-security-risk-summary)
