# Risk Register (Equifax 2017 Incident (2020 oversight))

## Purpose

This register captures material risks highlighted by Equifax 2017 Incident (2020 oversight) with severity, impact pathway, mitigation plan, and evidence expectations. It is intended for ongoing governance and audit use so risk acceptance, remediation progress, and accountability remain explicit over time.

## Risk Register

### VULN-PATCH-01 — Internet-facing critical patch latency
- **Severity:** Critical
- **Description:** Public enforcement narratives center on delayed remediation of critical external vulnerabilities.
- **Impact:** Repeat exposure path to sensitive consumer data and severe regulatory consequences.
- **Mitigation:** Risk-based patch SLAs, emergency CAB workflow, and verification testing for Tier-0 systems.
- **Evidence:** Patch latency dashboards, CAB records, verification reports, open critical CVE tracker.

### PRIV-IAM-02 — Over-privileged administrative access
- **Severity:** Critical
- **Description:** Broad IAM entitlements increase probability of unauthorized high-value data access.
- **Impact:** High-severity data exposure and prolonged incident blast radius.
- **Mitigation:** PAM rollout, entitlement recertification, just-in-time elevation, session monitoring.
- **Evidence:** PAM coverage reports, access review attestations, exception approvals, session logs.

### SIEM-COV-03 — Detection and retention coverage gaps
- **Severity:** High
- **Description:** Incomplete SIEM ingestion and inconsistent retention weaken detection and forensic response.
- **Impact:** Delayed incident response and weaker evidence for exams and civil proceedings.
- **Mitigation:** Expand SIEM onboarding, retention standards, and anomaly detection for data access paths.
- **Evidence:** SIEM onboarding metrics, retention conformance audits, detection tuning records.

### ASSESS-AGE-04 — Independent assessment finding recurrence
- **Severity:** High
- **Description:** Aged high-risk findings indicate weak closure discipline under federal oversight.
- **Impact:** Repeat regulator concern and prolonged remediation risk.
- **Mitigation:** Owner-based closure governance with escalation for overdue high-severity findings.
- **Evidence:** Assessment reports, finding-age dashboard, closure approvals, committee minutes.

### 3P-CONN-05 — Third-party connector risk
- **Severity:** Medium
- **Description:** External service and connector pathways introduce control variance across environments.
- **Impact:** Potential data access exposure and policy exceptions accumulation.
- **Mitigation:** Third-party segmentation reviews, contractual security requirements, periodic reassessment.
- **Evidence:** Vendor assessment files, connector inventories, exception logs, remediation plans.

