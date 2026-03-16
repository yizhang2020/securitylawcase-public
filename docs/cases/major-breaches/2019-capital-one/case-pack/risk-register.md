# Risk Register (Capital One 2019)

These entries are designed to be copied into your GRC tooling.

> Download the CSV version from the Templates section.

## Example risks

### CLD-BOUNDARY-01 — Boundary policy drift
- **Description:** Internet-facing boundary policies (WAF/routing/exposure) may drift from approved baseline.
- **Impact:** Unauthorized access paths; data exposure; regulatory and litigation exposure.
- **Mitigation:** Config-as-code, peer review, drift detection, emergency change controls.
- **Evidence:** PR approvals, baseline config, drift reports, change tickets.

### CLD-IAM-01 — Over-permissioned roles for sensitive storage
- **Description:** IAM roles allow broader access than required to sensitive object storage.
- **Impact:** Unauthorized reads/exfiltration; inability to demonstrate least privilege.
- **Mitigation:** Role scoping, explicit deny, quarterly access reviews, privileged inventory.
- **Evidence:** Policy JSON snapshots, access review attestations, role inventory, audit logs.

### LOG-EVID-01 — Insufficient evidence readiness
- **Description:** Logging and retention are incomplete; cannot produce evidence quickly.
- **Impact:** Weak regulatory response posture; litigation disadvantage; incomplete RCA.
- **Mitigation:** Centralize logs, enforce retention, standardize queries/runbooks.
- **Evidence:** Retention policy, log configs, sample queries, incident tickets.
