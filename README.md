# NetAgent

**Adaptive Clarification for LLM Agents: A Risk-Weighted Approach to Network Fault Remediation**

> An LLM-based autonomous agent for diagnosing and remediating network faults (BGP, OSPF, VLAN, STP) on Cisco IOS-XE / IOS-XR / NX-OS devices, with a novel risk-weighted adaptive clarification policy and formal safety guardrails.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Active Development](https://img.shields.io/badge/status-active%20development-orange.svg)]()

---

## 🎯 Motivation

Network operations are still reactive. When a fault occurs (BGP peer drop, OSPF adjacency failure, VLAN misconfiguration), engineers manually run dozens of `show` commands across multiple devices, correlate output, and apply config changes one by one. This is slow, error-prone, and doesn't scale.

Recent LLM agents (ReAct, Toolformer) hint at autonomous network operations, but two gaps remain:
1. **No adaptive clarification policy** — agents either over-clarify or under-clarify
2. **No formal safety framework** — engineers can't trust agents with write operations

**NetAgent** addresses both gaps for high-stakes infrastructure.

---

## ✨ Key Features

- 🤖 **Autonomous fault diagnosis** on Cisco IOS-XE/XR/NX-OS via LLM tool-calling
- 🧠 **Adaptive clarification policy** — combines uncertainty estimation + action-risk tiers
- 🛡️ **Formal safety taxonomy** with snapshot-rollback and human approval gates
- 📚 **RAG-backed memory** of Cisco docs and past incidents
- 🔬 **Reproducible benchmark** — 50 BGP / OSPF / VLAN / STP fault scenarios
- 📊 **Multi-LLM evaluation** — Claude (proprietary) vs LLaMA 3.1 / Qwen 2.5 (open-source)

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    NetAgent Core                         │
│                                                          │
│  ┌────────────┐   ┌──────────────────┐  ┌────────────┐   │
│  │Orchestrator│◄─►│   Adaptive       │  │  Memory    │   │
│  │ (LangGraph)│   │   Clarification  │  │  (RAG +    │   │
│  │            │   │   Policy         │  │  Vector DB)│   │
│  └─────┬──────┘   └──────────────────┘  └────────────┘   │
│        ▼                                                 │
│  ┌─────────────────────────────────────────────────────┐ │
│  │                 Tool Layer                          │ │
│  │ • run_show_command   • query_telemetry              │ │
│  │ • lookup_kb (RAG)    • propose_config_change        │ │
│  │ • rollback           • request_human_approval       │ │
│  └────────────────────┬────────────────────────────────┘ │
│                       ▼                                  │
│  ┌─────────────┐  ┌────────┐  ┌──────────────────┐       │
│  │  Safety     │  │ Audit  │  │  Approval Gate   │       │
│  │  Guardrail  │  │ Logger │  │  (human-in-loop) │       │
│  └─────────────┘  └────────┘  └──────────────────┘       │
└──────────────────────┬───────────────────────────────────┘
                       ▼
          ┌──────────────────────────┐
          │  Cisco Modeling Labs     │
          │  (pyATS / Genie / Netmiko)│
          │  R1–R4 + SW1–SW2         │
          └──────────────────────────┘
```

---

## 🚀 Quickstart

### Prerequisites
- Python 3.11+
- macOS or Linux (Apple Silicon recommended)
- Anthropic API key
- Access to Cisco Modeling Labs (or Containerlab fallback)
- [Ollama](https://ollama.com) (for open-source LLM evaluation)

### Installation

```bash
# Clone
git clone https://github.com/sowmyaavr/netagent.git
cd netagent

# Create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Set environment variables
cp .env.example .env
# Edit .env with your Anthropic API key and CML credentials
```

### Run the Hello-World Agent

```bash
python -m netagent.examples.hello_world
```

### Run a Single Scenario

```bash
python -m netagent.run \
    --llm claude-sonnet \
    --topology T1 \
    --scenario bgp_md5_mismatch_r1_r2
```

### Run the Full Benchmark

```bash
python eval/benchmark.py --llm claude-sonnet --scenarios all --runs 5
```

### Launch the Demo UI

```bash
streamlit run ui/streamlit_app.py
```

---

## 📂 Project Structure

```
netagent/
├── netagent/              # Core package
│   ├── orchestrator.py    # LangGraph ReAct loop
│   ├── tools/             # Network tools (show commands, config, RAG)
│   ├── clarification/     # Adaptive clarification policy (NOVEL)
│   ├── memory/            # Vector store + case memory
│   ├── safety/            # Safety taxonomy, guardrails, approval gate
│   ├── audit/             # Structured audit logging
│   └── llm/               # LLM client wrappers (Claude, Ollama)
├── testbed/               # CML topologies + fault scenarios
│   ├── topologies/        # 4 reference topologies
│   ├── fault_scenarios/   # 50 fault YAML definitions
│   ├── fault_injector/    # Robot Framework injection harness
│   └── ground_truth/      # Labels for each scenario
├── eval/                  # Benchmark driver + metrics
├── ui/                    # Streamlit demo UI
├── tests/                 # Unit / integration tests
└── docs/                  # MkDocs site
```

---

## 📊 Benchmark

**50 fault scenarios across 4 topologies:**

| Protocol | Count | Examples |
|----------|-------|----------|
| BGP | 15 | peer down, prefix limit, AS-path loop, MD5 mismatch, route-map misconfig |
| OSPF | 15 | neighbor stuck, MTU mismatch, area mismatch, auth mismatch |
| VLAN | 10 | trunking mismatch, VTP issue, allowed-VLAN, native VLAN mismatch |
| STP | 10 | root bridge change, BPDU guard trip, loop, port blocking |

Each scenario includes: trigger script, ground-truth root cause, ground-truth remediation, severity tag.

---

## 🔬 Evaluation

| Metric | Description |
|--------|-------------|
| Diagnosis Accuracy | % scenarios with correct root cause |
| Remediation Success Rate | % scenarios fully resolved |
| Simulated MTTR | Mean time from fault to resolution |
| Safety Violation Rate | % runs with disallowed actions |
| Clarification Rate | % decisions where agent asked |
| Cost per Scenario | Token cost (API) / compute (local) |

Compared against baselines: random, rule-based, zero-shot LLM, always-ask, always-act.

---

## 📚 Research Context

This work was conducted as part of an M.Tech (AI/ML) dissertation at BITS Pilani.

**Novel contributions:**
- **C1** — Risk-weighted adaptive clarification policy for LLM agents in high-stakes domains
- **C2** — Formal safety taxonomy for autonomous network configuration
- **C3** — Open, reproducible benchmark of 50 Cisco fault scenarios
- **C4** — Comparative study: proprietary vs open-source LLMs along cost-accuracy-safety axes

---

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Agent framework:** LangGraph
- **LLMs:** Claude Sonnet/Opus (Anthropic), LLaMA 3.1 8B, Qwen 2.5 7B (via Ollama)
- **RAG:** ChromaDB + Sentence-Transformers
- **Network:** pyATS, Genie, Netmiko, NAPALM
- **Testbed:** Cisco Modeling Labs (CML)
- **Fault injection:** Robot Framework
- **Demo:** Streamlit + FastAPI

---

## 📜 License

MIT — see [LICENSE](LICENSE).

---

## 🙏 Acknowledgements

- BITS Pilani WILP M.Tech (AI/ML) Programme
- Cisco Systems (employer, providing CML access)
- Anthropic (Claude API)
- Open-source maintainers of LangGraph, pyATS, ChromaDB, Ollama

---

## 📬 Contact

**Sowmyaa VR** — [GitHub](https://github.com/sowmyaavr)

---

> ⚠️ **Status:** Active development. This is a research project, not a production-ready tool. Do not run write operations against production networks without thorough testing in your own lab.
