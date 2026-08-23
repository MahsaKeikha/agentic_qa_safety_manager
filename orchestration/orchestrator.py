from AGENTS import release_agent, requirements_agent, safety_agent, security_agent, test_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "requirements": requirements_agent.run(case),
        "test": test_agent.run(case),
        "safety": safety_agent.run(case),
        "security": security_agent.run(case),
        "release": release_agent.run(case),
    }
    governance = authorize("release_qa_evidence_package", case.get("governance", {}))
    result["governance"] = governance
    result["released_for_human_review"] = governance["allowed"]
    return result
