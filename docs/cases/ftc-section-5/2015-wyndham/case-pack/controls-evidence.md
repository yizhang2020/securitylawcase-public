# Controls -> Evidence Map (FTC v. Wyndham Worldwide Corp.)

## Purpose

This technical appendix maps controls to objective evidence for FTC v. Wyndham Worldwide Corp., enabling rapid substantiation of implementation and operating effectiveness. It is used by security, compliance, and legal teams to demonstrate what is deployed, how it is monitored, and what records support examiner or litigation requests.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the Third Circuit Wyndham decision and the stipulated injunction **(time)**, the Senior Lead Security Engineer **(role)** prepares a controls to evidence map **(type)** for Chief Information Security Officer; Compliance Program Owner **(audience)**.

<div class="writing-example-formal">

<p><strong>CONTROLS -> EVIDENCE MAP (TECHNICAL APPENDIX)</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Chief Information Security Officer; Compliance Program Owner<br>
<strong>From: </strong>Senior Lead Security Engineer<br>
<strong>Date: </strong>August 22, 2016<br>
<strong>Subject: </strong>Control Implementation and Evidence Readiness — Payment Card and Connectivity Domains</p>
</div>

<p><strong>1) Segmentation and Connectivity: </strong><br>
<strong>Required Control State: </strong>Documented least-privilege connectivity between property environments and corporate cardholder-data segments; rule reviews on a defined cadence.<br>
<strong>Evidence Artifacts: </strong>Network diagrams; firewall rule exports; change tickets; periodic review attestations; exception register with approvals.<br>
<strong>Verification Signals: </strong>Count of undocumented connections (target zero); percentage of rules reviewed per quarter; time-to-remediate critical rule findings.</p>

<p><strong>2) Privileged and Remote Access: </strong><br>
<strong>Required Control State: </strong>Strong authentication for administrative access; controlled vendor remote access with logging.<br>
<strong>Evidence Artifacts: </strong>Authentication policy; MFA enforcement reports; vendor access logs; session recordings where used.<br>
<strong>Verification Signals: </strong>MFA coverage for privileged accounts; median vendor session provisioning time; count of emergency break-glass events.</p>

<p><strong>3) Monitoring and Incident Response: </strong><br>
<strong>Required Control State: </strong>Centralized security monitoring for lateral movement and bulk export patterns; documented IR playbooks.<br>
<strong>Evidence Artifacts: </strong>SIEM use cases; alert tuning history; incident timelines; post-incident review records.<br>
<strong>Verification Signals: </strong>Critical-use-case coverage; MTTD/MTTR for priority scenarios; repeat incident rate by root-cause category.</p>

<p><strong>4) Assessment and Remediation: </strong><br>
<strong>Required Control State: </strong>Annual PCI DSS–oriented assessments as described in the order; tracked remediation.<br>
<strong>Evidence Artifacts: </strong>Assessor reports; remediation plans; evidence of closure; management representation letters as applicable.<br>
<strong>Verification Signals: </strong>Open high-severity finding aging; repeat findings year over year.</p>

</div>

**Document-type guide:** [Security Control Implementation Explanation](../../../../document-types/regulatory-compliance/security-control-implementation-explanation.md)

**Writing tips:** [Writing best practices — Compliance Justification Document](../../../../studio/writing-best-practices.md#compliance-justification-document)
