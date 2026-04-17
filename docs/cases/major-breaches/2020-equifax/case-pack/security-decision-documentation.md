# Security Decision Documentation (Equifax 2017 Incident (2020 oversight))

> Use this to record a significant security-related decision: what was decided, why, who was involved, and what evidence or inputs were used; supports accountability and audit.

---

## Purpose

This document standardizes how significant security and disclosure decisions related to Equifax 2017 Incident (2020 oversight) are recorded, including rationale, approvers, assumptions, and follow-up actions. It supports legal defensibility, internal accountability, and post-incident learning.

## Hallucinated writing examples

**Scenario:** In an illustrative period following federal Equifax enforcement orders and ongoing MDL settlement administration **(time)**, the Security Director **(role)** prepares a security decision documentation **(type)** for leadership stakeholders **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY DECISION RECORD</strong></p>

<div class="doc-meta">
<p><strong>Decision: </strong>Mandatory risk-based patch SLA and privileged access governance for internet-facing and credit-data control planes<br>
<strong>Date: </strong>October 22, 2020<br>
<strong>Participants: </strong>Chief Information Security Officer, Security Director (Technology Risk), Chief Risk Officer, General Counsel, Compliance Officer</p>
</div>

<p><strong>Context: </strong>After the 2017 incident, federal enforcement actions (including FTC and CFPB tracks) and civil proceedings required demonstrable governance over vulnerability management and administrative access. Public narratives emphasized patch latency and privileged-path exposure. This decision documents the formal control standard and governance model selected to reduce recurrence risk and satisfy oversight expectations.</p>

<p><strong>Options Considered: </strong>(1) Enterprise patch SLA with emergency governance plus PAM expansion for privileged paths (selected). (2) Business-unit patch discretion with annual access reviews—rejected as insufficient for high-risk assets. (3) Temporary compensating controls without platform changes—rejected as non-durable for assessment and litigation scrutiny.</p>

<p><strong>Rationale: </strong>Selected because it directly targets root-cause themes and creates measurable governance outputs (latency, coverage, exceptions). Inputs included enforcement obligations, independent assessment findings, and engineering feasibility estimates.</p>

<p><strong>Commitments: </strong>Phase one delivery by Q1 2021 for Tier-0 assets; quarterly board risk reporting; mandatory exception approvals with revisit dates and closure tracking.</p>

</div>

**Document-type guide:** [Security Decision Documentation](../../../../document-types/legal-technical/security-decision-documentation.md)

**Writing tips:** [Writing best practices — Security Decision Documentation](../../../../studio/writing-best-practices.md#security-decision-documentation)
