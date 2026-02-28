# Vendor Experimental Feature Gap Matrix

**Generated:** 2026-02-28
**Author:** claude-code (gap matrix handoff from codex REQUEST 22:03Z)
**Policy:** Value gate min speedup ratio = 0.20; manual security + operability gates required

## Anthropic Claude Code CLI (v2.1.63)

### Feature Inventory (16 total)

#### Currently Enabled (9) -- in production use

| Feature | Setting | Notes |
|---------|---------|-------|
| `experimental_agent_teams` | `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` | Multi-agent team orchestration |
| `auto_compact_pct_override` | `CLAUDE_CODE_AUTOCOMPACT_PCT_OVERRIDE=80` | Context compaction threshold |
| `max_output_tokens` | `CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000` | Extended output window |
| `bash_default_timeout` | `BASH_DEFAULT_TIMEOUT_MS=300000` | 5min bash timeout |
| `hooks` | SessionStart/PreToolUse/PostToolUse/Notification | 7 hook scripts active |
| `status_line` | Custom status line script | Branch, bus, disk, ports |
| `enable_tool_search` | `ENABLE_TOOL_SEARCH` | Deferred tool discovery |
| `enable_tasks` | `CLAUDE_CODE_ENABLE_TASKS` | Task list management |
| `auto_memory` | Session auto memory | Persistent memory across sessions |

#### Phase 1 Evaluated (4) -- not enabled

| Feature | Decision | Speedup | Reliability | Value | Signal | Security | Operability | Evidence |
|---------|----------|---------|-------------|-------|--------|----------|-------------|----------|
| `task_list_id` | **HOLD** | +15% | pass | fail (< 20%) | pass | manual pending | manual pending | [scorecard](conformance/vendor_receipts/anthropic_task_list_id_scorecard_2026-02-28.json) |
| `precompact_hooks` | **HOLD** | 0% | pass | fail | pass | manual pending | manual pending | [scorecard](conformance/vendor_receipts/anthropic_precompact_hooks_scorecard_2026-02-28.json) |
| `terminal_progress_bar` | **HOLD** | 0% | pass | fail | pass | **passed** | **passed** | [scorecard](conformance/vendor_receipts/anthropic_terminal_progress_bar_scorecard_2026-02-28.json) |
| `always_thinking` | **NO-GO** | -35% | inconclusive | inconclusive | inconclusive | manual pending | manual pending | [scorecard](conformance/vendor_receipts/anthropic_always_thinking_scorecard_2026-02-28.json) |

#### Phase 2 Queued (3) -- not yet evaluated

| Feature | Setting | Status | Priority | Blocker |
|---------|---------|--------|----------|---------|
| `fast_mode_per_session_opt_in` | `fastModePerSessionOptIn=true` | **TEST-NEEDED** | Medium | Phase 1 cleanup |
| `enable_telemetry` | `CLAUDE_CODE_ENABLE_TELEMETRY=1` | **TEST-NEEDED** | Low | Privacy review |
| `enable_prompt_suggestion` | `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` | **TEST-NEEDED** | Low | Phase 1 cleanup |

### Anthropic Summary

```
Implemented (enabled):       9 / 16  (56%)
Evaluated (not enabled):     4 / 16  (25%)  -- 3 hold, 1 no-go
Test-needed (not evaluated): 3 / 16  (19%)
Promoted to default-on:      0 / 16  ( 0%)
```

---

## OpenAI Codex CLI (v0.106.0)

### Feature Inventory (4 singles + 2 combos)

| Feature | Decision | Speedup | Reliability | Value | Signal | Security | Operability | Evidence |
|---------|----------|---------|-------------|-------|--------|----------|-------------|----------|
| `multi_agent` | **HOLD** | -1.29% | pass | fail | pass | manual pending | manual pending | [scorecard](conformance/vendor_receipts/openai_codex_multi_agent_scorecard_2026-02-28.json) |
| `apps` | **HOLD** | -0.83% | pass | fail | pass | manual pending | manual pending | [scorecard](conformance/vendor_receipts/openai_codex_apps_scorecard_2026-02-28.json) |
| `prevent_idle_sleep` | **NO-GO** | -19.83% | pass | fail | pass | manual pending | manual pending | [scorecard](conformance/vendor_receipts/openai_codex_prevent_idle_sleep_scorecard_2026-02-28.json) |
| `js_repl` | **NO-GO** | -16.34% | pass | fail | pass | manual pending | manual pending | [scorecard](conformance/vendor_receipts/openai_codex_js_repl_scorecard_2026-02-28.json) |
| `multi_agent + apps` | **NO-GO** | -10.41% | pass | fail | pass | manual pending | manual pending | [scorecard](conformance/vendor_receipts/openai_codex_multi_agent_apps_scorecard_2026-02-28.json) |
| `multi_agent + prevent_idle_sleep` | **NO-GO** | -28.51% | inconclusive | inconclusive | inconclusive | manual pending | manual pending | [scorecard](conformance/vendor_receipts/openai_codex_multi_agent_prevent_idle_sleep_scorecard_2026-02-28.json) |

### Codex Summary

```
Evaluated (singles):         4 / 4   (100%)  -- 2 hold, 2 no-go
Evaluated (combos):          2 / 6   ( 33%)  -- all no-go
Promoted to default-on:      0 / 4   (  0%)
```

---

## Google Gemini CLI (v0.29.7)

| Feature | Status | Notes |
|---------|--------|-------|
| `experimental-acp` | **PENDING** | In inventory, awaiting pilot runs |

Action: `make vendor-scan` to collect baseline.

---

## OpenRouter API

| Feature | Status | Notes |
|---------|--------|-------|
| _(none inventoried)_ | **PENDING** | Awaiting capability scan |

