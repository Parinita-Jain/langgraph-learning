from langgraph.graph import StateGraph, START, END

from state import AgentState

from nodes import (
    agent_node,
    router_node,
    choose_route,
    retrieve_node,
    answer_node
)

workflow = StateGraph(AgentState)

workflow.add_node("agent", agent_node)
workflow.add_node("router", router_node)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("answer", answer_node)

workflow.add_edge(START, "agent")

workflow.add_edge("agent", "router")

workflow.add_conditional_edges(
    "router",
    choose_route,
    {
        "retrieve": "retrieve",
        "end": END
    }
)

workflow.add_edge("retrieve", "answer")

workflow.add_edge("answer", END)

app = workflow.compile()