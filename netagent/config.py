"""Configuration loader — reads environment variables via pydantic-settings."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:  # graceful fallback if pydantic-settings not installed yet
    BaseSettings = object  # type: ignore[assignment, misc]
    SettingsConfigDict = dict  # type: ignore[misc, assignment]


class Settings(BaseSettings):
    """Centralized configuration. Reads from .env or environment."""

    # LLM
    anthropic_api_key: str = ""
    ollama_host: str = "http://localhost:11434"
    ollama_model_llama: str = "llama3.1:8b-instruct-q5_K_M"
    ollama_model_qwen: str = "qwen2.5:7b-instruct-q5_K_M"

    # CML
    cml_host: str = ""
    cml_username: str = "admin"
    cml_password: str = ""

    # Device credentials
    device_username: str = "admin"
    device_password: str = "cisco"
    device_enable_password: str = "cisco"

    # Vector DB
    chroma_persist_dir: Path = Path("./chroma_db")

    # Safety
    approval_required_for_write: bool = True
    dry_run: bool = False

    # Logging
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
    audit_log_dir: Path = Path("./logs/audit")

    # Experiment tracking
    wandb_api_key: str = ""
    wandb_project: str = "netagent"
    wandb_entity: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


def get_settings() -> Settings:
    """Singleton accessor — use this everywhere instead of constructing directly."""
    return Settings()  # type: ignore[call-arg]
