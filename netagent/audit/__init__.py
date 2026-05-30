"""Structured audit logging — every agent action timestamped + replayable.

Phase-2 stub. Implement progressively from Week 3 onward.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class AuditLogger:
    """Append-only JSONL audit logger for agent runs."""

    def __init__(self, log_dir: Path | str = "./logs/audit") -> None:
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.current_run_id: str | None = None
        self._fp = None

    def start_run(self, run_id: str) -> None:
        """Start a new run — opens a fresh JSONL file."""
        self.current_run_id = run_id
        log_path = self.log_dir / f"{run_id}.jsonl"
        self._fp = log_path.open("a", encoding="utf-8")

    def log(self, event_type: str, **payload: Any) -> None:
        """Log a structured event."""
        if self._fp is None:
            raise RuntimeError("AuditLogger.start_run() must be called first.")
        event = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "run_id": self.current_run_id,
            "event": event_type,
            **payload,
        }
        self._fp.write(json.dumps(event, default=str) + "\n")
        self._fp.flush()

    def close(self) -> None:
        if self._fp is not None:
            self._fp.close()
            self._fp = None
