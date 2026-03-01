# OpenRouter Inventory Curation Plan

Schema: `eal.vendor.inventory.curation.plan.v1` (human-readable planning receipt)
Generated: 2026-03-01T00:21:00Z
Vendor/Surface: `openrouter/openrouter_api`

## Objective

Convert OpenRouter from surface-scanned state to curated feature inventory with reproducible evidence paths.

## Curation Steps

1. Enumerate capability dimensions to track:
  auth modes, routing knobs, model selection controls, safety/policy toggles, telemetry/usage controls.
2. For each discovered capability, map to normalized slug and source evidence.
3. Add curated entries to `feature_inventory` in `conformance/vendor_experimental_feature_gates.json`.
4. Emit inventory receipt JSON (`openrouter_openrouter_api_inventory_YYYY-MM-DD.json`) with normalized slugs.

## Required Artifacts

1. Curated inventory receipt JSON
2. Updated `vendor_experimental_feature_gates.json` OpenRouter block
3. Updated matrix row in `VENDOR_FEATURE_GAP_MATRIX.md` with evidence links

## Acceptance

1. OpenRouter inventory no longer empty unless explicitly justified by hard evidence
2. Every curated slug has a source pointer
3. Feature-gate verification remains PASS
