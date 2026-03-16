# Incident types (What happened technically)

Cases are tagged by incident type to support engineer-first browsing. For each type below, a short explanation is followed by a representative **legal case** (court or agency proceeding) with a link to a publicly available court or agency paper (opinion, order, complaint, or settlement).

## Common incident types

- **Cloud misconfiguration / exposure**  
  **What it is:** Misconfigured cloud controls (e.g., permissions, network exposure, or storage settings) that allow unauthorized access or public exposure of data or systems.  
  **Case:** [*In re Capital One Consumer Data Security Breach Litigation*](https://www.capitalonesettlement.com/Content/Documents/Final%20Approval%20Order.pdf) — U.S. District Court, E.D. Va., Final Order and Judgment Approving Class Settlement (Feb. 2022). See also [OCC Cease and Desist Order](https://www.occ.gov/static/enforcement-actions/ea2020-037.pdf) (Capital One, N.A., Aug. 2020) for the regulator’s technology-risk and cloud-governance findings.

- **SSRF / metadata service abuse**  
  **What it is:** Server-Side Request Forgery (SSRF) or abuse of cloud metadata services (e.g., to obtain temporary credentials) that enables an attacker to reach internal resources or assume roles and access data.  
  **Case:** Same as cloud misconfiguration above: [*In re Capital One Consumer Data Security Breach Litigation*](https://www.capitalonesettlement.com/Content/Documents/Final%20Approval%20Order.pdf) (E.D. Va., Final Approval Order); [OCC Cease and Desist Order](https://www.occ.gov/static/enforcement-actions/ea2020-037.pdf) (Capital One).

- **Credential stuffing / account takeover**  
  **What it is:** Use of stolen or reused credentials (e.g., from other breaches) to log in to user accounts at scale, often combined with weak authentication and poor access controls.  
  **Case:** [*In the Matter of Drizly, LLC*](https://www.ftc.gov/system/files/ftc_gov/pdf/202-3185-Drizly-Complaint.pdf) — FTC Complaint (Oct. 2022); FTC alleged security failures that allowed access to consumer data; [Consent Order](https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf).

- **Third-party / vendor breach**  
  **What it is:** Compromise of a service provider, supplier, or acquired entity that holds or processes the organization’s data, leading to unauthorized access or exfiltration.  
  **Case:** [*In re Target Corporation Customer Data Security Breach Litigation*](https://www.mnd.uscourts.gov/sites/mnd/files/2014-1202-14MDL2522-Order.pdf) — U.S. District Court, D. Minn., Memorandum and Order on motion to dismiss (Dec. 2014). Third-party HVAC vendor access was part of the attack path. See also [*Firemen’s Retirement System of St. Louis v. Sorenson*](https://courts.delaware.gov/Opinions/Download.aspx?id=325170) (Marriott/Starwood), Del. Ch., board-oversight opinion (2021).

- **Ransomware**  
  **What it is:** Malware that encrypts or exfiltrates data and demands payment; often involves unauthorized access, lateral movement, and impact on availability and confidentiality.  
  **Case:** [*In re Blackbaud, Inc., Customer Data Breach Litigation*](https://law.justia.com/cases/federal/district-courts/south-carolina/scdce/3:2020cv02930/261818/89/) — U.S. District Court, D.S.C., Memorandum Opinion and Order on motion to dismiss (Oct. 2021), MDL No. 2972; ransomware attack and exfiltration of constituent data.

- **Business Email Compromise (BEC)**  
  **What it is:** Social engineering or account takeover aimed at tricking employees into wiring funds or disclosing sensitive information to fraudsters impersonating executives, vendors, or partners.  
  **Case:** [*SEC v. Onyeachonam et al.*](https://www.sec.gov/files/litigation/complaints/2024/comp-pr2024-194.pdf) — U.S. District Court, SEC Complaint (2024), alleging impersonation of securities professionals and fraud; BEC-style schemes are often prosecuted by DOJ/USSS with parallel or similar fact patterns.

- **Web application vulnerability exploitation**  
  **What it is:** Exploitation of flaws in web applications (e.g., injection, weak authentication, inadequate segmentation) that allow unauthorized access or data exposure.  
  **Case:** [*FTC v. Wyndham Worldwide Corp.*](https://www2.ca3.uscourts.gov/opinarch/143514p.pdf) — U.S. Court of Appeals, Third Circuit, Opinion (Aug. 2015); FTC alleged unreasonable security (weak passwords, poor segmentation, clear-text card data); court affirmed FTC’s Section 5 authority.

- **Insider threat**  
  **What it is:** Misuse of access by employees, contractors, or business partners to steal, expose, or misuse data, or to facilitate external attackers.  
  **Case:** [*FTC v. ChoicePoint, Inc.*](https://www.ftc.gov/legal-library/browse/cases-proceedings/052-3069-choicepoint-inc) — FTC complaint and stipulated final judgment (2006); data broker sold sensitive data to fraudsters posing as legitimate customers; inadequate vetting and access controls.

- **Payment card / skimming**  
  **What it is:** Theft of payment card data via point-of-sale (POS) intrusion, skimming devices, or compromise of card-processing systems, often affecting retailers or processors.  
  **Case:** [*In re Target Corporation Customer Data Security Breach Litigation*](https://www.mnd.uscourts.gov/sites/mnd/files/2014-1202-14MDL2522-Order.pdf) — U.S. District Court, D. Minn., Memorandum and Order on motion to dismiss (Dec. 2014); POS breach affecting approximately 110 million individuals.

- **Logging / monitoring failures (as a central theme)**  
  **What it is:** Inadequate logging, monitoring, or detection that delays discovery of intrusions or prevents effective response and accountability; often cited alongside other control failures in enforcement and litigation.  
  **Case:** [*In re Equifax Inc. Customer Data Security Breach Litigation*](https://www.equifaxbreachsettlement.com/admin/services/connectedapps.cms.extensions/1.0.0.0/2867ad20-e831-4527-bd5a-90d9a7f83f74_1033_EFX_Final_Order_and_Judgment_%281.13.2020%29.pdf) — U.S. District Court, N.D. Ga., Final Order and Judgment (Jan. 2020); unpatched vulnerability and inadequate detection/monitoring were central to regulatory and civil resolution. See also [*In the Matter of Altaba Inc., f/d/b/a Yahoo! Inc.*](https://www.sec.gov/files/litigation/admin/2018/33-10485.pdf) (SEC order, 2018) on disclosure controls and procedures.

---

> Incident tags are descriptive—not a claim of root cause beyond the record.
