"""Smoke test — verifies the package imports correctly."""

import netagent


def test_version():
    assert netagent.__version__ == "0.1.0"


def test_imports():
    """All top-level modules should import without error."""
    from netagent import audit, clarification, config, llm, memory, safety, tools  # noqa: F401
