# Security Architecture Explanation for Legal Review (Capital One 2019)

> Use this to explain security architecture and key controls in language suitable for legal review; helps counsel understand technical design and risk.

---

## Purpose

Give counsel and disclosure owners a plain-language architecture and control summary tied to the incident vector, remediation, and limitations—so legal opinions and filings stay accurate and consistent with technical evidence.

---

## Hallucinated writing examples

**Scenario:** In October 2020, in connection with regulatory response (OCC) and potential litigation (consumer class-action, <em>In re Capital One Consumer Data Security Breach Litigation</em>) **(time)**, General Counsel **(audience)** requests a security architecture explanation for legal review. The Lead Security Engineer **(role)** is asked to produce a security architecture memo for legal review **(type)** that explains the AWS-hosted architecture, the July 2019 incident vector, and the post-remediation control environment in plain language suitable for counsel and disclosure. The document must be accurate as of the date of writing and cite the criminal case and Consent Order where relevant.

<div class="writing-example-formal">

<p><strong>SECURITY ARCHITECTURE EXPLANATION FOR LEGAL REVIEW</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Office of General Counsel<br>
<strong>From: </strong>Lead Security Engineer, Cloud Security<br>
<strong>Date: </strong>October 15, 2020<br>
<strong>Re: </strong>Security Architecture Overview — AWS-Hosted Infrastructure; July 2019 Incident and Post-Remediation Control Environment</p>
</div>

<p><strong>Scope: </strong>This memo summarizes the security architecture applicable to customer data stored in AWS-hosted infrastructure, as relevant to disclosure, litigation, or regulatory response. It describes the environment in which the July 2019 cybersecurity incident occurred, the vector used by the external actor, and the control environment after remediation. It is intended to support informed legal review and accurate disclosure. References: OCC Consent Order (Aug. 6, 2020), OCC NR 2020-98; <em>United States v. Paige A. Thompson</em>, U.S. District Court, W.D. Wash.; Capital One public statement (July 29, 2019).</p>

<p><strong>Architecture Overview: </strong>Customer-facing applications and supporting data that were affected in the July 2019 incident reside in our AWS-hosted infrastructure. Network segmentation separates tiers; perimeter controls include web application firewalls (WAF) and routing rules. At the time of the incident, a misconfiguration in one of the WAF components allowed the actor to obtain credentials and access data stored in our cloud environment. Following the incident, we have moved to config-as-code and peer review for perimeter controls and have deployed drift detection. Identity and access use AWS IAM (Identity and Access Management) with role-based access; a least-privilege review is in progress to reduce over-permissioned roles that contributed to the incident.</p>

<p><strong>Security Controls (Post-Remediation): </strong>(1) <em>Perimeter.</em> WAF and boundary rules are maintained in version control; changes require pull request and approval; drift detection alerts on unauthorized change. (2) <em>Access.</em> IAM roles are scoped to function; we are reducing broad and wildcard permissions. (3) <em>Data.</em> Encryption at rest and in transit; key management per policy. (4) <em>Monitoring.</em> Centralized logging with defined retention; alerting on anomalous access. Data flows enter via [described paths]; processing occurs within designated VPCs (virtual private clouds); egress is restricted and logged.</p>

<p><strong>Incident Vector and Remediation: </strong>The July 2019 incident involved access obtained via a misconfigured WAF; the actor exploited this to obtain credentials and access customer data. That vector has been remediated; the vulnerable configuration was fixed in July 2019 and we have strengthened configuration governance as described above. Residual risk includes misconfiguration or insider access; mitigations include config-as-code, peer review, drift detection, logging, and independent testing.</p>

<p><strong>Assumptions and Limitations: </strong>This description is accurate as of the date above. It does not constitute a guarantee of invulnerability; it supports informed disclosure and legal review. Technical detail is available in appended diagrams and control documentation.</p>

</div>

**Document-type guide:** [Security Architecture Explanation for Legal Review](../../../../document-types/legal-technical/security-architecture-explanation-legal-review.md)

**Writing tips:** [Writing best practices — Security Architecture Explanation for Legal Review](../../../../studio/writing-best-practices.md#security-architecture-explanation-for-legal-review)
