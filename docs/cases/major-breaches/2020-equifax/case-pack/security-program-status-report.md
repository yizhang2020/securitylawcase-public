# Security Program Status Report (Equifax 2017 Cybersecurity Incident)

> Use this to report program health, key metrics, and progress to leadership; supports board and multi-agency enforcement readiness.

---

## Purpose

This status report translates post-2017 breach remediation and federal order obligations into measurable program execution: patch and vulnerability management, identity and access, logging, and assessment closure. It gives leadership a consistent view of whether remediation is on track and where escalation or resourcing is required.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the FTC stipulated order (July 2019) and parallel CFPB action **(time)**, the Lead Security Engineer, Enterprise Defense **(role)** prepares a security program status report **(type)** for Security Director, Chief Information Security Officer **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY PROGRAM STATUS REPORT</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Security Director, Chief Information Security Officer<br>
<strong>From: </strong>Lead Security Engineer, Enterprise Defense<br>
<strong>Date: </strong>October 15, 2020<br>
<strong>Reporting period: </strong>Post–FTC order implementation (August 2019–October 2020)</p>
</div>

<p><strong>Overview: </strong>This report summarizes security program status following the September 2017 disclosure of a cybersecurity incident affecting tens of millions of U.S. consumers’ credit-file data and subsequent federal enforcement, including the FTC stipulated order entered July 22, 2019, and parallel CFPB action imposing comprehensive information security program requirements, assessments, and redress structures. Civil MDL and regulatory processes continue to stress evidence completeness, timely remediation, and credible metrics. This report covers vulnerability and patch management, privileged access to bureau systems, centralized logging and SIEM coverage, and encryption and key-management initiatives tied to the consent frameworks.</p>

<p><strong>Incident Context: </strong>The public narrative emphasizes internet-facing application vulnerability and related access paths into sensitive data stores. Remediation has focused on emergency patch SLAs for internet-facing assets, segmentation between perimeter and core data paths, and expanded monitoring for anomalous queries and bulk exports. Forensic evidence packages are maintained under legal hold discipline for regulatory and civil proceedings.</p>

<p><strong>Metrics and Progress: </strong>During the reporting period we have: (1) Reduced mean time to remediate critical CVEs on designated internet-facing applications from 18 days to 9 days (target 7 days by Q1 2021). (2) Achieved approximately 81% coverage of crown-jewel administrative sessions through privileged access management with session monitoring (target 95% by mid-2021). (3) Expanded centralized SIEM ingestion to roughly 88% of in-scope systems by transaction volume (target 95%). (4) Closed 64% of independent assessment findings opened in the prior cycle; 11 high-priority items remain with accountable owners and dates. (5) Published an updated control-to-evidence map used for regulatory and MDL audit packets.</p>

<p><strong>Issues and Next Period: </strong>Residual gaps include legacy application exceptions that still lack full segmentation and a backlog of medium findings tied to third-party connectors. Priorities for the next period: complete PAM coverage for remaining admin paths, finish SIEM onboarding for residual tiers, drive critical-patch latency to the 7-day target, and run executive review of aging assessment items with board escalation thresholds. This report supports internal governance and anticipated regulatory follow-up.</p>

</div>

**Document-type guide:** [Security Program Status Report](../../../../document-types/executive-board/security-program-status-report.md)

**Writing tips:** [Writing best practices — Security Program Status Report](../../../../studio/writing-best-practices.md#security-program-status-report)
