from typing import TypedDict

class AgentState(TypedDict, total=False):
    question: str
    route: str
    documents: list[str]
    answer: str