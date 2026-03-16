import json
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1] / "docs"
CASES_DIR = DOCS / "cases"
OUT = CASES_DIR / "index.md"

def main():
    cases = []
    for p in CASES_DIR.glob("**/case.json"):
        if "_template" in p.parts:
            continue
        data = json.loads(p.read_text(encoding="utf-8"))
        rel_dir = p.parent.relative_to(CASES_DIR).as_posix()
        cases.append({
            "year": data.get("year", ""),
            "title": data.get("title", "Untitled"),
            "regime": ", ".join(data.get("regime", [])),
            "incident": ", ".join(data.get("incident_type", [])),
            "link": f"{rel_dir}/"
        })

    cases.sort(key=lambda x: (x["year"], x["title"]), reverse=True)

    lines = [
        "# All cases\n\n",
        "This page is generated from each case folder’s `case.json`.\n\n",
        "| Year | Case | Regime | Incident type |\n",
        "|---:|---|---|---|\n",
    ]
    for c in cases:
        lines.append(f"| {c['year']} | [{c['title']}]({c['link']}) | {c['regime']} | {c['incident']} |\n")

    OUT.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
