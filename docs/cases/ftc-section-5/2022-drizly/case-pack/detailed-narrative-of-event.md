## Detailed Narrative of Events

*(Extended Documentation for the FTC v. Drizly, LLC (2022) Case Study)*

### Table of contents

1. [Overview](#overview)
2. [Pre-incident environment](#pre-incident-environment)
3. [Prior security incident (2018)](#prior-security-incident-2018)
4. [Initial breach and unauthorized access (July 2020)](#initial-breach-and-unauthorized-access-july-2020)
5. [Data exfiltration and attacker activity](#data-exfiltration-and-attacker-activity)
6. [Data types and volume](#data-types-and-volume)
7. [External discovery of the breach](#external-discovery-of-the-breach)
8. [Internal investigation and containment](#internal-investigation-and-containment)
9. [Regulatory investigation and resolution (2022)](#regulatory-investigation-and-resolution-2022)

---

## Overview

The **2020 Drizly data breach** involved unauthorized access to Drizly’s production environment and exfiltration of personal information relating to approximately **2.5 million consumers**. The attacker compromised an executive’s **GitHub** account (using credentials obtained from an unrelated breach), accessed Drizly’s **GitHub repositories** containing **AWS and database credentials** stored in source code, modified **AWS** security settings, and exfiltrated a **User Table** from Drizly’s production databases.

Drizly **did not detect** the intrusion through its own monitoring in the first instance; it learned that customer data was being offered for sale from **media and social media** reports referencing **dark web forums**. The **Federal Trade Commission** investigated and, on **October 24, 2022**, filed an administrative complaint and accepted a **consent order** against Drizly, LLC, and James Cory Rellas (CEO), alleging **unfair** and **deceptive** practices under **Section 5** of the FTC Act. The order requires a comprehensive **information security program**, **data minimization** and a **retention schedule**, **biennial independent assessments**, and—unusually—**individual obligations** on the CEO in future roles at covered companies. No monetary penalty was imposed.

---

## Pre-incident environment

Drizly operated an e-commerce platform that enabled local retailers to sell alcohol for delivery. The platform collected and stored substantial **personal information**, including names, email and postal addresses, phone numbers, device identifiers, order histories, partial payment information, and demographic data purchased from third parties. Passwords were stored using **hashed** formats (e.g., bcrypt or MD5).

Drizly hosted its production database on **Amazon RDS** and used **GitHub** for source code. Employees accessed Drizly’s GitHub organization using **personal GitHub accounts**. Drizly did **not** require **multifactor authentication** or strong, unique passwords for those accounts, and did not use **single sign-on** for the GitHub organization—conditions that increased exposure to **credential reuse** and **account takeover**.

---

## Prior security incident (2018)

In **2018**, a Drizly employee posted **Drizly AWS credentials** to the employee’s **personal public GitHub repository**. Third parties exploited those credentials before Drizly could remove the posting or rotate them; Drizly’s AWS servers were used for **cryptocurrency mining** until Drizly learned of the exploitation and changed the credentials.

The FTC later alleged that after this incident Drizly was **on notice** of risks from exposed credentials and GitHub access, but failed to implement adequate policies, procedures, and technical measures—including MFA, secrets hygiene, and monitoring—to prevent recurrence.

---

## Initial breach and unauthorized access (July 2020)

In **April 2018**, an executive was granted access to Drizly’s GitHub repositories to participate in a **one-day event**. That access was **not revoked** or meaningfully monitored afterward. The executive’s GitHub account used a **short, reused password** and did **not** use multifactor authentication.

In **early July 2020**, an attacker obtained the executive’s GitHub credentials (for example, from **credential stuffing** or a leak from an unrelated breach) and logged into the executive’s account. The attacker accessed Drizly repositories that contained **source code** and, in the same repositories, **AWS and database credentials**. Despite widely available industry guidance against storing secrets in repositories, those credentials enabled the attacker to **modify AWS security settings** and obtain access to Drizly’s **production environment**, including databases holding consumer personal information.

---

## Data exfiltration and attacker activity

The attacker exfiltrated Drizly’s **User Table**, comprising more than **2.5 million** consumer records. Public descriptions of the incident emphasize that Drizly’s own detective controls did **not** surface the exfiltration in real time; the company’s later understanding depended on **external** reporting and investigation.

---

## Data types and volume

Affected information included, among other fields, consumer **names**, **email addresses**, **phone numbers**, **delivery addresses**, **order information**, **dates of birth** (where collected), **hashed passwords**, and related account metadata—reflecting the User Table’s role in account and order management.

---

## External discovery of the breach

Drizly **did not** first learn of the breach from internal alerts alone. The company became aware that customer data was **offered for sale** on **dark web forums** (including, in public reporting, references to forums such as **RaidForums**) after **media and social media** attention. That **external discovery** pattern resembles other matters where **underground market visibility** precedes formal internal confirmation.

---

## Internal investigation and containment

After the incident became known, Drizly initiated **internal investigation** steps consistent with incident response practice: validating unauthorized access, identifying affected systems, rotating credentials, tightening access controls, and preserving records for regulators and law enforcement. Forensic and operational specifics are typically documented in non-public materials; this narrative summarizes publicly alleged themes from FTC and press sources.

---

## Regulatory investigation and resolution (2022)

The **FTC** investigated Drizly’s security practices and public representations. On **October 24, 2022**, the Commission filed an administrative **complaint** against **Drizly, LLC**, and **James Cory Rellas** (CEO), alleging **unfair** practices (failure to implement reasonable security) and **deception** (misrepresentations regarding safeguards) under **Section 5** of the FTC Act.

The same day, the Commission accepted a **Decision and Order** (consent order), FTC Docket No. **2023185**, requiring—among other obligations—a **comprehensive information security program** with a designated coordinator; **risk assessments**; safeguards for access control, credential management, secure development, monitoring, and vendor oversight; a **data retention schedule** and data minimization; **biennial independent security assessments**; and **recordkeeping**. The order also imposes **individual obligations** on the CEO if he becomes a senior officer at another company that collects consumer information from more than **25,000** individuals. **No civil money penalty** was imposed in the public order.
