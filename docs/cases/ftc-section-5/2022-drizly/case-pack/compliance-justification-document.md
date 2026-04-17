# Compliance Justification Document (FTC v. Drizly 2022)

> Justify how controls meet the FTC consent order and map to a framework (e.g., NIST CSF) for examiner or auditor review.

---

## Purpose

This mapping document shows how implemented controls satisfy obligations and expectations implicated by FTC v. Drizly 2022. It is structured for audit and legal review, so each requirement is tied to implementation rationale, ownership, and verifiable artifacts rather than policy statements alone.

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

**Document-type guide:** [Compliance Justification Document](../../../../document-types/regulatory-compliance/compliance-justification-document.md)

**Writing tips:** [Writing best practices — Compliance Justification Document](../../../../studio/writing-best-practices.md#compliance-justification-document)
