import dspy
from dspy import Module, OpenAI
from dspy.primitives.web import WebScraper
from dspy.utils import deduplicate
from typing import List, Dict

# Assuming the provided graph classes and functions are in graph_module.py
from modules.graph_of_thought import GraphOfThought, GraphNode, GraphEdge, GraphOfThoughtModel


class KnowledgeGraphBuilder(Module):
    def __init__(self):
        super().__init__()

        self.lm = OpenAI(
            model="gpt-3.5-turbo", max_tokens=4096
        )  # Adjust model as needed
        self.graph_of_thought = GraphOfThought(self.lm)
        self.web_scraper = WebScraper()

    def extract_information(self, url: str) -> str:
        """
        Extracts main content from a given URL.
        """
        content = self.web_scraper.scrape(url=url)
        return content

    def update_graph(self, prompt: str) -> GraphOfThoughtModel:
        """
        Updates the knowledge graph based on the given prompt.
        """
        return self.graph_of_thought.forward(prompt)

    def process_and_update(self, urls: List[str]) -> Dict[str, GraphOfThoughtModel]:
        """
        Processes each URL to extract information and update the knowledge graph.
        """
        graphs = {}
        for url in urls:
            content = self.extract_information(url)
            graph = self.update_graph(content)
            graphs[url] = graph
        return graphs


def main():
    kg_builder = KnowledgeGraphBuilder()
    urls = [
        "https://example.com/article1",
        "https://example.com/article2",
        # Add more URLs as needed
    ]
    knowledge_graphs = kg_builder.process_and_update(urls)

    # Optionally, visualize or save the updated knowledge graphs
    for url, graph in knowledge_graphs.items():
        print(f"Graph for {url}:")
        print(graph)


if __name__ == "__main__":
    main()
