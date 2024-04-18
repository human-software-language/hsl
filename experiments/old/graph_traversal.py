import dspy
from dspy import Module, settings, OpenAI
from pydantic import BaseModel, Field
from typing import List, Optional
from dspy.primitives.web import WebScraper

from modules.gen_pydantic_instance import GenPydanticInstance
from vis import visualize_and_save_graph_interactive


class GraphNode(BaseModel):
    id: str = Field(..., description="Unique identifier for the node")
    content: str = Field(
        ..., description="Content or question associated with the node"
    )
    answer: Optional[str] = Field(
        None, description="Answer or result of the node's reasoning step"
    )


class GraphEdge(BaseModel):
    source_id: str = Field(..., description="Source node ID")
    target_id: str = Field(..., description="Target node ID")
    relationship: str = Field(
        ...,
        description="Description of the relationship or reasoning link between them",
    )


class GraphOfThoughtModel(BaseModel):
    nodes: List[GraphNode] = Field(..., description="List of nodes in the graph")
    edges: List[GraphEdge] = Field(..., description="List of edges linking the nodes")


class GraphOfThought(Module):
    def __init__(self, lm):
        super().__init__()
        self.lm = lm

    def forward(self, prompt: str) -> GraphOfThoughtModel:
        return GenPydanticInstance(
            root_model=GraphOfThoughtModel, child_models=[GraphNode, GraphEdge]
        ).forward(prompt)


def main():

    # lm = dspy.OpenAI(model="gpt-4-turbo-preview", max_tokens=4096, model_type='chat')
    lm = dspy.OpenAI(max_tokens=2000)
    dspy.settings.configure(lm=lm)

    # prompt = "Decision Model Notation for cancer diagnosis"
    # prompt = "BPMN for ordering a sandwich"
    # prompt = "Explain the water cycle step by step."
    prompt = "How to find good agents and cofounders?"

    result_graph = GraphOfThought(lm).forward(prompt)
    print(result_graph)
    visualize_and_save_graph_interactive(result_graph)

    lm.inspect_history(n=1)


if __name__ == "__main__":
    main()
