# Understanding Regulatory and Court Orders (FTC v. Wyndham Worldwide Corp.)

## Table of contents

- [1. FTC complaint (federal court filing)](#1-ftc-complaint-federal-court-filing)
- [2. District court opinion denying motion to dismiss](#2-district-court-opinion-denying-motion-to-dismiss)
- [3. Third Circuit opinion (799 F.3d 236)](#3-third-circuit-opinion-799-f3d-236)
- [4. Stipulated order for injunction](#4-stipulated-order-for-injunction)
- [5. Consolidated view: requirements and holdings by source](#5-consolidated-view-requirements-and-holdings-by-source)
- [Appendix: Citation format](#appendix-citation-format)

---

## Purpose

Summarize the official complaint, district court and Third Circuit opinions, and stipulated order for this matter: what was alleged, what the courts held at the pleaded stage, and what the settlement order requires—so security, legal, and compliance teams can align controls, evidence, and governance.

---

## 1. FTC complaint (federal court filing)

### Official document

**Complaint for Injunctive and Other Equitable Relief** — *Federal Trade Commission v. Wyndham Worldwide Corporation*, et al.  
Filed June 26, 2012 (D.N.J.; later amended). Matter/File Nos. 1023142 / X120032.

- **Official PDF:** [Complaint (PDF)](https://www.ftc.gov/sites/default/files/documents/cases/2012/06/120626wyndamhotelscmpt.pdf)

### What the complaint alleges (condensed)

The FTC alleged that Wyndham’s cybersecurity practices were **unfair** under Section 5 and that Wyndham’s statements about safeguarding personal information were **deceptive** relative to actual practices. The public allegations emphasize **payment card data** in **property management systems** at Wyndham-branded hotels, **connections** between local hotel systems and **corporate networks**, and **three separate intrusions** between 2008 and 2009 with large-scale exposure of payment card data and substantial fraudulent charges. The complaint describes alleged deficiencies such as **weak access controls**, **default or inadequate credentials**, **insufficient firewall and segmentation**, **failure to remedy known weaknesses between incidents**, and **inadequate incident response**.

### Key interpretation (for security teams)

The complaint frames the issue as **enterprise security program failure in a distributed franchise/property environment**, not a single misconfiguration in isolation. Connections between **property systems** and **corporate infrastructure** are treated as a critical risk surface requiring **governance, technical controls, and monitoring**.

---

## 2. District court opinion denying motion to dismiss

### Official document

**Opinion Denying Wyndham Hotel and Resort LLC’s Motion to Dismiss**  
U.S. District Court, District of New Jersey  
April 7, 2014

- **Official PDF:** [Opinion (PDF)](https://www.ftc.gov/system/files/documents/cases/140407wyndhamopinion.pdf)

### What the opinion does

At the motion-to-dismiss stage, the district court rejected Wyndham’s arguments that the FTC could not proceed under Section 5 unfairness and addressed related pleading issues. The opinion is an early judicial endorsement of the FTC’s **court-enforcement path** for data security unfairness claims in this fact pattern (subject to later appellate review).

---

## 3. Third Circuit opinion (799 F.3d 236)

### Official document

**Opinion of the United States Court of Appeals for the Third Circuit** — *Fed. Trade Comm’n v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015)  
Argued March 3, 2015; filed August 24, 2015.

- **Official PDF (court):** [Third Circuit opinion (PDF)](https://www2.ca3.uscourts.gov/opinarch/143514p.pdf)  
- **Mirror (FTC case file):** [FTC-hosted copy (PDF)](https://www.ftc.gov/system/files/documents/cases/150824wyndhamopinion.pdf)

### Holdings (high level)

The Third Circuit **affirmed** the district court on the issues presented on interlocutory appeal, including that:

- The FTC may regulate **cybersecurity** under the **unfairness** prong of Section 5 (15 U.S.C. § 45(a)), within the constraints of Section 5(n).
- Wyndham had **fair notice** that its alleged conduct could violate Section 5, under the court’s analysis of **standards of unfairness** and the FTC’s prior cybersecurity enforcement history.

The court also addressed Wyndham’s arguments about whether the alleged conduct could be “unfair” as pleaded, assuming the facts as alleged for purposes of the motion-to-dismiss posture.

### Key interpretation (for legal and security leadership)

*Wyndham* is a foundational **appellate precedent** for FTC **Section 5 unfairness** enforcement involving **data security** in networked business models. For operators, the practical lesson is that **unreasonable security** in commerce can be actionable, and **program maturity, monitoring, and repeat failure** matter in regulatory narratives.

---

## 4. Stipulated order for injunction

### Official document

**Stipulated Order for Injunction**  
Filed December 11, 2015

- **Official PDF:** [Stipulated Order (PDF)](https://www.ftc.gov/system/files/documents/cases/151211wyndhamstip.pdf)

### What the order requires (read the order for exact text)

The stipulated order imposes a **comprehensive information security program** to protect **payment card information** and related personal information, with specific attention to risks arising from **network connections between Wyndham-branded hotels and the corporate network**. It includes **long-running assessment** obligations, including assessment under **PCI DSS** as described in the order, with additional certification elements relating to franchise/property connectivity. The order also includes **recordkeeping** and **compliance certification** provisions typical of FTC injunctive settlements.

**Note:** Do not paraphrase numeric durations or technical specifics without checking the PDF; use the order text as the obligation source of truth.

---

## 5. Consolidated view: requirements and holdings by source

| Topic | Complaint | District court (MTD) | Third Circuit | Stipulated order |
| ----- | --------- | ---------------------- | ------------- | ----------------- |
| Unfairness theory for data security | ✓ (alleged) | ✓ (pleading stage) | ✓ (authority / notice framework) | ✓ (program and safeguards) |
| Deception theory (policy vs. practice) | ✓ (alleged) | (MTD stage) | (discussed in opinion) | (ongoing accuracy obligations typical in orders) |
| Franchise/property connectivity risk | ✓ (alleged facts) | — | — | ✓ (explicitly addressed) |
| Assessments / PCI-oriented requirements | — | — | — | ✓ (order text) |

---

## Appendix: Citation format

**FTC Complaint**  
*Federal Trade Commission v. Wyndham Worldwide Corporation*, Complaint for Injunctive and Other Equitable Relief (D.N.J. filed June 26, 2012).  
[https://www.ftc.gov/sites/default/files/documents/cases/2012/06/120626wyndamhotelscmpt.pdf](https://www.ftc.gov/sites/default/files/documents/cases/2012/06/120626wyndamhotelscmpt.pdf)

**Third Circuit**  
*Fed. Trade Comm’n v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015).  
[https://www2.ca3.uscourts.gov/opinarch/143514p.pdf](https://www2.ca3.uscourts.gov/opinarch/143514p.pdf)

**Stipulated Order**  
*Federal Trade Commission v. Wyndham Worldwide Corporation*, Stipulated Order for Injunction (filed Dec. 11, 2015).  
[https://www.ftc.gov/system/files/documents/cases/151211wyndhamstip.pdf](https://www.ftc.gov/system/files/documents/cases/151211wyndhamstip.pdf)

---

**Document-type guide:** [Regulatory Security Explanation](../../../../document-types/regulatory-compliance/regulatory-security-explanation.md)

**Writing tips:** [Writing best practices — Regulatory Security Explanation](../../../../studio/writing-best-practices.md#regulatory-security-explanation)
