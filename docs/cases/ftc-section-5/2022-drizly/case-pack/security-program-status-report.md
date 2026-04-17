# Security Program Status Report (FTC v. Drizly 2022)

> Use this to report program health, key metrics, and progress to leadership; supports consent order execution and CEO attestation readiness.

---

## Purpose

This status report translates the FTC Decision and Order and the July 2020 incident lessons into measurable program execution: IAM, secrets management, detection, data minimization, and biennial assessments. It gives leadership a consistent view of whether remediation is on track and where escalation or resourcing is required.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the FTC October 2022 consent order after the July 2020 Drizly breach **(time)**, the Lead Security Engineer, Cloud Security **(role)** prepares a security program status report **(type)** for Security Director, Chief Information Security Officer **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY PROGRAM STATUS REPORT</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Security Director, Chief Information Security Officer<br>
<strong>From: </strong>Lead Security Engineer, Cloud Security<br>
<strong>Date: </strong>January 10, 2023<br>
<strong>Reporting period: </strong>Post–Decision and Order (November 2022–January 2023)</p>
</div>

<p><strong>Overview: </strong>This report summarizes security program status following the July 2020 incident affecting approximately 2.5 million consumers and the Decision and Order accepted by the Federal Trade Commission on October 24, 2022 (<em>In the Matter of Drizly, LLC, and James Cory Rellas</em>, FTC Docket No. 2023185). The FTC alleged unfair practices and deception regarding safeguards; the order requires a comprehensive information security program, data minimization and a retention schedule, biennial independent assessments, and individual obligations for the CEO in future covered roles. This report covers IAM and credential management, secrets and secure development, monitoring and detection, data minimization, and assessment readiness.</p>

<p><strong>Incident Context: </strong>The attack path described in public materials involved compromised credentials and access to source and cloud administration, with delayed internal detection relative to external reporting. Remediation has prioritized MFA enforcement, elimination of credentials in repositories, access reviews, and expanded logging for anomalous access and exfiltration.</p>

<p><strong>Metrics and Progress: </strong>During the reporting period we have: (1) Achieved approximately 92% MFA enrollment for in-scope developer and production administration accounts (target 100% by January 31, 2023). (2) Maintained zero open critical findings from secret scanning; two medium findings under remediation with due dates. (3) Onboarded roughly 85% of critical systems to centralized logging with a drafted retention standard (target 95%). (4) Published an internal data retention schedule draft; first deletion run completed on schedule for pilot categories. (5) Initiated biennial independent assessment procurement with draft scope aligned to the order.</p>

<p><strong>Issues and Next Period: </strong>Residual gaps include planned February rollout for advanced exfiltration detections and completion of external publication steps for the retention schedule. Priorities: close MFA gaps, finish logging onboarding, finalize assessor SOW, and present operating-effectiveness evidence plan to leadership. This report supports internal oversight and consent order milestones.</p>

</div>

**Document-type guide:** [Security Program Status Report](../../../../document-types/executive-board/security-program-status-report.md)

**Writing tips:** [Writing best practices — Security Program Status Report](../../../../studio/writing-best-practices.md#security-program-status-report)
