# Regulatory Security Explanation (*In re Target Corp.* Customer Data Security Breach Litigation)

> Use this to explain your organization’s security posture and controls to a regulator, state AG technical staff, or payment-industry assessor.

---

## Purpose

This explanation frames the organization’s security posture for regulator, examiner, or counsel review in light of *In re Target Corp.* Customer Data Security Breach Litigation (MDL No. 14-2522). It connects governance, technical controls, and evidence practices to the relevant legal or enforcement context so external stakeholders can assess control reasonableness and implementation maturity.

## Hallucinated writing examples

**Scenario:** In an illustrative period after remand and continued MDL supervision **(time)**, Target Corporation — Chief Information Security Officer **(role)** prepares a regulatory security explanation **(type)** for State Attorney General Office — Technical Staff **(audience)**.

<div class="writing-example-formal">

<p><strong>REGULATORY SECURITY EXPLANATION</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>State Attorney General Office — Technical Staff<br>
<strong>From: </strong>Target Corporation — Chief Information Security Officer<br>
<strong>Date: </strong>October 14, 2015<br>
<strong>Re: </strong>Information Security Program — Post-2013 Incident Controls; MDL No. 14-2522 Context</p>
</div>

<p><strong>Introduction: </strong>This submission summarizes Target’s information security program and control environment following the 2013 payment card and customer information incident, in light of public judicial opinions in this litigation including the district court’s December 18, 2014 order (*In re Target Corp. Customer Data Sec. Breach Litig.*, 66 F. Supp. 3d 1154 (D. Minn. 2014)) and the Eighth Circuit’s February 1, 2017 decision (*In re Target Corp. Customer Data Sec. Breach Litig.*, 847 F.3d 608 (8th Cir. 2017)). While those decisions address class and procedural issues, they frame the factual and security-governance context in which regulators and multistate inquiries evaluated Target’s posture. The scope includes governance, risk management, network and vendor access controls, logging and monitoring, and evidence practices. Detailed exhibits are provided under separate cover and listed in the attached evidence index.</p>

<p><strong>Governance: </strong>The board (and designated committees) receives regular reporting on cybersecurity risk, control testing results, and major initiatives. The Chief Information Security Officer has defined authority for security standards, exception governance, and coordination with legal, fraud, and enterprise risk functions.</p>

<p><strong>Risk Management: </strong>Following the 2013 incident, Target elevated risks relating to <em>network segmentation between vendor access paths and cardholder environments</em>, <em>privileged access and credential management</em>, <em>logging coverage and retention for investigations</em>, and <em>third-party connectivity to payment environments</em>. Risks are tracked in enterprise risk processes with owners, treatment plans, and revisit dates.</p>

<p><strong>Control Environment and Evidence Of Operation: </strong>Key controls by domain: (1) <em>Network segmentation and vendor access.</em> Hardened boundaries, monitored connections, and contractual and technical controls for vendor remote access to sensitive environments. Evidence: network diagrams, firewall reviews, vendor access logs (samples), change records. (2) <em>Privileged access and authentication.</em> Least privilege, MFA where required, and periodic reviews of administrative accounts. Evidence: IAM exports, review packs, exception register. (3) <em>Logging, monitoring, and detection.</em> Centralized security logging; monitoring for anomalous behavior; IR coordination. Evidence: SIEM configurations, alert samples, investigation tickets. (4) <em>Vulnerability and patch management.</em> Enterprise scanning, prioritization, and remediation metrics. Evidence: scan reports, remediation SLAs, verification tests. (5) <em>Testing and assurance.</em> Tabletops, penetration tests, and PCI-related assessments as applicable to in-scope systems. Evidence: test reports, remediation evidence, management responses.</p>

<p><strong>Incidents and Remediation: </strong>The 2013 incident involved unauthorized access to Target’s network via a third-party vendor connection and subsequent movement to point-of-sale environments. Remediation focused on segmentation, credential hygiene, monitoring, and governance of vendor access. This letter supports supervisory and multistate technical review and is supported by the attached evidence index.</p>

</div>

**Document-type guide:** [Regulatory Security Explanation](../../../../document-types/regulatory-compliance/regulatory-security-explanation.md)

**Writing tips:** [Writing best practices — Regulatory Security Explanation](../../../../studio/writing-best-practices.md#regulatory-security-explanation)
