from langgraph.graph import StateGraph, START, MessagesState
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import AIMessage, HumanMessage
from .models import get_llm


def create_graph():
    llm = get_llm()

    def model_node(state):
        # Get current messages
        current_messages = state["messages"]
        # Generate response
        response = llm.invoke(current_messages)
        return {"messages": response}

    graph = StateGraph(MessagesState)
    graph.add_node("model", model_node)
    graph.add_edge(START, "model")
    graph.set_entry_point("model")

    memory = MemorySaver()
    return  graph.compile(checkpointer=memory)