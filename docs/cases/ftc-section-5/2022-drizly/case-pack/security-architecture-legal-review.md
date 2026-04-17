# Security Architecture Explanation for Legal Review (FTC v. Drizly 2022)

> Use this to explain security architecture and key controls in language suitable for legal review; helps counsel understand technical design and risk.

---

## Purpose

This memorandum explains the relevant security architecture and control boundaries for FTC v. Drizly 2022 in terms accessible to legal stakeholders. It links technical design choices to risk outcomes, evidence availability, and obligations under investigation, enforcement, or litigation timelines.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the FTC October 2022 consent order after the July 2020 Drizly breach **(time)**, the Lead Security Engineer, Cloud and Application Security **(role)** prepares a security architecture explanation for legal review **(type)** for General Counsel **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY ARCHITECTURE EXPLANATION FOR LEGAL REVIEW</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>General Counsel<br>
<strong>From: </strong>Lead Security Engineer, Cloud and Application Security<br>
<strong>Date: </strong>December 1, 2022<br>
<strong>Re: </strong>Security Architecture Overview — Source Code Access, Cloud Environment, and FTC Order Remediation</p>
</div>

<p><strong>Scope: </strong>This memo summarizes the security architecture relevant to legal review and disclosure support for FTC v. Drizly 2022. It focuses on trust boundaries, control design, and evidence availability, with reference to the FTC Decision and Order in Docket No. 2023185 and related complaint allegations.</p>

<p><strong>Architecture Overview: </strong>The architecture includes source-code repositories, cloud administration pathways, production data stores, and security monitoring layers. Trust boundaries include developer identity systems, CI/CD and repository access, cloud control planes, and consumer data services. Post-incident architecture hardening prioritizes reducing single-account blast radius and improving detection.</p>

<p><strong>Security Controls (Post-Remediation): </strong>(1) <em>Perimeter and repository controls.</em> Enforced MFA and repository policy controls for sensitive code paths. (2) <em>Access.</em> Privileged account governance with rapid revocation and periodic recertification. (3) <em>Data.</em> Data minimization and retention controls for consumer information at rest and in transit. (4) <em>Monitoring.</em> Secret scanning, centralized logs, and anomalous access detection.</p>

<p><strong>Incident Vector and Remediation: </strong>Public allegations describe credential reuse and repository-access weaknesses that enabled downstream cloud access and data exfiltration. Remediation includes MFA enforcement, secret management, retention controls, and improved detection engineering. Residual risk remains in third-party dependencies and human credential behavior; mitigations include policy enforcement, monitoring, and independent assessments.</p>

<p><strong>Assumptions and Limitations: </strong>This legal-facing summary is accurate as of the date above and supports disclosure and oversight response. It does not guarantee invulnerability. Detailed diagrams and control-test artifacts are maintained for counsel and regulator review.</p>

</div>

**Document-type guide:** [Security Architecture Explanation for Legal Review](../../../../document-types/legal-technical/security-architecture-explanation-legal-review.md)

**Writing tips:** [Writing best practices — Security Architecture Explanation for Legal Review](../../../../studio/writing-best-practices.md#security-architecture-explanation-for-legal-review)
