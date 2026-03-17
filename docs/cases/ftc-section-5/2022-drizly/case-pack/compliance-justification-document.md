# Compliance Justification Document (FTC v. Drizly 2022)

> Justify how controls meet the FTC consent order and map to a framework (e.g., NIST CSF) for examiner or auditor review.

---

## Purpose

Following the FTC consent order, this document supports a **compliance justification** that maps the company’s controls to the order’s requirements and, where applicable, to NIST CSF or CIS Controls. It is intended for use by the security or compliance owner when responding to the FTC or an auditor.

**Key order requirements (condensed):** Written information security program; designated coordinator; risk assessment; safeguards (access control, credential management, monitoring, secure development, data minimization); training; testing; service provider oversight; biennial independent assessment; data retention schedule and deletion of unnecessary personal information.

**NIST CSF mapping (illustrative):** PR.AC (Identity Management, Access Control); PR.IP (Protection Processes and Procedures); DE.CM (Security Continuous Monitoring); ID.RA (Risk Assessment); ID.AM (Asset Management). The FTC order does not mandate a specific framework; mapping demonstrates alignment with recognized standards.

---

## Control-to-order mapping (summary)

| Order requirement | Control / evidence | Framework (optional) |
|-------------------|--------------------|----------------------|
| Written program | Program document; governance charter | PR.IP |
| Designated coordinator | Role designation; reporting structure | Governance |
| Risk assessment | Risk register; assessment reports | ID.RA |
| Access control / MFA | MFA enforcement; access reviews; offboarding | PR.AC |
| No credentials in code | Repo scanning; change review | PR.IP, secure SDLC |
| Monitoring | Logging; detection rules; assessment | DE.CM |
| Data minimization | Retention schedule; deletion logs | PR.IP, privacy |
| Biennial assessment | Third-party report; remediation tracking | Governance |

---

## Primary sources

- **FTC Decision and Order:** [Decision and Order — Drizly, LLC, and James Cory Rellas](https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf), FTC Docket No. 2023185 (Oct. 24, 2022).
- **NIST Cybersecurity Framework:** [NIST CSF](https://www.nist.gov/cyberframework) — for control-to-outcome mapping.
- **CIS Controls:** [CIS Critical Security Controls](https://www.cisecurity.org/controls) — often used in regulatory and audit contexts.
