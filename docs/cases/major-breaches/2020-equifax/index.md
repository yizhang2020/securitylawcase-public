# In re Equifax Inc. Customer Data Security Breach Litigation — MDL, FTC/CFPB, and related actions

## Table of contents

- [Executive Summary](#executive-summary)
- [Regulatory and Legal Outcomes](#regulatory-and-legal-outcomes)
- [Security Technical Summary](#security-technical-summary)
- [Understanding Regulatory and Court Orders](#understanding-regulatory-and-court-orders)
- [Case Pack Documents](#case-pack-documents)
- [Facts and Timeline](#facts-and-timeline)
- [References](#references)

## Executive Summary

**Equifax** disclosed a **2017** breach affecting **large numbers** of U.S. consumers, exposing **credit file** data and related identifiers. **Federal** regulators—the **FTC** and **CFPB**—obtained **orders** requiring **security program** upgrades, **assessments**, and **consumer redress**, among other terms. **Civil MDL** litigation addressed **class** claims and **settlement** administration.

## Regulatory and Legal Outcomes

### FTC

**Stipulated order** (July 2019) — comprehensive **information security program**, **assessments**, and **redress** (read the [order PDF](https://www.ftc.gov/system/files/documents/cases/equifax/172_3203_equifax_order_signed_7-23-19.pdf)).

### CFPB

Parallel **enforcement** with posted **complaint** and **order** on the [CFPB action page](https://www.consumerfinance.gov/enforcement/actions/equifax-inc/).

### MDL

**In re Equifax Inc. Customer Data Security Breach Litigation** — consumer **class** proceedings and **settlement** (see **MDL docket** and **settlement** documents).

## Security Technical Summary

### Summary

Public narratives focus on **patch management failure** for a **known vulnerability** in an **internet-facing** stack, leading to **mass data access** in a **credit bureau** environment.

### Attack chain (simplified)

1. **Known CVE** present in exposed application component.
2. **Exploitation** yields **access** to **consumer databases**.
3. **Exfiltration** at scale; **delayed** or **complex** internal detection narrative in public filings.

### Engineering takeaways

- **Emergency patch SLAs** for internet-facing apps with **PII**.
- **Segmentation** and **egress** controls for **data stores**.
- **Tabletop** exercises with **legal** and **comms** at **bureau** scale.

## Understanding Regulatory and Court Orders

See [**Understanding regulatory and court orders**](case-pack/understanding-regulator-court-orders.md).

<table class="case-pack-docs-table">
<thead>
<tr><th>Document</th><th>Date</th><th>Source</th><th>Key content</th></tr>
</thead>
<tbody>
<tr><td><a href="https://www.ftc.gov/system/files/documents/cases/equifax/172_3203_equifax_order_signed_7-23-19.pdf">FTC stipulated order — Equifax</a></td><td>Jul. 22, 2019</td><td>FTC</td><td>Security program, assessments, redress</td></tr>
<tr><td><a href="https://www.consumerfinance.gov/enforcement/actions/equifax-inc/">CFPB — Equifax, Inc.</a></td><td>—</td><td>CFPB</td><td>Enforcement order and complaint (as posted)</td></tr>
</tbody>
</table>

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

* **Sep. 2017** — Public breach disclosure.
* **Jul. 2019** — FTC stipulated order; CFPB action public materials.
* **2020+** — MDL settlement administration (see docket).

## References

**Primary**

- [FTC Equifax order (PDF)](https://www.ftc.gov/system/files/documents/cases/equifax/172_3203_equifax_order_signed_7-23-19.pdf)
- [CFPB Equifax action](https://www.consumerfinance.gov/enforcement/actions/equifax-inc/)

**Cited**

1. Federal Trade Commission. *Equifax* enforcement materials (case page and order).  
   [https://www.ftc.gov/enforcement/cases-proceedings/refunds/equifax-data-breach-settlement](https://www.ftc.gov/enforcement/cases-proceedings/refunds/equifax-data-breach-settlement)
