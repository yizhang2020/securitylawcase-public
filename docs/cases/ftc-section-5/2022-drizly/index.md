# FTC v. Drizly, LLC (2022) — Credential Stuffing and Reasonable Security

## Table of contents

- [Executive Summary](#executive-summary)
- [Regulatory and Legal Outcomes](#regulatory-and-legal-outcomes)
- [Security Technical Summary](#security-technical-summary)
- [Understanding Regulatory and Court Orders](#understanding-regulatory-and-court-orders)
- [Case Pack Documents](#case-pack-documents)
- [Facts and Timeline](#facts-and-timeline)
- [References](#references)

## Executive Summary

In or around July 2020, an attacker gained access to Drizly’s production systems and exfiltrated personal information of approximately **2.5 million consumers**. The Federal Trade Commission (FTC) investigated and alleged that Drizly, LLC, and its Chief Executive Officer failed to implement reasonable information security practices, leading to the breach. The company did not detect the intrusion; it learned of the incident from media and social media reports that customer data was offered for sale on dark web forums.

The FTC filed an administrative complaint in October 2022 and simultaneously announced a proposed consent order. The order required a comprehensive information security program, data minimization and retention limits, and—notably—binding obligations on the CEO personally if he moves to another company that collects consumer data above a specified threshold. The matter was resolved by consent; no litigated opinion was issued.

## Regulatory and Legal Outcomes

### FTC Enforcement

The **Federal Trade Commission** alleged that Drizly’s security practices were unfair under Section 5 of the FTC Act and that certain public statements about security were deceptive. The FTC did not impose a monetary penalty. The **Decision and Order** (consent order) requires Drizly to implement a comprehensive information security program, restrict data collection and retention, obtain biennial independent assessments, and comply with reporting and recordkeeping obligations. The order also imposes obligations on the CEO individually for future roles at companies that collect covered consumer data.

### Legal Theory

- **Unfairness:** Failure to use reasonable security measures caused or was likely to cause substantial injury to consumers that was not reasonably avoidable and not outweighed by countervailing benefits.
- **Deception:** Representations that Drizly used appropriate safeguards to protect personal information were false or misleading in light of the alleged failures.

## Security Technical Summary

### Summary

The breach resulted from **credential reuse and inadequate access controls**. An attacker obtained access to an executive’s GitHub account (using credentials from an unrelated breach), then used that account to access Drizly’s GitHub repositories. Those repositories contained **AWS and database credentials** stored in source code. The attacker used the credentials to modify AWS security settings and access Drizly’s production environment, including databases holding millions of consumer records. Drizly had experienced a prior security incident in 2018 involving exposed AWS credentials on GitHub but did not implement adequate policies, access controls, or monitoring to prevent recurrence.

### Attack Chain

1. An executive was granted access to Drizly’s GitHub repositories for a one-day event; access was not revoked afterward.
2. The executive’s GitHub account used a weak, reused password and did not use multifactor authentication.
3. An attacker obtained the executive’s credentials (e.g., from another breach) and logged into the GitHub account.
4. The attacker accessed Drizly repositories containing **AWS and database credentials** in source code.
5. The attacker used the credentials to modify AWS settings and access Drizly’s production environment.
6. The attacker exfiltrated the User Table containing more than **2.5 million** consumer records.
7. Drizly did not detect the breach; it learned of the incident from external reports of data offered for sale online.

### Engineering Takeaways

**Identity and access management (IAM)**  
- Enforce multifactor authentication for all accounts with access to source code or production credentials.  
- Implement role-based access, routine access reviews, and timely offboarding.

**Secrets and credential management**  
- Prohibit storing credentials in source repositories; implement continuous secrets scanning and remediation workflows.  
- Treat credential reuse and credential stuffing as expected threats; implement detection and rate limiting for anomalous access.

**Cloud security and monitoring**  
- Maintain logging and monitoring sufficient to detect anomalous access and data exfiltration; retain evidence for investigation and regulatory requests.  
- Apply change control and review to high-risk cloud security settings.

**Data security (minimization and retention)**  
- Retain personal information only as long as necessary; publish and enforce a data retention schedule; delete or de-identify data when no longer needed.

**Program governance and assurance**  
- Maintain a written information security program with clear ownership, risk assessment, training, testing, and service provider oversight.  
- Maintain evidence of implementation and prepare for biennial independent assessments required by the FTC order.

## Understanding Regulatory and Court Orders

**Read the originals**—the FTC complaint and consent order below are the authoritative sources. Use the [**Understanding regulatory and court orders**](case-pack/understanding-regulator-court-orders.md) page to interpret them and turn findings into action.

<table class="case-pack-docs-table">
<thead>
<tr><th>Document</th><th>Date</th><th>Source</th><th>Key obligation</th></tr>
</thead>
<tbody>
<tr><td><a href="https://www.ftc.gov/system/files/ftc_gov/pdf/202-3185-Drizly-Complaint.pdf">Complaint — In the Matter of Drizly, LLC, et al.</a></td><td>Oct. 24, 2022</td><td>FTC</td><td>Alleged unfair and deceptive practices; failure to implement reasonable security</td></tr>
<tr><td><a href="https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf">Decision and Order — Drizly, LLC, and James Cory Rellas</a></td><td>Oct. 24, 2022</td><td>FTC</td><td>Information security program, data minimization, assessments, individual CEO obligations</td></tr>
</tbody>
</table>

## Case Pack Documents

<table class="case-pack-docs-table">
<thead>
<tr><th>Case Document</th><th>Summary</th><th>Writing Scenario</th></tr>
</thead>
<tbody>
<tr class="case-pack-category"><td colspan="3">Executive and board</td></tr>
<tr><td><a href="case-pack/board-pack/">Board Pack</a></td><td>High-level security status and top risks for the board.</td><td>CISO delivers board security brief to Board Audit Committee following FTC consent order (Nov 2022).</td></tr>
<tr><td><a href="case-pack/executive-security-risk-summary/">Executive Security Risk Summary</a></td><td>Consolidated security risks and mitigation for executives.</td><td>Security Director produces executive security risk summary for CEO and leadership after FTC order.</td></tr>
<tr><td><a href="case-pack/security-program-status-report/">Security Program Status Report</a></td><td>Program health, metrics, and progress for leadership.</td><td>Lead Security Engineer submits status report to Security Director and CISO following breach and FTC order.</td></tr>
<tr><td><a href="case-pack/strategic-security-initiative-justification/">Strategic Security Initiative Justification</a></td><td>Business case for a major security initiative.</td><td>CISO presents business case for security program and data minimization initiative to leadership.</td></tr>
<tr class="case-pack-category"><td colspan="3">Regulatory and compliance</td></tr>
<tr><td><a href="case-pack/regulatory-security-explanation/">Regulatory Security Explanation</a></td><td>Explain security posture and controls to a regulator.</td><td>Security lead submits explanation of security program and consent order compliance to FTC.</td></tr>
<tr><td><a href="case-pack/compliance-justification-document/">Compliance Justification Document</a></td><td>Justify how controls meet a requirement or framework.</td><td>Lead Security Engineer produces compliance justification mapping controls to FTC order and framework.</td></tr>
<tr><td><a href="case-pack/controls-evidence/">Controls → Evidence Map</a></td><td>How controls are implemented and evidenced.</td><td>Security or control owner maps controls to evidence for regulator or auditor.</td></tr>
<tr><td><a href="case-pack/governance-response-memo/">Governance Response Memo</a></td><td>Respond to an audit or regulatory request on governance.</td><td>CISO submits governance response memo addressing FTC order and program oversight.</td></tr>
<tr class="case-pack-category"><td colspan="3">Legal-technical</td></tr>
<tr><td><a href="case-pack/detailed-narrative-of-event/">Detailed Narrative of Events</a></td><td>Chronological factual narrative for legal/regulatory use.</td><td>Security or legal prepares chronological narrative for counsel or regulator.</td></tr>
<tr><td><a href="case-pack/security-architecture-legal-review/">Security Architecture Explanation for Legal Review</a></td><td>Explain architecture and controls for counsel.</td><td>Lead Security Engineer produces security architecture memo for General Counsel.</td></tr>
<tr><td><a href="case-pack/risk-register/">Risk Register</a></td><td>Justify risk acceptance or mitigation for legal/audit.</td><td>Security Director maintains risk register for leadership and audit.</td></tr>
<tr><td><a href="case-pack/security-decision-documentation/">Security Decision Documentation</a></td><td>Record a significant security decision and rationale.</td><td>Security Director documents security decision record for board and counsel.</td></tr>
<tr class="case-pack-category"><td colspan="3">Policy and governance</td></tr>
<tr><td><a href="case-pack/security-policy-draft/">Security Policy Draft</a></td><td>Draft or update an enterprise security policy.</td><td>Security Director drafts enterprise security policy for CISO, Legal, and board.</td></tr>
<tr><td><a href="case-pack/security-governance-memo/">Security Governance Memo</a></td><td>Define or clarify governance roles and escalation.</td><td>CISO issues internal security governance memo to leadership.</td></tr>
<tr><td><a href="case-pack/security-program-justification/">Security Program Justification</a></td><td>Justify program scope, resourcing, or structure.</td><td>CISO presents security program justification to CEO and board.</td></tr>
<tr><td><a href="case-pack/internal-security-directive/">Internal Security Directive</a></td><td>Directive or mandate from leadership on security.</td><td>CISO issues internal security directive on access control and data retention.</td></tr>
<tr class="case-pack-category"><td colspan="3">Public communication</td></tr>
<tr><td><a href="case-pack/security-public-statement/">Security Public Statement</a></td><td>Draft for press or public breach/incident statement.</td><td>CISO drafts public statement for consumers and partners after breach disclosure.</td></tr>
<tr><td><a href="case-pack/customer-security-explanation/">Customer Security Explanation</a></td><td>Explain a security topic or incident to customers.</td><td>CISO drafts formal customer notice for affected consumers.</td></tr>
<tr><td><a href="case-pack/security-transparency-report-section/">Security Transparency Report Section</a></td><td>Section for an annual or ad-hoc transparency report.</td><td>CISO drafts security section of transparency report for public and partners.</td></tr>
<tr class="case-pack-category"><td colspan="3">Operational (case-pack specific)</td></tr>
<tr><td><a href="case-pack/audit-packet/">Audit Packet Checklist</a></td><td>What to produce within 48 hours for evidence readiness.</td><td>Checklist for audit or regulator request.</td></tr>
<tr><td><a href="case-pack/implementation-checklist/">Implementation Checklist</a></td><td>0–30 / 30–60 / 60–90 day execution plan.</td><td>Security or program owner executes plan for leadership or board.</td></tr>
</tbody>
</table>

## Facts and Timeline

* **2018** — A Drizly employee posts AWS credentials to a personal public GitHub repository; credentials are exploited before Drizly can rotate them (servers used for cryptocurrency mining). Drizly is on notice of risks from exposed credentials and GitHub access.

* **April 2018** — An executive is granted access to Drizly’s GitHub repositories for a one-day event; access is not revoked or monitored after the event.

* **Early July 2020** — An attacker gains access to the executive’s GitHub account via credential reuse (credentials from an unrelated breach). The account used a short, reused password and no multifactor authentication.

* **July 2020** — The attacker uses the executive’s GitHub access to obtain AWS and database credentials stored in Drizly’s repositories, modifies AWS security settings, and exfiltrates the User Table containing personal information of approximately **2.5 million** consumers.

* **July 2020** — Drizly does not detect the breach internally. It learns of the incident from media and social media reports that customer data is offered for sale on dark web forums.

* **Oct. 24, 2022** — The FTC files an administrative complaint against Drizly, LLC, and James Cory Rellas (CEO) and announces a proposed consent order. The order is accepted by the Commission; no monetary penalty is imposed. The order requires an information security program, data minimization, biennial assessments, and—for the CEO—binding obligations if he moves to another company that collects consumer data from more than 25,000 individuals.

## References

**Primary (official documents)**

- **FTC Complaint** — In the Matter of Drizly, LLC, and James Cory Rellas, FTC Docket No. 2023185, Oct. 24, 2022. [Complaint (PDF)](https://www.ftc.gov/system/files/ftc_gov/pdf/202-3185-Drizly-Complaint.pdf)
- **FTC Decision and Order** — In the Matter of Drizly, LLC, and James Cory Rellas, FTC Docket No. 2023185, Oct. 24, 2022. [Decision and Order (PDF)](https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf)

**Cited**

1. Federal Trade Commission. *FTC Takes Action Against Drizly and Its CEO for Security Failures That Exposed Data of 2.5 Million Consumers*, Oct. 24, 2022.  
   [https://www.ftc.gov/news-events/news/press-releases/2022/10/ftc-takes-action-against-drizly-its-ceo-james-cory-rellas-security-failures-exposed-data-25-million](https://www.ftc.gov/news-events/news/press-releases/2022/10/ftc-takes-action-against-drizly-its-ceo-james-cory-rellas-security-failures-exposed-data-25-million)

2. Federal Trade Commission. *In the Matter of Drizly, LLC* — case page and document index.  
   [https://www.ftc.gov/legal-library/browse/cases-proceedings/202-3185-drizly-llc-matter](https://www.ftc.gov/legal-library/browse/cases-proceedings/202-3185-drizly-llc-matter)
