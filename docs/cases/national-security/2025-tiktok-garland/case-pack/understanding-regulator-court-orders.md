# Understanding Regulatory and Court Orders (TikTok Inc. v. Garland)

## Purpose

This guide turns the Supreme Court opinion into operational questions for security, legal, privacy, product, and governance teams. The case does not create a generic ban on foreign-linked platforms. It is a narrow decision about a specific statute, a specific record, and the Court's treatment of data collection, foreign-adversary control, and First Amendment burden.

## Holding posture

The Court affirmed the D.C. Circuit and held that the Protecting Americans from Foreign Adversary Controlled Applications Act survived the First Amendment challenge as applied to TikTok and its users. The Court treated the data-collection justification as content neutral and held the challenged provisions were not substantially broader than necessary to address the government's data-collection concerns.

## Operational translation

| Opinion theme | Practical security question | Evidence to preserve |
|---|---|---|
| Scale and sensitive data | What sensitive data is collected from U.S. users and at what scale? | Data inventory, data-flow map, retention map, access logs |
| Foreign-adversary control | Who can compel, influence, or technically access data, code, or operations? | Ownership map, access-control records, legal-control analysis |
| Recommendation algorithm | Who owns and changes ranking, recommendation, moderation, and promotion systems? | Change-control tickets, model ownership records, approval logs |
| Qualified divestiture | Would a separation actually sever foreign control over operations and data? | Separation architecture, dependency map, third-party validation |
| Narrow holding | What facts make this platform different from ordinary data collectors? | Risk memo, user-scale metrics, threat model, board decision record |

## Key implementation rule

Treat control as an engineering fact. A legal structure is not enough if data, code, recommendation systems, credentials, infrastructure, or operational runbooks remain dependent on the controlled entity.

## Primary sources

- [Supreme Court opinion](https://www.supremecourt.gov/opinions/24pdf/24-656_new_3dq3.pdf)
