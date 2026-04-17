# Security Decision Documentation (FTC v. Drizly 2022)

> Use this to record a significant security-related decision: what was decided, why, who was involved, and what evidence or inputs were used; supports accountability and audit.

---

## Purpose

This document standardizes how significant security and disclosure decisions related to FTC v. Drizly 2022 are recorded, including rationale, approvers, assumptions, and follow-up actions. It supports legal defensibility, internal accountability, and post-incident learning.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the FTC October 2022 consent order after the July 2020 Drizly breach **(time)**, the Security Director **(role)** prepares a security decision documentation **(type)** for leadership stakeholders **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY DECISION RECORD</strong></p>

<div class="doc-meta">
<p><strong>Decision: </strong>Mandate MFA and secrets-governance controls across developer and production administration paths under FTC order implementation<br>
<strong>Date: </strong>December 1, 2022<br>
<strong>Participants: </strong>Chief Information Security Officer, VP Engineering, General Counsel, Compliance Lead, Security Operations Manager</p>
</div>

<p><strong>Context: </strong>Following the 2020 breach and FTC Decision and Order (Docket No. 2023185), leadership required a documented decision to eliminate exposed credential pathways and improve privileged governance. This record captures the formal decision and implementation commitments.</p>

<p><strong>Options Considered: </strong>(1) Enforce MFA and secret scanning with policy-backed exception controls across all sensitive paths (selected). (2) Adopt monitoring-only without access control changes—rejected as insufficient. (3) Delay implementation until next platform migration—rejected due to order obligations and ongoing risk.</p>

<p><strong>Rationale: </strong>Selected for direct alignment to FTC allegations and order requirements while providing measurable implementation milestones. Inputs included incident root-cause review, order obligations, and engineering delivery estimates.</p>

<p><strong>Commitments: </strong>Complete phase one MFA and scanning controls by Q1 2023; quarterly governance reporting; exceptions require CISO and compliance sign-off with revisit dates.</p>

</div>

**Document-type guide:** [Security Decision Documentation](../../../../document-types/legal-technical/security-decision-documentation.md)

**Writing tips:** [Writing best practices — Security Decision Documentation](../../../../studio/writing-best-practices.md#security-decision-documentation)
