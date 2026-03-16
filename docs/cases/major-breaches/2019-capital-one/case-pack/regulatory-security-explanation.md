# Regulatory Security Explanation (Capital One 2019)

> Use this to explain your organization’s security posture and controls to a regulator (e.g., OCC, FTC, SEC); demonstrates program effectiveness and responsiveness.

---

## Hallucinated writing examples

**Scenario.** In December 2020, following the July 2019 incident and the Consent Order (August 6, 2020) **(time)**, the OCC examiner **(audience)** requests a formal written explanation of the Bank’s security posture and control environment following the July 2019 incident and the Consent Order (August 6, 2020). The Chief Information Security Officer **(role)** must submit a regulatory security explanation **(type)** that addresses governance, risk management, control environment, evidence of operation, and the specific incident and remediation. The document will be used in the examination and must be supportable by policies, assessments, and artifacts.

<div class="writing-example-formal">

<p><strong>REGULATORY SECURITY EXPLANATION</strong></p>

<div class="doc-meta">
<p><strong>To:</strong> Office of the Comptroller of the Currency (Examiner)<br>
<strong>From:</strong> Capital One Bank (USA), N.A. — Chief Information Security Officer<br>
<strong>Date:</strong> December 1, 2020<br>
<strong>Re:</strong> Response to Cybersecurity Examination — Security Posture and Control Environment (Post–July 2019 Incident; Consent Order)</p>
</div>

<p><strong>Introduction.</strong> This submission describes the Bank’s security posture, governance, and control environment for the period following the July 2019 cybersecurity incident and in response to the Consent Order and Civil Money Penalty issued by the Office of the Comptroller of the Currency on August 6, 2020 (OCC News Release NR 2020-98). The scope of this response includes governance, risk management, control environment, evidence of operation, and the incident and remediation. All assertions are supportable by the attached evidence index and underlying policies, assessments, and operational artifacts.</p>

<p><strong>Governance.</strong> The Board of Directors delegates oversight of technology and cybersecurity risk to the Board Audit Committee. The Committee receives quarterly reporting on cybersecurity risk, control effectiveness, and Consent Order progress. The Chief Information Security Officer reports to [designated executive] and has authority over security policy, standards, and control implementation. Security and technology risk committees meet on a [cadence] basis; charters and minutes are maintained and available for examiner review.</p>

<p><strong>Risk management.</strong> The Bank identifies, assesses, and mitigates cyber risk through a defined risk taxonomy, risk register, and escalation to the Board. Following the July 2019 incident and the OCC’s findings, cloud configuration governance, identity and access management (IAM), and logging and retention were elevated as top risks. Mitigation is tracked with revisit dates and evidence linkage; progress is reported to the OCC per the Consent Order.</p>

<p><strong>Control environment and evidence of operation.</strong> Key controls by domain: (1) <em>Cloud and perimeter.</em> Config-as-code and peer review for designated AWS perimeter and WAF controls; drift detection deployed with remediation or documented exception. Evidence: repository history, change tickets, baseline documents, drift reports. (2) <em>Identity and access.</em> Least-privilege review and reduction of over-permissioned roles. Evidence: IAM inventory, review records. (3) <em>Logging and retention.</em> Centralized logging; 90-day retention for designated security-relevant data. Evidence: retention policy, log coverage reports. (4) <em>Incident response.</em> IR plan, tabletop exercises, forensic readiness. Evidence: plan document, exercise summaries.</p>

<p><strong>Incidents and remediation.</strong> The July 2019 incident involved unauthorized access by an external actor to customer data stored in AWS-hosted infrastructure. The actor exploited a WAF misconfiguration and over-permissioned IAM roles. Root causes were identified as configuration weakness and governance gaps. Remediation: the vulnerability was secured in July 2019; law enforcement was notified; the individual was arrested (<em>United States v. Paige A. Thompson</em>). Consent order commitments are in progress and reported to the OCC. The Bank has strengthened governance, risk management, and controls per the Consent Order and internal roadmap. This response is submitted for examiner review and is supported by the attached evidence index.</p>

</div>

---

## Official document (regulatory context and consent order)

The **OCC** investigated Capital One’s cybersecurity and cloud governance after the 2019 breach and issued a consent order and civil money penalty. The order describes what the regulator expected and what the bank committed to—a direct example of “security posture and controls” in a regulatory response.

- **OCC Consent Order (2020):** [OCC Consent Order and Civil Money Penalty against Capital One](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html) — findings, required improvements (risk management, board reporting, cloud security, third-party risk), and compliance commitments.
- **OCC Guidelines:** [OCC Heightened Standards](https://www.occ.gov/topics/supervision-and-examination/guidance/operational-risk/heightened-standards.html) and related bulletins — expectations for governance, risk management, and controls that shape how banks explain posture.
- **Capital One 10-K:** [Capital One 10-K](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000927628&type=10-K&dateb=&owner=include&count=40) — Item 1C and risk factors show how the company describes security to the SEC and investors.

*Regulatory security explanations are often confidential; the consent order and 10-K show the standard of detail and structure regulators expect.*

---

## Writing analysis

**How regulatory security explanations are typically structured**

- **Introduction** — Scope, period, and context of the response.
- **Governance** — Oversight, roles, and accountability for security.
- **Risk management** — How risks are identified, assessed, and mitigated.
- **Control environment** — Key controls by domain (e.g., access, logging, IR, third-party).
- **Evidence of operation** — How controls are tested, monitored, and evidenced.
- **Incidents and remediation** — Relevant incidents and lessons applied.
- **Conclusion** — Summary of posture and any commitments.

**What to emulate**

- Every assertion supportable by policies, assessments, logs, and testing results.
- Align language with regulatory guidance (e.g., OCC, FTC, SEC) so examiners see expected concepts.
- Clear “evidence of operation” section so the document bridges artifacts and expectations.

**What to improve**

- Avoid generic statements; cite specific controls, metrics, and review cadences.
- If an incident is in scope, describe cause, impact, and remediation so the regulator sees accountability.

