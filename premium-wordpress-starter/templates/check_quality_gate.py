#!/usr/bin/env python3
"""Check future client-site evidence gates. Checks declarations, NOT visual truth.

Copy into a new client repository as scripts/check_quality_gate.py.
Use with templates/premium-quality-gate.yml and repository protection.
A direct WordPress/Orange MCP publication bypasses GitHub Actions.
"""
import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = {
    "gate_k1_source": (
        "project_decisions_reference",
        "brand_assets_reference",
        "reference_site_review_reference",
        "scope_and_services_reference",
    ),
    "gate_k2_pilot": (
        "desktop_visual_evidence",
        "mobile_visual_evidence",
        "reference_comparison_reference",
        "client_design_approval_reference",
    ),
    "gate_k3_quality": (
        "desktop_review_reference",
        "tablet_review_reference",
        "mobile_review_reference",
        "navigation_and_cta_reference",
        "content_and_media_reference",
    ),
    "gate_k4_release": (
        "production_url",
        "file_and_database_backup_reference",
        "rollback_plan_reference",
        "client_publish_approval_reference",
        "deployment_method",
    ),
}
NOT_EVIDENCE = {"", "todo", "tbd", "none", "null", "placeholder", "pending", "blocked", "n/a", "na", "-"}
METHODS = {"github_actions", "wordpress_direct", "other"}


def real_reference(value):
    return isinstance(value, str) and value.strip().lower() not in NOT_EVIDENCE and len(value.strip()) >= 8


def check_gate(name, info):
    errors = []
    if not isinstance(info, dict):
        return [f"{name}: missing gate object"]
    status = info.get("status")
    if status != "PASS":
        errors.append(f"{name}.status must be PASS, got {status!r}")
    for key in REQUIRED[name]:
        if not real_reference(info.get(key)):
            errors.append(f"{name}.{key} needs a concrete source, screenshot or approval reference")
    return errors


def validate(data, stage):
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return ["schema_version must be 1"]
    if not real_reference(data.get("project")) or data["project"] == "NEW_CUSTOMER_PROJECT":
        errors.append("project: set real customer project identifier")
    gates = list(REQUIRED)[:2] if stage == "pilot" else list(REQUIRED)
    for gate in gates:
        errors.extend(check_gate(gate, data.get(gate)))
    if stage == "release":
        k3 = data.get("gate_k3_quality") or {}
        critical = k3.get("critical_issues")
        if isinstance(critical, bool) or type(critical) is not int or critical != 0:
            errors.append("gate_k3_quality.critical_issues must be integer 0")
        k4 = data.get("gate_k4_release") or {}
        method = k4.get("deployment_method")
        if method not in METHODS:
            errors.append(f"gate_k4_release.deployment_method must be one of {sorted(METHODS)}")
        url = k4.get("production_url")
        if isinstance(url, str) and url.strip():
            parsed = urlparse(url.strip())
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append("gate_k4_release.production_url must be an HTTPS site URL")
        if method == "github_actions" and k4.get("github_production_environment_protected") is not True:
            errors.append("gate_k4_release.github_production_environment_protected must be true for GitHub Actions deployments")
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--manifest", default="PROJECT-QUALITY-GATE.json")
    ap.add_argument("--stage", choices=["pilot", "release"], default="release")
    args = ap.parse_args()
    try:
        data = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"BLOCKED: cannot read quality gate manifest: {exc}")
        return 2
    errors = validate(data, args.stage)
    if errors:
        print(f"BLOCKED: {args.stage} gate has {len(errors)} outstanding conditions:")
        for error in errors:
            print(f" - {error}")
        return 1
    print(f"PASS: {args.stage} manifest fields are complete.")
    print("Important: this check does not visually inspect the site or authenticate customer approval.")
    print("GitHub Actions cannot prevent a direct WordPress MCP/admin publication.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
