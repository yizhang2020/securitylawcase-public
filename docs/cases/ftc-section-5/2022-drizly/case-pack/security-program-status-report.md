# Security Program Status Report (FTC v. Drizly 2022)

> Program health, metrics, and progress for leadership and consent order reporting.

---

## Purpose

A status report that tracks progress against the FTC consent order and the information security program. Typically includes: (1) program elements implemented (coordinator, risk assessment, safeguards, training, testing, data retention); (2) key metrics (e.g., MFA coverage, credential-scan results, retention schedule compliance); (3) open items and target dates; (4) biennial assessment status.

**Metrics aligned with FTC order:** Written program in place; coordinator designated; risk assessment completed; MFA enforced for privileged/sensitive access; no credentials in repositories; retention schedule published and deletion process operating; biennial assessment scheduled or completed.

---

## Hallucinated writing examples

**Scenario:** In January 2023, during initial implementation of the FTC consent order **(time)**, a Lead Security Engineer **(role)** submits a security program status report **(type)** to the CISO **(audience)**. The report provides measurable progress against program and data-retention requirements and identifies blockers requiring executive action.

<div class="writing-example-formal">

<p><strong>SECURITY PROGRAM STATUS REPORT</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Chief Information Security Officer<br>
<strong>From: </strong>Lead Security Engineer<br>
<strong>Date: </strong>January 10, 2023<br>
<strong>Re: </strong>Status Report — Information Security Program and FTC Consent Order Readiness</p>
</div>

<p>This report summarizes implementation status for the information security program and data minimization obligations required by the FTC Decision and Order (FTC Docket No. 2023185). The scenario is illustrative; the obligations reflected below derive from the Order.</p>

<p><strong>1) Program governance</strong> (order requirement)<br>
Program coordinator: Designated; reporting line documented. Status: complete.<br>
Written program: Draft finalized for executive approval. Status: in progress. Blocker: approval scheduling.</p>

<p><strong>2) IAM and credential management</strong><br>
MFA enforcement (source code and production credentials): Status: in progress. Metric: 92% enrolled; enforcement targeted for Jan 31.<br>
Access review / offboarding: Status: in progress. Metric: 100% privileged accounts reviewed; remediation of 3 stale accounts pending.</p>

<p><strong>3) Secrets management and secure development</strong><br>
No credentials in repositories: Status: in progress. Metric: secret scanning enabled; 0 open critical findings; 2 medium findings under remediation.<br>
Change control for high-risk settings: Status: in progress.</p>

<p><strong>4) Monitoring and detection</strong><br>
Logging coverage and retention: Status: in progress. Metric: 85% of critical systems onboarded; retention policy drafted.<br>
Exfiltration/anomalous access detection: Status: planned (February rollout).</p>

<p><strong>5) Data minimization and retention</strong><br>
Retention schedule: Draft published internally; external publication queued. Status: in progress.<br>
Deletion/de-identification process: Status: in progress. Metric: first deletion run scheduled Jan 20.</p>

<p><strong>6) Independent assessment</strong> (biennial)<br>
Assessor selection and scope: Status: in progress. Next step: finalize SOW and timeline.</p>

<p><strong>Requests For Action: </strong>Approve the written program and retention schedule publication; confirm budget for assessment and monitoring enhancements.</p>

</div>

**Document-type guide:** [Security Program Status Report](../../../../document-types/executive-board/security-program-status-report.md)

**Writing tips:** [Writing best practices — Security Program Status Report](../../../../studio/writing-best-practices.md#security-program-status-report)
