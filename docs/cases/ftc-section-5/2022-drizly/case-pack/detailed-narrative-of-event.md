# Detailed Narrative of Events (FTC v. Drizly)

*Chronological factual narrative for legal and regulatory use.*

## Table of contents

1. [Overview](#overview)
2. [Pre-incident environment](#pre-incident-environment)
3. [Prior security incident (2018)](#prior-security-incident-2018)
4. [Initial breach and unauthorized access (2020)](#initial-breach-and-unauthorized-access-2020)
5. [Data exfiltration and discovery](#data-exfiltration-and-discovery)
6. [Regulatory outcome (2022)](#regulatory-outcome-2022)

---

## Overview

The **2020 Drizly data breach** involved unauthorized access to Drizly’s production environment and exfiltration of personal information of approximately **2.5 million consumers**. The attacker gained access by compromising an executive’s GitHub account (using credentials from an unrelated breach) and then using that account to access Drizly’s GitHub repositories, which contained AWS and database credentials stored in source code. Drizly did not detect the breach internally; it learned of the incident from external reports that customer data was offered for sale on dark web forums.

The Federal Trade Commission investigated and, in October 2022, filed an administrative complaint and accepted a consent order requiring Drizly and its CEO to implement a comprehensive information security program, data minimization and retention limits, and biennial independent assessments.

---

## Pre-incident environment

Drizly operated an e-commerce platform enabling local retailers to sell alcohol online. The platform collected and stored personal information, including names, email and postal addresses, phone numbers, device identifiers, order histories, partial payment information, and demographic data purchased from third parties. Passwords were hashed (bcrypt or MD5). Drizly used **Amazon RDS** to host its production database and **GitHub** for source code. Employees accessed Drizly’s GitHub repositories using personal GitHub accounts; the company did not require multifactor authentication or unique, complex passwords for those accounts, and did not use single sign-on for the GitHub organization.

---

## Prior security incident (2018)

In 2018, a Drizly employee posted Drizly AWS credentials to that employee’s **personal public GitHub repository**. The credentials were exploited before Drizly could delete the posting or rotate them; Drizly’s AWS servers were used for cryptocurrency mining until Drizly learned of the exploitation and changed the credentials. The FTC later alleged that after this incident, Drizly was on notice of the risks of exposed credentials and of GitHub access but failed to implement adequate policies, procedures, and technical measures to address those risks.

---

## Initial breach and unauthorized access (2020)

In **April 2018**, an executive was granted access to Drizly’s GitHub repositories to participate in a one-day event. That access was not revoked or monitored after the event. The executive’s GitHub account used a short, reused password and did not use multifactor authentication.

In **early July 2020**, an attacker obtained the executive’s GitHub credentials (e.g., from an unrelated breach) and logged into the executive’s account. The attacker then accessed Drizly’s GitHub repositories, which contained **source code and, in the same repositories, AWS and database credentials**. Drizly had stored these credentials in the repositories despite widely available guidance against doing so. The attacker used the compromised credentials to modify Drizly’s AWS security settings and gain access to Drizly’s production environment, including databases containing consumer personal information.

---

## Data exfiltration and discovery

The attacker exfiltrated Drizly’s **User Table**, comprising more than **2.5 million** consumer records. Drizly did not detect the breach or the exfiltration through its own systems. The company learned of the incident from **media and social media reports** that customer data was being offered for sale on dark web forums (e.g., RaidForums). Personal information exfiltrated from Drizly was offered for sale on at least two publicly accessible forums.

---

## Regulatory outcome (2022)

The Federal Trade Commission investigated and on **October 24, 2022** filed an administrative complaint against Drizly, LLC, and James Cory Rellas (CEO), alleging unfair and deceptive acts or practices in violation of Section 5 of the FTC Act. The same day, the Commission accepted a **Decision and Order** (consent order) that required: (1) a comprehensive information security program; (2) data minimization and a public data retention schedule; (3) biennial independent third-party assessments; (4) reporting and recordkeeping; and (5) for the CEO individually, binding obligations if he moves to another company that collects consumer data from more than 25,000 individuals. No monetary penalty was imposed.

---

## References

- **FTC Complaint** — [In the Matter of Drizly, LLC, and James Cory Rellas](https://www.ftc.gov/system/files/ftc_gov/pdf/202-3185-Drizly-Complaint.pdf), FTC Docket No. 2023185 (Oct. 24, 2022).
- **FTC Decision and Order** — [In the Matter of Drizly, LLC, and James Cory Rellas](https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf), FTC Docket No. 2023185 (Oct. 24, 2022).
- **FTC Press Release** — [FTC Takes Action Against Drizly and Its CEO for Security Failures](https://www.ftc.gov/news-events/news/press-releases/2022/10/ftc-takes-action-against-drizly-its-ceo-james-cory-rellas-security-failures-exposed-data-25-million) (Oct. 24, 2022).
