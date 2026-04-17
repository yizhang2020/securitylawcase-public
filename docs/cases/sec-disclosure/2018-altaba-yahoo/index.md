# In the Matter of Altaba Inc., f/d/b/a Yahoo! Inc. (2018) — SEC Cybersecurity Disclosure

## Table of contents

- [Executive Summary](#executive-summary)
- [Regulatory and Legal Outcomes](#regulatory-and-legal-outcomes)
- [Security Technical Summary](#security-technical-summary)
- [Understanding Regulatory and Court Orders](#understanding-regulatory-and-court-orders)
- [Case Pack Documents](#case-pack-documents)
- [Facts and Timeline](#facts-and-timeline)
- [References](#references)

## Executive Summary

The **Securities and Exchange Commission** charged **Yahoo! Inc.** (later **Altaba Inc.**) with **misleading investors** by failing to disclose a **2014 data breach** affecting **hundreds of millions** of user accounts. According to the SEC’s **April 24, 2018** order, Yahoo’s security team learned of the intrusion **within days**, yet for approximately **two years** the company’s **periodic reports** did not disclose the breach and instead described data-breach risk only in **generic** terms. The Commission found failures of **disclosure controls and procedures** and imposed a **cease-and-desist order** and **$35 million** civil penalty; Yahoo **neither admitted nor denied** the findings.

## Regulatory and Legal Outcomes

### SEC enforcement

**Administrative proceeding** File No. **3-18448** — *In the Matter of Altaba Inc., f/d/b/a Yahoo! Inc.* The order finds violations of **Securities Act** Sections **17(a)(2) and (3)** and **Exchange Act** Section **13(a)** and Rules **12b-20**, **13a-1**, **13a-11**, **13a-13**, and **13a-15** (including **disclosure controls**). Remedies include **cease-and-desist** and a **civil money penalty**.

### Legal theory (high level)

- **Material omission:** Failure to disclose a known, large-scale breach while filing periodic reports that did not inform investors of that fact.
- **Disclosure controls:** Inadequate procedures to ensure cybersecurity incident information reached personnel responsible for **accurate Exchange Act reporting**, including coordination with **auditors** and **outside counsel**.

## Security Technical Summary

### Summary

The SEC’s findings emphasize **governance and disclosure** more than a particular exploit chain: a **2014 intrusion** led to theft of a **user database backup** at massive scale. **Security identified** the incident quickly, but **enterprise disclosure processes** did not result in **timely investor-facing disclosure** for an extended period.

### Incident flow (as described in public materials)

1. **December 2014** — Intrusion and theft of user database backup files (names, emails, phones, DOB, hashed passwords, security Q&A) affecting **hundreds of millions** of accounts.
2. **Within days** — Yahoo information security confirms unauthorized access.
3. **2015–2016** — Periodic reports continue without disclosure of the specific breach; risk factors describe breach risk in general terms.
4. **September 2016** — Public disclosure of the 2014 breach.
5. **April 2018** — SEC order and penalty.

### Engineering and process takeaways

**Incident-to-disclosure workflow**  
- Define when a confirmed intrusion triggers **legal**, **finance**, and **disclosure committee** review.  
- Preserve **timelines** tying detection, containment, and disclosure decisions.

**Materiality and documentation**  
- Document **why** incident information was or was not included in filings.  
- Align **security severity** metrics with **securities counsel** criteria for materiality.

**Third-party assurance**  
- Ensure **auditors** and **outside counsel** receive information needed to assess **reporting obligations**.

## Understanding Regulatory and Court Orders

**Read the originals**—the SEC order is the authoritative source. Use [**Understanding regulatory and court orders**](case-pack/understanding-regulator-court-orders.md) to interpret findings and undertakings.

<table class="case-pack-docs-table">
<thead>
<tr><th>Document</th><th>Date</th><th>Source</th><th>Key obligation / holding</th></tr>
</thead>
<tbody>
<tr><td><a href="https://www.sec.gov/files/litigation/admin/2018/33-10485.pdf">Order Instituting Cease-and-Desist Proceedings (File No. 3-18448)</a></td><td>Apr. 24, 2018</td><td>SEC</td><td>Cease-and-desist; civil penalty; findings on disclosure failures and disclosure controls</td></tr>
<tr><td><a href="https://www.sec.gov/newsroom/press-releases/2018-71">SEC press release (2018-71)</a></td><td>Apr. 24, 2018</td><td>SEC</td><td>Public summary of charges and settlement</td></tr>
</tbody>
</table>

## Case Pack Documents

<table class="case-pack-docs-table">
<thead>
<tr><th>Case Document</th><th>Summary</th><th>Writing Scenario</th></tr>
</thead>
<tbody>
<tr class="case-pack-category"><td colspan="3">Executive and board</td></tr>
<tr><td><a href="case-pack/board-pack/">Board Pack</a></td><td>Security status and disclosure risk after SEC order.</td><td>CISO briefs Board Audit Committee after SEC cease-and-desist order (May 2018).</td></tr>
<tr><td><a href="case-pack/executive-security-risk-summary/">Executive Security Risk Summary</a></td><td>Executive view of incident and disclosure risks.</td><td>Security Director prepares summary for CEO and CFO on disclosure control gaps.</td></tr>
<tr><td><a href="case-pack/security-program-status-report/">Security Program Status Report</a></td><td>Program metrics and remediation status.</td><td>Lead Security Engineer reports IR and escalation process improvements post-order.</td></tr>
<tr><td><a href="case-pack/strategic-security-initiative-justification/">Strategic Security Initiative Justification</a></td><td>Business case for disclosure-aligned security investments.</td><td>CISO seeks funding for incident-to-disclosure workflow tooling.</td></tr>
<tr class="case-pack-category"><td colspan="3">Regulatory and compliance</td></tr>
<tr><td><a href="case-pack/regulatory-security-explanation/">Regulatory Security Explanation</a></td><td>Explain controls and escalation to regulators.</td><td>CISO drafts narrative on security-to-disclosure escalation for SEC staff (illustrative).</td></tr>
<tr><td><a href="case-pack/compliance-justification-document/">Compliance Justification Document</a></td><td>Map controls to disclosure obligations.</td><td>Compliance maps disclosure controls to SOC and IR evidence.</td></tr>
<tr><td><a href="case-pack/controls-evidence/">Controls → Evidence Map</a></td><td>Evidence for disclosure and security controls.</td><td>Senior engineer prepares evidence appendix for counsel.</td></tr>
<tr><td><a href="case-pack/governance-response-memo/">Governance Response Memo</a></td><td>Governance response on oversight.</td><td>CISO responds to board questions on incident escalation governance.</td></tr>
<tr class="case-pack-category"><td colspan="3">Legal-technical</td></tr>
<tr><td><a href="case-pack/detailed-narrative-of-event/">Detailed Narrative of Events</a></td><td>Chronology for counsel.</td><td>Legal and security align on SEC order timeline.</td></tr>
<tr><td><a href="case-pack/security-architecture-legal-review/">Security Architecture Explanation for Legal Review</a></td><td>Technical context for investigations.</td><td>Engineer explains logging and detection for disclosure support.</td></tr>
<tr><td><a href="case-pack/risk-register/">Risk Register</a></td><td>Material risks post-order.</td><td>Security Director maintains register including disclosure risk.</td></tr>
<tr><td><a href="case-pack/security-decision-documentation/">Security Decision Documentation</a></td><td>Document major decisions.</td><td>Document rationale for incident classification vs. disclosure trigger.</td></tr>
<tr class="case-pack-category"><td colspan="3">Policy and governance</td></tr>
<tr><td><a href="case-pack/security-policy-draft/">Security Policy Draft</a></td><td>Policy updates.</td><td>Director drafts policy for incident escalation to legal.</td></tr>
<tr><td><a href="case-pack/security-governance-memo/">Security Governance Memo</a></td><td>Roles and escalation.</td><td>CISO clarifies RACI for disclosure committee inputs.</td></tr>
<tr><td><a href="case-pack/security-program-justification/">Security Program Justification</a></td><td>Program scope and resources.</td><td>CISO justifies disclosure-controls alignment program.</td></tr>
<tr><td><a href="case-pack/internal-security-directive/">Internal Security Directive</a></td><td>Mandatory internal requirements.</td><td>CISO mandates reporting line for confirmed intrusions.</td></tr>
<tr class="case-pack-category"><td colspan="3">Public communication</td></tr>
<tr><td><a href="case-pack/security-public-statement/">Security Public Statement</a></td><td>External statement drafting.</td><td>CISO drafts coordinated disclosure language (illustrative).</td></tr>
<tr><td><a href="case-pack/customer-security-explanation/">Customer Security Explanation</a></td><td>Customer-facing explanation.</td><td>Security lead drafts customer FAQ on incident history (illustrative).</td></tr>
<tr><td><a href="case-pack/security-transparency-report-section/">Security Transparency Report Section</a></td><td>Transparency reporting.</td><td>CISO drafts transparency section on incident response and disclosure process.</td></tr>
<tr class="case-pack-category"><td colspan="3">Operational (case-pack specific)</td></tr>
<tr><td><a href="case-pack/audit-packet/">Audit Packet Checklist</a></td><td>48-hour evidence readiness.</td><td>Team assembles disclosure-control evidence.</td></tr>
<tr><td><a href="case-pack/implementation-checklist/">Implementation Checklist</a></td><td>Phased remediation.</td><td>Program owner executes 0–90 day disclosure-alignment plan.</td></tr>
<tr><td><a href="case-pack/understanding-regulator-court-orders/">Understanding Regulatory and Court Orders</a></td><td>Interpret the SEC order.</td><td>Counsel and CISO walk through order sections.</td></tr>
</tbody>
</table>

## Facts and Timeline

* **December 2014** — Intrusion affecting user account data at massive scale (per SEC order).
* **Within days of intrusion** — Yahoo information security confirms unauthorized access (per SEC order).
* **2015–2016** — Periodic Exchange Act filings do not disclose the specific breach; generic cyber risk disclosure continues (per SEC order).
* **September 2016** — Public disclosure of the 2014 breach.
* **April 24, 2018** — SEC issues cease-and-desist order and $35 million civil penalty; neither admit nor deny.

## References

**Primary (official documents)**

- **SEC Order** — *In the Matter of Altaba Inc., f/d/b/a Yahoo! Inc.*, File No. 3-18448 (Apr. 24, 2018). [PDF](https://www.sec.gov/files/litigation/admin/2018/33-10485.pdf)
- **EDGAR exhibit** — [Exhibit 99.1 (HTML)](https://www.sec.gov/Archives/edgar/data/1011006/000119312518131302/d577037dex991.htm)

**Cited**

1. U.S. Securities and Exchange Commission. *Altaba, Formerly Known as Yahoo!, Charged With Failing to Disclose Massive Cybersecurity Breach; Agrees To Pay $35 Million*, Apr. 24, 2018.  
   [https://www.sec.gov/newsroom/press-releases/2018-71](https://www.sec.gov/newsroom/press-releases/2018-71)
