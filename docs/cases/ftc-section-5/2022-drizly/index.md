# FTC v. Drizly, LLC (2022) — Credential Stuffing and Reasonable Security

> **Executive summary:** The FTC alleged that Drizly failed to implement reasonable security measures, leading to a credential-stuffing attack that exposed personal information of approximately 2.5 million consumers. The order imposed security program requirements and a data minimization mandate—highlighting that “reasonable security” now includes MFA, credential attack defenses, and data retention discipline.



## Primary sources
- FTC press release — <a href="https://www.ftc.gov/news-events/news/press-releases/2022/10/ftc-takes-action-against-drizly" target="_blank" rel="noopener noreferrer">https://www.ftc.gov/news-events/news/press-releases/2022/10/ftc-takes-action-against-drizly</a>
- FTC Complaint (PDF)
- FTC Decision and Order (PDF)



## Procedural timeline
- **July 2020** — Credential stuffing breach discovered.
- **Oct 24, 2022** — FTC files complaint and announces settlement.



## Legal analysis (engineer translation)

### Legal theory
FTC Section 5 — **Unfairness**:
Failure to implement reasonable data security practices causing substantial consumer injury.

### What made it “unreasonable” (FTC view)
- No mandatory MFA for administrators
- Weak monitoring of credential stuffing
- Retention of personal data beyond business necessity
- Lack of formal security program maturity

### Remedy
- Comprehensive information security program
- Independent third-party assessments
- Data minimization requirements
- Oversight obligations



## Technical deep dive

### Attack pattern
- Credential reuse attack (passwords from other breaches)
- Automated login attempts
- Insufficient detection/rate limiting
- Privileged access weaknesses

### Control failures (portable lessons)

#### Identity & Access
- MFA not enforced universally
- Admin account protections inadequate

#### Detection
- Credential stuffing monitoring insufficient
- Alerting thresholds not effective

#### Governance
- Security program maturity gaps
- Incomplete risk management documentation

#### Data minimization
- Retention of personal data beyond operational necessity



## Compliance → Controls → Evidence

### NIST CSF
- PR.AC — Access control
- DE.CM — Continuous monitoring
- ID.RA — Risk assessment
- PR.IP — Information protection processes

### What regulators expect you to prove
- MFA enforcement logs
- Account lockout / rate limiting configs
- Credential stuffing detection metrics
- Risk register entries for auth threats
- Data deletion reports



## Engineering takeaways

- Enforce MFA for all privileged and high-value accounts.
- Deploy credential stuffing detection and rate limiting; track login anomaly metrics.
- Review and enforce data retention; delete or de-identify data beyond business necessity.
- Document authentication and access control in risk assessments and control evidence.
- Maintain evidence of security program maturity (policies, testing, oversight) for regulatory readiness.

## Premium case pack includes

A premium case pack for FTC v. Drizly is not yet published. When available, it may include:

- Board briefing memo
- Controls → evidence mapping
- Audit packet checklist
- Risk register entries
- Implementation roadmap

See the [Capital One (2019)](../../major-breaches/2019-capital-one/index.md) case for an example of a full case pack.

## Impact

Drizly reinforces that:

- Credential stuffing is foreseeable.
- MFA is baseline.
- Data minimization is becoming a core enforcement lever.
