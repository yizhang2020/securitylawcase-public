# Security Decision Documentation (FTC v. ChoicePoint Inc. (2006))

> Use this to record a significant security-related decision: what was decided, why, who was involved, and what evidence or inputs were used; supports accountability and audit.

---

## Purpose

This document standardizes how significant security and disclosure decisions related to FTC v. ChoicePoint Inc. (2006) are recorded, including rationale, approvers, assumptions, and follow-up actions. It supports legal defensibility, internal accountability, and post-incident learning.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the FTC 2006 settlement and findings on fraudulent account onboarding **(time)**, the Security Director **(role)** prepares a security decision documentation **(type)** for leadership stakeholders **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY DECISION RECORD</strong></p>

<div class="doc-meta">
<p><strong>Decision: </strong>Enterprise decision to mandate high-assurance subscriber verification and fraud analytics before granting access to sensitive consumer data<br>
<strong>Date: </strong>March 25, 2006<br>
<strong>Participants: </strong>Chief Information Security Officer, Fraud Operations Director, General Counsel, Compliance Officer, Chief Risk Officer</p>
</div>

<p><strong>Context: </strong>The FTC action and stipulated judgment (Matter No. 052-3069) required formal governance decisions to address fraudulent onboarding pathways and unauthorized data acquisition. This record documents the selected decision framework for subscriber verification and monitoring controls.</p>

<p><strong>Options Considered: </strong>(1) Require multi-layer business verification plus behavioral analytics before account activation (selected). (2) Continue manual review-only onboarding—rejected as unscalable and inconsistent. (3) Delegate verification to external partners with minimal internal checks—rejected due to accountability and evidence gaps.</p>

<p><strong>Rationale: </strong>Selected because it most directly reduces fraudulent account creation risk and strengthens auditability for FTC oversight. Inputs included enforcement findings, fraud case analysis, and operational capacity modeling.</p>

<p><strong>Commitments: </strong>Implement in staged rollout through Q3 2006; monthly fraud-risk governance reviews; any verification bypass requires executive approval and documented expiration.</p>

</div>

**Document-type guide:** [Security Decision Documentation](../../../../document-types/legal-technical/security-decision-documentation.md)

**Writing tips:** [Writing best practices — Security Decision Documentation](../../../../studio/writing-best-practices.md#security-decision-documentation)
