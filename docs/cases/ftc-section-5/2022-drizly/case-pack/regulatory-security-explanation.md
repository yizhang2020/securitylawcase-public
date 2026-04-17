# Regulatory Security Explanation (FTC v. Drizly 2022)

> Use this to explain your organization’s security posture and controls to a regulator (e.g., FTC); demonstrates program effectiveness and responsiveness to a consent order.

---

## Purpose

This explanation frames the organization’s security posture for regulator, examiner, or counsel review in light of FTC v. Drizly 2022. It connects governance, technical controls, and evidence practices to the relevant legal or enforcement context so external stakeholders can assess control reasonableness and implementation maturity.

## Hallucinated writing examples

**Scenario:** In an illustrative period following acceptance of the FTC Decision and Order on October 24, 2022 **(time)**, Drizly, LLC — Chief Information Security Officer **(role)** prepares a regulatory security explanation **(type)** for Federal Trade Commission (Bureau of Consumer Protection — Staff) **(audience)**.

<div class="writing-example-formal">

<p><strong>REGULATORY SECURITY EXPLANATION</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Federal Trade Commission (Bureau of Consumer Protection — Staff)<br>
<strong>From: </strong>Drizly, LLC — Chief Information Security Officer<br>
<strong>Date: </strong>November 15, 2022<br>
<strong>Re: </strong>Information Security Program and Order Compliance — <em>In the Matter of Drizly, LLC, and James Cory Rellas</em>, FTC Docket No. 2023185</p>
</div>

<p><strong>Introduction: </strong>This submission describes Drizly’s information security program and control environment following the July 2020 data incident and in response to the administrative complaint and <strong>Decision and Order</strong> accepted by the Commission on October 24, 2022 (<em>In the Matter of Drizly, LLC, and James Cory Rellas</em>, FTC Docket No. 2023185). The FTC alleged unfair practices under Section 5 of the FTC Act (failure to implement reasonable security) and deception (misrepresentations regarding safeguards). The order requires, among other things, a comprehensive information security program, data minimization and a written retention schedule, biennial independent security assessments, and specified recordkeeping. The scope of this response includes governance, risk management, safeguards by domain, evidence of operation, and remediation status. Assertions below are supportable by the attached evidence index and underlying policies, assessments, and operational records.</p>

<p><strong>Governance: </strong>The Chief Executive Officer has designated a qualified employee to coordinate the information security program as required by the order. Security and privacy governance includes documented reporting to executive leadership and the board (or designated committee) on program effectiveness, material incidents, and consent-order milestones. The Chief Information Security Officer maintains authority to implement technical and administrative standards, approve exceptions with documented risk acceptance, and direct remediation priorities.</p>

<p><strong>Risk Management: </strong>Following the July 2020 incident and the FTC’s complaint, we elevated risks associated with <em>long-lived privileged access to source code and cloud administration</em>, <em>credential reuse and absent multifactor authentication</em>, <em>secrets stored in repositories</em>, and <em>insufficient monitoring of production access and exfiltration</em>. Risks are recorded, prioritized, assigned owners, and tracked to completion with evidence links (tickets, retest results, attestations).</p>

<p><strong>Control Environment and Evidence Of Operation: </strong>Key controls by domain: (1) <em>Identity, access, and credential management.</em> Multifactor authentication for accounts with access to source code or production credentials; prohibition on storing secrets in repositories; role-based access; periodic access reviews and timely offboarding. Evidence: IAM configuration exports, MFA enrollment reports, access review packs, repository scanning outputs. (2) <em>Secure development and change management.</em> Pull-request review for high-risk changes; pipeline checks for secrets; baseline for repository permissions. Evidence: merge history, scan reports, exception register. (3) <em>Monitoring and incident response.</em> Logging and alerting for anomalous access and bulk data movement; IR playbooks and tabletops. Evidence: alert samples, investigation tickets, retained logs per retention policy. (4) <em>Data minimization and retention.</em> Published retention schedule; processes to delete or de-identify personal information when no longer needed. Evidence: schedule document, deletion job records, sampling results. (5) <em>Assessments and service providers.</em> Biennial independent assessment process as required; vendor security requirements and oversight for in-scope processors. Evidence: assessment reports, vendor questionnaires, contracts.</p>

<p><strong>Incidents and Remediation: </strong>In July 2020, an external actor obtained access to Drizly’s environment and exfiltrated personal information relating to approximately 2.5 million consumers after compromising an executive’s GitHub account and obtaining AWS and database credentials stored in source code. Drizly did not initially detect the intrusion internally; we learned from external reporting. Root causes included credential reuse, lack of MFA, failure to revoke temporary access, and inadequate monitoring. Remediation has focused on the control domains above and on compliance with the Decision and Order’s program, retention, assessment, and reporting requirements. This response is submitted for staff review and is supported by the attached evidence index.</p>

</div>

**Document-type guide:** [Regulatory Security Explanation](../../../../document-types/regulatory-compliance/regulatory-security-explanation.md)

**Writing tips:** [Writing best practices — Regulatory Security Explanation](../../../../studio/writing-best-practices.md#regulatory-security-explanation)
