# F13 | Agentic QA Safety Manager | L3 Gold Standard | v1.0

A governed five-agent reference architecture for quality assurance, safety assurance, security and privacy review, evidence traceability, release readiness, and human-controlled production decisions.

F13 is an assurance and decision-support system. It is not an autonomous release authority, deployment system, regulator, legal authority, security officer, safety officer, or substitute for accountable human review.

## Assurance lifecycle

```text
Requirements and Intended Use
        -> Test Evidence
        -> Safety Risk Review
        -> Security and Privacy Review
        -> Reliability and Release Assurance
        -> Traceable Evidence Package
        -> Authorized Human Release Decision
```

The architecture follows a core principle: **capability is not authority**. The system can collect evidence, analyze gaps, run bounded checks, draft findings, and recommend escalation. It cannot approve production release, conceal known defects, bypass controls, or declare regulatory compliance.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Requirements Agent | Requirements, intended use, acceptance criteria, testability, traceability | What must the system do, and how will we know? |
| Test Agent | Test design, coverage, regression, reproducibility, evidence quality | What was tested, what passed, what failed, and what remains unknown? |
| Safety Agent | Hazards, misuse, unsafe failures, human factors, residual risk | How could the system cause harm or fail unsafely? |
| Security Agent | Security, privacy, access control, injection, secrets, supply chain | Can the system or its evidence be compromised, abused, or leaked? |
| Release Agent | Reliability, release criteria, rollback, monitoring, incident response, approvals | Is the evidence package complete enough for an authorized human release decision? |

## Required reviews

All eight executable reviews must pass:

```text
requirements_acceptance_reviewed
test_evidence_reviewed
safety_risk_reviewed
security_privacy_reviewed
reliability_resilience_reviewed
compliance_traceability_reviewed
release_rollback_reviewed
human_approval_reviewed
```

Missing any review fails closed.

## Requirements and acceptance assurance

Requirements should identify intended users, intended use, operating environment, functional expectations, quality attributes, constraints, assumptions, prohibited behavior, and measurable acceptance criteria.

Requirements should be testable where practical. Ambiguous terms such as fast, robust, safe, intelligent, accurate, intuitive, secure, or reliable should be translated into measurable or reviewable criteria before they become release claims.

Requirement changes should preserve version, source, rationale, owner, affected tests, affected hazards, and approval state.

`requirements_gap` blocks the evidence package when material requirements, acceptance criteria, intended-use boundaries, or testability remain unresolved.

## Test strategy

Testing can include unit, integration, system, end-to-end, regression, acceptance, exploratory, performance, load, stress, reliability, compatibility, accessibility, usability, security, privacy, recovery, and adversarial testing as appropriate to the system.

A passing test suite is evidence, not proof that no defects exist.

## Test evidence integrity

Test evidence should preserve environment, configuration, code or artifact version, input or fixture identity, expected result, actual result, timestamp where appropriate, and reproducibility information.

The system must not fabricate test execution, coverage, pass rates, defects, logs, screenshots, approvals, or evidence.

`test_evidence_gap` blocks release when material coverage, reproducibility, test oracle, regression, or evidence gaps remain unresolved.

## Coverage

Coverage metrics can reveal untested areas but should not be treated as equivalent to correctness. Code coverage, requirement coverage, risk coverage, state coverage, scenario coverage, and boundary coverage answer different questions.

High numeric coverage does not automatically mean strong tests.

## Regression

A defect fix should be accompanied by a regression test when practical so that the failure can be detected if it returns.

## Negative testing

QA should test invalid, malformed, missing, contradictory, oversized, stale, unauthorized, adversarial, and boundary inputs rather than only expected happy paths.

## Property and invariant testing

Where suitable, invariants can provide stronger assurance than isolated examples. Examples include authorization boundaries, monotonic counters, schema validity, conservation properties, data isolation, and fail-closed behavior.

## Reproducibility

A defect or safety finding should preserve enough context for another authorized reviewer to reproduce or meaningfully investigate it.

## Defect management

Defects should preserve severity, impact, affected versions, reproduction steps, evidence, owner, status, mitigation, fix reference, verification result, and residual risk where applicable.

Severity should not be silently lowered to satisfy a release target.

## Safety assurance

