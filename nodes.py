knowledge_base = {
    "langgraph":
        ["""LangGraph is a framework for building stateful AI workflows.""",
         """LangGraph is a specialized framework developed by LangChain """],

    "fastapi":
        ["""FastAPI is a modern Python framework for building APIs.""",
         """FastAPI is a modern, high-performance web framework """],

    "rag":
        ["""RAG stands for Retrieval Augmented Generation.""",
         """RAG (Retrieval-Augmented Generation) is an architectural pattern that optimizes the output"""]
}

def agent_node(state):

    print("Agent")
    return {
        "route": "test"
    }

def router_node(state):

    print("\n===== ROUTER NODE =====")

    question = state["question"].lower()

    retrieval_triggers = [
        "what",
        "explain",
        "describe",
        "tell me",
        "define"
    ]

    route = "end"

    if any(trigger in question for trigger in retrieval_triggers):
        route = "retrieve"

    result = {
        "route": route
    }
    return result

    

def retrieve_node(state):

    print("\n===== RETRIEVE NODE =====")
    print("Incoming State:")
    print(state)

    question = state["question"].lower()

    for keyword, doc in knowledge_base.items():

        if keyword in question:

            return {
                "documents": doc
            }

    return {
        "documents": ["No document found."]
    }



def choose_route(state):

    print("\n===== CHOOSE ROUTE =====")
    print("Route Selected:", state["route"])

    return state["route"]

def answer_node(state):

    print("\n===== ANSWER NODE =====")
    print("Incoming State:")
    print(state)

    result = {
        "answer": "\n".join(state["documents"])
    }

    

    return result
    

