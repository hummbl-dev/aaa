# Gemini Experimental ACP Pilot Plan

Schema: `eal.vendor.pilot.plan.v1` (human-readable planning receipt)
Generated: 2026-03-01T00:21:00Z
Vendor/Surface: `google/gemini_cli`
Feature: `experimental-acp`

## Objective

Produce first scorecard-quality evidence for `experimental-acp` under existing promotion policy (value/security/operability gates).

## Task Matrix

1. `acp_enabled_flow_smoke`
  Verify CLI startup and basic command flow with `experimental-acp` enabled.
2. `acp_disabled_flow_baseline`
  Run matching flow with feature disabled for baseline parity.
3. `acp_failure_path_observability`
  Trigger controlled error and confirm deterministic failure signal.
4. `acp_rollback_drill`
  Disable feature, rerun smoke, confirm baseline behavior restored.

## Required Artifacts

1. Baseline receipt JSON in `conformance/vendor_receipts/google_gemini_cli_experimental_acp_baseline_YYYY-MM-DD.json`
2. Scorecard receipt JSON in `conformance/vendor_receipts/google_gemini_cli_experimental_acp_scorecard_YYYY-MM-DD.json`
3. Decision row update in `VENDOR_FEATURE_GAP_MATRIX.md`
4. Gate artifact update in `conformance/vendor_experimental_feature_gates.json`

## Acceptance

1. Scorecard includes `task_count_scored >= 3`
2. Explicit confound accounting present
3. Decision resolved to `hold`, `no-go`, or `promote` with rationale
