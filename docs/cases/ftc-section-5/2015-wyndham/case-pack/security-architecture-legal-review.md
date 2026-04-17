# Security Architecture Explanation for Legal Review (FTC v. Wyndham Worldwide Corp.)

> Use this to explain security architecture and key controls in language suitable for legal review; helps counsel understand technical design and risk.

---

## Purpose

This memorandum explains the relevant security architecture and control boundaries for FTC v. Wyndham Worldwide Corp. in terms accessible to legal stakeholders. It links technical design choices to risk outcomes, evidence availability, and obligations under investigation, enforcement, or litigation timelines.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the Third Circuit Wyndham decision and the stipulated injunction **(time)**, the Lead Security Engineer, Hospitality Network Security **(role)** prepares a security architecture explanation for legal review **(type)** for General Counsel **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY ARCHITECTURE EXPLANATION FOR LEGAL REVIEW</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>General Counsel<br>
<strong>From: </strong>Lead Security Engineer, Hospitality Network Security<br>
<strong>Date: </strong>March 10, 2016<br>
<strong>Re: </strong>Security Architecture Overview — Property and Corporate Connectivity; FTC Order Compliance</p>
</div>

<p><strong>Scope: </strong>This memo summarizes the security architecture relevant to legal review and disclosure support for FTC v. Wyndham Worldwide Corp.. It focuses on trust boundaries, control design, and evidence availability, with reference to the Third Circuit decision at 799 F.3d 236 and the stipulated injunction entered December 11, 2015.</p>

<p><strong>Architecture Overview: </strong>This architecture review covers property-managed environments, corporate systems, and connectivity pathways affecting payment-card data risk. Trust boundaries must account for franchise variability and shared service dependencies across hospitality operations. The architecture program emphasizes enforceable network boundaries and centralized visibility across distributed properties.</p>

<p><strong>Security Controls (Post-Remediation): </strong>(1) <em>Perimeter and segmentation.</em> Connectivity baselines between property and corporate zones with controlled routing. (2) <em>Access.</em> Privileged access controls and periodic review of remote administration paths. (3) <em>Data.</em> Protection controls for card-related data domains aligned with policy and assessment requirements. (4) <em>Monitoring.</em> Logging and detection coverage for anomalous movement across property-corporate boundaries.</p>

<p><strong>Incident Vector and Remediation: </strong>FTC allegations and court records described repeated intrusions tied to weak segmentation, remote-access hygiene, and uneven monitoring across environments. Remediation includes stronger boundary governance, access review controls, and assessment-driven closure plans. Residual risk remains where legacy property systems require staged upgrades; mitigations include compensating controls and dated exception tracking.</p>

<p><strong>Assumptions and Limitations: </strong>This description supports legal and regulatory review as of the date above. It does not guarantee invulnerability. Supplementary architecture diagrams and assessment evidence are available on request.</p>

</div>

**Document-type guide:** [Security Architecture Explanation for Legal Review](../../../../document-types/legal-technical/security-architecture-explanation-legal-review.md)

**Writing tips:** [Writing best practices — Security Architecture Explanation for Legal Review](../../../../studio/writing-best-practices.md#security-architecture-explanation-for-legal-review)
