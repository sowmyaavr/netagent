# Benchmark Driver

`benchmark.py` runs the agent against all (or a subset of) fault scenarios and
emits structured results into `results/`.

## Phase 9 — implement in Week 9.

Sketch:
```bash
python eval/benchmark.py \
    --llm claude-sonnet \
    --scenarios all \
    --runs 5 \
    --output results/run_2026-08-01.json
```

## Metrics computed
- Diagnosis accuracy
- Top-K accuracy
- Remediation success rate
- Simulated MTTR
- Safety violation rate
- Clarification rate
- Wasted-clarification rate
- Cost per scenario (tokens / wallclock)
