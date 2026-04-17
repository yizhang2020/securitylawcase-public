# Security Decision Documentation (Spokeo, Inc. v. Robins)

> Use this to record a significant security-related decision: what was decided, why, who was involved, and what evidence or inputs were used; supports accountability and audit.

---

## Purpose

This document standardizes how significant security and disclosure decisions related to Spokeo, Inc. v. Robins are recorded, including rationale, approvers, assumptions, and follow-up actions. It supports legal defensibility, internal accountability, and post-incident learning.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the Supreme Court ruling on Article III standing in Spokeo **(time)**, the Security Director **(role)** prepares a security decision documentation **(type)** for leadership stakeholders **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY DECISION RECORD</strong></p>

<div class="doc-meta">
<p><strong>Decision: </strong>Approve enterprise data-lineage and dispute-SLA governance standard for high-risk consumer attributes<br>
<strong>Date: </strong>January 12, 2017<br>
<strong>Participants: </strong>Chief Information Security Officer, Chief Privacy Officer, General Counsel, Data Governance Lead, Product Engineering Director</p>
</div>

<p><strong>Context: </strong>After the Supreme Court decision at 578 U.S. 330, leadership required formal governance decisions on data-accuracy, traceability, and dispute responsiveness to reduce legal and reputational risk. This record documents the selected standard.</p>

<p><strong>Options Considered: </strong>(1) Adopt mandatory lineage and dispute SLA controls for designated high-risk attributes (selected). (2) Continue policy-only guidance without instrumentation—rejected as non-verifiable. (3) Narrow controls to legal-case subsets only—rejected due to systemic quality exposure.</p>

<p><strong>Rationale: </strong>Selected for stronger demonstrability of control effectiveness and faster correction workflows. Inputs included dispute trend analysis, legal risk review, and internal data-quality assessments.</p>

<p><strong>Commitments: </strong>Implement phase one controls by Q2 2017; monthly KPI review (error rates, dispute aging); exceptions require cross-functional approval and dated remediation.</p>

</div>

**Document-type guide:** [Security Decision Documentation](../../../../document-types/legal-technical/security-decision-documentation.md)

**Writing tips:** [Writing best practices — Security Decision Documentation](../../../../studio/writing-best-practices.md#security-decision-documentation)
