# Implementation Checklist (Capital One 2019)

A practical rollout plan with measurable proof.

## 0–30 days (stabilize + baseline)
- Inventory internet-facing apps and associated WAF policies
- Move WAF and boundary policies into Git (config-as-code)
- Establish approval workflow for high-risk changes (WAF/IAM/storage access)
- Centralize cloud control-plane logging (if gaps exist)
- Define retention targets (e.g., 180–365 days) for key logs

**Deliverables**
- Baseline WAF policy repo with PR approvals enabled
- “Critical boundary change” SOP
- Log coverage report for cloud audit + WAF + auth

## 30–60 days (control effectiveness)
- Implement drift detection for boundary configs
- Enforce IAM least privilege review for sensitive storage roles
- Create anomaly detections for high-volume reads and unusual access
- Add incident investigation templates and required ticket fields

**Deliverables**
- Drift detection alerting + monthly metrics
- IAM access review pack (who/what/why/when)
- Detection rules documented + tested

## 60–90 days (evidence readiness)
- Build a “48-hour evidence pack” checklist and dry-run it
- Add independent testing checkpoints (audit or external assessment)
- Establish quarterly reporting to executives: control effectiveness + risk posture

**Deliverables**
- Evidence pack folder structure + owners
- Mock regulator/litigation evidence drill outcomes
- Quarterly security governance report template

## Ongoing metrics (prove it’s real)
- % boundary changes via PR review
- Drift detection MTTR
- IAM wildcard permission count
- Log coverage percentage
- High-risk findings closure time