Action: `make vendor-scan` to enumerate features.

---

## Ollama Local (v0.15.4)

| Feature | Status | Notes |
|---------|--------|-------|
| _(none inventoried)_ | **BLOCKED** | Daemon unreachable on this machine (CPU constraint); blocked by HUM-9 (Mac Mini) |

---

## Cross-Vendor Summary

| Vendor | Surface | Features | Evaluated | Promoted | Status |
|--------|---------|----------|-----------|----------|--------|
| Anthropic | claude_code_cli | 16 | 4 / 7 candidates | 0 | Phase 1 complete, Phase 2 queued |
| OpenAI | codex_cli | 4 | 4 / 4 | 0 | Fully evaluated |
| Google | gemini_cli | 1 | 0 / 1 | 0 | Pending evidence |
| OpenRouter | openrouter_api | 0 | -- | -- | Pending scan |
| Ollama | ollama_local | 0 | -- | -- | Blocked (HUM-9) |

**Total features inventoried:** 21
**Total features evaluated:** 8
**Total features promoted:** 0

---

## Recommended Rollout Order

### Tier 1 -- Closest to Promotion (manual gates only)

1. **`terminal_progress_bar`** (Anthropic)
   - Security gate: **passed**; Operability gate: **passed**
   - Speedup: 0% (neutral) -- value gate blocks promotion (< 20%)
   - Recommendation: Promote if value gate threshold is relaxed for UI-only features with no performance regression. Lowest risk of all candidates.

2. **`task_list_id`** (Anthropic)
   - Speedup: +15% -- closest to the 20% value gate threshold
   - Needs: security review, operability drill
   - Recommendation: Re-pilot with expanded task matrix (current matrix may undercount task-list-heavy workflows). If speedup reaches 20%, promote after manual gates.

### Tier 2 -- Hold, Needs Re-evaluation

3. **`precompact_hooks`** (Anthropic)
   - Speedup: 0% (safety/infrastructure feature, not a performance feature)
   - Recommendation: Evaluate separately as a safety feature where value gate is waived. Focus on reliability and correctness.

4. **`multi_agent`** (Codex)
   - Speedup: -1.29% (marginal negative, within noise)
   - Recommendation: Re-pilot with explicitly parallelizable tasks. Current matrix is dominated by sequential analysis tasks.

5. **`apps`** (Codex)
   - Speedup: -0.83% (marginal negative, within noise)
   - Recommendation: Hold until explicit connector use-case arises.

### Tier 3 -- No-Go, Needs Clean Data or Isolation Fix

6. **`always_thinking`** (Anthropic)
   - Speedup: -35% (confounded with adaptive thinking)
   - Recommendation: Re-evaluate with cleaner isolation. Confound makes data unreliable. Do not promote.

7. **`prevent_idle_sleep`** (Codex)
   - Speedup: -19.83%
   - Recommendation: No-go for default-on. Only revisit if use-case requires long-running unattended sessions.

8. **`js_repl`** (Codex)
   - Speedup: -16.34%
   - Recommendation: No-go for default-on. Material slowdown with no observed benefit.

### Tier 4 -- Not Yet Tested

9. **`fast_mode_per_session_opt_in`** (Anthropic) -- Phase 2 priority
10. **`enable_prompt_suggestion`** (Anthropic) -- Phase 2
11. **`enable_telemetry`** (Anthropic) -- Phase 2 (low priority, privacy review needed)
12. **`experimental-acp`** (Gemini) -- Awaiting pilot infrastructure

---

## Open Actions

| # | Action | Owner | Blocker |
|---|--------|-------|---------|
| 1 | Relax value gate for UI-only features (terminal_progress_bar) | Owner decision | Policy change |
| 2 | Re-pilot task_list_id with task-list-heavy workflow matrix | codex | Phase 1 cleanup |
| 3 | Schedule manual security review for hold candidates | Reuben | Calendar |
| 4 | Run Phase 2 pilots (fast_mode, prompt_suggestion, telemetry) | claude-code / codex | Phase 1 closure |
| 5 | Run `make vendor-scan` for Gemini + OpenRouter | codex | None |
| 6 | Provision Mac Mini for Ollama evidence | Reuben | HUM-9 |

---

## Evidence Index

### Anthropic
- Inventory: [`conformance/vendor_receipts/anthropic_claude_code_inventory_2026-02-28.json`](conformance/vendor_receipts/anthropic_claude_code_inventory_2026-02-28.json)
- Gate config: [`conformance/vendor_experimental_feature_gates.json`](conformance/vendor_experimental_feature_gates.json)
- Baselines: `conformance/vendor_receipts/anthropic_*_baseline_2026-02-28.json` (4 files)
- Scorecards: `conformance/vendor_receipts/anthropic_*_scorecard_2026-02-28.json` (4 files)

### OpenAI Codex
- Gate config: [`conformance/experimental_feature_gate.json`](conformance/experimental_feature_gate.json)
- Baseline snapshot: [`conformance/vendor_receipts/openai_codex_baseline_2026-02-28.json`](conformance/vendor_receipts/openai_codex_baseline_2026-02-28.json)
- Scorecards: `conformance/vendor_receipts/openai_codex_*_scorecard_2026-02-28.json` (6 files)
- Decision docs: [`founder_mode/docs/testing/CODEX_FEATURE_PROMOTION_DECISION.md`](/Users/others/founder_mode/docs/testing/CODEX_FEATURE_PROMOTION_DECISION.md), [`CODEX_FEATURE_ROLLOUT_DECISION.md`](/Users/others/founder_mode/docs/testing/CODEX_FEATURE_ROLLOUT_DECISION.md)
