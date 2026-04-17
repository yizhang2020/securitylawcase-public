# Spokeo, Inc. v. Robins (2016) — Article III Standing, FCRA, and “Concrete” Injury

## Table of contents

- [Executive Summary](#executive-summary)
- [Regulatory and Legal Outcomes](#regulatory-and-legal-outcomes)
- [Security Technical Summary](#security-technical-summary)
- [Understanding Regulatory and Court Orders](#understanding-regulatory-and-court-orders)
- [Case Pack Documents](#case-pack-documents)
- [Facts and Timeline](#facts-and-timeline)
- [References](#references)

## Executive Summary

Thomas Robins sued Spokeo, Inc. under the **Fair Credit Reporting Act (FCRA)**, alleging Spokeo published inaccurate “consumer report” information about him in connection with its **people-search** product. The U.S. Supreme Court held that **Article III standing** requires a plaintiff to allege an injury that is both **concrete** and **particularized**. A **bare procedural violation** of a statute, divorced from concrete harm, is not enough. The Court **vacated** the Ninth Circuit’s decision because that court’s standing analysis did not address **concreteness** adequately, and **remanded** for further consideration.

For cybersecurity and privacy programs, *Spokeo* is a core citation in **federal court standing** debates—especially whether statutory claims after **data incidents** or **reporting inaccuracies** satisfy Article III. It does not decide the merits of Robins’s FCRA claims and **does not hold** that Robins lacked standing; it requires lower courts to evaluate **both** concreteness and particularization.

## Regulatory and Legal Outcomes

### Supreme Court (Article III)

The **Supreme Court of the United States** decided *Spokeo, Inc. v. Robins*, 578 U.S. 330 (2016), clarifying that **injury-in-fact** under Article III requires:

- **Particularization:** the injury must affect the plaintiff in a **personal and individual** way.
- **Concreteness:** the injury must be **real**, not **abstract**, even when a statute creates legal rights—though some harms can be **intangible** if they have a close relationship to traditional harms.

The Court emphasized that not every **statutory violation** produces a concrete injury. The decision **vacated and remanded** the Ninth Circuit’s standing determination.

### FCRA context (procedural posture)

Robins alleged violations of **15 U.S.C. Section 1681e(b)** (reasonable procedures to assure **maximum possible accuracy**) among other provisions. The Supreme Court’s opinion discusses FCRA’s purposes and the nature of alleged inaccuracies (e.g., employment status) as part of the standing analysis, without resolving whether Robins ultimately had standing on remand.

## Security Technical Summary

### Summary

*Spokeo* is not a “breach forensics” opinion. Its technical implication for product teams is about **data accuracy**, **attribute provenance**, and **consumer reporting**-like outputs: systems that publish **personal profiles** can create **litigation risk** under **FCRA** if they operate as consumer reporting in context and if inaccuracies cause **concrete** harm (as determined on remand).

### “Attack chain” analog (risk engineering framing)

1. **Data aggregation and matching** pipelines ingest imperfect sources.
2. **Profile publication** exposes inaccurate attributes to users or downstream systems.
3. **Consumer disputes** and regulatory scrutiny follow when processes do not meet **accuracy** and **dispute** obligations for covered reports.
4. **Federal litigation** turns on whether plaintiffs allege (and can show) **concrete, particularized** harm—not merely a statutory paperwork violation.

### Engineering takeaways

**Data quality and lineage**  
- Treat high-risk attributes (employment, financial, legal) with **source verification**, **confidence scoring**, and **human review** where appropriate.

**FCRA-sensitive product design**  
- Determine whether a product is a **consumer report** in context; if so, implement **reasonable procedures** for **maximum possible accuracy** and robust **dispute handling**.

**Litigation and class actions**  
- **Standing** is a gatekeeper: plaintiffs must satisfy **Article III** even when statutes provide private rights of action.

**Public statements**  
- Avoid marketing claims that understate error rates or overstate verification if accuracy is a core legal duty.

## Understanding Regulatory and Court Orders

Use [**Understanding regulatory and court orders**](case-pack/understanding-regulator-court-orders.md) for a structured summary of the **Supreme Court opinion** and the **FCRA provisions** discussed there.

<table class="case-pack-docs-table">
<thead>
<tr><th>Document</th><th>Date</th><th>Source</th><th>Key holding or focus</th></tr>
</thead>
<tbody>
<tr><td><a href="https://tile.loc.gov/storage-services/service/ll/usrep/usrep578/usrep578330/usrep578330.pdf"><em>Spokeo, Inc. v. Robins</em>, 578 U.S. 330 (2016)</a></td><td>May 16, 2016</td><td>U.S. Supreme Court</td><td>Article III injury must be concrete and particularized; vacatur/remand of Ninth Circuit standing analysis</td></tr>
<tr><td><a href="https://www.law.cornell.edu/uscode/text/15/1681e">15 U.S.C. Section 1681e (FCRA)</a></td><td>(statute)</td><td>U.S. Code (Cornell LII)</td><td>Statutory duties discussed in the opinion (accuracy-related provisions)</td></tr>
</tbody>
</table>

## Case Pack Documents

<table class="case-pack-docs-table">
<thead>
<tr><th>Case Document</th><th>Summary</th><th>Writing Scenario</th></tr>
</thead>
<tbody>
<tr class="case-pack-category"><td colspan="3">Executive and board</td></tr>
<tr><td><a href="case-pack/board-pack/">Board Pack</a></td><td>Board brief on litigation risk from FCRA/standing.</td><td>CISO briefs the board after Supreme Court remand on Article III issues (2016).</td></tr>
<tr><td><a href="case-pack/executive-security-risk-summary/">Executive Security Risk Summary</a></td><td>Executive summary of accuracy and litigation risk.</td><td>Security Director summarizes FCRA exposure for people-data products.</td></tr>
<tr><td><a href="case-pack/security-program-status-report/">Security Program Status Report</a></td><td>Program status for data-quality governance.</td><td>Lead engineer reports data-quality control rollout to the CISO.</td></tr>
<tr><td><a href="case-pack/strategic-security-initiative-justification/">Strategic Security Initiative Justification</a></td><td>Business case for accuracy program investment.</td><td>CISO seeks funding for data provenance and dispute tooling.</td></tr>
<tr class="case-pack-category"><td colspan="3">Regulatory and compliance</td></tr>
<tr><td><a href="case-pack/regulatory-security-explanation/">Regulatory Security Explanation</a></td><td>Explain controls for accuracy and disputes.</td><td>Privacy lead explains accuracy program to FTC staff (illustrative).</td></tr>
<tr><td><a href="case-pack/compliance-justification-document/">Compliance Justification Document</a></td><td>Map controls to FCRA accuracy duties.</td><td>Compliance maps controls to Section 1681e(b) procedures.</td></tr>
<tr><td><a href="case-pack/controls-evidence/">Controls → Evidence Map</a></td><td>Evidence for data-quality controls.</td><td>Engineer documents lineage, review logs, and dispute SLAs.</td></tr>
<tr><td><a href="case-pack/governance-response-memo/">Governance Response Memo</a></td><td>Governance for consumer reporting operations.</td><td>CISO defines governance for “report-like” outputs.</td></tr>
<tr class="case-pack-category"><td colspan="3">Legal-technical</td></tr>
<tr><td><a href="case-pack/detailed-narrative-of-event/">Detailed Narrative of Events</a></td><td>Procedural chronology for counsel.</td><td>Legal team chronology from complaint through remand.</td></tr>
<tr><td><a href="case-pack/security-architecture-legal-review/">Security Architecture Explanation for Legal Review</a></td><td>Explain data pipeline architecture for counsel.</td><td>Lead engineer explains ingestion, scoring, and publication paths.</td></tr>
<tr><td><a href="case-pack/risk-register/">Risk Register</a></td><td>Risks tied to accuracy and standing exposure.</td><td>Security Director maintains litigation-informed register.</td></tr>
<tr><td><a href="case-pack/security-decision-documentation/">Security Decision Documentation</a></td><td>Document major data-quality decisions.</td><td>Document decision to add human review for employment fields.</td></tr>
<tr class="case-pack-category"><td colspan="3">Policy and governance</td></tr>
<tr><td><a href="case-pack/security-policy-draft/">Security Policy Draft</a></td><td>Policy for data ingestion and publication.</td><td>Security Director drafts data publication policy.</td></tr>
<tr><td><a href="case-pack/security-governance-memo/">Security Governance Memo</a></td><td>Clarify roles for privacy/security/legal.</td><td>CISO memo on triage for dispute escalations.</td></tr>
<tr><td><a href="case-pack/security-program-justification/">Security Program Justification</a></td><td>Justify accuracy program budget.</td><td>CISO justifies tooling for lineage and monitoring.</td></tr>
<tr><td><a href="case-pack/internal-security-directive/">Internal Security Directive</a></td><td>Mandate verification steps for high-risk fields.</td><td>CISO mandates review gates before publishing certain attributes.</td></tr>
<tr class="case-pack-category"><td colspan="3">Public communication</td></tr>
<tr><td><a href="case-pack/security-public-statement/">Security Public Statement</a></td><td>Accurate marketing about data practices.</td><td>Communications draft aligned to actual verification.</td></tr>
<tr><td><a href="case-pack/customer-security-explanation/">Customer Security Explanation</a></td><td>Explain disputes and corrections to users.</td><td>Customer-facing explanation of dispute process.</td></tr>
<tr><td><a href="case-pack/security-transparency-report-section/">Security Transparency Report Section</a></td><td>Transparency on accuracy efforts.</td><td>Transparency section on data governance metrics.</td></tr>
<tr class="case-pack-category"><td colspan="3">Operational (case-pack specific)</td></tr>
<tr><td><a href="case-pack/audit-packet/">Audit Packet Checklist</a></td><td>Evidence for FCRA procedures audits.</td><td>Checklist for CFPB/FTC-style accuracy examinations (illustrative).</td></tr>
<tr><td><a href="case-pack/implementation-checklist/">Implementation Checklist</a></td><td>0–90 day accuracy program execution.</td><td>Program owner executes remediation after *Spokeo* remand planning.</td></tr>
</tbody>
</table>

## Facts and Timeline

* **Complaint** — Robins sues Spokeo alleging FCRA violations based on alleged inaccuracies in a report about him.

* **District court** — (Procedural history summarized in the Supreme Court opinion; the district court dismissed for lack of standing at one stage of the litigation path described in the opinion.)

* **Ninth Circuit** — Concludes Robins adequately alleged injury in fact (as described by the Supreme Court), focusing on particularization; the Supreme Court finds the analysis incomplete as to **concreteness**.

* **May 16, 2016** — The Supreme Court vacates and remands. *Spokeo, Inc. v. Robins*, 578 U.S. 330 (2016).

* **After remand** — Lower courts continued proceedings consistent with the Supreme Court’s standing framework (follow district and Ninth Circuit dockets for subsequent opinions).

## References

**Primary (official documents)**

- **Supreme Court opinion (PDF, U.S. Reports via Library of Congress)** — *Spokeo, Inc. v. Robins*, 578 U.S. 330 (2016). [PDF](https://tile.loc.gov/storage-services/service/ll/usrep/usrep578/usrep578330/usrep578330.pdf)
- **FCRA (accuracy-related provisions)** — 15 U.S.C. Section 1681e et seq. (Office of Law Revision Counsel). [https://uscode.house.gov/view.xhtml?path=/prelim@title15/chapter41&edition=prelim](https://uscode.house.gov/view.xhtml?path=/prelim@title15/chapter41&edition=prelim)

**Cited**

1. Legal Information Institute. *15 U.S.C. Section 1681e* — Cornell LII. [https://www.law.cornell.edu/uscode/text/15/1681e](https://www.law.cornell.edu/uscode/text/15/1681e)

2. Supreme Court docket and materials — *Spokeo, Inc. v. Robins*, No. 13-1339. [https://www.supremecourt.gov/docket/docketfiles/html/public/13-1339.html](https://www.supremecourt.gov/docket/docketfiles/html/public/13-1339.html)
