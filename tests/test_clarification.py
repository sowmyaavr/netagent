"""Unit tests for the Adaptive Clarification Policy.

Phase-4 — extended in Week 7.
"""

from netagent.clarification.policy import (
    AdaptiveClarificationPolicy,
    PolicyDecision,
    PolicyVariant,
)
from netagent.clarification.risk import ActionRiskTier
from netagent.clarification.uncertainty import UncertaintyScore


def _score(aggregate: float) -> UncertaintyScore:
    return UncertaintyScore(
        self_consistency=aggregate,
        logprob_confidence=aggregate,
        tool_entropy=aggregate,
        aggregate=aggregate,
    )


def test_always_act():
    p = AdaptiveClarificationPolicy(variant=PolicyVariant.ALWAYS_ACT)
    assert p.decide(_score(0.99), ActionRiskTier.DISRUPTIVE) == PolicyDecision.ACT


def test_always_ask():
    p = AdaptiveClarificationPolicy(variant=PolicyVariant.ALWAYS_ASK)
    assert p.decide(_score(0.01), ActionRiskTier.READ_ONLY) == PolicyDecision.ASK


def test_risk_weighted_low_risk_certain():
    p = AdaptiveClarificationPolicy(variant=PolicyVariant.RISK_WEIGHTED)
    # high confidence, read-only -> act
    assert p.decide(_score(0.01), ActionRiskTier.READ_ONLY) == PolicyDecision.ACT


def test_risk_weighted_high_risk_uncertain():
    p = AdaptiveClarificationPolicy(variant=PolicyVariant.RISK_WEIGHTED)
    # moderate uncertainty, disruptive -> ask (defensive)
    assert p.decide(_score(0.5), ActionRiskTier.DISRUPTIVE) == PolicyDecision.ASK
