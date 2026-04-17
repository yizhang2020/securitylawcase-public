# Security Decision Documentation (Yahoo MDL (2018))

> Use this to record a significant security-related decision: what was decided, why, who was involved, and what evidence or inputs were used; supports accountability and audit.

---

## Purpose

This document standardizes how significant security and disclosure decisions related to Yahoo MDL (2018) are recorded, including rationale, approvers, assumptions, and follow-up actions. It supports legal defensibility, internal accountability, and post-incident learning.

## Hallucinated writing examples

**Scenario:** In an illustrative period during Yahoo MDL motion practice after public disclosures of large-scale account compromise **(time)**, the Security Director **(role)** prepares a security decision documentation **(type)** for leadership stakeholders **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY DECISION RECORD</strong></p>

<div class="doc-meta">
<p><strong>Decision: </strong>Adoption of centralized legal-hold logging and account-security control hardening as mandatory decision framework for MDL response<br>
<strong>Date: </strong>June 22, 2018<br>
<strong>Participants: </strong>Chief Information Security Officer, Security Director (Identity), General Counsel, Chief Privacy Officer, Litigation Program Lead</p>
</div>

<p><strong>Context: </strong>Following public disclosures of large-scale Yahoo account compromise and consolidated consumer litigation in MDL No. 16-md-02752, leadership required a durable decision framework for evidence readiness and control remediation. The district court opinion reported at 313 F. Supp. 3d 1113 (N.D. Cal. Mar. 8, 2018) intensified scrutiny of injury theories, discovery posture, and technical fact consistency. This record formalizes the selected approach for legal-hold-aligned logging, MFA expansion, and governance tracking to support litigation defensibility and operational risk reduction.</p>

<p><strong>Options Considered: </strong>(1) Centralize legal-hold logging and prioritize identity-control hardening with executive oversight (selected). This supports defensible discovery response and measurable control closure. (2) Keep decentralized logging and case-by-case remediation only—rejected as too slow and weak for cross-case evidence consistency. (3) Outsource evidence preparation and retain current control architecture—rejected because ownership and traceability requirements remain internal.</p>

<p><strong>Rationale: </strong>The selected option provides a direct path to consistent evidence production and measurable risk reduction. Inputs relied on include MDL procedural posture, internal architecture and logging gap reviews, legal hold requirements, and delivery estimates from engineering and security operations.</p>

<p><strong>Commitments: </strong>Implement in phased rollout with phase one completion in Q3 2018; publish monthly risk and evidence-readiness dashboard to legal and executive governance. Any exception requires CISO and General Counsel approval with a documented revisit date and compensating controls.</p>

</div>

**Document-type guide:** [Security Decision Documentation](../../../../document-types/legal-technical/security-decision-documentation.md)

**Writing tips:** [Writing best practices — Security Decision Documentation](../../../../studio/writing-best-practices.md#security-decision-documentation)
