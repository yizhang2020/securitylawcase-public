# Security Program Status Report (FTC v. Drizly 2022)

> Program health, metrics, and progress for leadership and consent order reporting.

---

## Purpose

A status report that tracks progress against the FTC consent order and the information security program. Typically includes: (1) program elements implemented (coordinator, risk assessment, safeguards, training, testing, data retention); (2) key metrics (e.g., MFA coverage, credential-scan results, retention schedule compliance); (3) open items and target dates; (4) biennial assessment status.

**Metrics aligned with FTC order:** Written program in place; coordinator designated; risk assessment completed; MFA enforced for privileged/sensitive access; no credentials in repositories; retention schedule published and deletion process operating; biennial assessment scheduled or completed.

---

## Hallucinated writing examples

**Scenario.** In January 2023, during initial implementation of the FTC consent order **(time)**, a Lead Security Engineer **(role)** submits a security program status report **(type)** to the CISO **(audience)**. The report provides measurable progress against program and data-retention requirements and identifies blockers requiring executive action.

<div class="writing-example-formal">

<p><strong>SECURITY PROGRAM STATUS REPORT</strong></p>

<div class="doc-meta">
<p><strong>To:</strong> Chief Information Security Officer<br>
<strong>From:</strong> Lead Security Engineer<br>
<strong>Date:</strong> January 10, 2023<br>
<strong>Re:</strong> Status Report — Information Security Program and FTC Consent Order Readiness</p>
</div>

<p>This report summarizes implementation status for the information security program and data minimization obligations required by the FTC Decision and Order (FTC Docket No. 2023185). The scenario is illustrative; the obligations reflected below derive from the Order.</p>

<p><strong>1) Program governance (Order requirement).</strong><br>
- <strong>Program coordinator:</strong> Designated; reporting line documented. <strong>Status:</strong> Complete.<br>
- <strong>Written program:</strong> Draft finalized for executive approval. <strong>Status:</strong> In progress. <strong>Blocker:</strong> approval scheduling.</p>

<p><strong>2) IAM and credential management.</strong><br>
- <strong>MFA enforcement (source code and production credentials):</strong> <strong>Status:</strong> In progress. <strong>Metric:</strong> 92% enrolled; enforcement targeted for Jan 31.<br>
- <strong>Access review / offboarding:</strong> <strong>Status:</strong> In progress. <strong>Metric:</strong> 100% privileged accounts reviewed; remediation of 3 stale accounts pending.</p>

<p><strong>3) Secrets management and secure development.</strong><br>
- <strong>No credentials in repositories:</strong> <strong>Status:</strong> In progress. <strong>Metric:</strong> secret scanning enabled; 0 open critical findings; 2 medium findings under remediation.<br>
- <strong>Change control for high-risk settings:</strong> <strong>Status:</strong> In progress.</p>

<p><strong>4) Monitoring and detection.</strong><br>
- <strong>Logging coverage and retention:</strong> <strong>Status:</strong> In progress. <strong>Metric:</strong> 85% of critical systems onboarded; retention policy drafted.<br>
- <strong>Exfiltration/anomalous access detection:</strong> <strong>Status:</strong> Planned (Feb rollout).</p>

<p><strong>5) Data minimization and retention.</strong><br>
- <strong>Retention schedule:</strong> Draft published internally; external publication queued. <strong>Status:</strong> In progress.<br>
- <strong>Deletion/de-identification process:</strong> <strong>Status:</strong> In progress. <strong>Metric:</strong> first deletion run scheduled Jan 20.</p>

<p><strong>6) Independent assessment (biennial).</strong><br>
- <strong>Assessor selection and scope:</strong> <strong>Status:</strong> In progress. <strong>Next step:</strong> finalize SOW and timeline.</p>

<p><strong>Requests for action.</strong> Approve the written program and retention schedule publication; confirm budget for assessment and monitoring enhancements.</p>

</div>

## Primary sources

- **FTC Decision and Order:** [Decision and Order — Drizly, LLC, and James Cory Rellas](https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf), FTC Docket No. 2023185 (Oct. 24, 2022).