Safety analysis should be proportionate to consequence. Relevant techniques may include hazard analysis, misuse cases, abuse cases, failure-mode analysis, scenario analysis, human-factors review, safety constraints, and residual-risk documentation.

`safety_risk_gap` blocks release when material hazards, misuse, unsafe failures, human-factors issues, or residual risk remain unresolved.

## Hazard identification

Hazards should consider normal operation, foreseeable misuse, component failure, dependency failure, stale information, automation surprise, operator error, degraded modes, and recovery behavior.

## Safety constraints

A safety constraint should describe what must never occur or what condition must hold to prevent unacceptable harm.

## Fail-safe and fail-closed behavior

Where consequences justify it, uncertain or invalid states should move the system toward a bounded safe state rather than silently continuing with elevated authority.

## Human factors

Safety can depend on how people understand alerts, confidence, uncertainty, controls, overrides, handoffs, and system limitations. Human review should not be reduced to a meaningless click-through gate.

## Residual risk

Residual risk should be visible to the authorized decision maker. F13 cannot accept residual risk on behalf of the organization.

## AI and agentic system QA

For AI systems, quality assurance can include task success, hallucination behavior, calibration, robustness, data quality, bias and fairness, privacy, jailbreak resistance, prompt injection, tool-use boundaries, retrieval quality, grounding, refusal behavior, unsafe-completion behavior, latency, cost, and model or prompt regressions.

For agentic systems, additional assurance should cover delegated authority, agent identity, tool permissions, handoff contracts, shared state, approval gates, auditability, retry behavior, partial failures, context poisoning, memory poisoning, cascade failures, and external side effects.

## Prompt injection and untrusted context

Retrieved webpages, documents, emails, tickets, logs, tool descriptions, and agent messages should be treated as potentially untrusted inputs rather than automatically trusted instructions.

Security-sensitive controls must be enforced in code or infrastructure rather than relying only on prompt wording.

## Tool governance

Tools should use least privilege, explicit contracts, scoped credentials, validated inputs, bounded outputs, and approval gates for consequential side effects.

Broad unrestricted tools increase assurance burden.

## Agent identity and delegation

Each agent should have a traceable identity and bounded authority. Delegation should not silently expand permissions.

## Multi-agent failure modes

QA should consider spoofed agent identity, trust laundering, unsafe delegation, conflicting agents, collusion, poisoned shared state, cascading failures, stale context, lost approval state, and partial completion.

## Security assurance

`security_privacy_gap` blocks release when material security, privacy, secrets, access-control, prompt-injection, data-leakage, or supply-chain issues remain unresolved.

Security review can include authentication, authorization, secrets management, dependency risk, input validation, output encoding, isolation, sandboxing, network boundaries, logging, encryption, secure defaults, abuse prevention, and incident readiness.

## Least privilege

Users, services, agents, tools, workflows, and CI systems should receive only the access required for their role.

## Secrets

Credentials, tokens, private keys, passwords, API keys, signing material, and confidential configuration should not be committed to the repository or exposed in logs and test fixtures.

## Supply chain

Dependencies, build systems, packages, models, datasets, plugins, actions, containers, and deployment artifacts can introduce supply-chain risk. Provenance and version pinning should be preserved where appropriate.

## Privacy assurance

Privacy review should consider data minimization, purpose limitation, retention, access, disclosure, third-party data, deletion, sensitive attributes, logs, telemetry, and test data.

Production personal data should not be copied into QA environments without appropriate authorization and safeguards.

## Reliability and resilience

`reliability_resilience_gap` blocks release when material reliability, availability, recovery, timeout, retry, idempotency, cascade, or observability issues remain unresolved.

## Failure testing

Systems should be tested under dependency failures, timeouts, malformed responses, network interruption, rate limiting, partial writes, resource exhaustion, stale caches, unavailable services, and restart conditions where relevant.

## Retry safety

Retries can duplicate side effects. Consequential operations should use idempotency or equivalent controls where appropriate.

## Timeouts

External calls and long-running operations should have bounded timeout behavior rather than hanging indefinitely.

## Circuit breaking and containment

High-impact cascading failures may require circuit breakers, isolation, degraded modes, kill switches, or other containment mechanisms.

## Recovery

Recovery procedures should be tested rather than assumed.

## Observability

Logs, metrics, traces, alerts, audit events, and health signals should provide enough evidence to investigate failures without unnecessarily exposing sensitive data.

