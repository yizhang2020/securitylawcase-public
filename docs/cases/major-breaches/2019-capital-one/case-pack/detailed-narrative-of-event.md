## Detailed Narrative of Events

*(Extended Documentation for the Capital One 2019 Cloud Breach Case Study)*

### Table of Contents

1. [Overview](#overview)
2. [Pre-Incident Environment](#pre-incident-environment)
3. [Initial Breach and Unauthorized Access](#initial-breach-and-unauthorized-access)
4. [Data Exfiltration and Attacker Activity](#data-exfiltration-and-attacker-activity)
5. [Data Types and Volume](#data-types-and-volume)
6. [External Discovery of the Breach](#external-discovery-of-the-breach)
7. [Internal Investigation by Capital One](#internal-investigation-by-capital-one)
8. [Engagement with Law Enforcement](#engagement-with-law-enforcement)
9. [Arrest of the Attacker](#arrest-of-the-attacker)
10. [Public Disclosure and Customer Notification](#public-disclosure-and-customer-notification)
11. [Immediate Post-Incident Response](#immediate-post-incident-response)
12. [Subsequent Investigations and Legal Proceedings](#subsequent-investigations-and-legal-proceedings)

---

## Overview

The **2019 Capital One data breach** involved unauthorized access to sensitive customer data stored in cloud infrastructure operated by Capital One and hosted on Amazon Web Services.

The incident was ultimately traced to a cloud configuration flaw that allowed an attacker to exploit a web application firewall through a Server-Side Request Forgery (SSRF) technique. The attack enabled the retrieval of cloud credentials and access to data stored in Amazon S3 storage.

The breach was **not initially detected internally**. Instead, it was discovered by an external security researcher who reported the issue through Capital One’s responsible disclosure channel in July 2019. Within approximately two weeks of the report, federal authorities identified and arrested the attacker.

---

## Pre-Incident Environment

Before the incident, Capital One had adopted a cloud-first infrastructure strategy. Many of its applications and data processing systems were hosted on AWS cloud infrastructure.

The company implemented several cloud security mechanisms, including:

* Web Application Firewall (WAF) protections
* Identity and Access Management (IAM) roles
* Amazon S3 storage for application data
* Logging and monitoring systems for cloud operations

However, the security configuration governing these systems contained a weakness that allowed unauthorized requests to reach AWS metadata services.

---

## Initial Breach and Unauthorized Access

In **March 2019**, the attacker began exploiting a vulnerability associated with a misconfigured web application firewall protecting Capital One cloud applications.

The vulnerability allowed **Server-Side Request Forgery (SSRF)** requests to be executed against AWS internal metadata endpoints. These endpoints store temporary security credentials assigned to cloud services.

By sending specially crafted requests, the attacker obtained temporary credentials associated with an IAM role assigned to a Capital One application.

These credentials allowed access to certain internal cloud resources.

---

## Data Exfiltration and Attacker Activity

After obtaining valid credentials, the attacker began exploring accessible resources within the AWS environment.

Using AWS command-line tools and cloud queries, the attacker accessed multiple **Amazon S3 storage buckets** that contained application data and customer information.

The attacker downloaded large volumes of data from these storage repositories.

Investigators later determined that the attacker stored the stolen data on external servers under her control. Evidence of the breach was also referenced in posts and files shared on GitHub.

The attacker reportedly discussed aspects of the breach in online forums and communication channels, leaving a digital trail that investigators later used to identify her.

---

## Data Types and Volume

Approximately **106 million individuals** were affected.

Exposed information included:

* Names
* Addresses
* Phone numbers
* Dates of birth
* Credit scores and credit limits
* Payment histories
* Approximately **140,000 Social Security numbers**
* Approximately **80,000 bank account numbers**
* Credit application information

Credit card numbers were not exposed.

---

## External Discovery of the Breach

The breach was discovered by an independent security researcher who observed references to Capital One data appearing in online repositories and discussions.

The researcher recognized that the data appeared to originate from Capital One systems and contacted the company through its responsible disclosure program.

On **17 July 2019**, the researcher sent an email notifying Capital One of the potential exposure.

The report included references to locations where the stolen data appeared to be stored or discussed.

---

## Internal Investigation by Capital One

Upon receiving the disclosure report, Capital One’s security team initiated an internal investigation.

Investigators reviewed cloud activity logs and examined AWS access records associated with the reported data exposure.

Within a short period, the company confirmed that unauthorized access had occurred.

Security teams then:

* Identified the vulnerable configuration responsible for the breach
* Disabled the exposed access path
* Secured the affected systems
* Preserved system logs and forensic evidence

Once the breach was confirmed, Capital One contacted federal law enforcement authorities.

---

## Engagement with Law Enforcement

Capital One cooperated with investigators from the **Federal Bureau of Investigation (FBI)** and the **U.S. Department of Justice**.

Law enforcement began analyzing technical evidence, including:

* AWS access logs
* Infrastructure metadata records
* Online repositories containing the stolen data
* Communication records linked to the attacker

Investigators quickly identified an individual connected to the stolen data through online accounts and infrastructure records.

---

## Arrest of the Attacker

On **29 July 2019**, federal authorities arrested **Paige Thompson** in Seattle, Washington.

Thompson had previously worked as a cloud systems engineer and possessed knowledge of cloud infrastructure.

According to federal prosecutors, evidence linking her to the breach included:

* GitHub repositories referencing the stolen data
* Slack messages discussing the breach
* Infrastructure logs connecting her accounts to the accessed data

Following her arrest, Thompson was charged under federal computer crime statutes.

---

## Public Disclosure and Customer Notification

Later on **29 July 2019**, Capital One publicly disclosed the breach.

The company announced that approximately **106 million individuals** were affected.

Affected individuals included:

* Approximately **100 million U.S. customers**
* Approximately **6 million Canadian customers**

The company stated that the exposed data included credit application information and limited financial identifiers.

Capital One began notifying affected individuals and offered:

* Free credit monitoring services
* Identity protection services
* Assistance for potential fraud incidents

The company also issued a public statement acknowledging the breach and apologizing to affected customers.

---

## Immediate Post-Incident Response

Following disclosure, Capital One implemented several remediation measures.

These actions included:

* Reviewing cloud configuration policies
* Strengthening monitoring of cloud infrastructure
* Enhancing access control policies and IAM role restrictions
* Conducting additional security assessments of cloud systems

The company also cooperated with regulators and investigators reviewing the incident.

---

## Subsequent Investigations and Legal Proceedings

After the breach was disclosed, several government agencies initiated investigations into the company’s cybersecurity practices.

Regulators examined whether Capital One had implemented appropriate controls for protecting consumer financial data.

Civil litigation also followed the breach. Consumers filed lawsuits alleging that the company failed to implement adequate cybersecurity protections.

These cases were eventually consolidated in federal court.

In subsequent years, the incident resulted in:

* Regulatory enforcement actions against Capital One
* An **$80 million penalty imposed by the Office of the Comptroller of the Currency**
* A **$190 million consumer class-action settlement approved in 2022**

Meanwhile, the attacker was prosecuted in federal court and convicted of computer fraud offenses.

