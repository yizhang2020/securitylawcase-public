# Understanding Regulatory and Court Orders (FTC v. Drizly)

## Table of contents

- [1. FTC Complaint](#1-ftc-complaint)
- [2. FTC Decision and Order](#2-ftc-decision-and-order)
- [3. Consolidated view: requirements by source](#3-consolidated-view-requirements-by-source)
- [Appendix: Citation format](#appendix-citation-format)

---

## Purpose

Provide a structured summary of the FTC complaint and decision and order for this case—official links, alleged practices, binding requirements, and a consolidated requirement view—for security, legal, and compliance alignment.

---

## 1. FTC Complaint

### Official document

**Complaint** — In the Matter of Drizly, LLC, and James Cory Rellas  
Federal Trade Commission, Docket No. 2023185  
October 24, 2022

- **Official PDF:** [FTC Complaint](https://www.ftc.gov/system/files/ftc_gov/pdf/202-3185-Drizly-Complaint.pdf)

The FTC alleged that Drizly failed to use reasonable information security practices and made deceptive statements about security, and that the CEO had authority to control and participated in those practices. The complaint did not seek a monetary penalty; it led to a consent order.

### What the complaint alleges

**Unfair practices (condensed)**  
The FTC alleged that Drizly:

- Failed to develop adequate written information security standards, policies, and procedures; failed to assess or enforce compliance; and failed to implement training.
- Stored AWS and database credentials in GitHub repositories and did not scan repositories for exposed credentials.
- Failed to impose reasonable access controls: no requirement for strong passwords or multifactor authentication for GitHub or database access; inadequate role-based access and offboarding; no restriction of inbound connections or appropriate authentication between applications and production.
- Failed to prevent or detect data loss: no monitoring for exfiltration; inadequate logging and monitoring; no regular assessments of protection measures.
- Failed to test, audit, or assess security features and did not conduct regular risk assessments, vulnerability scans, or penetration testing.
- Had no policy or practice for inventorying and deleting unnecessary consumer personal information.

**Deceptive practices**  
Drizly’s privacy policy stated that it used “standard security practices,” “encryption and firewalls,” and “appropriate safeguards” to protect personal information. The FTC alleged that in light of the above failures, these representations were false or misleading.

**Prior incident**  
In 2018, another employee had posted Drizly AWS credentials to a public GitHub repository; the credentials were exploited before Drizly could rotate them. The FTC alleged that Drizly was on notice of the dangers of exposed credentials and failed to implement appropriate policies and technical measures afterward.

### Key passage and interpretation

> Drizly failed to use reasonable information security practices to protect consumers’ personal information. … Rellas is responsible for this failure, as he did not implement, or properly delegate the responsibility to implement, reasonable information security practices. Indeed, as CEO of Drizly prior to and during the breach, Rellas hired senior executives dedicated to finance, legal, marketing, retail, human resources, product, and analytics, but **failed to hire a senior executive responsible for the security of consumers’ personal information** collected and maintained by Drizly.

The FTC treated security as a **senior leadership and resource allocation** issue, not only a technical one. “Reasonable” security includes assigning clear ownership, written policies, access controls (including MFA and credential hygiene), monitoring, and data retention discipline.

---

## 2. FTC Decision and Order

### Official document

**Decision and Order** — In the Matter of Drizly, LLC, and James Cory Rellas  
Federal Trade Commission, Docket No. 2023185  
October 24, 2022

- **Official PDF:** [Decision and Order (combined consent)](https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf)

The order binds Drizly and the CEO. It requires a comprehensive information security program, data minimization and retention limits, biennial independent assessments, and reporting and recordkeeping. It also imposes **individual obligations on the CEO** if he moves to a company that collects consumer data from more than 25,000 individuals.

### What the order requires

**Information security program**  
Drizly must implement a program that includes: (1) designating a qualified person or persons to coordinate the program; (2) identifying material internal and external risks; (3) implementing safeguards to control those risks (e.g., access controls, credential management, monitoring, secure development); (4) training; (5) testing and monitoring; (6) oversight of service providers; (7) evaluation and adjustment of the program. The program must be documented in writing and supported by evidence.

**Data minimization and retention**  
Respondents must (1) publish a data retention schedule that specifies retention periods and deletion for personal information; (2) delete or de-identify personal information that is no longer necessary for the specified purpose; (3) not collect or use personal information beyond what is necessary. The order restricts future data collection and retention practices.

**Independent assessments**  
A qualified, independent third party must assess the information security program every two years and provide a written report. The assessment must be based on recognized standards and include testing. Respondents must provide the report to the FTC upon request.

**Individual obligations (CEO)**  
If the CEO becomes a senior officer or majority owner of a company that collects or processes personal information from more than 25,000 individuals, that company must implement an information security program that includes the same types of requirements (designation of responsible person, risk assessment, safeguards, etc.), and the CEO must submit a certification and, upon request, the program documentation and assessment report to the FTC. This “follow the person” provision is a notable remedy for individual accountability.

**Reporting and recordkeeping**  
Respondents must retain documents relating to compliance for specified periods and provide them to the FTC upon request.

### Regulatory security requirements summary

The order treats the breach as a **program and governance failure**: lack of written security program, inadequate access control and credential management, insufficient monitoring and detection, and retention of personal data beyond necessity. “Reasonable” security under Section 5, as reflected in this order, includes: **written program**, **designated responsibility**, **access control and MFA**, **no credentials in source code**, **monitoring and testing**, **data minimization and retention schedule**, and **independent assessment**.

---

## 3. Consolidated view: requirements by source

| Requirement area | FTC complaint | FTC order | Example actions |
| -----------------|---------------|-----------|-----------------|
| Written information security program | ✓ | ✓ | Documented program; designated coordinator; risk assessment; safeguards; training; testing; oversight |
| Access control and credential management | ✓ | ✓ | MFA for privileged/sensitive access; no credentials in repos; role-based access; offboarding |
| Monitoring and detection | ✓ | ✓ | Logging; monitoring for exfiltration and anomalous access; regular assessments |
| Data minimization and retention | ✓ | ✓ | Retention schedule; delete or de-identify when no longer necessary; limit collection |
| Independent assessment | — | ✓ | Biennial third-party assessment; report available to FTC |
| Individual accountability (CEO) | ✓ | ✓ | Obligations follow CEO to future companies above threshold |

---

## Appendix: Citation format

**FTC Complaint**  
Federal Trade Commission, *Complaint*, In the Matter of Drizly, LLC, and James Cory Rellas, FTC Docket No. 2023185 (Oct. 24, 2022).  
[https://www.ftc.gov/system/files/ftc_gov/pdf/202-3185-Drizly-Complaint.pdf](https://www.ftc.gov/system/files/ftc_gov/pdf/202-3185-Drizly-Complaint.pdf)

**FTC Decision and Order**  
Federal Trade Commission, *Decision and Order*, In the Matter of Drizly, LLC, and James Cory Rellas, FTC Docket No. 2023185 (Oct. 24, 2022).  
[https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf](https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf)

---

**Document-type guide:** [Regulatory Security Explanation](../../../../document-types/regulatory-compliance/regulatory-security-explanation.md)

**Writing tips:** [Writing best practices — Regulatory Security Explanation](../../../../studio/writing-best-practices.md#regulatory-security-explanation)
