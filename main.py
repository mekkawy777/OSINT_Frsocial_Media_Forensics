from __future__ import annotations

# Stability guard for macOS/Apple Silicon: keep BLAS thread stacks small and
# force headless Matplotlib rendering before importing analysis modules.
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
os.environ.setdefault("MPLBACKEND", "Agg")

import argparse
import json
from pathlib import Path

from osint_forensics.analysis.network_graph import NetworkGraphBuilder
from osint_forensics.collectors.archive_collector import SocialMediaArchiver
from osint_forensics.collectors.deleted_recovery import DeletedContentRecovery
from osint_forensics.collectors.profile_extractor import ProfileExtractor
from osint_forensics.collectors.username_search import UsernameSearcher
from osint_forensics.reporting.report_generator import ReportGenerator
from osint_forensics.storage.case_store import CaseStore
from osint_forensics.utils.logging_config import setup_logging
from osint_forensics.workflow import InvestigationWorkflow
from osint_forensics.utils.system_check import run_system_check


def print_json(obj):
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=str))


def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Social Media Forensics & OSINT Investigation Framework")
    parser.add_argument("--base-dir", default="data", help="Evidence storage directory")
    parser.add_argument("--browser", action="store_true", help="Enable optional browser/Selenium snapshots when ChromeDriver is available")
    parser.add_argument("--no-selenium", action="store_true", help="Compatibility flag: keep browser collection disabled")
    parser.add_argument("--gui", action="store_true", help="Launch the PySide6 GUI")
    parser.add_argument("--demo", action="store_true", help="Run a complete safe demo workflow")
    parser.add_argument("--case", default="demo_case", help="Case ID for --demo")
    sub = parser.add_subparsers(dest="cmd")

    p_arch = sub.add_parser("archive", help="Archive a public URL and extract profile/page signals")
    p_arch.add_argument("url"); p_arch.add_argument("--case-id", default="demo_case")

    p_user = sub.add_parser("username", help="Search a username across public platform URL patterns")
    p_user.add_argument("username"); p_user.add_argument("--case-id", default="demo_case")

    p_rec = sub.add_parser("recover", help="Query public historical archive/cache records for a URL")
    p_rec.add_argument("url"); p_rec.add_argument("--case-id", default="demo_case")
    p_rec.add_argument("--fetch-snapshots", action="store_true", help="Download oldest/latest public archived bodies for diff analysis")
    p_rec.add_argument("--limit", type=int, default=25, help="Maximum archive records to keep")

    p_graph = sub.add_parser("graph", help="Generate network graph from a case")
    p_graph.add_argument("--case-id", default="demo_case")

    p_report = sub.add_parser("report", help="Generate HTML/Markdown report from a case")
    p_report.add_argument("--case-id", default="demo_case")

    p_verify = sub.add_parser("verify", help="Verify evidence hashes for a case")
    p_verify.add_argument("--case-id", default="demo_case")

    p_export = sub.add_parser("export", help="Export CSV, manifest, and evidence bundle ZIP")
    p_export.add_argument("--case-id", default="demo_case")

    p_note = sub.add_parser("note", help="Add an analyst note to a case")
    p_note.add_argument("note")
    p_note.add_argument("--case-id", default="demo_case")
    p_note.add_argument("--evidence-id", type=int, default=None)
    p_note.add_argument("--status", default="Reviewed")

    p_cases = sub.add_parser("cases", help="List known cases")

    p_target = sub.add_parser("add-target", help="Add a case-scoped target with duplicate prevention")
    p_target.add_argument("value")
    p_target.add_argument("--case-id", default="demo_case")
    p_target.add_argument("--type", default="URL", choices=["URL", "Username", "Domain", "Profile"])
    p_target.add_argument("--priority", default="Medium", choices=["High", "Medium", "Low"])
    p_target.add_argument("--tags", default="")
    p_target.add_argument("--notes", default="")

    p_targets = sub.add_parser("targets", help="List targets for a case")
    p_targets.add_argument("--case-id", default="demo_case")

    p_collect_targets = sub.add_parser("collect-targets", help="Collect all pending targets, then build graph/report/export")
    p_collect_targets.add_argument("--case-id", default="demo_case")

    p_final = sub.add_parser("final", help="Generate final graph, report, verification and export bundle")
    p_final.add_argument("--case-id", default="demo_case")

    p_status = sub.add_parser("status", help="Show guided workflow status for a case")
    p_status.add_argument("--case-id", default="demo_case")

    p_health = sub.add_parser("health", help="Show final readiness, warnings, and next best actions for a case")
    p_health.add_argument("--case-id", default="demo_case")

    p_audit = sub.add_parser("audit", help="Show immutable-style audit trail for a case")
    p_audit.add_argument("--case-id", default="demo_case")


    p_match = sub.add_parser("account-match", help="Run public account matching for username vs known reference account URL")
    p_match.add_argument("username")
    p_match.add_argument("reference_url")
    p_match.add_argument("--case-id", default="demo_case")

    p_start = sub.add_parser("start", help="Run one unified investigation from targets and optional reference URL")
    p_start.add_argument("targets", nargs="+", help="URLs, domains, usernames, or public profiles")
    p_start.add_argument("--reference-url", default="", help="Optional known public reference account URL for account matching")
    p_start.add_argument("--case-id", default="demo_case")

    p_doctor = sub.add_parser("doctor", help="Run dependency and environment readiness checks")
    p_smoke = sub.add_parser("smoke-test", help="Run offline demo, report, export, and hash verification test")
    p_smoke.add_argument("--case-id", default="smoke_test")

    p_verify_all = sub.add_parser("verify-all", help="Run full deterministic QA suite for university/demo submission")
    p_verify_all.add_argument("--keep-artifacts", action="store_true", help="Save QA artifacts under base-dir/qa_results")

    args = parser.parse_args()
    if getattr(args, "cmd", None) == "doctor":
        print_json(run_system_check(args.base_dir)); return

    if args.gui:
        from osint_forensics.gui.app import run_gui
        run_gui()
        return

    workflow = InvestigationWorkflow(base_dir=args.base_dir, use_selenium=bool(args.browser and not args.no_selenium))
    if args.demo:
        print_json(workflow.run_demo(args.case)); return
    if args.cmd == "verify-all":
        from osint_forensics.utils.qa import run_full_self_test
        print_json(run_full_self_test(args.base_dir, keep_artifacts=args.keep_artifacts)); return
    if args.cmd == "smoke-test":
        demo = workflow.run_demo(args.case_id)
        final = workflow.final_package(args.case_id)
        verification = workflow.verify_evidence(args.case_id)
        print_json({"demo": demo, "final": final, "verification": verification, "passed": verification.get("issues", 0) == 0})
        return
    if args.cmd == "archive":
        print_json(workflow.archive_and_extract(args.url, args.case_id)); return
    if args.cmd == "username":
        print_json(workflow.username_searcher.search(args.username, args.case_id)); return
    if args.cmd == "recover":
        print_json(workflow.recovery.query_archives(args.url, args.case_id, limit=args.limit, fetch_snapshots=args.fetch_snapshots)); return
    if args.cmd == "account-match":
        print_json(workflow.account_match_investigation(args.case_id, args.username, args.reference_url)); return
    if args.cmd == "start":
        print_json(workflow.unified_investigation(args.case_id, args.targets, reference_url=args.reference_url or None)); return
    if args.cmd == "graph":
        print_json(workflow.graph_builder.build_from_case(args.case_id)); return
    if args.cmd == "report":
        print_json(workflow.reporter.generate(args.case_id)); return
    if args.cmd == "verify":
        print_json(workflow.verify_evidence(args.case_id)); return
    if args.cmd == "export":
        print_json(workflow.export_bundle(args.case_id)); return
    if args.cmd == "note":
        print_json(workflow.add_note(args.case_id, args.note, evidence_id=args.evidence_id, status=args.status)); return
    if args.cmd == "cases":
        print_json(workflow.list_cases()); return
    if args.cmd == "add-target":
        print_json(workflow.add_target(args.case_id, args.value, args.type, args.priority, args.tags, args.notes)); return
    if args.cmd == "targets":
        print_json(workflow.list_targets(args.case_id)); return
    if args.cmd == "collect-targets":
        print_json(workflow.collect_all_targets(args.case_id)); return
    if args.cmd == "final":
        print_json(workflow.final_package(args.case_id)); return
    if args.cmd == "status":
        print_json(workflow.workflow_status(args.case_id)); return
    if args.cmd == "health":
        print_json(workflow.case_health(args.case_id)); return
    if args.cmd == "audit":
        print_json(workflow.audit_trail(args.case_id)); return

    parser.print_help()

if __name__ == "__main__":
    main()
