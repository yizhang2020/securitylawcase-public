# Security Program Status Report (Capital One 2019)

> Use this to report program health, key metrics, and progress to leadership; supports board and regulator questions on program maturity.

---

## Purpose

Summarize remediation progress, metrics, and gaps after the breach—for internal leadership and early regulatory engagement—so decision-makers see control effectiveness and evidence readiness against root-cause issues.

---

## Hallucinated writing examples

**Scenario:** In November 2019, approximately four months after the July 2019 breach disclosure and arrest of Paige Thompson **(time)**, the Lead Security Engineer **(role)** is required to submit a security program status report **(type)** to the Security Director and CISO **(audience)**. The report will be used for internal leadership and for early discussions with regulators. It must document what has been done since the incident, current metrics, and remaining gaps—all in the context of the Capital One AWS environment and the upcoming OCC examination.

<div class="writing-example-formal">

<p><strong>SECURITY PROGRAM STATUS REPORT</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Security Director, Chief Information Security Officer<br>
<strong>From: </strong>Lead Security Engineer, Cloud Security<br>
<strong>Date: </strong>November 15, 2019<br>
<strong>Reporting period: </strong>Post-incident remediation (July 2019–November 2019)</p>
</div>

<p><strong>Overview: </strong>This report summarizes the security program status following the July 2019 cybersecurity incident involving unauthorized access to customer data in our AWS-hosted infrastructure. The incident was disclosed on July 29, 2019; the individual responsible was arrested the same day (<em>United States v. Paige A. Thompson</em>, U.S. District Court, W.D. Wash.). This report covers remediation actions, current control state, and remaining work in the areas of cloud perimeter configuration, identity and access management (IAM), and logging and retention, which were identified as root causes or contributing factors.</p>

<p><strong>Incident Context: </strong>The actor exploited a misconfiguration in a web application firewall (WAF) protecting our AWS environment, obtained credentials, and accessed data stored in our cloud storage. We have since fixed the vulnerable configuration, implemented additional monitoring, and preserved forensic evidence for law enforcement and potential regulatory or legal proceedings. Federal and state regulators have begun inquiries into our cybersecurity practices.</p>

<p><strong>Metrics and Progress: </strong>Since July 2019 we have: (1) Enforced a mandatory peer-review workflow for all perimeter and WAF changes affecting production; approximately 78% of such changes in the reporting period went through the workflow (target 90% by Q1 2020). (2) Initiated an IAM least-privilege review; we have reduced the number of roles with broad or wildcard permissions by roughly 25% and are continuing the review. (3) Deployed centralized logging for designated AWS workloads and defined a 90-day retention standard for security-relevant logs. (4) Mapped control domains to evidence artifacts so we can produce an audit packet on short notice. Open high-risk findings from our internal review: 12 (down from 18 at the start of the period).</p>

<p><strong>Issues and Next Period: </strong>Drift detection for perimeter configuration is not yet fully deployed across all critical assets; we expect completion in Q1 2020. One control domain still lacks complete evidence mapping. Priorities for the next period: complete the IAM review, achieve 90% of perimeter changes via the approved workflow, close evidence gaps, and engage independent testing for control effectiveness. This report is prepared for internal use and in anticipation of regulatory and legal process.</p>

</div>

**Document-type guide:** [Security Program Status Report](../../../../document-types/executive-board/security-program-status-report.md)

**Writing tips:** [Writing best practices — Security Program Status Report](../../../../studio/writing-best-practices.md#security-program-status-report)
