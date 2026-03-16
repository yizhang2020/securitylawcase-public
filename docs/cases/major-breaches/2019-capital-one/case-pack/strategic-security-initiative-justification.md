# Strategic Security Initiative Justification (Capital One 2019)

> Use this to build a business case for a major security initiative (e.g., IAM overhaul, zero trust, SOC upgrade); supports approval, budget, and prioritization.

---

## Hallucinated writing examples

**Scenario.** In November 2020, three months after the OCC Consent Order (August 6, 2020) **(time)**, the Chief Information Security Officer **(role)** must present a business case **(type)** to Executive Leadership and the Board Finance Committee **(audience)** for the Cloud Configuration Governance and Drift Detection initiative. The initiative is a direct response to the July 2019 incident root cause and the Consent Order’s required improvements. The CISO must justify scope, resources, and timeline and obtain approval to execute and report to the OCC.

<div class="writing-example-formal">

<p><strong>STRATEGIC SECURITY INITIATIVE JUSTIFICATION</strong></p>

<div class="doc-meta">
<p><strong>To:</strong> Executive Leadership, Board Finance Committee<br>
<strong>From:</strong> Chief Information Security Officer<br>
<strong>Date:</strong> November 15, 2020<br>
<strong>Subject:</strong> Business Case — Cloud Configuration Governance and Drift Detection Initiative (Post–July 2019 Incident; OCC Consent Order)</p>
</div>

<p><strong>Initiative summary.</strong> This document requests approval and budget for an enterprise-wide initiative to implement config-as-code and automated drift detection for cloud perimeter and critical infrastructure controls. The initiative is required under the Consent Order issued by the Office of the Comptroller of the Currency on August 6, 2020 (OCC NR 2020-98) and directly addresses the root cause of the July 2019 cybersecurity incident, in which an external actor exploited a misconfiguration in our AWS-hosted WAF to gain access to customer data. Scope: AWS WAF, routing, and boundary policies; phased rollout over 12 months with Phase 1 completion Q1 2021.</p>

<p><strong>Business and regulatory context.</strong> The 2019 incident resulted in unauthorized access to approximately 106 million individuals’ data, the arrest of the threat actor (<em>United States v. Paige A. Thompson</em>), an $80 million civil money penalty and Consent Order from the OCC, and consumer class-action litigation (later settled). The OCC found that our cloud security and risk management did not meet heightened standards and required the Bank to strengthen configuration governance and control effectiveness. This initiative implements that requirement and reduces the risk of repeat exposure from configuration drift or human error.</p>

<p><strong>Options considered.</strong> (1) Full config-as-code and drift detection (recommended): all designated perimeter changes via version control and peer review; automated drift detection with remediation or documented exception. (2) Manual baselines and periodic review only: rejected as insufficient to meet Consent Order expectations and residual risk. (3) Third-party managed service: evaluated; we recommend a hybrid approach with internal ownership to retain control and evidence for regulators and counsel.</p>

<p><strong>Benefits, resources, and risks of inaction.</strong> Benefits include reduced risk of boundary drift, demonstrable control operation for the OCC and auditors, and faster evidence production for exams and litigation. Estimated cost [X]; headcount [Y]; milestones tied to Consent Order reporting. Risks of inaction: Consent Order deadlines may be missed; likelihood of repeat configuration-related exposure remains elevated; additional regulatory or audit findings. We recommend approval of scope, budget, and timeline and authorize the CISO to execute and report progress quarterly to the Board and OCC.</p>

</div>

---

## Official document (post-incident initiative and consent order commitments)

After the 2019 breach, Capital One and the **OCC consent order** committed to specific program improvements. These function as publicly referenced “strategic initiatives” that had to be justified to the board and regulator.

- **OCC Consent Order (2020):** [OCC Consent Order and Civil Money Penalty against Capital One](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html) — required risk management, board reporting, cloud security, and third-party risk improvements; effectively a mandated initiative set.
- **Capital One 10-K:** [Capital One 10-K](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000927628&type=10-K&dateb=&owner=include&count=40) — describes investments and program changes in response to the incident and consent order.
- **SEC guidance:** Major initiatives that affect material risk or disclosure are reflected in 10-K and proxy; justification should align with that narrative.

*Consent orders turn “what we should do” into “what we must do”; the business case still needs to articulate why, options, and resources.*

---

## Writing analysis

**How initiative justifications are typically structured**

- **Initiative summary** — What, why, and high-level scope.
- **Business context** — Risk or compliance driver; strategic alignment.
- **Options considered** — Alternatives and why this path.
- **Benefits** — Risk reduction, compliance, efficiency, or other outcomes.
- **Resources and timeline** — Cost, headcount, and milestones.
- **Risks of inaction** — What happens if we do nothing.
- **Recommendation and ask** — Clear ask (approval, budget, authority).

**What to emulate**

- Reference risk assessments, regulatory expectations, or audit findings so the ask is evidence-based.
- One-page summary plus appendix; decision-makers need a clear “recommendation and ask.”
- Spell out risks of inaction so the cost of delay is explicit.

**What to improve**

- Avoid technical deep-dives in the main summary; keep benefits and trade-offs in business language.
- Tie approved initiatives to program status and risk register so execution is tracked.

