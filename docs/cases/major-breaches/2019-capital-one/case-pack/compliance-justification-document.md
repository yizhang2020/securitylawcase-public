# Compliance Justification Document (Capital One 2019)

> Use this to justify how specific controls or practices meet a regulatory requirement or framework (e.g., NIST, CIS, PCI-DSS); maps “what we do” to “what is required.”

---

## Purpose

Demonstrate how specific controls satisfy named requirements (e.g., NIST CSF, OCC expectations) after the July 2019 incident and consent order—requirement, interpretation, implementation, evidence, and ownership—so examiners and auditors can verify compliance.

---

## Hallucinated writing examples

**Scenario:** In November 2020, following the Consent Order (August 6, 2020) and the root cause of the July 2019 incident **(time)**, the OCC examiner **(audience)** requests a control-to-requirement mapping for cloud configuration governance. The Lead Security Engineer **(role)** is tasked with producing a compliance justification document **(type)** that maps one or more requirements (e.g., NIST CSF, OCC expectations) to the Bank's implementation and evidence. The document must be precise and auditable.

<div class="writing-example-formal">

<p><strong>COMPLIANCE JUSTIFICATION DOCUMENT</strong></p>

<div class="doc-meta">
<p><strong>Document: </strong>Control-to-Requirement Mapping — Cloud Configuration Governance (Post–July 2019 Incident; OCC Consent Order)<br>
<strong>Framework: </strong>NIST CSF ID.AM-2 / OCC Heightened Standards (aligned)<br>
<strong>Owner: </strong>Lead Security Engineer, Cloud Security<br>
<strong>Last review: </strong>November 15, 2020</p>
</div>

<p><strong>Requirement: </strong>NIST Cybersecurity Framework, ID.AM-2: "Software platforms and applications within the organization are inventoried." OCC Heightened Standards and Consent Order expectation: Software and systems supporting critical operations are managed consistent with approved baselines; changes are authorized, peer-reviewed, and documented. (See OCC NR 2020-98; Consent Order requirements re cloud security and risk management.)</p>

<p><strong>Interpretation: </strong>In the context of the July 2019 incident—in which an external actor exploited a misconfiguration in our AWS-hosted web application firewall (WAF) to gain access to customer data—this requirement is interpreted to mean: (1) Cloud perimeter and boundary controls (WAF, routing, exposure rules) must be defined as code and maintained in a version-controlled repository. (2) All production changes to these controls must be proposed via pull request, peer-reviewed, and merged after approval. (3) Drift from approved baselines must be detected and remediated or formally accepted with documented rationale and revisit date.</p>

<p><strong>Implementation: </strong>The Bank has implemented config-as-code for designated AWS perimeter controls following the incident and per the Consent Order. All changes are proposed via pull request, reviewed by [designated role], and merged after approval. Drift detection runs [frequency]; exceptions are logged and either remediated or formally accepted with revisit dates. As of the last review, [X]% of perimeter assets are in scope; the remainder are targeted for Q1 2021.</p>

<p><strong>Evidence: </strong>Git repository history (commits, pull requests, approvals); change tickets linking to risk review; baseline configuration documents; drift detection reports and remediation tickets; exception register. Evidence packages are maintained for examiner and audit review. Owner: Lead Security Engineer; next review January 2021.</p>

</div>

**Document-type guide:** [Compliance Justification Document](../../../../document-types/regulatory-compliance/compliance-justification-document.md)

**Writing tips:** [Writing best practices — Compliance Justification Document](../../../../studio/writing-best-practices.md#compliance-justification-document)
