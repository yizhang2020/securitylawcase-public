# In the Matter of Zoom Video Communications, Inc. (2020) — Encryption Claims, Mac Update, and FTC Security Order

## Table of contents

- [Executive Summary](#executive-summary)
- [Regulatory and Legal Outcomes](#regulatory-and-legal-outcomes)
- [Security Technical Summary](#security-technical-summary)
- [Understanding Regulatory and Court Orders](#understanding-regulatory-and-court-orders)
- [Case Pack Documents](#case-pack-documents)
- [Facts and Timeline](#facts-and-timeline)
- [References](#references)

## Executive Summary

In November 2020, the Federal Trade Commission announced a proposed settlement with Zoom Video Communications, Inc. The FTC alleged that Zoom deceived users about the level of security provided for Zoom meetings, including claims about "end-to-end, 256-bit encryption," and that Zoom misled cloud-recording users about when recordings were encrypted. The FTC also alleged that Zoom unfairly undermined a Safari browser safeguard when a July 2018 Mac update installed the ZoomOpener web server without adequate notice or consent.

The Commission finalized the order in January 2021 and announced final approval in February 2021. The order requires a comprehensive information security program, security review of software updates, independent biennial assessments, Commission notification for covered incidents, and restrictions on privacy and security misrepresentations. The matter was resolved by consent; it is an enforcement and remediation record, not a litigated court holding.

## Regulatory and Legal Outcomes

### FTC Enforcement

The FTC alleged deceptive and unfair practices under Section 5 of the FTC Act. The deception theory focused on public and product statements about encryption and cloud-recording protection. The unfairness theory focused on the Mac ZoomOpener web server, which allegedly bypassed a Safari safeguard, increased the risk of remote video surveillance by strangers, persisted after deletion of the Zoom app, and could reinstall the app in certain circumstances.

### Legal Theory

- **Deception:** Security and privacy claims must match actual architecture, cryptographic key custody, storage behavior, and product operation.
- **Unfairness:** Product changes that undermine user security controls can create unreasonable injury risk even when framed as convenience features.
- **Order compliance:** A comprehensive security program must be documented, measured, assessed, and embedded into software release and claims-review workflows.

## Security Technical Summary

### Summary

The FTC matter centered on gaps between security representations and product behavior. The FTC alleged that Zoom did not provide end-to-end encryption for all meetings because Zoom maintained cryptographic keys that could allow access to meeting content. It alleged Zoom secured meetings in part with a lower level of encryption than promised and stored some cloud recordings unencrypted on Zoom servers for up to 60 days before transfer to secure cloud storage. It also alleged that a Mac update installed ZoomOpener, which bypassed a Safari security prompt and remained after app deletion.

### Engineering Takeaways

**Security claims and architecture**

- Validate every encryption, privacy, and security representation against implemented design and key custody.
- Maintain an approval workflow for claims used in product UI, marketing, blogs, and customer materials.

**Secure release governance**

- Review software updates for security impact before release, including interactions with browser and operating-system safeguards.
- Document release notes accurately and require Legal/Security review for security-sensitive changes.

**Program and evidence readiness**

- Maintain annual risk assessments, vulnerability management, MFA and credential controls, data deletion controls, and incident notification processes.
- Preserve evidence for independent biennial assessments and potential FTC review.

## Understanding Regulatory and Court Orders

**Read the originals**—the FTC complaint, final order, and FTC press releases below are the authoritative sources. Use the [**Understanding regulatory and court orders**](case-pack/understanding-regulator-court-orders.md) page to convert order language into operational obligations.

<table class="case-pack-docs-table">
<thead>
<tr><th>Document</th><th>Date</th><th>Source</th><th>Key obligation or allegation</th></tr>
</thead>
<tbody>
<tr><td><a href="https://www.ftc.gov/system/files/documents/cases/1923167zoomcomplaint.pdf">Complaint — In the Matter of Zoom Video Communications, Inc.</a></td><td>Nov. 9, 2020</td><td>FTC</td><td>Alleged deception about encryption and cloud recordings; unfair Mac ZoomOpener deployment</td></tr>
<tr><td><a href="https://www.ftc.gov/system/files/documents/cases/1923167_c-4731_zoom_final_order.pdf">Decision and Order — Zoom Video Communications, Inc.</a></td><td>Jan. 19, 2021</td><td>FTC</td><td>Comprehensive security program, update review, assessments, breach notification, misrepresentation prohibition</td></tr>
</tbody>
</table>

## Case Pack Documents

<table class="case-pack-docs-table">
<thead>
<tr><th>Case Document</th><th>Summary</th><th>Writing Scenario</th></tr>
</thead>
<tbody>
<tr class="case-pack-category"><td colspan="3">Executive and board</td></tr>
<tr><td><a href="case-pack/board-pack/">Board Pack</a></td><td>Board briefing on FTC order response and trust remediation.</td><td>CISO briefs the Board Audit Committee after the proposed FTC settlement.</td></tr>
<tr><td><a href="case-pack/executive-security-risk-summary/">Executive Security Risk Summary</a></td><td>Executive view of deception, software-update, and program risks.</td><td>Security Director summarizes Zoom order obligations for CEO and leadership.</td></tr>
<tr><td><a href="case-pack/security-program-status-report/">Security Program Status Report</a></td><td>Program status against FTC order obligations.</td><td>Program owner reports progress to CISO and General Counsel.</td></tr>
<tr><td><a href="case-pack/strategic-security-initiative-justification/">Strategic Security Initiative Justification</a></td><td>Business case for security-by-design and encryption claims governance.</td><td>CISO requests funding for order remediation initiative.</td></tr>
<tr class="case-pack-category"><td colspan="3">Regulatory and compliance</td></tr>
<tr><td><a href="case-pack/regulatory-security-explanation/">Regulatory Security Explanation</a></td><td>Plain-language explanation of controls for FTC-facing review.</td><td>Security lead explains program design to FTC staff.</td></tr>
<tr><td><a href="case-pack/compliance-justification-document/">Compliance Justification Document</a></td><td>Maps controls to FTC order obligations.</td><td>GRC lead justifies controls for counsel and assessor.</td></tr>
<tr><td><a href="case-pack/controls-evidence/">Controls Evidence Map</a></td><td>Evidence map for order compliance.</td><td>Control owners prepare evidence package for independent assessment.</td></tr>
<tr><td><a href="case-pack/governance-response-memo/">Governance Response Memo</a></td><td>Governance response to regulator or assessor questions.</td><td>CISO responds to audit request about program oversight.</td></tr>
<tr class="case-pack-category"><td colspan="3">Legal-technical</td></tr>
<tr><td><a href="case-pack/detailed-narrative-of-event/">Detailed Narrative of Event</a></td><td>Chronology of alleged statements, cloud recording handling, and Mac update issue.</td><td>Legal and security prepare factual narrative for counsel.</td></tr>
<tr><td><a href="case-pack/security-architecture-legal-review/">Security Architecture Explanation for Legal Review</a></td><td>Architecture/legal review of encryption, key handling, and update safety.</td><td>Lead engineer explains technical posture to General Counsel.</td></tr>
<tr><td><a href="case-pack/risk-register/">Risk Register</a></td><td>Risk register for claims, cryptography, update, and evidence risks.</td><td>Security Director maintains risk register for remediation steering committee.</td></tr>
<tr><td><a href="case-pack/security-decision-documentation/">Security Decision Documentation</a></td><td>Decision record for encryption-claims review and release gating.</td><td>Security Director records control decision for counsel and product leadership.</td></tr>
<tr class="case-pack-category"><td colspan="3">Policy and governance</td></tr>
<tr><td><a href="case-pack/security-policy-draft/">Security Policy Draft</a></td><td>Policy draft for security claims, cryptography, and software updates.</td><td>Security Director drafts enterprise policy for CISO approval.</td></tr>
<tr><td><a href="case-pack/security-governance-memo/">Security Governance Memo</a></td><td>Governance model for product security, legal review, and order compliance.</td><td>CISO issues governance memo to product, engineering, legal, and marketing.</td></tr>
<tr><td><a href="case-pack/security-program-justification/">Security Program Justification</a></td><td>Program scope and resourcing rationale under FTC order.</td><td>CISO presents program justification to executive team.</td></tr>
<tr><td><a href="case-pack/internal-security-directive/">Internal Security Directive</a></td><td>Directive for encryption representations and secure update review.</td><td>CISO mandates immediate operating changes.</td></tr>
<tr class="case-pack-category"><td colspan="3">Public communication</td></tr>
<tr><td><a href="case-pack/security-public-statement/">Security Public Statement</a></td><td>Public-facing security statement aligned with order restrictions.</td><td>Communications team drafts public statement with Legal and Security.</td></tr>
<tr><td><a href="case-pack/customer-security-explanation/">Customer Security Explanation</a></td><td>Customer explanation of meeting security changes.</td><td>Security and customer trust team explains controls to enterprise customers.</td></tr>
<tr><td><a href="case-pack/security-transparency-report-section/">Security Transparency Report Section</a></td><td>Transparency-report section on FTC order remediation.</td><td>CISO drafts annual trust report section.</td></tr>
<tr class="case-pack-category"><td colspan="3">Operational</td></tr>
<tr><td><a href="case-pack/audit-packet/">Audit Packet Checklist</a></td><td>Evidence checklist for order and assessment readiness.</td><td>GRC lead assembles regulator or assessor packet within 48 hours.</td></tr>
<tr><td><a href="case-pack/implementation-checklist/">Implementation Checklist</a></td><td>0-30 / 30-60 / 60-90 day implementation plan.</td><td>Program owner drives near-term execution against order obligations.</td></tr>
</tbody>
</table>

## Facts and Timeline

* **June 2016 onward** — FTC materials state that Zoom represented that users could secure meetings with end-to-end encryption and made related statements about 256-bit encryption.

* **July 2018** — Zoom deployed a Mac desktop update that installed the ZoomOpener web server, which the FTC alleged bypassed a Safari browser safeguard and remained after users deleted the Zoom app.

* **July 2019** — Apple removed the ZoomOpener web server from users' computers through an automatic update, according to FTC materials.

* **December 2019 to April 2020** — FTC materials state Zoom's user base grew from about 10 million to 300 million during the COVID-19 pandemic.

* **Nov. 9, 2020** — The FTC announced an administrative complaint and proposed settlement requiring a comprehensive security program and related relief.

* **Jan. 19, 2021** — The Commission voted 3-2 to finalize the settlement.

* **Feb. 1, 2021** — The FTC announced final approval of the Zoom settlement.

## References

**Primary (official documents)**

- **FTC case page** — *Zoom Video Communications, Inc., In the Matter of*, FTC Matter/File No. 192 3167. [https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3167-zoom-video-communications-inc-matter](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3167-zoom-video-communications-inc-matter)
- **FTC Complaint** — *In the Matter of Zoom Video Communications, Inc.*, Nov. 9, 2020. [Complaint (PDF)](https://www.ftc.gov/system/files/documents/cases/1923167zoomcomplaint.pdf)
- **FTC Decision and Order** — *In the Matter of Zoom Video Communications, Inc.*, Docket No. C-4731, issued Jan. 19, 2021. [Decision and Order (PDF)](https://www.ftc.gov/system/files/documents/cases/1923167_c-4731_zoom_final_order.pdf)

**Cited**

1. Federal Trade Commission. *FTC Requires Zoom to Enhance its Security Practices as Part of Settlement*, Nov. 9, 2020.  
   [https://www.ftc.gov/news-events/news/press-releases/2020/11/ftc-requires-zoom-enhance-its-security-practices-part-settlement](https://www.ftc.gov/news-events/news/press-releases/2020/11/ftc-requires-zoom-enhance-its-security-practices-part-settlement)

2. Federal Trade Commission. *FTC Gives Final Approval to Settlement with Zoom over Allegations the Company Misled Consumers about Its Data Security Practices*, Feb. 1, 2021.  
   [https://www.ftc.gov/news-events/news/press-releases/2021/02/ftc-gives-final-approval-settlement-zoom-over-allegations-company-misled-consumers-about-its-data](https://www.ftc.gov/news-events/news/press-releases/2021/02/ftc-gives-final-approval-settlement-zoom-over-allegations-company-misled-consumers-about-its-data)

3. Federal Register. *Zoom Video Communications, Inc.; Analysis to Aid Public Comment*, Nov. 13, 2020.  
   [https://www.federalregister.gov/documents/2020/11/13/2020-25130/zoom-video-communications-inc-analysis-to-aid-public-comment](https://www.federalregister.gov/documents/2020/11/13/2020-25130/zoom-video-communications-inc-analysis-to-aid-public-comment)
