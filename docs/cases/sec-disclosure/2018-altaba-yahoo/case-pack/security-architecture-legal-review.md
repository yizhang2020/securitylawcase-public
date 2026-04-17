# Security Architecture Explanation for Legal Review (Altaba / Yahoo SEC (2018))

> Use this to explain security architecture and key controls in language suitable for legal review; helps counsel understand technical design and risk.

---

## Purpose

This memorandum explains the relevant security architecture and control boundaries for Altaba / Yahoo SEC (2018) in terms accessible to legal stakeholders. It links technical design choices to risk outcomes, evidence availability, and obligations under investigation, enforcement, or litigation timelines.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the SEC April 2018 cease-and-desist order on delayed breach disclosure **(time)**, the Lead Security Engineer, Incident and Disclosure Controls **(role)** prepares a security architecture explanation for legal review **(type)** for Office of General Counsel **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY ARCHITECTURE EXPLANATION FOR LEGAL REVIEW</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Office of General Counsel<br>
<strong>From: </strong>Lead Security Engineer, Incident and Disclosure Controls<br>
<strong>Date: </strong>May 18, 2018<br>
<strong>Re: </strong>Security Architecture Overview — Incident Evidence and Disclosure-Control Support; SEC File No. 3-18448</p>
</div>

<p><strong>Scope: </strong>This memo summarizes the security architecture relevant to legal review and disclosure support for Altaba / Yahoo SEC (2018). It focuses on trust boundaries, control design, and evidence availability, with reference to the SEC administrative order of April 24, 2018 (File No. 3-18448).</p>

<p><strong>Architecture Overview: </strong>The architecture in scope includes incident-detection telemetry, identity and account services, evidence-retention pipelines, and governance interfaces to legal and finance disclosure workflows. Trust boundaries are defined across security operations systems, incident response case management, and reporting control channels used for securities disclosures.</p>

<p><strong>Security Controls (Post-Remediation): </strong>(1) <em>Perimeter and detection controls.</em> Monitoring on account-facing services and incident triage workflows. (2) <em>Access.</em> Controlled administrative access to incident evidence and disclosure-support systems. (3) <em>Data.</em> Retention policies and legal-hold controls for logs and investigative artifacts. (4) <em>Monitoring.</em> Alerting and escalation checkpoints tied to disclosure-control procedures.</p>

<p><strong>Incident Vector and Remediation: </strong>The SEC order emphasized delay between internal confirmation of unauthorized access and investor-facing disclosure. Remediation focuses on architecture-level support for timely escalation, evidence integrity, and cross-functional review. Residual risk remains in manual handoffs and legacy logging islands; mitigations include workflow automation, retention controls, and testing of disclosure controls.</p>

<p><strong>Assumptions and Limitations: </strong>This summary is accurate as of the date above and intended for legal review. It does not guarantee invulnerability. Additional architecture diagrams, runbooks, and evidence maps are available to counsel.</p>

</div>

**Document-type guide:** [Security Architecture Explanation for Legal Review](../../../../document-types/legal-technical/security-architecture-explanation-legal-review.md)

**Writing tips:** [Writing best practices — Security Architecture Explanation for Legal Review](../../../../studio/writing-best-practices.md#security-architecture-explanation-for-legal-review)
