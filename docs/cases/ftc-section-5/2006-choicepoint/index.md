# In the Matter of ChoicePoint Inc. (2006) — FTC Data Security and Consumer Redress

## Table of contents

- [Executive Summary](#executive-summary)
- [Regulatory and Legal Outcomes](#regulatory-and-legal-outcomes)
- [Security Technical Summary](#security-technical-summary)
- [Understanding Regulatory and Court Orders](#understanding-regulatory-and-court-orders)
- [Case Pack Documents](#case-pack-documents)
- [Facts and Timeline](#facts-and-timeline)
- [References](#references)

## Executive Summary

ChoicePoint disclosed that fraudsters obtained consumer records by exploiting weaknesses in customer credentialing and access approval controls. The FTC pursued enforcement and in 2006 announced a stipulated settlement requiring a comprehensive security program, independent assessments, and consumer redress obligations.

## Regulatory and Legal Outcomes

- **Regulator:** Federal Trade Commission (Section 5 / FCRA-related consumer protection context).
- **Resolution:** Stipulated final judgment and order (settlement), including civil penalties and injunctive security requirements.
- **Core obligations:** Security program governance, stronger credentialing and access controls, monitoring, independent assessment, and compliance reporting.

## Security Technical Summary

### Summary

The incident pattern reflected verification and access governance failure: fraudulent account/customer onboarding pathways enabled unauthorized data access to high-value consumer records.

### Attack Chain

1. Fraudulent actors submitted/used customer identities to obtain access through weak vetting gates.
2. Access enablement controls were insufficiently strict for high-risk data access.
3. Consumer records were retrieved through approved-but-fraudulent pathways.
4. Detection and escalation controls were not sufficient to prevent broad exposure early.

### Engineering Takeaways

- Enforce risk-based applicant/customer verification controls.
- Apply least-privilege access design and periodic entitlement recertification.
- Deploy fraud/anomaly monitoring with tested escalation playbooks.
- Maintain control-to-evidence mapping and regulator-ready artifact packaging.

## Understanding Regulatory and Court Orders

Use [Understanding regulatory and court orders](case-pack/understanding-regulator-court-orders/) for the official document interpretation and requirement mapping.

## Case Pack Documents

<table class="case-pack-docs-table">
<thead>
<tr><th>Case Document</th><th>Summary</th><th>Writing Scenario</th></tr>
</thead>
<tbody>
<tr class="case-pack-category"><td colspan="3">Executive and board</td></tr>
<tr><td><a href="case-pack/board-pack/">Board Pack</a></td><td>High-level security status and top risks for the board.</td><td>CISO delivers a board security brief to the Board Audit Committee.</td></tr>
<tr><td><a href="case-pack/executive-security-risk-summary/">Executive Security Risk Summary</a></td><td>Consolidated security risks and mitigation for executives.</td><td>Security Director prepares executive risk summary for CEO and leadership.</td></tr>
<tr><td><a href="case-pack/security-program-status-report/">Security Program Status Report</a></td><td>Program health, metrics, and progress for leadership.</td><td>Lead Security Engineer submits status report to Security Director and CISO.</td></tr>
<tr><td><a href="case-pack/strategic-security-initiative-justification/">Strategic Security Initiative Justification</a></td><td>Business case for a major security initiative.</td><td>CISO presents business case for program investment and remediation.</td></tr>
<tr class="case-pack-category"><td colspan="3">Regulatory and compliance</td></tr>
<tr><td><a href="case-pack/regulatory-security-explanation/">Regulatory Security Explanation</a></td><td>Explain security posture and controls to a regulator.</td><td>Security lead submits explanation of program and compliance posture.</td></tr>
<tr><td><a href="case-pack/compliance-justification-document/">Compliance Justification Document</a></td><td>Justify how controls meet a requirement or framework.</td><td>Lead Security Engineer maps controls to legal or regulatory requirements.</td></tr>
<tr><td><a href="case-pack/controls-evidence/">Controls -> Evidence Map</a></td><td>How controls are implemented and evidenced.</td><td>Security or control owner maps controls to evidence for regulator or auditor.</td></tr>
<tr><td><a href="case-pack/governance-response-memo/">Governance Response Memo</a></td><td>Respond to an audit or regulatory request on governance.</td><td>CISO submits governance response memo for oversight review.</td></tr>
<tr class="case-pack-category"><td colspan="3">Legal-technical</td></tr>
<tr><td><a href="case-pack/detailed-narrative-of-event/">Detailed Narrative of Events</a></td><td>Chronological factual narrative for legal or regulatory use.</td><td>Security or legal prepares chronology for counsel or regulator.</td></tr>
<tr><td><a href="case-pack/security-architecture-legal-review/">Security Architecture Explanation for Legal Review</a></td><td>Explain architecture and controls for counsel.</td><td>Lead Security Engineer produces architecture memo for General Counsel.</td></tr>
<tr><td><a href="case-pack/risk-register/">Risk Register</a></td><td>Justify risk acceptance or mitigation for legal or audit.</td><td>Security Director maintains risk register for leadership and audit.</td></tr>
<tr><td><a href="case-pack/security-decision-documentation/">Security Decision Documentation</a></td><td>Record a significant security decision and rationale.</td><td>Security Director documents decision record for board and counsel.</td></tr>
<tr class="case-pack-category"><td colspan="3">Policy and governance</td></tr>
<tr><td><a href="case-pack/security-policy-draft/">Security Policy Draft</a></td><td>Draft or update an enterprise security policy.</td><td>Security Director drafts policy for CISO, Legal, and board review.</td></tr>
<tr><td><a href="case-pack/security-governance-memo/">Security Governance Memo</a></td><td>Define or clarify governance roles and escalation.</td><td>CISO issues internal governance memo to leadership.</td></tr>
<tr><td><a href="case-pack/security-program-justification/">Security Program Justification</a></td><td>Justify program scope, resourcing, or structure.</td><td>CISO presents program justification to CEO and board.</td></tr>
<tr><td><a href="case-pack/internal-security-directive/">Internal Security Directive</a></td><td>Directive or mandate from leadership on security.</td><td>CISO issues internal directive on priority control requirements.</td></tr>
<tr class="case-pack-category"><td colspan="3">Public communication</td></tr>
<tr><td><a href="case-pack/security-public-statement/">Security Public Statement</a></td><td>Draft for press or public breach or incident statement.</td><td>CISO drafts public statement for consumers and partners.</td></tr>
<tr><td><a href="case-pack/customer-security-explanation/">Customer Security Explanation</a></td><td>Explain a security topic or incident to customers.</td><td>CISO drafts formal customer explanation for affected users.</td></tr>
<tr><td><a href="case-pack/security-transparency-report-section/">Security Transparency Report Section</a></td><td>Section for an annual or ad-hoc transparency report.</td><td>CISO drafts security section of transparency report for external audiences.</td></tr>
<tr class="case-pack-category"><td colspan="3">Operational (case-pack specific)</td></tr>
<tr><td><a href="case-pack/audit-packet/">Audit Packet Checklist</a></td><td>What to produce within 48 hours for evidence readiness.</td><td>Checklist for audit or regulator request.</td></tr>
<tr><td><a href="case-pack/implementation-checklist/">Implementation Checklist</a></td><td>0-30 / 30-60 / 60-90 day execution plan.</td><td>Security or program owner executes plan for leadership or board.</td></tr>
</tbody>
</table>


## Facts and Timeline

- **2005:** Unauthorized access to consumer records discovered.
- **2005:** Public disclosures and customer notification processes begin.
- **Jan 2006:** FTC announces settlement with penalties and security program requirements.
- **2006 onward:** Program remediation, governance reporting, and independent assessment execution.

## References

**Primary (official documents)**

- FTC case page: [ChoicePoint, Inc. matter](https://www.ftc.gov/legal-library/browse/cases-proceedings/052-3069-choicepoint-inc-matter)
- FTC press release: [ChoicePoint settles data security breach charges](https://www.ftc.gov/news-events/news/press-releases/2006/01/choicepoint-settles-data-security-breach-charges-pays-10-million-civil-penalties-5-million-consumer)
