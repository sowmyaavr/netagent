"""Uncertainty estimation for LLM agent decisions.

Phase-4 stub. Implement in Weeks 6-7.

Will combine:
  - Self-consistency sampling (Wang et al. 2022): generate N candidate plans,
    measure agreement via embedding distance.
  - Token-probability scoring (sum of logprobs of the chosen action).
  - Tool-output entropy (when parsed outputs are ambiguous).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class UncertaintyScore:
    """Composite uncertainty signal for one agent decision."""

    self_consistency: float  # 0.0 (full disagreement) .. 1.0 (full agreement) — inverted to uncertainty
    logprob_confidence: float  # 0.0 .. 1.0
    tool_entropy: float  # 0.0 .. 1.0
    aggregate: float  # 0.0 (certain) .. 1.0 (uncertain) — weighted combination

    def is_uncertain(self, threshold: float) -> bool:
        return self.aggregate >= threshold


class UncertaintyEstimator:
    """Estimates uncertainty for a proposed action.

    Week-6 implementation will:
      1. Sample N=5 plans from the LLM at temperature 0.7
      2. Embed each via Sentence-Transformers
      3. Compute pairwise cosine similarity -> self-consistency
      4. Extract logprobs for the chosen action's tokens
      5. Combine into an aggregate uncertainty score
    """

    def __init__(self, n_samples: int = 5, w_consistency: float = 0.6,
                 w_logprob: float = 0.3, w_entropy: float = 0.1) -> None:
        self.n_samples = n_samples
        self.weights = (w_consistency, w_logprob, w_entropy)

    def estimate(self, *args, **kwargs) -> UncertaintyScore:  # noqa: ANN002,ANN003
        """Placeholder — Week-6 implementation."""
        raise NotImplementedError("Implement in Week 6 — see clarification/policy.py")
