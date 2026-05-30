"""Read-only show-command tool.

Phase-2 stub. The Week-3 implementation will wrap pyATS / Genie / Netmiko
to execute show commands against CML devices and return parsed JSON.
"""

from __future__ import annotations

from typing import Any


def run_show_command(device: str, command: str) -> dict[str, Any]:
    """Execute a show command on a network device and return structured output.

    Args:
        device: Hostname or alias of the target device (e.g., "R1", "SW2").
        command: The show command to run (e.g., "show ip bgp summary").

    Returns:
        A dict with keys: device, command, raw_output, parsed (optional), timestamp.
    """
    # TODO (Week 3): Implement via pyATS or Netmiko.
    # Pseudo-flow:
    #   1. Look up device connection from testbed.yaml
    #   2. Connect via SSH (Netmiko) or pyATS
    #   3. Run command, capture raw output
    #   4. Attempt Genie parsing -> structured dict
    #   5. Return {device, command, raw_output, parsed, timestamp}
    return {
        "device": device,
        "command": command,
        "raw_output": "<stub — implement in Week 3>",
        "parsed": None,
        "timestamp": None,
    }


# Tool schema for Anthropic / OpenAI function-calling
TOOL_SCHEMA = {
    "name": "run_show_command",
    "description": (
        "Execute a read-only show command on a Cisco network device. "
        "Returns structured (parsed via Genie when possible) or raw CLI output."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "device": {
                "type": "string",
                "description": "Hostname or alias of the target device (e.g. 'R1').",
            },
            "command": {
                "type": "string",
                "description": "Show command to execute (e.g. 'show ip bgp summary').",
            },
        },
        "required": ["device", "command"],
    },
}
