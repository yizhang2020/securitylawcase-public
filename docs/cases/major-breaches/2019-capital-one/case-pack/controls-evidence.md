# Controls -> Evidence Map (Capital One 2019)

## Purpose

This technical appendix maps controls to objective evidence for Capital One 2019, enabling rapid substantiation of implementation and operating effectiveness. It is used by security, compliance, and legal teams to demonstrate what is deployed, how it is monitored, and what records support examiner or litigation requests.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the 2019 Capital One cloud breach and related enforcement and litigation tracks **(time)**, the Senior Lead Security Engineer, Cloud Security **(role)** prepares a controls to evidence map **(type)** for Chief Information Security Officer; Audit Committee Technical Review Team **(audience)**.

<div class="writing-example-formal">

<p><strong>CONTROLS -> EVIDENCE MAP (TECHNICAL APPENDIX)</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Chief Information Security Officer; Audit Committee Technical Review Team<br>
<strong>From: </strong>Senior Lead Security Engineer, Cloud Security<br>
<strong>Date: </strong>November 20, 2020<br>
<strong>Subject: </strong>Control Implementation and Evidence Readiness Appendix — Capital One 2019 Incident Remediation</p>
</div>

<p><strong>Technical Objective: </strong>This appendix documents required control state, available evidence artifacts, and verification signals for the key control domains implicated by the 2019 incident and subsequent enforcement actions. It is designed for technical and compliance stakeholders who need implementation-level proof, not policy-only assertions.</p>

<p><strong>Scope: </strong>Cloud boundary controls, IAM and privileged access, detection and investigation readiness, vulnerability and exposure management, and governance assurance evidence.</p>

<p><strong>1) Cloud Configuration Governance (Config-as-Code): </strong></p>
<p><strong>Required Control State: </strong>Boundary controls (WAF/routing/exposure) are managed as code; all production changes require peer-reviewed approval; drift detection is enabled for high-risk resources; baseline and exception records are maintained.<br>
<strong>Evidence Artifacts: </strong>Repository pull-request history for boundary policy changes; approved change tickets linked to risk review; baseline configuration snapshots; drift alerts and remediation tickets.<br>
<strong>Verification Signals: </strong>Percentage of perimeter changes executed through PR workflow; mean time to detect and remediate drift; \# of emergency changes without post-approval.</p>

<p><strong>2) IAM Least Privilege for Sensitive Storage: </strong></p>
<p><strong>Required Control State: </strong>Roles are explicitly scoped to function; app runtime access is separated from administrative access; periodic access recertification is enforced; explicit deny controls protect sensitive data paths.<br>
<strong>Evidence Artifacts: </strong>IAM policy JSON snapshots and diffs; access review attestations with approver and rationale; privileged role inventory; stale-permission removal evidence.<br>
<strong>Verification Signals: </strong>\# of wildcard-permission roles; percentage of in-scope roles reviewed in the last 90 days; privilege-escalation alert volume and closure time.</p>

<p><strong>3) Detection and Investigation Readiness: </strong></p>
<p><strong>Required Control State: </strong>Centralized telemetry covers cloud control plane, WAF, authentication, and sensitive data access paths; alert thresholds are documented for anomalous access/exfiltration patterns; investigation runbooks are operationalized with consistent ticketing fields; log retention supports legal and regulatory inquiry timelines.<br>
<strong>Evidence Artifacts: </strong>Log retention configuration exports; versioned anomaly-detection queries and rules; SOC runbooks; incident investigation tickets with timeline reconstruction.<br>
<strong>Verification Signals: </strong>Log coverage percentage for critical systems; alert-to-triage and triage-to-containment durations; investigation completeness scoring.</p>

<p><strong>4) Vulnerability and Attack Surface Management: </strong></p>
<p><strong>Required Control State: </strong>Internet-facing assets are inventoried with accountable owners; continuous scanning is enforced with SLA-based remediation; high-risk applications maintain WAF rules aligned to threat models.<br>
<strong>Evidence Artifacts: </strong>Asset inventory exports with ownership mapping; vulnerability backlog and SLA metrics; approved exceptions with expiry date and compensating controls.<br>
<strong>Verification Signals: </strong>SLA compliance percentage; \# of critical vulnerabilities past SLA; percentage of internet-facing assets with owner and risk tier.</p>

<p><strong>5) Governance, Risk, and Independent Testing: </strong></p>
<p><strong>Required Control State: </strong>Risk assessments produce tracked remediation items; risk acceptance requires formal approval with revisit date; independent testing validates operating effectiveness and closure quality.<br>
<strong>Evidence Artifacts: </strong>Risk register entries with mitigation status; signed risk acceptance records; independent assessment/audit reports and remediation tracking evidence.<br>
<strong>Verification Signals: </strong>\# of accepted risks without revisit date; audit-finding closure rate; time-to-close for high-risk findings.</p>

<p><strong>Submission Note: </strong>This appendix is technical by design and intended to accompany executive or regulator-facing narrative documents as implementation proof.</p>

</div>

**Document-type guide:** [Security Control Implementation Explanation](../../../../document-types/regulatory-compliance/security-control-implementation-explanation.md)

**Writing tips:** [Writing best practices — Compliance Justification Document](../../../../studio/writing-best-practices.md#compliance-justification-document)
