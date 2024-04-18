import dspy
from dspy.signatures import Signature, InputField, OutputField
from typing import List, Dict, Any


# Define GraphNode as a DSPy Signature for node processing
class GraphNode(Signature):
    node_id = InputField(desc="Unique identifier for the node")
    content = InputField(desc="Content or question associated with the node")
    answer = OutputField(desc="Answer or result of the node's reasoning step")


# Define GraphEdge as a DSPy Signature for edge processing
class GraphEdge(Signature):
    source_id = InputField(desc="Source node ID")
    target_id = InputField(desc="Target node ID")
    relationship = InputField(
        desc="Description of the relationship or reasoning link between nodes"
    )


# Define GraphOfThoughtModel not as a signature but as a container for nodes and edges
class GraphOfThoughtModel:
    def __init__(self, nodes: List[Dict[str, any]], edges: List[Dict[str, any]]):
        self.nodes = [GraphNode(**node) for node in nodes]
        self.edges = [GraphEdge(**edge) for edge in edges]

    def add_node(self, node: Dict[str, any]):
        self.nodes.append(GraphNode(**node))

    def add_edge(self, edge: Dict[str, any]):
        self.edges.append(GraphEdge(**edge))


class GraphOfThought(dspy.Module):
    def __init__(self, input_signature, process_signature, output_signature, **config):
        super().__init__()
        # Initialize predictors for each phase of graph handling
        self.input_predict = dspy.Predict(input_signature, **config)
        self.process_predict = dspy.Predict(process_signature, **config)
        self.output_predict = dspy.Predict(output_signature, **config)

    def forward(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        # Main entry point: process input data to output data through a graph
        graph = self.input_to_graph(input_data)
        processed_graph = self.process_graph(graph)
        output_data = self.graph_to_output(processed_graph, input_data)
        return output_data

    def input_to_graph(self, input_data: Dict[str, Any]) -> GraphOfThoughtModel:
        # Convert input data to a graph model
        prediction = self.input_predict(**input_data)
        nodes = prediction.get("nodes", [])
        edges = prediction.get("edges", [])
        return GraphOfThoughtModel(nodes=nodes, edges=edges)

    def process_graph(self, graph: GraphOfThoughtModel) -> GraphOfThoughtModel:
        # Process each node in the graph
        for node in graph.nodes:
            processed_content = self.process_predict(
                node_id=node.id, content=node.content
            )
            node.answer = processed_content.get("answer", {})
        return graph

    def graph_to_output(
        self, processed_graph: GraphOfThoughtModel, original_input: Dict[str, Any]
    ) -> Dict[str, Any]:
        # Convert processed graph to output data
        node_answers = {node.id: node.answer for node in processed_graph.nodes}
        output_data = self.output_predict(
            nodes=node_answers, original_input=original_input
        )
        return output_data
