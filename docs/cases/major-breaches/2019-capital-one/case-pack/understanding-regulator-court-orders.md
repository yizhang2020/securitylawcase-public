# Understanding Regulatory and Court Orders


## Table of contents

- [1. OCC Cease and Desist Order](#1-occ-cease-and-desist-order)
- [2. Federal Reserve Enforcement Order](#2-federal-reserve-enforcement-order)
- [3. Class Action Settlement — Federal Court](#3-class-action-settlement-federal-court)
- [4. Consolidated view: requirements by source](#4-consolidated-view-requirements-by-source)
- [Appendix: Citation Format](#appendix-citation-format)

---

## 1. OCC Cease and Desist Order

### Official document

**Cease and Desist Order** — Office of the Comptroller of the Currency  
August 6, 2020

- **Official PDF:** [ea2020-037.pdf](https://www.occ.gov/static/enforcement-actions/ea2020-037.pdf)
- **Related announcement:** [OCC News Release nr-occ-2020-101](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html)

The OCC assessed an **$80 million civil money penalty** and required the bank to strengthen risk management, cloud risk assessment, audit oversight, and board-level compliance, and to provide periodic remediation reports.

### What the order says

**Findings (condensed)**  
The OCC concluded that Capital One:

- failed to establish **effective risk assessment processes before migrating operations to public cloud**
- failed to **identify and correct internal control deficiencies in a timely manner**
- engaged in **unsafe or unsound banking practices**

**Legal basis**  
12 C.F.R. Part 30 (Safety and Soundness), Interagency Guidelines on Information Security, and Gramm–Leach–Bliley Act information security requirements.

**Required actions**  
The bank had to strengthen enterprise risk management, improve cloud risk assessment, strengthen audit oversight, create board-level compliance oversight, and submit periodic remediation reports to the regulator.

### Key passage and interpretation

> The OCC took these actions based on the bank's **failure to establish effective risk assessment processes prior to migrating significant information technology operations to the public cloud environment** and the bank's **failure to correct the deficiencies in a timely manner**. … The OCC found the noted deficiencies to constitute **unsafe or unsound practices** and resulted in **noncompliance with 12 C.F.R. Part 30, Appendix B, "Interagency Guidelines Establishing Information Security Standards."**

Regulators did not cite "one misconfigured WAF" in isolation. They cited the **absence of a defined, repeatable risk assessment process before** a major cloud migration and the **absence of a process to find and fix control gaps in a timely way**. "Effective" means documented, executed before the migration, and tied to the actual environment. "Timely" correction implies ongoing monitoring and remediation with clear ownership and deadlines.

> While the OCC encourages responsible innovation in all banks it supervises, **sound risk management and internal controls are critical to ensuring bank operations remain safe and sound and adequately protect their customers.**

Innovation (including cloud adoption) is allowed, but it must be backed by **risk management and internal controls** that examiners can review. "Sound" and "adequate" are legal/regulatory standards: you must be able to **demonstrate** that controls were designed and operating—via policies, baselines, testing, and audit.

### Regulatory Security Requirements Summary

Regulators did not focus only on "fix the one misconfiguration." They treated the breach as a **program and process failure**: risk assessment before and around cloud use, ongoing identification and correction of control gaps, and governance and audit so that deficiencies are found and fixed in time. "Effective" risk assessment means a **repeatable, documented process** that happens before significant cloud adoption or changes, not a one-time review. "Identify and correct in a timely manner" implies **continuous control monitoring**, **drift detection**, and **remediation workflows** with clear ownership and deadlines.

### Derived technical and programmatic requirements

Use these to align your program with what the OCC order effectively required:

- **Pre–cloud and ongoing risk assessment** — Establish and document a risk assessment process that runs **before** migrating workloads to public cloud and when making material changes; update when the environment or threat landscape changes.
- **Cloud configuration governance** — Define and maintain **baselines** for cloud security controls (e.g., WAF rules, metadata service access, network segmentation); implement **change approval** and **drift detection** so deviations are detected and corrected in a timely manner.
- **Internal control identification and remediation** — Maintain a **control inventory** and map controls to risks; have a process to **identify deficiencies** (via assessments, audits, or monitoring) and **remediate with target dates** and accountability.
- **Audit and testing** — Strengthen **audit coverage** of cloud and third-party environments; retain **evidence** of control design and operating effectiveness (e.g., config baselines, test results, exception tracking).
- **Board and management oversight** — Ensure **board-level compliance and risk oversight** (e.g., committee charter, reporting); management must own risk decisions and remediation with clear escalation and reporting to the board and regulator.
- **Remediation reporting** — Be able to **report periodically to the regulator** on remediation status, with supporting evidence (policies, configs, test results) that examiners can review.

---

## 2. Federal Reserve Enforcement Order

### Official document

**Enforcement Order** — Federal Reserve Board  
August 6, 2020

- **Official PDF:** [enf20200806a1.pdf](https://www.federalreserve.gov/newsevents/pressreleases/files/enf20200806a1.pdf)

This order applied to the **holding company**. It did not impose a monetary penalty but required the **board of directors to submit a plan** to strengthen risk management and internal controls related to **data protection**.

### What the order says

The Federal Reserve required the board to submit a plan addressing risk management and internal controls for data protection. The emphasis is on **governance and board accountability**: the board must own and approve the plan, not only IT or security.

### Key passage and interpretation

> The Board … is **requiring it to enhance its risk-management program and related governance and controls, specifically around cybersecurity and information security.**

The requirement is at the **holding-company level** and targets **program, governance, and controls**—not only a technical fix. "Enhance" means the board must adopt a plan that improves how the organization manages cyber and information security risk and how it governs and operates controls. Engineers should ensure **technical controls** (e.g., configuration governance, access control, detection) are **explicitly linked** to that program and to board-level reporting, so examiners can trace from board oversight to implementation.

### Regulatory Security Requirements Summary

"Plan to strengthen risk management and internal controls related to data protection" implies:

- **Written, board-approved plan** that describes how the organization will manage risk and maintain internal controls over data (including in cloud).
- **Control environment** that is defined, documented, and auditable — e.g., policies, standards, control ownership, and evidence that controls operate as intended.
- **Data protection** interpreted broadly: access control, encryption, configuration management, monitoring, and incident response, aligned with the kind of failure seen in this case (cloud configuration and access).

Engineers should ensure that technical controls (config governance, IAM, logging, detection) are **explicitly tied to** that plan and to board reporting, so examiners can see a clear line from board oversight to technical execution.

### Derived technical and programmatic requirements

- **Board-approved data protection and risk plan** — Document a **plan** (or program description) that covers cloud and data protection risks, control objectives, and how the board oversees them; obtain **board approval** and keep it current.
- **Control documentation and evidence** — Maintain **policies and standards** for data protection and cloud security; maintain **evidence** of implementation (e.g., config baselines, test results, exception logs) that support the plan.
- **Ownership and accountability** — Assign **clear ownership** for key controls and risk areas; ensure **reporting to the board** on risk, control effectiveness, and material issues so the board can exercise oversight.

---

## 3. Class Action Settlement — Federal Court

### Official document

**Final Order and Judgment Approving Class Settlement**  
U.S. District Court, Eastern District of Virginia

- **Official PDF:** [Final Approval Order (PDF)](https://www.capitalonesettlement.com/Content/Documents/Final%20Approval%20Order.pdf)

**Case:** *In re Capital One Consumer Data Security Breach Litigation*, MDL No. 1:19-md-02915  
**Settlement approved:** February 2022

The settlement established a **$190 million** compensation fund for affected consumers (reimbursement, identity protection, credit monitoring). Approximately **106 million individuals** were affected.

### What the settlement reflects

The underlying lawsuits alleged **failure to implement reasonable safeguards**, **failure to detect the breach promptly**, and **failure to protect sensitive information**. The settlement does not create new legal obligations for other organizations, but it **reflects what plaintiffs claimed was lacking**: reasonable technical and organizational measures, effective detection, and adequate protection of personal data. Regulators' findings in the OCC (and Fed) orders are consistent with those themes.

### IRAC Report

**Issue**  
Whether the proposed class action settlement is **fair, reasonable, and adequate** under Federal Rule of Civil Procedure 23(e), and whether certification of the settlement class is proper.

**Rule**  
1. Fed. R. Civ. P. 23(e) requires court approval of a class action settlement and a finding that the settlement is fair, reasonable, and adequate.  
2. The court must satisfy itself that the settlement, as a whole, is a fair, adequate, and reasonable **resolution of the class claims asserted**—not that every class member is fully satisfied.  
3. Approval is not a substantive adjudication of the underlying causes of action; the court need not definitively determine whether the plaintiffs proved their claims.  
4. Common questions predominate where class members assert injury from the same conduct (e.g., exposure of personal data in a single breach) and the same legal theories.

**Analysis**  
*Plaintiffs' argument.* The representative plaintiffs alleged that **Capital One** (and Amazon) failed to implement reasonable safeguards, failed to detect the breach promptly, and failed to protect sensitive information. They asserted negligence, negligence per se, breach of express and implied contract (including a duty to provide safeguards for personal information), unjust enrichment, and state statutory claims. Plaintiffs contended that the breach and the exposure of roughly 98 million individuals' data supported class-wide liability and that a **$190 million** settlement fund, together with identity protection and credit monitoring, was a fair and adequate resolution of those claims.

*Capital One's counter-argument.* **Capital One** moved to dismiss the representative complaint in its entirety and later moved for summary judgment on plaintiffs' claims. It challenged, among other things, whether plaintiffs had sufficiently alleged a duty of care (including under Virginia law), whether they had Article III standing, and whether class certification was appropriate. Capital One did not admit liability; settlement approval does not require the court to decide the merits of those defenses.

*Court's analysis and final opinion.* The court did not decide the underlying merits. It evaluated whether the settlement was fair, reasonable, and adequate under Rule 23(e), whether the settlement class satisfied Rule 23(a) and (b)(3), and whether notice and the claims process were adequate. The court stated:

> Nothing has occurred that would alter the Court's initial determination that the Settlement is fair, reasonable, and adequate. In fact, the response of the class members to the Settlement further underscores that the Settlement is, in fact, fair, reasonable, and adequate.

It also relied on the principle that **"the issue is not whether everyone affected by the settlement is completely satisfied. Instead, the test is whether the settlement, as a whole, is a fair, adequate, and reasonable resolution of the class claims asserted."** The court granted final approval of the settlement and certified the settlement class.

**Conclusion**  
The court held that the settlement is **"fair, reasonable, and adequate"** and granted final approval. That conclusion does not mean the court found Capital One liable on the merits; it means the court found the *compromise*—the $190 million fund, identity protection, and monitoring—to be a fair and adequate resolution of the *asserted* claims (failure to implement reasonable safeguards, failure to detect promptly, failure to protect sensitive information).  

*Interpretation for security engineers.* The claims that were *resolved* by this settlement are the same themes regulators emphasized: **reasonable safeguards** (e.g., risk assessment, configuration governance, timely correction of deficiencies), **prompt detection** (monitoring, logging, incident response), and **protection of sensitive information** (controls and evidence). For engineers, the takeaway is to align controls and evidence with those themes so that, in a similar matter, the organization can show that safeguards were reasonable, detection was in place, and protection was documented and operable.

### Regulatory Security Requirements Summary

Treat the settlement as a **signal** of what "reasonable" and "prompt" can mean in hindsight after a cloud configuration failure:

- **Reasonable safeguards** — In this case, regulators pointed to pre-migration risk assessment, cloud configuration governance, and timely correction of control deficiencies. For engineers, that translates to: **baselines, change control, drift detection, and least-privilege access** so that a single misconfiguration cannot lead to mass data access.
- **Prompt detection** — Plaintiffs argued the breach was not detected soon enough. That supports **monitoring and logging** (e.g., metadata service access, SSRF patterns, anomalous S3 or API access) and **incident response** that can contain and assess quickly.
- **Protection of sensitive information** — Map data to controls (encryption, access control, configuration of storage and network). Be able to **show** that controls were designed and operating; courts and regulators look for **evidence**, not assertions.


### Derived technical and programmatic requirements

- **Safeguards aligned with "reasonable"** — Implement and document **cloud configuration governance** (WAF, metadata service, IAM, network) and **least privilege**; retain **evidence** of baselines, reviews, and testing so you can show what was in place before an incident.
- **Detection and response** — Deploy **detection** for SSRF, credential abuse, and anomalous access to sensitive data; **retain logs** for investigation and legal/regulatory use; have **incident response** that can contain, assess, and notify in line with legal and regulatory expectations.
- **Evidence of protection** — Maintain **control-to-evidence mapping** (e.g., policy → standard → config → test result) so you can produce, under pressure, proof of design and operation of controls over sensitive data.

---

## 4. Consolidated view: requirements by source

Use this table to map **what you build or improve** back to **which primary source** it supports. It helps when justifying scope to leadership, audit, or counsel.

| Requirement area | OCC order | Fed order | Court settlement (themes) | Example actions |
| ----------------- | --------- | --------- | -------------------------- | ---------------- |
| Cloud risk assessment before/after migration | ✓ | ✓ | (reasonable safeguards) | Documented risk assessment; updates when architecture or threats change |
| Cloud configuration baseline and drift detection | ✓ | ✓ | ✓ | WAF/metadata/IAM baselines; change approval; automated drift detection and remediation |
| Timely identification and correction of control deficiencies | ✓ | ✓ | ✓ | Control inventory; deficiency tracking; remediation with dates and owners |
| Board-approved plan and oversight | ✓ | ✓ | — | Board-approved data protection/risk plan; regular reporting to board |
| Audit and evidence for examiners | ✓ | ✓ | ✓ | Audit coverage of cloud; policies, configs, test results available for review |
| Detection, logging, and incident response | ✓ | (internal controls) | ✓ | Monitoring for SSRF, credential abuse; log retention; IR playbooks |

---

## Appendix: Citation Format

When citing these documents in papers or deliverables:

**OCC**  
Office of the Comptroller of the Currency, *Cease and Desist Order — Capital One, N.A.*, Aug. 6, 2020.  
[https://www.occ.gov/static/enforcement-actions/ea2020-037.pdf](https://www.occ.gov/static/enforcement-actions/ea2020-037.pdf)

**Federal Reserve**  
Federal Reserve Board, *Enforcement Order — Capital One Financial Corporation*, Aug. 6, 2020.  
[https://www.federalreserve.gov/newsevents/pressreleases/files/enf20200806a1.pdf](https://www.federalreserve.gov/newsevents/pressreleases/files/enf20200806a1.pdf)

**Court**  
*In re Capital One Consumer Data Security Breach Litigation*, U.S. District Court, E.D. Virginia, Final Approval Order (Feb. 2022).  
[https://www.capitalonesettlement.com/Content/Documents/Final%20Approval%20Order.pdf](https://www.capitalonesettlement.com/Content/Documents/Final%20Approval%20Order.pdf)
