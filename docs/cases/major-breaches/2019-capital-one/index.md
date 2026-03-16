# Capital One (2019) — Cloud Breach, Regulatory Enforcement, and Class Settlement

## Table of contents

- [Executive Summary](#executive-summary)
- [Regulatory and Legal Outcomes](#regulatory-and-legal-outcomes)
- [Security Technical Summary](#security-technical-summary)
- [Understanding Regulatory and Court Orders](#understanding-regulatory-and-court-orders)
- [Case Pack Documents](#case-pack-documents)
- [Facts and Timeline](#facts-and-timeline)
- [References](#references)

## Executive Summary
In July 2019, a security researcher reported exposed data associated with Capital One after discovering evidence of stolen information posted online. Capital One investigated the report and confirmed that an attacker had accessed data stored in infrastructure hosted on Amazon Web Services. The company secured the affected systems and notified federal law enforcement.

Authorities later arrested Paige Thompson and linked her to the breach through digital evidence. Capital One publicly disclosed the incident on July 29, 2019, stating that approximately **106 million individuals** in the United States and Canada were affected. The incident later resulted in regulatory enforcement actions and a consumer class-action settlement.

## Regulatory and Legal Outcomes

Following the breach, regulators examined whether Capital One’s cybersecurity program complied with regulatory expectations for financial institutions.

### Regulatory Enforcement

The **Office of the Comptroller of the Currency (OCC)** determined that Capital One failed to establish effective risk management processes governing its cloud infrastructure. The OCC imposed an **$80 million civil penalty** and issued a consent order requiring improvements to the bank’s cybersecurity and operational risk management program. The **FTC** also investigated under consumer protection authority.

### Legal Claims and Outcome

Consumers filed lawsuits alleging failure to implement reasonable safeguards, detect the breach promptly, and protect sensitive information. Claims were consolidated and resolved through a **$190 million** class-action settlement (2022). Legal and regulatory outcomes included the **$80 million OCC penalty**, consent orders, the **$190 million** settlement, and criminal prosecution of the attacker.

## Security Technical Summary

### Summary

The breach resulted from a **misconfigured cloud security control that allowed a Server-Side Request Forgery (SSRF) attack against a web application firewall**. The attacker used this vulnerability to obtain temporary AWS credentials and access internal data stored in cloud storage.

### Attack Chain

1. The attacker identified a **misconfigured web application firewall (WAF)** protecting Capital One cloud applications.
2. The configuration flaw allowed a **Server-Side Request Forgery (SSRF)** request to reach the AWS metadata service.
3. The attacker retrieved **temporary AWS credentials** associated with an IAM role.
4. The credentials provided access to internal AWS resources.
5. The attacker used the credentials to query **Amazon S3 storage buckets** containing Capital One data.
6. The attacker copied the data and stored it on external infrastructure.

### Engineering takeaways

- **Cloud configuration governance** — Establish and enforce baselines for WAF and metadata service access; use change approval and drift detection.
- **IAM and least privilege** — Limit what roles and credentials can access; ensure no single role can reach all sensitive data.
- **Detection and logging** — Detect SSRF and anomalous access to metadata and S3; retain logs for investigation and evidence.
- **Risk management** — Document cloud risk assessments and risk acceptance; track mitigations and show program effectiveness.
- **Evidence readiness** — Maintain control-to-evidence mapping so you can produce policies, config baselines, and testing results quickly for regulators and counsel.

## Understanding Regulatory and Court Orders

**Read the originals**—the regulatory and court orders below are the authoritative sources. Then use our [**Understanding regulatory and court orders**](case-pack/understanding-regulator-court-orders.md) page to learn how to interpret them and turn findings into action.

<table class="case-pack-docs-table">
<thead>
<tr><th>Document</th><th>Date</th><th>Source</th><th>Key obligation</th></tr>
</thead>
<tbody>
<tr><td><a href="https://www.occ.gov/static/enforcement-actions/ea2020-037.pdf">Cease and Desist Order — Capital One, N.A.</a></td><td>Aug. 6, 2020</td><td>OCC</td><td>Effective cloud risk assessment and internal controls; remediation and reporting</td></tr>
<tr><td><a href="https://www.federalreserve.gov/newsevents/pressreleases/files/enf20200806a1.pdf">Enforcement Order — Capital One Financial Corporation</a></td><td>Aug. 6, 2020</td><td>Federal Reserve</td><td>Board-approved plan for risk management and internal controls for data protection</td></tr>
<tr><td><a href="https://www.capitalonesettlement.com/Content/Documents/Final%20Approval%20Order.pdf">Final Order and Judgment Approving Class Settlement</a></td><td>Feb. 2022</td><td>U.S. District Court (E.D. Va.)</td><td>Settlement fund and consumer remedies (reflects claims over safeguards and detection)</td></tr>
</tbody>
</table>

## Case Pack Documents

<table class="case-pack-docs-table">
<thead>
<tr><th>Case Document</th><th>Summary</th><th>Hallucinated Writing Scenario</th></tr>
</thead>
<tbody>
<tr class="case-pack-category"><td colspan="3">Executive and board</td></tr>
<tr><td><a href="case-pack/board-pack/">Board Pack</a></td><td>High-level security status and top risks for the board.</td><td>CISO delivers board security brief to Board Audit Committee; one month after OCC Consent Order (Aug 2020).</td></tr>
<tr><td><a href="case-pack/executive-security-risk-summary/">Executive Security Risk Summary</a></td><td>Consolidated security risks and mitigation for executives.</td><td>Security Director, asked by CEO and CRO, produces executive security risk summary; Sept 2020, one month after OCC Consent Order.</td></tr>
<tr><td><a href="case-pack/security-program-status-report/">Security Program Status Report</a></td><td>Program health, metrics, and progress for leadership.</td><td>Lead Security Engineer submits security program status report to Security Director and CISO; Nov 2019, ~4 months after breach disclosure and arrest.</td></tr>
<tr><td><a href="case-pack/strategic-security-initiative-justification/">Strategic Security Initiative Justification</a></td><td>Business case for a major security initiative.</td><td>CISO presents business case to Executive Leadership and Board Finance Committee; Nov 2020, three months after OCC Consent Order.</td></tr>
<tr class="case-pack-category"><td colspan="3">Regulatory and compliance</td></tr>
<tr><td><a href="case-pack/regulatory-security-explanation/">Regulatory Security Explanation</a></td><td>Explain security posture and controls to a regulator.</td><td>CISO submits regulatory security explanation to OCC examiner; Dec 2020, following incident and Consent Order.</td></tr>
<tr><td><a href="case-pack/compliance-justification-document/">Compliance Justification Document</a></td><td>Justify how controls meet a requirement or framework.</td><td>Lead Security Engineer produces compliance justification document for OCC examiner; Nov 2020, following Consent Order and root cause.</td></tr>
<tr><td><a href="case-pack/controls-evidence/">Controls → Evidence Map</a></td><td>How controls are implemented and evidenced.</td><td>Security or control owner maps controls to evidence for regulator or auditor; on request during examination or audit.</td></tr>
<tr><td><a href="case-pack/governance-response-memo/">Governance Response Memo</a></td><td>Respond to an audit or regulatory request on governance.</td><td>CISO submits governance response memo to OCC examiner; Nov 2020, following incident and Consent Order.</td></tr>
<tr class="case-pack-category"><td colspan="3">Legal-technical</td></tr>
<tr><td><a href="case-pack/detailed-narrative-of-event/">Detailed Narrative of Events</a></td><td>Chronological factual narrative for legal/regulatory use.</td><td>Security or legal prepares chronological narrative for counsel or regulator; in connection with investigation or litigation.</td></tr>
<tr><td><a href="case-pack/security-architecture-legal-review/">Security Architecture Explanation for Legal Review</a></td><td>Explain architecture and controls for counsel.</td><td>Lead Security Engineer produces security architecture memo for General Counsel; Oct 2020, in connection with regulatory response and litigation.</td></tr>
<tr><td><a href="case-pack/risk-register/">Risk Register</a></td><td>Justify risk acceptance or mitigation for legal/audit.</td><td>Security Director or CISO maintains risk register for leadership and audit; ongoing, with updates for material changes.</td></tr>
<tr><td><a href="case-pack/security-decision-documentation/">Security Decision Documentation</a></td><td>Record a significant security decision and rationale.</td><td>Security Director documents security decision record for Board, OCC, and counsel; Sept 2020, one month after OCC Consent Order.</td></tr>
<tr class="case-pack-category"><td colspan="3">Policy and governance</td></tr>
<tr><td><a href="case-pack/security-policy-draft/">Security Policy Draft</a></td><td>Draft or update an enterprise security policy.</td><td>Security Director drafts enterprise security policy for CISO, Legal, and Board Audit Committee; Nov 2020, following OCC Consent Order and incident.</td></tr>
<tr><td><a href="case-pack/security-governance-memo/">Security Governance Memo</a></td><td>Define or clarify governance roles and escalation.</td><td>CISO issues internal security governance memo to leadership and OCC examiner; Oct 2020, two months after OCC Consent Order.</td></tr>
<tr><td><a href="case-pack/security-program-justification/">Security Program Justification</a></td><td>Justify program scope, resourcing, or structure.</td><td>CISO presents security program justification to CEO and Board Audit Committee; Nov 2020, following incident, Consent Order, and settlement.</td></tr>
<tr><td><a href="case-pack/internal-security-directive/">Internal Security Directive</a></td><td>Directive or mandate from leadership on security.</td><td>CISO issues internal security directive to Board and Bank leadership; Sept 2019, ~6 weeks after breach disclosure and arrest.</td></tr>
<tr class="case-pack-category"><td colspan="3">Public communication</td></tr>
<tr><td><a href="case-pack/security-public-statement/">Security Public Statement (2019)</a></td><td>Draft for press or public breach/incident statement.</td><td>CISO drafts public statement for investors and public; July 29, 2019, same day as FBI arrest.</td></tr>
<tr><td><a href="case-pack/customer-security-explanation/">Customer Security Explanation</a></td><td>Explain a security topic or incident to customers.</td><td>CISO drafts formal customer notice for affected customers; July 29, 2019, same day as disclosure and arrest.</td></tr>
<tr><td><a href="case-pack/security-transparency-report-section/">Security Transparency Report Section</a></td><td>Section for an annual or ad-hoc transparency report.</td><td>CISO drafts security section of transparency report for public and investors; March 2021, for 2020 reporting period.</td></tr>
<tr class="case-pack-category"><td colspan="3">Operational (case-pack specific)</td></tr>
<tr><td><a href="case-pack/audit-packet/">Audit Packet Checklist</a></td><td>What to produce within 48 hours for evidence readiness.</td><td>Checklist for what to produce for audit or regulator; within 48 hours of request.</td></tr>
<tr><td><a href="case-pack/implementation-checklist/">Implementation Checklist</a></td><td>0–30 / 30–60 / 60–90 day execution plan.</td><td>Security or program owner executes plan for leadership or board; 0–30 / 30–60 / 60–90 day phases.</td></tr>
</tbody>
</table>

## Facts and Timeline

* **March 2019** — The attacker begins exploiting a configuration weakness in Capital One’s cloud infrastructure hosted on AWS.

* **March–July 2019** — Data is accessed and exfiltrated from cloud storage using credentials obtained through the exploit.

* **17 July 2019** — A security researcher reports exposed Capital One data to the company after discovering references to the data posted online on GitHub.

* **19 July 2019** — Capital One’s security team begins investigating the report and confirms unauthorized access to customer data.

* **Late July 2019** — Capital One secures the vulnerable configuration, preserves forensic evidence, and notifies federal law enforcement.

* **29 July 2019 (morning)** — Authorities arrest Paige Thompson in Seattle after linking the breach to online activity and infrastructure under her control.

* **29 July 2019 (later the same day)** — Capital One publicly discloses the breach affecting approximately **106 million individuals** in the United States and Canada.

* **Late July–August 2019** — The company notifies affected customers and provides credit monitoring and identity protection services.

* **Late 2019** — Government regulators begin investigations into Capital One’s cybersecurity practices and cloud governance.

* **2020** — The **Office of the Comptroller of the Currency (OCC)** imposes an **$80 million civil penalty** and issues a consent order requiring improvements to Capital One’s cybersecurity program.

* **2022** — A federal court approves a **$190 million settlement** resolving consumer class-action litigation related to the breach.

## References

**Primary (official documents)**

- **OCC Cease and Desist Order** — Office of the Comptroller of the Currency, Aug. 6, 2020. [ea2020-037.pdf](https://www.occ.gov/static/enforcement-actions/ea2020-037.pdf)
- **Federal Reserve Enforcement Order** — Federal Reserve Board, Aug. 6, 2020. [enf20200806a1.pdf](https://www.federalreserve.gov/newsevents/pressreleases/files/enf20200806a1.pdf)
- **Final Order and Judgment Approving Class Settlement** — U.S. District Court, E.D. Virginia, Feb. 2022. *In re Capital One Consumer Data Security Breach Litigation*, MDL No. 1:19-md-02915. [Final Approval Order (PDF)](https://www.capitalonesettlement.com/Content/Documents/Final%20Approval%20Order.pdf)

**Cited**

1. Capital One Financial Corporation. *Capital One Announces Data Security Incident*, July 29, 2019.  
   [https://www.capitalone.com/about/newsroom/capital-one-data-security-incident/](https://www.capitalone.com/about/newsroom/capital-one-data-security-incident/)

2. U.S. Department of Justice. *Seattle Woman Charged with Computer Fraud in Capital One Data Breach*.  
   [https://www.justice.gov/usao-wdwa/pr/seattle-woman-charged-computer-fraud-capital-one-data-breach](https://www.justice.gov/usao-wdwa/pr/seattle-woman-charged-computer-fraud-capital-one-data-breach)

3. Office of the Comptroller of the Currency. *OCC News Release 2020-101: Consent Order and Civil Money Penalty against Capital One*, 2020.  
   [https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html)

4. *In re Capital One Consumer Data Security Breach Litigation* — settlement information.  
   [https://www.capitalonesettlement.com](https://www.capitalonesettlement.com)

5. U.S. Department of Justice. *Criminal Case: United States v. Paige A. Thompson*.  
   [https://www.justice.gov/usao-wdwa/united-states-v-paige-thompson](https://www.justice.gov/usao-wdwa/united-states-v-paige-thompson)
