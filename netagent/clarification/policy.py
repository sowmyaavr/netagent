"""Risk-Weighted Adaptive Clarification Policy — the novel contribution.

Implements four policy variants for ablation studies (Week 7):
  V1: Always-act (no clarification)
  V2: Always-ask (clarify before every action)
  V3: Fixed-threshold (clarify if uncertainty > 0.5)
  V4: Risk-weighted adaptive (OURS)

Phase-4 stub. Implement in Weeks 6-7.
"""

from __future__ import annotations

from enum import Enum

from netagent.clarification.risk import ActionRiskTier
from netagent.clarification.uncertainty import UncertaintyScore


class PolicyDecision(str, Enum):
    """What the policy tells the orchestrator to do next."""

    ACT = "act"
    ASK = "ask"


class PolicyVariant(str, Enum):
    """Ablation variants."""

    ALWAYS_ACT = "v1_always_act"
    ALWAYS_ASK = "v2_always_ask"
    FIXED_THRESHOLD = "v3_fixed_threshold"
    RISK_WEIGHTED = "v4_risk_weighted"  # OURS


class AdaptiveClarificationPolicy:
    """Decides whether to ASK or ACT given uncertainty + risk.

    Week-7 implementation will derive risk-weighted thresholds:
        threshold(risk) = base - alpha * risk_tier
    so that higher-risk actions require LOWER uncertainty before acting.

    Example default thresholds:
        READ_ONLY  : 0.95  (act aggressively)
        CONFIG     : 0.50  (act only when fairly certain)
        DISRUPTIVE : 0.20  (almost always ask)
    """

    DEFAULT_THRESHOLDS: dict[ActionRiskTier, float] = {
        ActionRiskTier.READ_ONLY: 0.95,
        ActionRiskTier.CONFIG: 0.50,
        ActionRiskTier.DISRUPTIVE: 0.20,
    }

    def __init__(
        self,
        variant: PolicyVariant = PolicyVariant.RISK_WEIGHTED,
        thresholds: dict[ActionRiskTier, float] | None = None,
    ) -> None:
        self.variant = variant
        self.thresholds = thresholds or self.DEFAULT_THRESHOLDS

    def decide(self, uncertainty: UncertaintyScore, risk: ActionRiskTier) -> PolicyDecision:
        """Return ACT or ASK based on the configured variant."""
        if self.variant == PolicyVariant.ALWAYS_ACT:
            return PolicyDecision.ACT
        if self.variant == PolicyVariant.ALWAYS_ASK:
            return PolicyDecision.ASK
        if self.variant == PolicyVariant.FIXED_THRESHOLD:
            return PolicyDecision.ASK if uncertainty.aggregate > 0.5 else PolicyDecision.ACT
        # V4 — risk-weighted (ours)
        threshold = self.thresholds[risk]
        # The lower the threshold, the more cautious we are at this risk tier.
        # Act if (1 - uncertainty) >= threshold, else ask.
        confidence = 1.0 - uncertainty.aggregate
        return PolicyDecision.ACT if confidence >= threshold else PolicyDecision.ASK