## Compliance and traceability

`compliance_traceability_gap` blocks release when material provenance, auditability, requirement-to-test traceability, policy, regulatory, or evidence-retention issues remain unresolved.

F13 can organize evidence and identify gaps. It does not independently certify legal or regulatory compliance.

## Traceability

Where consequence warrants it, traceability should connect:

```text
Requirement -> Risk or Hazard -> Control -> Test -> Evidence -> Finding -> Resolution -> Approval
```

## Provenance

Evidence should identify its source, version, author or generating process where relevant, collection method, and relationship to the system under review.

## Audit integrity

Audit records should not be silently altered or deleted. Corrections should preserve history where appropriate.

`alter_or_delete_audit_evidence` is a protected action.

## Reviewer independence

High-consequence release decisions may require separation between the person or system that created a change and the person authorized to approve it.

## Conflicts of interest

`approval_conflict_gap` blocks release when reviewer independence, segregation of duties, conflicts of interest, exceptions, waivers, or approval issues remain unresolved.

## Exceptions and waivers

An exception should identify the requirement being waived, rationale, owner, scope, duration, compensating controls, residual risk, and authorized approver.

F13 cannot grant its own waiver.

## Release assurance

`release_rollback_gap` blocks release when material release criteria, rollback, kill-switch, monitoring, incident-response, or change-control issues remain unresolved.

## Release criteria

Release criteria should be explicit before the final decision where practical. Criteria can include required tests, defect thresholds, unresolved-risk rules, performance targets, security findings, documentation, monitoring, rollback readiness, and approvals.

## Release decision boundary

`approve_production_release` is protected. F13 may recommend ready, not ready, conditionally ready, or insufficient evidence, but an authorized human or organizational process owns the production release decision.

## Deployment boundary

`deploy_or_modify_production` is protected. QA evidence does not authorize deployment.

## Safety-control boundary

`disable_safety_security_or_quality_control` is protected. The system cannot disable tests, monitoring, access controls, safety gates, security checks, or other assurance mechanisms merely to obtain a passing result.

## Compliance boundary

`accept_regulatory_or_legal_compliance` is protected. Compliance acceptance belongs to appropriately authorized legal, regulatory, quality, safety, or organizational authorities.

## Transparency boundary

`conceal_known_defect_incident_or_safety_risk` is protected. Known material defects, incidents, or safety risks must not be hidden to improve release metrics.

## Rollback

A release plan should identify rollback or forward-recovery strategy when practical, including conditions that trigger action and who has authority to execute it.

## Kill switch

Systems with consequential autonomous behavior may require a tested mechanism for rapidly stopping or constraining operation.

## Monitoring after release

Pre-release testing cannot cover every production condition. Post-release monitoring should detect escaped defects, safety events, security events, regressions, and unexpected behavior.

## Incident response

Incident readiness should identify detection, triage, containment, communication, evidence preservation, remediation, recovery, and post-incident review responsibilities.

## Escaped defects

Escaped defects should feed back into regression tests, risk models, requirements, monitoring, and process improvements.

## Quality metrics

Useful metrics can include defect escape rate, severity distribution, test stability, requirement coverage, risk coverage, regression recurrence, mean time to detection, mean time to recovery, flaky test rate, and unresolved high-risk findings.

Metrics should not become incentives to hide defects or manipulate severity.

## Evidence over assertion

A claim such as safe, secure, compliant, production-ready, fully tested, zero defects, or reliable should require defined evidence and scope.

Absence of observed failure is not equivalent to proof of safety.

## Uncertainty

Unknowns should remain visible. F13 should prefer `insufficient evidence` over invented confidence.

## Protected actions

The following actions remain outside autonomous authority even when every review passes:

```text
approve_production_release
deploy_or_modify_production
disable_safety_security_or_quality_control
alter_or_delete_audit_evidence
accept_regulatory_or_legal_compliance
conceal_known_defect_incident_or_safety_risk
```

## Explicit failure states

