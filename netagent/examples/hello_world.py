"""Hello-world agent — verifies Claude API + tool-use works end-to-end.

Run with:
    python -m netagent.examples.hello_world
"""

from __future__ import annotations

from netagent.llm.claude_client import ClaudeClient
from netagent.tools.show_commands import TOOL_SCHEMA, run_show_command


def main() -> None:
    """Tiny demo: ask Claude to diagnose a fake BGP issue using one tool."""
    client = ClaudeClient()

    messages: list[dict] = [
        {
            "role": "user",
            "content": (
                "R1 reports that its BGP session with R2 (10.0.0.2) is down. "
                "Investigate using available tools and report what you find."
            ),
        }
    ]
    response = client.chat(
        messages=messages,
        tools=[TOOL_SCHEMA],
        system="You are a Cisco network engineer. Use the available tools to diagnose issues.",
        max_tokens=512,
    )
    print("─── Claude response ───")
    for block in response.content:
        if block.type == "text":
            print(block.text)
        elif block.type == "tool_use":
            print(f"[tool_use] {block.name}({block.input})")
            # Execute the tool stub
            result = run_show_command(**block.input)
            print(f"[tool_result] {result}")


if __name__ == "__main__":
    main()
