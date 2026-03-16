# Audit Packet Checklist (48-hour evidence readiness)

If examined (regulator, auditor, litigation), you should be able to produce the following within **48 hours**.

## A) Architecture + boundaries
- Cloud architecture diagram (current + at time of incident if available)
- Internet-facing app inventory and ownership
- WAF/boundary baseline policy documentation
- Exception register (with expiry + compensating controls)

## B) Change control proof
- PR approvals for boundary config changes
- Change tickets and approval records for high-risk modifications
- Emergency change log + post-approval review evidence

## C) IAM least privilege proof
- IAM role inventory (especially roles with access to sensitive storage)
- Policy JSON snapshots and changes
- Access review attestations + remediation of stale access

## D) Logging + monitoring proof
- Log sources list (cloud audit, WAF, auth, data access)
- Retention configuration + policy
- Detection rules and alert thresholds
- Investigation tickets (sample) with timestamps and outcomes

## E) Risk management & governance
- Risk register entries related to cloud boundaries/IAM/logging
- Risk acceptance memos and revisit schedules
- Audit/independent testing reports + remediation closure evidence
- Executive reporting samples (quarterly security governance)

## F) Incident response readiness
- IR plan + runbooks for cloud data exposure scenarios
- Tabletop exercise records
- Post-incident review format + lessons learned tracking
