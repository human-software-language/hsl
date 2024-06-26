import dspy
from pydantic import BaseModel, Field
from typing import List, Optional

from modules.gen_pydantic_instance import GenPydanticInstance


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
        ..., description="Description of the relationship or reasoning link"
    )


class GraphOfThoughtModel(BaseModel):
    nodes: List[GraphNode] = Field(..., description="List of nodes in the graph")
    edges: List[GraphEdge] = Field(..., description="List of edges linking the nodes")


class GraphOfThought(dspy.Module):
    def __init__(self, signature):
        super().__init__()
        self.signature = dspy.Prediction.from_completions(signature).signature

    def forward(self, prompt) -> GraphOfThoughtModel:
        print(self.signature)
        return GenPydanticInstance(
            root_model=GraphOfThoughtModel, child_models=[GraphNode, GraphEdge]
        ).forward(prompt)


def main():
    lm = dspy.OpenAI(max_tokens=1000)
    dspy.settings.configure(lm=lm)

    prompt = "Decision Model Notation for cancer diagnosis"
    # prompt = "BPMN for ordering a sandwich"
    # prompt = "Explain the water cycle step by step."

    result_graph = GraphOfThought().forward(prompt)
    print(result_graph)

    lm.inspect_history(n=1)


if __name__ == "__main__":
    main()
