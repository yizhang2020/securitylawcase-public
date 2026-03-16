# Controls → Evidence Map (Capital One 2019)

This is the core premium artifact: **what to implement** and **what to prove**.

## How to use this
For each control domain:
- **Required control state** = what “good” looks like
- **Evidence artifacts** = what you should be able to produce quickly
- **Verification signals** = what proves it’s operating (not just documented)

---

## 1) Cloud configuration governance (Config-as-code)

### Required control state
- Edge/perimeter controls (WAF, routing, exposure rules) are managed as code
- Peer-reviewed changes with approvals
- Drift detection + alerting for high-risk changes
- Standard baselines and exceptions tracked

### Evidence artifacts
- Repository history (PRs, approvals, commits) for WAF/boundary policies
- Change tickets linking to approvals and risk review
- Baseline configuration documents + exception register
- Drift detection reports + remediation tickets

### Verification signals
- % of perimeter changes via PR workflow
- Mean time to detect and remediate drift
- # of emergency changes without post-approval (should trend down)

---

## 2) IAM least privilege for sensitive storage

### Required control state
- Explicitly scoped roles for data access
- Separation between app runtime roles and data admin roles
- Regular access review with accountable sign-off
- Explicit deny patterns for sensitive data paths

### Evidence artifacts
- IAM role definitions (snapshots) and policy JSON
- Access review records (who approved, when, and why)
- Privileged role inventory + rotation policy
- Evidence of removal of stale permissions

### Verification signals
- # of roles with wildcard permissions (should trend down)
- % of roles reviewed in last 90 days
- Alerts for privilege escalation events

---

## 3) Detection & investigation readiness (cloud audit + WAF + auth logs)

### Required control state
- Centralized logging for: cloud control plane, WAF, auth, sensitive data access
- Documented alert thresholds for anomalous reads/exfil patterns
- Playbooks for investigation with consistent ticketing
- Defined retention + access to logs for legal inquiry

### Evidence artifacts
- Log retention policy and configuration evidence
- Sample queries used to detect anomalies (stored and versioned)
- SOC runbooks + investigation ticket examples
- Post-incident review format + “lessons learned” tracking

### Verification signals
- Log coverage % for critical systems
- Alert-to-triage time and triage-to-containment time
- Investigation completeness scoring (required fields filled)

---

## 4) Vulnerability management & attack surface control

### Required control state
- Asset inventory for internet-facing apps
- Continuous scanning + defined remediation SLAs
- WAF rules tied to threat models and application risk

### Evidence artifacts
- Asset inventory exports + ownership mapping
- Vulnerability backlog with SLA metrics
- Exceptions with expiry dates and compensating controls

### Verification signals
- SLA compliance %
- # of critical vulns past SLA
- % internet-facing assets with owner + risk tier assigned

---

## 5) Governance: risk management + independent testing

### Required control state
- Risk assessments produce tracked remediation
- Risk acceptance requires approval + follow-up plan
- Independent testing/audit validates effectiveness and closure

### Evidence artifacts
- Risk register entries + mitigation status reports
- Risk acceptance memos with approvers + revisit schedule
- Audit/assessment reports + remediation tracking evidence

### Verification signals
- # of accepted risks without revisit dates
- Closure rate for audit findings
- Time-to-close for high-risk findings
