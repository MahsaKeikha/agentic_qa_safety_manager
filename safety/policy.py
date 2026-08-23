"""Fail-closed governance for F13 Agentic QA Safety Manager."""

PROTECTED_ACTIONS = {
    "approve_production_release",
    "deploy_or_modify_production",
    "disable_safety_security_or_quality_control",
    "alter_or_delete_audit_evidence",
    "accept_regulatory_or_legal_compliance",
    "conceal_known_defect_incident_or_safety_risk",
}

REQUIRED_REVIEWS = (
    "requirements_acceptance_reviewed",
    "test_evidence_reviewed",
    "safety_risk_reviewed",
    "security_privacy_reviewed",
    "reliability_resilience_reviewed",
    "compliance_traceability_reviewed",
    "release_rollback_reviewed",
    "human_approval_reviewed",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {
            "allowed": False,
            "reason": "production release, deployment, control bypass, evidence alteration, compliance acceptance, or risk concealment is outside autonomous QA authority",
        }
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required QA safety review", "missing": missing}

    checks = {
        "requirements_gap": "material requirement, acceptance criterion, intended-use, or testability gap remains unresolved",
        "test_evidence_gap": "material test coverage, reproducibility, oracle, regression, or evidence gap remains unresolved",
        "safety_risk_gap": "material hazard, misuse, unsafe failure, human-factors, or residual-risk issue remains unresolved",
        "security_privacy_gap": "material security, privacy, secrets, access-control, prompt-injection, data-leakage, or supply-chain issue remains unresolved",
        "reliability_resilience_gap": "material reliability, availability, recovery, timeout, retry, idempotency, cascade, or observability issue remains unresolved",
        "compliance_traceability_gap": "material provenance, auditability, requirement-to-test traceability, policy, regulatory, or evidence-retention issue remains unresolved",
        "release_rollback_gap": "material release criteria, rollback, kill-switch, monitoring, incident-response, or change-control issue remains unresolved",
        "approval_conflict_gap": "material reviewer independence, conflict-of-interest, segregation-of-duties, exception, waiver, or human-approval issue remains unresolved",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "QA safety governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "QA safety evidence package approved for authorized human release review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
