# Security Architecture Explanation for Legal Review (SEC v. SolarWinds (2023–2025))

> Use this to explain security architecture and key controls in language suitable for legal review; helps counsel understand technical design and risk.

---

## Purpose

This memorandum explains the relevant security architecture and control boundaries for SEC v. SolarWinds (2023–2025) in terms accessible to legal stakeholders. It links technical design choices to risk outcomes, evidence availability, and obligations under investigation, enforcement, or litigation timelines.

## Hallucinated writing examples

**Scenario:** In an illustrative period following SEC v. SolarWinds pleadings and subsequent dismissal developments **(time)**, the Lead Security Engineer, Secure Build Architecture **(role)** prepares a security architecture explanation for legal review **(type)** for Office of General Counsel **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY ARCHITECTURE EXPLANATION FOR LEGAL REVIEW</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Office of General Counsel<br>
<strong>From: </strong>Lead Security Engineer, Secure Build Architecture<br>
<strong>Date: </strong>February 14, 2025<br>
<strong>Re: </strong>Security Architecture Overview — Secure Build and Release Controls; Post-SUNBURST Governance</p>
</div>

<p><strong>Scope: </strong>This memo summarizes the security architecture relevant to legal review and disclosure support for SEC v. SolarWinds (2023–2025). It focuses on trust boundaries, control design, and evidence availability, with reference to the SEC civil action filed October 30, 2023, subsequent motion practice, and dismissal developments in 2025.</p>

<p><strong>Architecture Overview: </strong>The architecture under review covers software build and release pipelines, signing systems, developer access boundaries, telemetry controls, and customer-facing update distribution layers. Trust boundaries are defined between source control, build infrastructure, signing keys, and release publication channels.</p>

<p><strong>Security Controls (Post-Remediation): </strong>(1) <em>Perimeter and build isolation.</em> Segmented build environments with controlled ingress/egress. (2) <em>Access.</em> Privileged access controls for build and signing systems with recertification and session logging. (3) <em>Data and artifact integrity.</em> Release attestation, signature validation, and artifact provenance controls. (4) <em>Monitoring.</em> Detection for anomalous build activity, code changes, and publishing events.</p>

<p><strong>Incident Vector and Remediation: </strong>SUNBURST demonstrated compromise of software supply-chain trust boundaries. Remediation emphasizes secure build hardening, attestation coverage, and improved alignment between technical risk findings and disclosure workflows. Residual risk remains in complex legacy pipeline stages and third-party dependencies; mitigations include phased modernization and independent testing.</p>

<p><strong>Assumptions and Limitations: </strong>This memo is accurate as of the date above and supports legal and disclosure review. It does not guarantee invulnerability. Supplemental architecture diagrams and control validation reports are available for counsel.</p>

</div>

**Document-type guide:** [Security Architecture Explanation for Legal Review](../../../../document-types/legal-technical/security-architecture-explanation-legal-review.md)

**Writing tips:** [Writing best practices — Security Architecture Explanation for Legal Review](../../../../studio/writing-best-practices.md#security-architecture-explanation-for-legal-review)