```text
REQUIREMENTS AND ACCEPTANCE REVIEW REQUIRED
TEST EVIDENCE REVIEW REQUIRED
SAFETY RISK REVIEW REQUIRED
SECURITY AND PRIVACY REVIEW REQUIRED
RELIABILITY AND RESILIENCE REVIEW REQUIRED
COMPLIANCE AND TRACEABILITY REVIEW REQUIRED
RELEASE AND ROLLBACK REVIEW REQUIRED
HUMAN APPROVAL REVIEW REQUIRED
REQUIREMENTS GAP
TEST EVIDENCE GAP
SAFETY RISK GAP
SECURITY OR PRIVACY GAP
RELIABILITY OR RESILIENCE GAP
COMPLIANCE OR TRACEABILITY GAP
RELEASE OR ROLLBACK GAP
APPROVAL OR CONFLICT GAP
AUTONOMOUS PRODUCTION RELEASE APPROVAL PROHIBITED
AUTONOMOUS PRODUCTION DEPLOYMENT PROHIBITED
SAFETY OR SECURITY CONTROL BYPASS PROHIBITED
AUDIT EVIDENCE ALTERATION PROHIBITED
AUTONOMOUS COMPLIANCE ACCEPTANCE PROHIBITED
KNOWN RISK CONCEALMENT PROHIBITED
```

## End-to-end reference workflow

1. Capture intended use, requirements, acceptance criteria, constraints, prohibited behavior, and quality attributes.
2. Map requirements to testable evidence and identify ambiguous or untestable claims.
3. Design risk-based tests across functional, integration, regression, boundary, negative, performance, reliability, accessibility, security, privacy, and adversarial dimensions as applicable.
4. Preserve reproducible evidence for execution environment, versions, fixtures, expected results, actual results, and failures.
5. Identify hazards, misuse, unsafe failure modes, human-factor risks, and residual risk.
6. Review security, privacy, access control, prompt injection, secrets, data leakage, isolation, and supply-chain concerns.
7. Review reliability, recovery, retries, timeouts, idempotency, observability, containment, and incident readiness.
8. Build traceability from requirements and risks through controls, tests, evidence, findings, resolutions, and approvals.
9. Review release criteria, unresolved defects, exceptions, waivers, rollback, kill switch, monitoring, and change control.
10. Check reviewer independence, conflicts of interest, segregation of duties, and human approval.
11. Apply fail-closed governance and produce a bounded evidence package.
12. Leave production release, deployment, compliance acceptance, and residual-risk acceptance to authorized humans and organizational processes.

## Evaluation and held-out governance suite

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out suite covering missing reviews, approved evidence-package release for human review, requirements gaps, test-evidence gaps, safety risks, security/privacy gaps, reliability/resilience gaps, compliance/traceability gaps, release/rollback gaps, and approval/conflict gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed governance, held-out scenarios, and execution of the governed five-agent QA safety workflow.

## Repository structure

```text
AGENTS/
├── requirements_agent.py
├── test_agent.py
├── safety_agent.py
├── security_agent.py
└── release_agent.py

orchestration/
├── orchestrator.py

safety/
├── policy.py

tests/
├── test_system.py

evals/
├── held_out.py

.github/workflows/
├── ci.yml

run.py
pyproject.toml
README.md
```

## Extension points

Production implementations can add governed integrations for issue trackers, requirements systems, test management, CI/CD, vulnerability scanners, SAST, DAST, SBOM systems, observability platforms, incident systems, model evaluations, red-team frameworks, safety cases, and evidence stores.

Any integration capable of modifying production, approving releases, deleting evidence, changing security controls, granting waivers, or making external compliance claims should remain behind explicit authorization, least privilege, separation of duties, and audit logging.

## Design principles

1. Quality and safety claims require evidence, not confidence language.
2. Requirements, risks, controls, tests, evidence, findings, and approvals should be traceable where consequence warrants it.
3. Unknowns and untested conditions remain visible.
4. Safety and security controls are enforced outside model persuasion.
5. Agent capability never implies release authority.
6. Test metrics must not create incentives to hide defects or weaken severity.
7. Consequential side effects require explicit human or organizational authority.
8. Audit evidence and provenance are first-class artifacts.
9. The system fails closed when material assurance evidence is incomplete.
10. Production release remains a human-accountable decision.

## Scope statement

F13 demonstrates a governed multi-agent architecture for QA and safety management. It combines specialized requirements, test, safety, security, and release agents with deterministic governance, traceable evidence expectations, held-out evaluation, and multi-version CI while preserving strict human authority over production release, deployment, compliance acceptance, audit evidence, safety controls, and residual-risk decisions.

Author: Mahsa Keikha
