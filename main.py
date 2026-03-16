from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List


def define_env(env):
    """
    Exposes `all_cases()` to Markdown/Jinja templates.
    Scans docs/cases/**/case.json and returns a sorted list of case metadata.
    """

    docs_dir = Path(__file__).parent / "docs"
    cases_dir = docs_dir / "cases"

    def _load_case_json(p: Path) -> Dict[str, Any]:
        data = json.loads(p.read_text(encoding="utf-8"))
        # Compute relative link from docs/cases/index.md to the case folder:
        # e.g. docs/cases/ftc-section-5/2022-drizly/case.json -> ftc-section-5/2022-drizly/
        rel_dir = p.parent.relative_to(cases_dir).as_posix()
        data["_rel_link"] = f"{rel_dir}/"
        data["_rel_dir"] = rel_dir
        return data

    @env.macro
    def all_cases() -> List[Dict[str, Any]]:
        items: List[Dict[str, Any]] = []
        for p in cases_dir.glob("**/case.json"):
            # Skip template case.json if you keep one under cases/_template
            if "_template" in p.parts:
                continue
            try:
                items.append(_load_case_json(p))
            except Exception:
                # If a case.json is malformed, skip it rather than breaking the whole site
                continue

        # Sort newest first, then title
        items.sort(key=lambda x: (x.get("year", 0), x.get("title", "")), reverse=True)
        return items
