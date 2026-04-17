# Regulatory Security Explanation (Equifax — FTC / CFPB enforcement)

> Use this to explain your organization’s security posture and controls to federal regulators and in MDL-related oversight.

---

## Purpose

This explanation frames the organization’s security posture for regulator, examiner, or counsel review in light of Equifax 2017–2020 federal enforcement and related MDL remediation. It connects governance, technical controls, and evidence practices to the relevant legal or enforcement context so external stakeholders can assess control reasonableness and implementation maturity.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the FTC stipulated order (July 2019) and parallel CFPB action **(time)**, Equifax Inc. — Chief Information Security Officer **(role)** prepares a regulatory security explanation **(type)** for Federal Trade Commission and Bureau of Consumer Financial Protection examination staff **(audience)**.

<div class="writing-example-formal">

<p><strong>REGULATORY SECURITY EXPLANATION</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Federal Trade Commission / Consumer Financial Protection Bureau — Examination Staff (Illustrative)<br>
<strong>From: </strong>Equifax Inc. — Chief Information Security Officer<br>
<strong>Date: </strong>September 30, 2020<br>
<strong>Re: </strong>Information Security Program — Post-2017 Incident; FTC Stipulated Order (July 22, 2019); CFPB Action (Parallel Track)</p>
</div>

<p><strong>Introduction: </strong>This submission describes Equifax’s information security program and control environment following the 2017 cybersecurity incident involving consumer credit files, in connection with the <strong>FTC stipulated order</strong> entered July 22, 2019 (see FTC Equifax enforcement materials, including the published order PDF on the FTC’s Equifax case page) and parallel <strong>CFPB</strong> public enforcement action materials. These instruments impose comprehensive information security program obligations, assessment and reporting requirements, and long-running compliance duties appropriate to a nationwide consumer reporting agency. The scope of this response includes governance, risk management, technical safeguards across on-premise and cloud systems, evidence of operation, and remediation status. Assertions are supportable by the attached evidence index and underlying policies, assessments, logs, and test results.</p>

<p><strong>Governance: </strong>The board and designated committees receive regular reporting on cybersecurity and technology risk, major incidents, and progress against regulatory commitments. The Chief Information Security Officer has defined authority for enterprise security standards, control testing, and coordination with legal, compliance, and internal audit.</p>

<p><strong>Risk Management: </strong>Following the 2017 incident, elevated themes include <em>patch and vulnerability management for internet-facing and critical applications</em>, <em>identity and access governance for large-scale data stores</em>, <em>network segmentation and data flow controls</em>, <em>encryption and key management</em>, and <em>detection and response for anomalous data access</em>. Risks are recorded with owners, treatment plans, and measurable outcomes.</p>

<p><strong>Control Environment and Evidence Of Operation: </strong>Key controls by domain: (1) <em>Vulnerability and patch management.</em> Enterprise scanning, exception governance, and verification testing for critical systems. Evidence: scan reports, change records, closure evidence. (2) <em>Access control and privileged access.</em> Least privilege, MFA, PAM where deployed, periodic reviews. Evidence: IAM inventories, review attestations, PAM session samples. (3) <em>Logging, monitoring, and SIEM.</em> Centralized collection; detection use cases; IR workflows. Evidence: architecture docs, alert samples, investigation tickets. (4) <em>Encryption and data protection.</em> Standards for data at rest and in transit; key management controls. Evidence: crypto standards, KMS policies, implementation attestations. (5) <em>Independent assessments and audits.</em> Third-party testing and regulator-driven assessments tracked to closure. Evidence: reports, management responses, remediation tickets.</p>

<p><strong>Incidents and Remediation: </strong>The 2017 incident involved exploitation of a vulnerability in an internet-facing application leading to exposure of substantial consumer credit file data. Remediation has focused on the domains above and on fulfilling FTC and CFPB program and reporting obligations. This response is submitted for examination staff review and is supported by the attached evidence index.</p>

</div>

**Document-type guide:** [Regulatory Security Explanation](../../../../document-types/regulatory-compliance/regulatory-security-explanation.md)

**Writing tips:** [Writing best practices — Regulatory Security Explanation](../../../../studio/writing-best-practices.md#regulatory-security-explanation)
