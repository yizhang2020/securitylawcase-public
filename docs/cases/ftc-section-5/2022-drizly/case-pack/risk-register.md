# Risk Register (FTC v. Drizly 2022)

## Purpose

This register captures material risks highlighted by FTC v. Drizly 2022 with severity, impact pathway, mitigation plan, and evidence expectations. It is intended for ongoing governance and audit use so risk acceptance, remediation progress, and accountability remain explicit over time.

## Risk Register

### MFA-IAM-01 — Privileged MFA and IAM control variance
- **Severity:** Critical
- **Description:** Incomplete MFA and entitlement hygiene on sensitive paths can enable account compromise.
- **Impact:** High likelihood of unauthorized cloud and data access.
- **Mitigation:** Enforce MFA universally on privileged paths and tighten role scopes.
- **Evidence:** MFA enrollment metrics, entitlement review logs, policy enforcement reports.

### SECRETS-02 — Secrets exposure in code and pipelines
- **Severity:** Critical
- **Description:** Credentials in repositories create direct compromise pathways.
- **Impact:** Rapid escalation from developer compromise to production access.
- **Mitigation:** Secret scanning, commit blocking, rotation policy, and exception expiry controls.
- **Evidence:** Scanner findings, rotation records, exception approvals, pipeline policy logs.

### DETECT-03 — Detection latency for data exfiltration
- **Severity:** High
- **Description:** Insufficient high-fidelity detections delay response to anomalous access.
- **Impact:** Longer dwell time and greater consumer impact.
- **Mitigation:** Telemetry expansion and dedicated exfiltration detection engineering backlog.
- **Evidence:** Alert MTTD metrics, detection rule change log, incident reports.

### RET-MIN-04 — Data retention/minimization noncompliance
- **Severity:** High
- **Description:** Weak retention enforcement conflicts with FTC order obligations.
- **Impact:** Regulatory exposure and increased breach impact surface.
- **Mitigation:** Publish retention schedule and automate deletion/de-identification jobs.
- **Evidence:** Retention schedule attestations, deletion run logs, exception register.

### ASSESS-05 — Independent assessment readiness gaps
- **Severity:** Medium
- **Description:** Incomplete evidence or control maturity can delay assessment closure.
- **Impact:** Extended compliance risk and regulator scrutiny.
- **Mitigation:** Assessment readiness program with owner assignments and milestone tracking.
- **Evidence:** Assessment plans, readiness checklists, closure evidence.

