# FTC v. Wyndham Worldwide Corp. (2015) — FTC Section 5, Cybersecurity Unfairness, and Third Circuit Affirmance

## Table of contents

- [Executive Summary](#executive-summary)
- [Regulatory and Legal Outcomes](#regulatory-and-legal-outcomes)
- [Security Technical Summary](#security-technical-summary)
- [Understanding Regulatory and Court Orders](#understanding-regulatory-and-court-orders)
- [Case Pack Documents](#case-pack-documents)
- [Facts and Timeline](#facts-and-timeline)
- [References](#references)

## Executive Summary

The Federal Trade Commission sued Wyndham Worldwide Corporation and related hospitality entities in federal court, alleging that inadequate data security contributed to three payment-card breaches between 2008 and 2009 and that Wyndham’s public statements overstated its security practices. Wyndham moved to dismiss, arguing in part that the FTC lacked authority to regulate cybersecurity through Section 5’s unfairness prong and that it lacked fair notice. The U.S. District Court for the District of New Jersey denied the motion. The U.S. Court of Appeals for the Third Circuit affirmed, holding that the FTC could proceed under Section 5 unfairness and that Wyndham had fair notice that its alleged conduct could violate the statute.

The parties later resolved the enforcement action. In December 2015, the FTC announced a stipulated order requiring a comprehensive information security program for payment card data, addressing risks from connections between franchised properties and corporate systems, and imposing long-running assessment obligations (including PCI DSS–related assessments as described in the order).

## Regulatory and Legal Outcomes

### FTC enforcement (federal court)

The **Federal Trade Commission** pursued injunctive relief under **Section 5** of the FTC Act, alleging **unfair** cybersecurity practices and **deceptive** privacy-policy statements relative to actual practices. The district court allowed the case to proceed; the Third Circuit **affirmed** on the interlocutory appeal regarding FTC authority and fair notice. The matter concluded with a **stipulated order for injunction** (settlement) that imposed detailed program, assessment, and recordkeeping requirements.

### Legal theories (as framed in public court filings)

- **Unfairness:** Alleged failure to implement reasonable security contributed to unauthorized access to consumers’ payment card information and downstream harm, within the framework of Section 5 unfairness analysis (including the limitations in 15 U.S.C. § 45(n)).
- **Deception:** Alleged that Wyndham’s statements about safeguarding personal information were misleading compared with actual practices described in the complaint and court opinions.

## Security Technical Summary

### Summary

The public allegations and opinions describe a **hospitality franchise and property-management environment** in which **property-level systems** handling payment card data were connected to **corporate networks**, with alleged weaknesses in **access controls, segmentation, and security hygiene** that allowed intruders to move from hotel environments to corporate systems. The FTC’s complaint also described **misconfiguration** (e.g., vendor default settings) and **insufficient monitoring and incident response** across repeated intrusions.

### Attack chain (as alleged in public filings)

1. Intruders exploited weaknesses at Wyndham-branded hotel property management environments and gained access to corporate networks through alleged **inadequate segmentation** and **weak remote-access and credential practices**.
2. Attackers accessed and exported **payment card data** for large numbers of accounts across multiple incidents between 2008 and 2009.
3. Fraudulent transactions followed, with **millions of dollars** in fraudulent charges described in public opinions.
4. The FTC alleged that **known deficiencies were not adequately remediated** between incidents, increasing exposure for later breaches.

### Engineering takeaways

**Network segmentation and franchise connectivity**  
- Treat property-to-corporate connectivity as a **high-risk trust boundary**; enforce segmentation, least privilege, and monitored remote access.

**Identity, credentials, and configuration hygiene**  
- Eliminate **default vendor credentials** and weak authentication for remote access; enforce strong authentication and logging for administrative paths.

**Detection, logging, and incident response**  
- Operate monitoring and response capabilities that can detect **cross-segment movement** and **large-scale data export**; document post-incident remediation and control changes.

**Assurance against recurring failure**  
- After a material incident, perform **evidence-backed control uplift** (not only point fixes) and track closure of findings through governance reporting.

**Regulatory posture**  
- Section 5 unfairness cases can turn on whether practices are **reasonable** in context; maintain **documented risk assessment**, **service provider oversight**, and **assessment artifacts** aligned to cardholder-data environments.

## Understanding Regulatory and Court Orders

**Read the originals**—the complaint, district court and Third Circuit opinions, and stipulated order are the authoritative sources. Use [**Understanding regulatory and court orders**](case-pack/understanding-regulator-court-orders.md) to interpret them and translate obligations into security and compliance work.

<table class="case-pack-docs-table">
<thead>
<tr><th>Document</th><th>Date</th><th>Source</th><th>Key obligation or holding</th></tr>
</thead>
<tbody>
<tr><td><a href="https://www.ftc.gov/sites/default/files/documents/cases/2012/06/120626wyndamhotelscmpt.pdf">Complaint for Injunctive and Other Equitable Relief</a></td><td>June 26, 2012</td><td>FTC (D.N.J. filing)</td><td>Alleged unfair and deceptive data security practices related to payment card data and franchise/property systems</td></tr>
<tr><td><a href="https://www.ftc.gov/system/files/documents/cases/140407wyndhamopinion.pdf">Opinion Denying Motion to Dismiss</a></td><td>Apr. 7, 2014</td><td>D.N.J.</td><td>FTC authority and pleading issues at motion-to-dismiss stage</td></tr>
<tr><td><a href="https://www2.ca3.uscourts.gov/opinarch/143514p.pdf"><em>Fed. Trade Comm’n v. Wyndham Worldwide Corp.</em>, 799 F.3d 236 (3d Cir. 2015)</a></td><td>Aug. 24, 2015</td><td>Third Circuit</td><td>Affirmed FTC Section 5 unfairness authority over alleged cybersecurity failures; fair notice analysis</td></tr>
<tr><td><a href="https://www.ftc.gov/system/files/documents/cases/151211wyndhamstip.pdf">Stipulated Order for Injunction</a></td><td>Dec. 11, 2015</td><td>FTC / D.N.J.</td><td>Comprehensive information security program; PCI-related assessments and long-running obligations as specified in the order</td></tr>
</tbody>
</table>

## Case Pack Documents

<table class="case-pack-docs-table">
<thead>
<tr><th>Case Document</th><th>Summary</th><th>Writing Scenario</th></tr>
</thead>
<tbody>
<tr class="case-pack-category"><td colspan="3">Executive and board</td></tr>
<tr><td><a href="case-pack/board-pack/">Board Pack</a></td><td>High-level security status and top risks for the board.</td><td>CISO briefs the Board Audit Committee after the Third Circuit affirmance and stipulated order (early 2016).</td></tr>
<tr><td><a href="case-pack/executive-security-risk-summary/">Executive Security Risk Summary</a></td><td>Consolidated security risks and mitigation for executives.</td><td>Security Director summarizes franchise connectivity and cardholder-data risks for leadership during order implementation.</td></tr>
<tr><td><a href="case-pack/security-program-status-report/">Security Program Status Report</a></td><td>Program health, metrics, and progress for leadership.</td><td>Lead Security Engineer reports program and assessment progress to the CISO after the stipulated order.</td></tr>
<tr><td><a href="case-pack/strategic-security-initiative-justification/">Strategic Security Initiative Justification</a></td><td>Business case for a major security initiative.</td><td>CISO seeks approval for segmentation and property-connectivity remediation aligned to the order.</td></tr>
<tr class="case-pack-category"><td colspan="3">Regulatory and compliance</td></tr>
<tr><td><a href="case-pack/regulatory-security-explanation/">Regulatory Security Explanation</a></td><td>Explain security posture and controls to a regulator.</td><td>CISO explains payment card program and franchise network controls to FTC counsel or an examiner.</td></tr>
<tr><td><a href="case-pack/compliance-justification-document/">Compliance Justification Document</a></td><td>Justify how controls meet a requirement or framework.</td><td>Lead Security Engineer maps controls to the stipulated order and PCI-oriented assessment expectations.</td></tr>
<tr><td><a href="case-pack/controls-evidence/">Controls → Evidence Map</a></td><td>How controls are implemented and evidenced.</td><td>Senior engineer documents evidence for segmentation, logging, and property connectivity controls.</td></tr>
<tr><td><a href="case-pack/governance-response-memo/">Governance Response Memo</a></td><td>Respond to an audit or regulatory request on governance.</td><td>CISO responds to governance questions tied to the order’s program and assessment requirements.</td></tr>
<tr class="case-pack-category"><td colspan="3">Legal-technical</td></tr>
<tr><td><a href="case-pack/detailed-narrative-of-event/">Detailed Narrative of Events</a></td><td>Chronological factual narrative for legal/regulatory use.</td><td>Security or legal prepares a chronology from complaint and court opinions for counsel.</td></tr>
<tr><td><a href="case-pack/security-architecture-legal-review/">Security Architecture Explanation for Legal Review</a></td><td>Explain architecture and controls for counsel.</td><td>Lead Security Engineer explains property-to-corporate architecture and controls for General Counsel.</td></tr>
<tr><td><a href="case-pack/risk-register/">Risk Register</a></td><td>Justify risk acceptance or mitigation for legal/audit.</td><td>Security Director maintains breach- and order-aligned risks for audit.</td></tr>
<tr><td><a href="case-pack/security-decision-documentation/">Security Decision Documentation</a></td><td>Record a significant security decision and rationale.</td><td>Security Director documents decisions on assessor scope and segmentation standards.</td></tr>
<tr class="case-pack-category"><td colspan="3">Policy and governance</td></tr>
<tr><td><a href="case-pack/security-policy-draft/">Security Policy Draft</a></td><td>Draft or update an enterprise security policy.</td><td>Security Director updates standards for franchise and vendor connectivity.</td></tr>
<tr><td><a href="case-pack/security-governance-memo/">Security Governance Memo</a></td><td>Define or clarify governance roles and escalation.</td><td>CISO clarifies ownership for property-managed systems and corporate security requirements.</td></tr>
<tr><td><a href="case-pack/security-program-justification/">Security Program Justification</a></td><td>Justify program scope, resourcing, or structure.</td><td>CISO justifies expanded monitoring and segmentation investment post-order.</td></tr>
<tr><td><a href="case-pack/internal-security-directive/">Internal Security Directive</a></td><td>Directive or mandate from leadership on security.</td><td>CISO mandates controls for remote access and default configurations across properties.</td></tr>
<tr class="case-pack-category"><td colspan="3">Public communication</td></tr>
<tr><td><a href="case-pack/security-public-statement/">Security Public Statement</a></td><td>Draft for press or public breach/incident statement.</td><td>CISO drafts consumer-facing language consistent with accurate security posture.</td></tr>
<tr><td><a href="case-pack/customer-security-explanation/">Customer Security Explanation</a></td><td>Explain a security topic or incident to customers.</td><td>CISO drafts customer notice framing payment card safeguards and monitoring.</td></tr>
<tr><td><a href="case-pack/security-transparency-report-section/">Security Transparency Report Section</a></td><td>Section for an annual or ad-hoc transparency report.</td><td>CISO drafts a transparency section describing program and assessments at a high level.</td></tr>
<tr class="case-pack-category"><td colspan="3">Operational (case-pack specific)</td></tr>
<tr><td><a href="case-pack/audit-packet/">Audit Packet Checklist</a></td><td>What to produce within 48 hours for evidence readiness.</td><td>Checklist for order-related document requests and assessor evidence pulls.</td></tr>
<tr><td><a href="case-pack/implementation-checklist/">Implementation Checklist</a></td><td>0–30 / 30–60 / 60–90 day execution plan.</td><td>Program owner tracks early order implementation milestones.</td></tr>
</tbody>
</table>

## Facts and Timeline

* **June 26, 2012** — The FTC files a federal complaint in the District of New Jersey alleging unfair and deceptive practices related to Wyndham’s protection of consumers’ payment card information.

* **April 7, 2014** — The district court denies Wyndham’s motion to dismiss in relevant part, allowing the FTC’s claims to proceed.

* **Aug. 24, 2015** — The Third Circuit affirms the district court, rejecting Wyndham’s arguments that the FTC lacks Section 5 unfairness authority over the alleged cybersecurity practices and addressing fair notice. *Fed. Trade Comm’n v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015).

* **Dec. 9–11, 2015** — The FTC files and announces a stipulated order resolving the matter, imposing a comprehensive information security program and long-running assessment obligations for payment card data and related connectivity risks.

## References

**Primary (official documents)**

- **FTC matter page** — Wyndham Worldwide Corporation (Matter/File Nos. 1023142 / X120032). [Case timeline and filings](https://www.ftc.gov/legal-library/browse/cases-proceedings/1023142-x120032-wyndham-worldwide-corporation)
- **FTC Complaint** — *Federal Trade Commission v. Wyndham Worldwide Corporation*, et al., filed June 26, 2012 (D.N.J.). [Complaint (PDF)](https://www.ftc.gov/sites/default/files/documents/cases/2012/06/120626wyndamhotelscmpt.pdf)
- **District court opinion** — Order denying motion to dismiss (opinion), Apr. 7, 2014. [Opinion (PDF)](https://www.ftc.gov/system/files/documents/cases/140407wyndhamopinion.pdf)
- **Third Circuit opinion** — *Fed. Trade Comm’n v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. Aug. 24, 2015). [Opinion (PDF)](https://www2.ca3.uscourts.gov/opinarch/143514p.pdf)
- **Stipulated order** — Stipulated Order for Injunction, Dec. 11, 2015. [Order (PDF)](https://www.ftc.gov/system/files/documents/cases/151211wyndhamstip.pdf)

**Cited**

1. Federal Trade Commission. *Wyndham Settles FTC Charges It Unfairly Placed Consumers’ Payment Card Information At Risk*, Dec. 9, 2015. [Press release](https://www.ftc.gov/news-events/news/press-releases/2015/12/wyndham-settles-ftc-charges-it-unfairly-placed-consumers-payment-card-information-risk)

2. Federal Trade Commission. *Statement from FTC Chairwoman Edith Ramirez on Appellate Ruling in the Wyndham Hotels and Resorts Matter*, Aug. 24, 2015. [Press release](https://www.ftc.gov/news-events/news/press-releases/2015/08/statement-ftc-chairwoman-edith-ramirez-appellate-ruling-wyndham-hotels-resorts-matter)
