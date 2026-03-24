# Internal Security Directive (Capital One 2019)

> Use this to issue a directive or mandate from leadership on security: required actions, deadlines, or standards; creates clear accountability and follow-up.

---

## Purpose

Mandate immediate, measurable actions on cloud perimeter and boundary controls after the breach—deadlines, owners, and escalation—so the organization can show leadership commitment and a compliance trail for regulators and the board.

---

## Hallucinated writing examples

**Scenario:** In September 2019, approximately six weeks after the July 2019 breach disclosure and the arrest of the individual responsible **(time)**, the Chief Information Security Officer **(role)** issues an internal security directive **(type)** to the Board and Bank leadership **(audience)** mandating immediate controls for cloud perimeter configuration. The directive is issued during the incident response and regulatory scrutiny; it is intended to prevent recurrence and to demonstrate to the Board and future regulators that the Bank has mandated specific, measurable actions. The directive will be tracked for compliance and may be referenced in OCC or legal process.

<div class="writing-example-formal">

<p><strong>INTERNAL SECURITY DIRECTIVE</strong></p>

<div class="doc-meta">
<p><strong>Issuing authority: </strong>Chief Information Security Officer (with acknowledgment of Chief Executive Officer and General Counsel)<br>
<strong>Effective date: </strong>September 15, 2019<br>
<strong>Subject: </strong>Mandatory Control — Cloud Perimeter and Boundary Configuration; No Production Changes Without Peer Review and Documentation</p>
</div>

<p><strong>Context: </strong>On July 29, 2019, the Company publicly disclosed that an unauthorized individual had obtained access to customer data stored in our AWS-hosted infrastructure. The vulnerability has been secured and law enforcement was notified; the individual was arrested the same day. This directive is issued to prevent recurrence and to establish mandatory controls for cloud perimeter and boundary configuration. It applies to all business and technology units responsible for web application firewall (WAF), routing, exposure rules, and designated equivalent controls in our AWS and other cloud environments.</p>

<p><strong>Directive: </strong>Effective immediately, no production change to cloud perimeter or boundary controls (WAF, routing, exposure rules, and designated equivalent) shall be made outside an approved change workflow that includes (1) proposal and review in version control or equivalent, (2) peer review by a designated reviewer, and (3) approval before merge or deployment. All such changes must be documented and traceable. Exceptions require CISO approval and documented risk acceptance with a defined revisit date. In addition, all teams that administer perimeter or boundary configuration affecting [designated data or systems] shall, by December 31, 2019, document current baselines and establish a process for detecting and remediating unauthorized or unapproved changes (drift). Third-party managed components are in scope where the Bank controls or can influence configuration.</p>

<p><strong>Accountability and Deadlines: </strong>Technology owners are responsible for implementation and for producing evidence of compliance (e.g., repository coverage, change tickets, baseline documentation). The CISO organization is responsible for defining the change workflow, approving exceptions, and reporting to the Board and to Risk. Compliance and progress shall be reported to the CISO and Risk per [cadence]. Failure to meet the requirements or deadlines may result in escalation to [executive] and reporting to the Audit Committee. Questions: Contact the CISO organization at [contact]. Supporting standards and procedures will be published by [date].</p>

</div>

**Document-type guide:** [Internal Security Directive](../../../../document-types/policy-governance/internal-security-directive.md)

**Writing tips:** [Writing best practices — Internal Security Directive](../../../../studio/writing-best-practices.md#internal-security-directive)
