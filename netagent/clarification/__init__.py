"""Adaptive Clarification Policy — the novel research contribution of NetAgent.

Combines LLM uncertainty estimation with action-risk tiers to decide when the
agent should ask the human vs. act autonomously.

Phase-4 stub. Implement in Weeks 6-7.
"""

from netagent.clarification.policy import AdaptiveClarificationPolicy  # noqa: F401
from netagent.clarification.risk import ActionRiskTier  # noqa: F401
from netagent.clarification.uncertainty import UncertaintyEstimator  # noqa: F401
