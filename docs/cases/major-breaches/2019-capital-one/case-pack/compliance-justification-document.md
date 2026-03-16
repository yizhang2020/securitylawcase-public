# Compliance Justification Document (Capital One 2019)

> Use this to justify how specific controls or practices meet a regulatory requirement or framework (e.g., NIST, CIS, PCI-DSS); maps “what we do” to “what is required.”

---

## Hallucinated writing examples

**Scenario.** In November 2020, following the Consent Order (August 6, 2020) and the root cause of the July 2019 incident **(time)**, the OCC examiner **(audience)** requests a control-to-requirement mapping for cloud configuration governance. The Lead Security Engineer **(role)** is tasked with producing a compliance justification document **(type)** that maps one or more requirements (e.g., NIST CSF, OCC expectations) to the Bank's implementation and evidence. The document must be precise and auditable.

<div class="writing-example-formal">

<p><strong>COMPLIANCE JUSTIFICATION DOCUMENT</strong></p>

<div class="doc-meta">
<p><strong>Document:</strong> Control-to-Requirement Mapping — Cloud Configuration Governance (Post–July 2019 Incident; OCC Consent Order)<br>
<strong>Framework:</strong> NIST CSF ID.AM-2 / OCC Heightened Standards (aligned)<br>
<strong>Owner:</strong> Lead Security Engineer, Cloud Security<br>
<strong>Last review:</strong> November 15, 2020</p>
</div>

<p><strong>Requirement.</strong> NIST Cybersecurity Framework, ID.AM-2: "Software platforms and applications within the organization are inventoried." OCC Heightened Standards and Consent Order expectation: Software and systems supporting critical operations are managed consistent with approved baselines; changes are authorized, peer-reviewed, and documented. (See OCC NR 2020-98; Consent Order requirements re cloud security and risk management.)</p>

<p><strong>Interpretation.</strong> In the context of the July 2019 incident—in which an external actor exploited a misconfiguration in our AWS-hosted web application firewall (WAF) to gain access to customer data—this requirement is interpreted to mean: (1) Cloud perimeter and boundary controls (WAF, routing, exposure rules) must be defined as code and maintained in a version-controlled repository. (2) All production changes to these controls must be proposed via pull request, peer-reviewed, and merged after approval. (3) Drift from approved baselines must be detected and remediated or formally accepted with documented rationale and revisit date.</p>

<p><strong>Implementation.</strong> The Bank has implemented config-as-code for designated AWS perimeter controls following the incident and per the Consent Order. All changes are proposed via pull request, reviewed by [designated role], and merged after approval. Drift detection runs [frequency]; exceptions are logged and either remediated or formally accepted with revisit dates. As of the last review, [X]% of perimeter assets are in scope; the remainder are targeted for Q1 2021.</p>

<p><strong>Evidence.</strong> Git repository history (commits, pull requests, approvals); change tickets linking to risk review; baseline configuration documents; drift detection reports and remediation tickets; exception register. Evidence packages are maintained for examiner and audit review. Owner: Lead Security Engineer; next review January 2021.</p>

</div>

---

## Official document (control-to-requirement mapping)

The **OCC consent order** and **SEC disclosure guidance** create explicit expectations that banks map controls to requirements. Capital One’s post-breach commitments (cloud security, IAM, logging, risk management) align with standard frameworks examiners use.

- **OCC Consent Order (2020):** [OCC Consent Order and Civil Money Penalty against Capital One](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html) — required improvements imply control expectations (e.g., configuration management, access control, monitoring) that can be mapped to NIST, CIS, or OCC guidance.
- **NIST Cybersecurity Framework:** [NIST CSF](https://www.nist.gov/cyberframework) — common reference for control-to-outcome mapping.
- **CIS Controls:** [CIS Critical Security Controls](https://www.cisecurity.org/controls) — often used in regulatory and audit contexts.

*Compliance justification documents are usually prepared for exams or audits; the consent order shows which control domains regulators focus on after an incident.*

---

## Writing analysis

**How compliance justification documents are typically structured**

- **Requirement** — Citation (regulation, standard, or control).
- **Interpretation** — What the requirement means in practice.
- **Implementation** — How the organization meets it (process and controls).
- **Evidence** — Artifacts that demonstrate compliance (policies, logs, reviews, tests).
- **Gaps and exceptions** — Any shortfalls, compensating controls, or risk acceptance.
- **Owner and review** — Accountability and last review date.

**What to emulate**

- One row or section per requirement; each with implementation + evidence so auditors can verify.
- Use the same citation format as the framework or regulator (e.g., NIST ID, CIS control number).
- Document gaps and risk acceptance explicitly so there are no surprises.

**What to improve**

- Avoid “we have a policy” without pointing to evidence of operation (testing, reviews, logs).
- Keep owner and review date current so the document is a living control-to-evidence map.

