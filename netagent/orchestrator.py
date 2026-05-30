"""LangGraph-based orchestrator implementing a ReAct-style reasoning loop.

This is a Phase-2 stub. Implement in Week 3.
"""

from __future__ import annotations

# TODO (Week 3): Build the LangGraph ReAct loop here.
# - State: messages, tool calls, observations, clarification triggers
# - Nodes: plan, tool-call, observe, clarify, summarize
# - Edges: conditional routing based on uncertainty + risk
#
# Sketch:
#   from langgraph.graph import StateGraph, END
#   from netagent.tools import all_read_only_tools
#   from netagent.llm.claude_client import ClaudeClient
#
#   def build_graph():
#       graph = StateGraph(AgentState)
#       graph.add_node("plan", plan_node)
#       graph.add_node("act", act_node)
#       graph.add_node("clarify", clarify_node)
#       graph.add_node("respond", respond_node)
#       graph.add_conditional_edges("plan", route_after_plan)
#       graph.set_entry_point("plan")
#       return graph.compile()
