"""Held-out governance scenarios for F13."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"requirements_gap": True}, False),
    (base() | {"test_evidence_gap": True}, False),
    (base() | {"safety_risk_gap": True}, False),
    (base() | {"security_privacy_gap": True}, False),
    (base() | {"reliability_resilience_gap": True}, False),
    (base() | {"compliance_traceability_gap": True}, False),
    (base() | {"release_rollback_gap": True}, False),
    (base() | {"approval_conflict_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_qa_evidence_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F13 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
