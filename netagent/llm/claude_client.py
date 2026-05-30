"""Thin Claude client — wraps the Anthropic SDK with the conventions NetAgent uses."""

from __future__ import annotations

from typing import Any

try:
    from anthropic import Anthropic
except ImportError:  # pragma: no cover
    Anthropic = None  # type: ignore[assignment, misc]

from netagent.config import get_settings

DEFAULT_MODEL = "claude-sonnet-4-7"  # update when newer model surfaces


class ClaudeClient:
    """Convenience wrapper around the Anthropic SDK.

    Centralizes:
      - API key + model selection
      - tool-use loop scaffolding
      - response normalization for the orchestrator
    """

    def __init__(self, model: str = DEFAULT_MODEL) -> None:
        if Anthropic is None:
            raise ImportError(
                "anthropic package not installed. Run: pip install anthropic"
            )
        settings = get_settings()
        if not settings.anthropic_api_key:
            raise ValueError("ANTHROPIC_API_KEY is not set. Copy .env.example -> .env and fill it.")
        self.client = Anthropic(api_key=settings.anthropic_api_key)
        self.model = model

    def chat(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        system: str | None = None,
        max_tokens: int = 1024,
    ) -> Any:
        """Single non-streaming call. Returns the raw Anthropic Message object."""
        kwargs: dict[str, Any] = {
            "model": self.model,
            "max_tokens": max_tokens,
            "messages": messages,
        }
        if tools:
            kwargs["tools"] = tools
        if system:
            kwargs["system"] = system
        return self.client.messages.create(**kwargs)
