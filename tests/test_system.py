from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({})
    for key in ("requirements", "test", "safety", "security", "release"):
        assert key in result
    assert result["released_for_human_review"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_qa_evidence_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_evidence_package_can_release_for_human_review():
    assert authorize("release_qa_evidence_package", approved_context())["allowed"] is True


def test_test_evidence_gap_blocks():
    assert authorize("release_qa_evidence_package", approved_context() | {"test_evidence_gap": True})["allowed"] is False


def test_safety_risk_blocks():
    assert authorize("release_qa_evidence_package", approved_context() | {"safety_risk_gap": True})["allowed"] is False


def test_security_privacy_gap_blocks():
    assert authorize("release_qa_evidence_package", approved_context() | {"security_privacy_gap": True})["allowed"] is False


def test_release_rollback_gap_blocks():
    assert authorize("release_qa_evidence_package", approved_context() | {"release_rollback_gap": True})["allowed"] is False


def test_protected_actions_never_autonomously_release():
    for action in PROTECTED_ACTIONS:
        assert authorize(action, approved_context())["allowed"] is False
