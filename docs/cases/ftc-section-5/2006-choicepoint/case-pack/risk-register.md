# Risk Register (FTC v. ChoicePoint Inc. (2006))

## Purpose

This register captures material risks highlighted by FTC v. ChoicePoint Inc. (2006) with severity, impact pathway, mitigation plan, and evidence expectations. It is intended for ongoing governance and audit use so risk acceptance, remediation progress, and accountability remain explicit over time.

## Risk Register

### SUB-VET-01 — Fraudulent subscriber onboarding
- **Severity:** Critical
- **Description:** Weak business verification enables illegitimate entities to obtain sensitive consumer data.
- **Impact:** Large-scale unauthorized data acquisition and enforcement exposure.
- **Mitigation:** Enhanced identity-proofing, manual review queues, and KYB controls for high-risk applicants.
- **Evidence:** Verification workflow records, onboarding decision logs, fraud-case files.

### QUERY-MON-02 — Abnormal query/export behavior under-detection
- **Severity:** High
- **Description:** Insufficient analytics on access patterns delays identification of misuse.
- **Impact:** Extended unauthorized access duration and higher consumer harm.
- **Mitigation:** Anomaly detection for query volume/export behavior with analyst response runbooks.
- **Evidence:** Detection rule catalog, alert outcomes, investigation timelines.

### ACCESS-RECERT-03 — Entitlement staleness and over-access
- **Severity:** High
- **Description:** Legacy and stale entitlements increase misuse risk internally and externally.
- **Impact:** Unauthorized access risk and weaker enforcement defensibility.
- **Mitigation:** Quarterly recertification with forced removal of orphaned privileges.
- **Evidence:** Recertification attestations, entitlement inventory, deprovisioning logs.

### ASSESS-04 — Annual assessment evidence quality risk
- **Severity:** Medium
- **Description:** Poor evidence organization can weaken FTC confidence in compliance maturity.
- **Impact:** Findings recurrence and reporting friction.
- **Mitigation:** Control-to-evidence index and quality review before assessor cycles.
- **Evidence:** Evidence catalog, assessment prep checklists, assessor feedback.

### FRAUD-CAP-05 — Fraud operations surge capacity gaps
- **Severity:** Medium
- **Description:** Spike periods can exceed investigation and response capacity.
- **Impact:** Delayed containment and reporting gaps.
- **Mitigation:** Surge staffing model and prioritized triage criteria for high-severity fraud indicators.
- **Evidence:** Staffing plans, SLA metrics, backlog trends, escalation logs.

