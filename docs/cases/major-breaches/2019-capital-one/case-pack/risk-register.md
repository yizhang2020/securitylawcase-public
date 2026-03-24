# Risk Register (Capital One 2019)

## Purpose

Provide an incident-grounded register of the material security risks revealed by the 2019 Capital One breach, so engineering, security leadership, and risk/compliance teams can track remediation, assign owners, and demonstrate control effectiveness to internal and external stakeholders.
The entries below are prepared for copy and paste into `executive-security-risk-summary.md`, `security-program-status-report.md`, `compliance-justification-document.md`, and `security-governance-memo.md` (either in the main body where risk posture is discussed or as an appendix for detailed risk records).

## Risk Register

### CLD-BOUNDARY-01 — Internet-Facing Control Misconfiguration (WAF/Boundary)
- **Severity:** Critical
- **Description:** Cloud boundary and WAF configuration weaknesses enabled SSRF-style exploitation and unauthorized access path creation.
- **Impact:** Initial compromise vector into internal cloud resources; high likelihood of data exposure and regulatory consequences.
- **Mitigation:** Config-as-code for boundary controls, mandatory peer review, pre-deploy validation, and continuous drift detection with time-bound remediation.
- **Evidence:** Approved pull requests, baseline configurations, drift alerts, remediation tickets, change records.

### CLD-IAM-02 — Excessive IAM Permissions and Credential Misuse Path
- **Severity:** Critical
- **Description:** IAM permissions and credential handling allowed privilege expansion and access to sensitive storage beyond least-privilege intent.
- **Impact:** Unauthorized access to customer data stores and large-scale exfiltration potential.
- **Mitigation:** Least-privilege role redesign, explicit deny guardrails, scoped credential access, and periodic entitlement recertification.
- **Evidence:** IAM policy diffs, access review attestations, privileged access inventory, exception approvals.

### CLD-META-03 — Metadata Service Abuse Exposure
- **Severity:** High
- **Description:** Workload exposure to instance metadata retrieval created a pathway to obtain temporary cloud credentials.
- **Impact:** Credential theft leading to lateral movement and unauthorized data access.
- **Mitigation:** IMDS hardening (IMDSv2), metadata access restrictions, network egress controls, and workload-level protections against SSRF patterns.
- **Evidence:** Cloud configuration snapshots, IMDS settings reports, network policy evidence, penetration test results.

### DET-IR-04 — Delayed Detection and Escalation
- **Severity:** High
- **Description:** Monitoring and alerting did not provide timely detection of suspicious activity and exfiltration behavior.
- **Impact:** Extended attacker dwell time, increased data loss, and higher response/legal cost.
- **Mitigation:** Centralized logging, high-fidelity detections for anomalous access/exfiltration, alert tuning, and tested escalation runbooks.
- **Evidence:** SIEM coverage reports, alert definitions, incident timelines, mean-time-to-detect metrics.

### GOV-EVID-05 — Governance and Evidence Readiness Gaps
- **Severity:** Medium
- **Description:** Incomplete evidence mapping and inconsistent governance reporting reduced ability to prove control effectiveness quickly.
- **Impact:** Regulatory and litigation disadvantage, slower audit/exam response, and decision latency.
- **Mitigation:** Control-to-evidence index, standardized evidence retention, recurring governance reporting, and independent control validation.
- **Evidence:** Evidence catalog, board/risk committee reporting packs, control test reports, audit remediation status.
