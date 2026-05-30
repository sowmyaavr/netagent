"""Action-risk tiers — used by the clarification policy to weight uncertainty thresholds.

Phase-4 stub. Implement in Week 6.
"""

from __future__ import annotations

from enum import IntEnum


class ActionRiskTier(IntEnum):
    """Risk tiers for agent actions, ordered from least to most risky.

    READ_ONLY  — show commands, telemetry queries, KB lookups. Always safe.
    CONFIG     — non-disruptive config changes (e.g., route-map update, ACL add).
    DISRUPTIVE — actions that can disrupt traffic (interface shutdown, BGP clear).
    """

    READ_ONLY = 0
    CONFIG = 1
    DISRUPTIVE = 2


# Mapping from tool name -> risk tier. Extended in Week 8.
TOOL_RISK_MAP: dict[str, ActionRiskTier] = {
    "run_show_command": ActionRiskTier.READ_ONLY,
    "query_telemetry": ActionRiskTier.READ_ONLY,
    "lookup_kb": ActionRiskTier.READ_ONLY,
    "propose_config_change": ActionRiskTier.CONFIG,
    "apply_with_snapshot": ActionRiskTier.CONFIG,
    "rollback": ActionRiskTier.CONFIG,
    "shutdown_interface": ActionRiskTier.DISRUPTIVE,
    "clear_bgp_peer": ActionRiskTier.DISRUPTIVE,
}


def risk_of(tool_name: str) -> ActionRiskTier:
    """Lookup helper. Defaults to DISRUPTIVE if unknown (fail-safe)."""
    return TOOL_RISK_MAP.get(tool_name, ActionRiskTier.DISRUPTIVE)
