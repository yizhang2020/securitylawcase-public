# Risk Register (Spokeo, Inc. v. Robins)

## Purpose

This register captures material risks highlighted by Spokeo, Inc. v. Robins with severity, impact pathway, mitigation plan, and evidence expectations. It is intended for ongoing governance and audit use so risk acceptance, remediation progress, and accountability remain explicit over time.

## Risk Register

### ACC-DATA-01 — Published attribute accuracy failures
- **Severity:** High
- **Description:** Incorrect consumer profile attributes create legal and consumer harm exposure.
- **Impact:** FCRA-related claims, reputational damage, and remediation cost.
- **Mitigation:** QA sampling expansion and source-validation controls for high-risk fields.
- **Evidence:** Error-rate dashboards, QA logs, source validation evidence.

### DISP-SLA-02 — Dispute resolution delay risk
- **Severity:** High
- **Description:** Slow correction workflows amplify harm narratives and legal exposure.
- **Impact:** Increased complaint volume and litigation sensitivity.
- **Mitigation:** Dispute SLA controls, escalation triggers, and root-cause tracking.
- **Evidence:** Dispute aging reports, closure records, escalation logs.

### LINEAGE-03 — Data provenance traceability gaps
- **Severity:** High
- **Description:** Insufficient lineage makes it hard to explain how attributes were derived.
- **Impact:** Weak legal defensibility and audit friction.
- **Mitigation:** Lineage tooling and immutable change history for contested attributes.
- **Evidence:** Lineage reports, change histories, reconciliation logs.

### OVERRIDE-04 — Manual override governance weakness
- **Severity:** Medium
- **Description:** Uncontrolled overrides can introduce inconsistent or stale data.
- **Impact:** Quality drift and repeat disputes.
- **Mitigation:** Dual-approval workflow and periodic override review.
- **Evidence:** Override approval records, periodic review attestations.

### CLAIMS-05 — Legal/technical narrative mismatch
- **Severity:** Medium
- **Description:** Differences between operational metrics and legal arguments can undermine strategy.
- **Impact:** Reduced credibility in proceedings.
- **Mitigation:** Joint legal-security review cadence for risk and accuracy reporting.
- **Evidence:** Joint review notes, approved summaries, issue trackers.

