from typing import Annotated, TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, MessageGraph
from langgraph.graph.state import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
from langchain_core.runnables import RunnableConfig
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API keys from environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Define state structure for the graph
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# Initialize the LLM model
llm_model = ChatOpenAI(temperature=0)

def create_basic_agent():
    """
    Creates a simple LLM-based agent without tool use.
    """
    def process_messages(state: AgentState):
        return {"messages": [llm_model.invoke(state["messages"])]}
    
    agent_graph = StateGraph(AgentState)
    agent_graph.add_node("llm_response", process_messages)
    agent_graph.add_edge("llm_response", END)
    agent_graph.add_edge(START, "llm_response")
    
    return agent_graph.compile()

def create_tool_using_agent():
    """
    Creates an LLM-based agent that can call mathematical tools.
    """
    
    # Define tool functions
    @tool
    def add(a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        return a + b
    
    @tool
    def multiply(a: int, b: int) -> int:
        """Returns the product of two numbers."""
        return a * b
    
    @tool
    def divide(a: int, b: int) -> float:
        """Returns the result of dividing `a` by `b`."""
        return a / b
    
    # Create tool node and bind tools to the LLM model
    tool_node = ToolNode([add, multiply, divide])
    llm_with_tools = llm_model.bind_tools([add, multiply, divide])
    
    def process_messages(state: AgentState):
        """Processes the state using the LLM with tool capabilities."""
        return {"messages": [llm_with_tools.invoke(state["messages"])]}
    
    def determine_next_step(state: AgentState):
        """Determines whether to continue tool execution or finish."""
        return "tools" if state["messages"][-1].tool_calls else END
    
    # Define the graph workflow
    agent_graph = StateGraph(AgentState)
    agent_graph.add_node("llm_response", process_messages)
    agent_graph.add_node("tools", tool_node)
    agent_graph.add_edge("tools", "llm_response")
    agent_graph.add_edge(START, "llm_response")
    agent_graph.add_conditional_edges("llm_response", determine_next_step)
    
    return agent_graph.compile()

# Create an agent with tool support
intelligent_agent = create_tool_using_agent()
