# Security Architecture Explanation for Legal Review (Firemen’s v. Sorenson (Marriott derivative))

> Use this to explain security architecture and key controls in language suitable for legal review; helps counsel understand technical design and risk.

---

## Purpose

This memorandum explains the relevant security architecture and control boundaries for Firemen’s v. Sorenson (Marriott derivative) in terms accessible to legal stakeholders. It links technical design choices to risk outcomes, evidence availability, and obligations under investigation, enforcement, or litigation timelines.

## Hallucinated writing examples

**Scenario:** In an illustrative period during Delaware derivative litigation over Marriott-Starwood cyber oversight allegations **(time)**, the Lead Security Engineer, Hospitality Platform Security **(role)** prepares a security architecture explanation for legal review **(type)** for General Counsel **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY ARCHITECTURE EXPLANATION FOR LEGAL REVIEW</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>General Counsel<br>
<strong>From: </strong>Lead Security Engineer, Hospitality Platform Security<br>
<strong>Date: </strong>July 2, 2021<br>
<strong>Re: </strong>Security Architecture Overview — Reservation Platform Integration and Oversight Evidence (C.A. No. 2019-0965-LWW)</p>
</div>

<p><strong>Scope: </strong>This memo summarizes the security architecture relevant to legal review and disclosure support for Firemen’s v. Sorenson (Marriott derivative). It focuses on trust boundaries, control design, and evidence availability, with reference to the Chancery litigation context and oversight themes in C.A. No. 2019-0965-LWW.</p>

<p><strong>Architecture Overview: </strong>Architecture scope includes Starwood-legacy and Marriott-legacy reservation and identity systems, integration layers, monitoring services, and administrative control paths. Trust boundaries focus on guest-data environments, franchise-connected systems, and cross-platform identity administration. Post-incident architecture work targets consistent controls across inherited stacks.</p>

<p><strong>Security Controls (Post-Remediation): </strong>(1) <em>Perimeter and segmentation.</em> Boundary controls between guest-facing services and core data stores. (2) <em>Access.</em> Privileged account governance and integration-era entitlement cleanup. (3) <em>Data.</em> Data-protection controls for reservation and loyalty records. (4) <em>Monitoring.</em> Centralized telemetry and alerting across legacy environments with retention for oversight review.</p>

<p><strong>Incident Vector and Remediation: </strong>Oversight allegations focused on whether diligence and post-close integration controls were sufficient. Remediation emphasizes closure of legacy control debt, improved board-visible metrics, and documented architecture decisions. Residual risk remains in phased integrations and franchise complexity; mitigations include exception governance, milestone tracking, and independent validation.</p>

<p><strong>Assumptions and Limitations: </strong>This memo reflects architecture status as of the date above for legal and committee review. It does not guarantee invulnerability. Additional diagrams, control inventories, and test evidence are available to counsel.</p>

</div>

**Document-type guide:** [Security Architecture Explanation for Legal Review](../../../../document-types/legal-technical/security-architecture-explanation-legal-review.md)

**Writing tips:** [Writing best practices — Security Architecture Explanation for Legal Review](../../../../studio/writing-best-practices.md#security-architecture-explanation-for-legal-review)
