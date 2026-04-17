# Implementation Checklist (Drizly (FTC 2022))

A practical rollout plan with measurable proof for cloud control hardening and FTC-order execution tracking.

## 0–30 days (stabilize + baseline)
- Inventory cloud services handling customer data and current boundary controls
- Move high-risk cloud/IAM settings into controlled configuration workflow
- Centralize cloud audit and auth logs with retention baselines

**Deliverables**
- Cloud control baseline register and owners
- High-risk cloud change SOP with approval gates
- Cloud telemetry coverage and retention report

## 30–60 days (control effectiveness)
- Implement drift detection for cloud boundary and identity controls
- Perform least-privilege review for cloud admin and service roles
- Deploy detections for unusual cloud data-access patterns

**Deliverables**
- Drift alerting dashboard with monthly metrics
- IAM review pack and remediation backlog
- Detection engineering test records

## 60–90 days (evidence readiness)
- Execute 48-hour evidence-pack dry run for FTC-order support
- Add independent testing checkpoints for prioritized cloud controls
- Publish quarterly management reporting on order milestones and risk posture

**Deliverables**
- Evidence-pack structure with accountable owners
- Readiness drill findings and closure plan
- Quarterly order-progress governance template

## Ongoing metrics (prove it's real)
- % high-risk cloud changes approved pre-deploy
- Cloud control drift MTTR
- Admin privilege reduction trend
- Coverage % for cloud audit/auth/data logs
- Time to close high-severity control findings
