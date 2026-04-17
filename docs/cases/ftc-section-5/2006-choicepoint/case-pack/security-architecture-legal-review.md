# Security Architecture Explanation for Legal Review (FTC v. ChoicePoint Inc. (2006))

> Use this to explain security architecture and key controls in language suitable for legal review; helps counsel understand technical design and risk.

---

## Purpose

This memorandum explains the relevant security architecture and control boundaries for FTC v. ChoicePoint Inc. (2006) in terms accessible to legal stakeholders. It links technical design choices to risk outcomes, evidence availability, and obligations under investigation, enforcement, or litigation timelines.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the FTC 2006 settlement and findings on fraudulent account onboarding **(time)**, the Lead Security Engineer, Fraud and Access Controls **(role)** prepares a security architecture explanation for legal review **(type)** for General Counsel **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY ARCHITECTURE EXPLANATION FOR LEGAL REVIEW</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>General Counsel<br>
<strong>From: </strong>Lead Security Engineer, Fraud and Access Controls<br>
<strong>Date: </strong>March 22, 2006<br>
<strong>Re: </strong>Security Architecture Overview — Subscriber Vetting and Data Access Controls; Matter No. 052-3069</p>
</div>

<p><strong>Scope: </strong>This memo summarizes the security architecture relevant to legal review and disclosure support for FTC v. ChoicePoint Inc. (2006). It focuses on trust boundaries, control design, and evidence availability, with reference to the Stipulated Final Judgment and Order entered January 26, 2006 (Matter No. 052-3069).</p>

<p><strong>Architecture Overview: </strong>The relevant architecture centers on subscriber onboarding workflows, identity-proofing systems, query and export services, and fraud-monitoring pipelines for consumer data access. Trust boundaries separate onboarding channels, authenticated subscriber access, and sensitive data retrieval services. This is a data-broker access-governance architecture, not a source-code credential incident architecture.</p>

<p><strong>Security Controls (Post-Remediation): </strong>(1) <em>Perimeter and onboarding controls.</em> Verification gates for business identity and account activation. (2) <em>Access.</em> Role and entitlement controls for internal and subscriber-facing functions. (3) <em>Data.</em> Guardrails on sensitive consumer report retrieval and export channels. (4) <em>Monitoring.</em> Analytics for suspicious query volume, export behavior, and account anomaly patterns.</p>

<p><strong>Incident Vector and Remediation: </strong>The FTC matter focused on fraudulent entities obtaining access through weak onboarding and credentialing controls. Remediation strengthens business verification, query monitoring, and investigative workflows. Residual risk remains in high-volume onboarding channels and evolving fraud tactics; mitigations include adaptive analytics, manual review queues, and annual assessment evidence.</p>

<p><strong>Assumptions and Limitations: </strong>This memorandum reflects architecture as of the date above for legal and regulator response. It is not a guarantee of invulnerability. Additional control documentation and process diagrams are available for examiner review.</p>

</div>

**Document-type guide:** [Security Architecture Explanation for Legal Review](../../../../document-types/legal-technical/security-architecture-explanation-legal-review.md)

**Writing tips:** [Writing best practices — Security Architecture Explanation for Legal Review](../../../../studio/writing-best-practices.md#security-architecture-explanation-for-legal-review)
