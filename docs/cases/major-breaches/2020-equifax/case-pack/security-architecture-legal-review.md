# Security Architecture Explanation for Legal Review (Equifax 2017 Incident (2020 oversight))

> Use this to explain security architecture and key controls in language suitable for legal review; helps counsel understand technical design and risk.

---

## Purpose

This memorandum explains the relevant security architecture and control boundaries for Equifax 2017 Incident (2020 oversight) in terms accessible to legal stakeholders. It links technical design choices to risk outcomes, evidence availability, and obligations under investigation, enforcement, or litigation timelines.

## Hallucinated writing examples

**Scenario:** In an illustrative period following federal Equifax enforcement orders and ongoing MDL settlement administration **(time)**, the Lead Security Engineer, Enterprise Architecture Security **(role)** prepares a security architecture explanation for legal review **(type)** for General Counsel **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY ARCHITECTURE EXPLANATION FOR LEGAL REVIEW</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>General Counsel<br>
<strong>From: </strong>Lead Security Engineer, Enterprise Architecture Security<br>
<strong>Date: </strong>October 20, 2020<br>
<strong>Re: </strong>Security Architecture Overview — Consumer Credit Data Environment; Post-2017 Incident and Federal Oversight</p>
</div>

<p><strong>Scope: </strong>This memo summarizes the security architecture relevant to legal review and disclosure support for Equifax 2017 Incident (2020 oversight). It focuses on trust boundaries, control design, and evidence availability, with reference to the FTC stipulated order entered July 22, 2019, parallel CFPB action, and ongoing civil proceedings.</p>

<p><strong>Architecture Overview: </strong>The reviewed architecture includes internet-facing dispute and consumer services, middleware and data-access tiers, and backend credit data stores segmented by role and function. Core trust boundaries separate public ingress, administrative control planes, and sensitive data domains. Post-incident architecture updates prioritize reducing direct paths from perimeter applications to high-value datasets.</p>

<p><strong>Security Controls (Post-Remediation): </strong>(1) <em>Perimeter.</em> Hardened boundary configurations and vulnerability patch SLAs for internet-facing assets. (2) <em>Access.</em> Privileged access management, role scoping, and periodic recertification for administrative accounts. (3) <em>Data.</em> Encryption controls and key-management policy alignment for sensitive stores. (4) <em>Monitoring.</em> Centralized SIEM ingestion with retention and alerting on anomalous access patterns.</p>

<p><strong>Incident Vector and Remediation: </strong>Public findings emphasized exploitation of a critical internet-facing vulnerability and subsequent access pathways into sensitive consumer data. Remediation includes patch-governance controls, segmentation improvements, IAM contraction, and stronger monitoring coverage. Residual risk remains from legacy system dependencies and third-party connectors; mitigations include independent assessments and aging-based escalation for open findings.</p>

<p><strong>Assumptions and Limitations: </strong>This explanation reflects architecture state as of the date above for legal and oversight use. It is not a guarantee of invulnerability. Supporting diagrams, evidence maps, and assessment artifacts are maintained for regulator and litigation response.</p>

</div>

**Document-type guide:** [Security Architecture Explanation for Legal Review](../../../../document-types/legal-technical/security-architecture-explanation-legal-review.md)

**Writing tips:** [Writing best practices — Security Architecture Explanation for Legal Review](../../../../studio/writing-best-practices.md#security-architecture-explanation-for-legal-review)
