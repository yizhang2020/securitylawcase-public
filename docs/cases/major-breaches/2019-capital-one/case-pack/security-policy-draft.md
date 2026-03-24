# Security Policy Draft (Capital One 2019)

> Use this to draft or update an enterprise security policy; defines required behavior and controls in policy language and supports consistency and auditability.

---

## Purpose

Codify mandatory requirements for cloud perimeter and boundary security after the WAF misconfiguration root cause—so policy, standards, and evidence align with OCC consent order expectations and audit review.

---

## Hallucinated writing examples

**Scenario:** In November 2020, following the OCC Consent Order (August 6, 2020) and the July 2019 incident **(time)**, the Security Director **(role)** is tasked with drafting an enterprise security policy for cloud configuration and boundary security **(type)** for the CISO, Legal, and the Board Audit Committee **(audience)**. The policy is required under the Consent Order and must address the root cause of the incident (WAF misconfiguration and configuration governance). The draft must be supportable by standards and evidence.

<div class="writing-example-formal">

<p><strong>ENTERPRISE SECURITY POLICY — DRAFT</strong></p>

<div class="doc-meta">
<p><strong>Policy title: </strong>Cloud Configuration and Boundary Security<br>
<strong>Version: </strong>1.0 (Draft)<br>
<strong>Owner: </strong>Chief Information Security Officer<br>
<strong>Effective date: </strong>Upon approval<br>
<strong>Last reviewed: </strong>November 2020<br>
<strong>Context: </strong>Post–July 2019 incident; OCC Consent Order (OCC NR 2020-98)</p>
</div>

<p><strong>Purpose and Scope: </strong>This policy establishes requirements for the design, change, and monitoring of cloud perimeter and boundary controls to reduce the risk of unauthorized access and to support audit and regulatory expectations, including those set forth in the Consent Order issued by the Office of the Comptroller of the Currency on August 6, 2020. The July 2019 cybersecurity incident involved exploitation of a misconfiguration in our AWS-hosted web application firewall (WAF); this policy is intended to prevent recurrence and to demonstrate control effectiveness to the OCC and other stakeholders. It applies to all business units and technology teams responsible for cloud-hosted systems that process [designated data].</p>

<p><strong>Policy Statement: </strong>The organization shall manage cloud perimeter and boundary controls (including WAF, routing, and exposure rules) using config-as-code with mandatory peer review. Changes shall be authorized, documented, and monitored for drift. Exceptions shall be requested, approved, and documented with rationale, mitigation, and revisit date. This approach aligns with the Consent Order's requirement for strengthened cloud security and risk management.</p>

<p><strong>Roles and Responsibilities: </strong>The CISO owns this policy and approves exceptions within defined criteria. Technology owners implement and operate controls per supporting standards. Risk owners acknowledge risk acceptances. Audit may verify compliance. The Security Director is responsible for maintaining supporting standards and evidence of implementation.</p>

<p><strong>Requirements: </strong>(1) Designated perimeter controls shall be defined in version-controlled configuration. (2) All changes shall follow the approved change workflow (e.g., pull request, review, approval). (3) Drift detection shall be enabled; exceptions remediated or formally accepted with revisit date. (4) Baselines and exceptions shall be documented and reviewed per [cadence]. Related documents: [Cloud Configuration Standard]; [Change Management Procedure]; [Risk Acceptance Procedure]. This policy shall be reviewed annually. Non-compliance shall be reported and remediated; repeated or material non-compliance may result in [consequences per HR/governance]. Revision history: [Version, date, summary.]</p>

</div>

**Document-type guide:** [Security Policy Draft](../../../../document-types/policy-governance/security-policy-draft.md)

**Writing tips:** [Writing best practices — Security Policy Draft](../../../../studio/writing-best-practices.md#security-policy-draft)
