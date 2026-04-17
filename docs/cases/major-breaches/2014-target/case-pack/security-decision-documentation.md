# Security Decision Documentation (In re Target Corp. MDL)

> Use this to record a significant security-related decision: what was decided, why, who was involved, and what evidence or inputs were used; supports accountability and audit.

---

## Purpose

This document standardizes how significant security and disclosure decisions related to In re Target Corp. MDL are recorded, including rationale, approvers, assumptions, and follow-up actions. It supports legal defensibility, internal accountability, and post-incident learning.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the Target payment-card breach litigation milestones in the MDL record **(time)**, the Security Director **(role)** prepares a security decision documentation **(type)** for leadership stakeholders **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY DECISION RECORD</strong></p>

<div class="doc-meta">
<p><strong>Decision: </strong>Standardization of vendor remote-access architecture and POS segmentation governance across in-scope store environments<br>
<strong>Date: </strong>April 9, 2015<br>
<strong>Participants: </strong>Chief Information Security Officer, Security Director (Retail Infrastructure), General Counsel, Internal Audit Lead, Operations VP</p>
</div>

<p><strong>Context: </strong>The 2013 incident and subsequent MDL litigation (No. 14-2522) required clear decisions on architecture and governance for vendor access and payment-environment segmentation. The court’s pleading-stage opinion increased pressure for auditable remediation evidence. This decision sets the selected model for consistent controls and legal defensibility.</p>

<p><strong>Options Considered: </strong>(1) Mandate monitored jump-host pathways plus segmentation baselines for store environments (selected). (2) Vendor-by-vendor custom access controls—rejected due to inconsistency and audit complexity. (3) Deferral until hardware refresh cycles—rejected for unacceptable interim risk.</p>

<p><strong>Rationale: </strong>The selected option best balances speed, control uniformity, and evidentiary clarity. Inputs included forensic findings, card-brand control expectations, and deployment constraints across store networks.</p>

<p><strong>Commitments: </strong>Rollout milestone gates through Q4 2015; monthly remediation aging review; governance exceptions require CISO approval and documented compensating controls.</p>

</div>

**Document-type guide:** [Security Decision Documentation](../../../../document-types/legal-technical/security-decision-documentation.md)

**Writing tips:** [Writing best practices — Security Decision Documentation](../../../../studio/writing-best-practices.md#security-decision-documentation)
