import plotly.graph_objects as go
import networkx as nx


def visualize_and_save_graph_interactive(
    graph_of_thought_model, filename="GraphOfThought.html"
):
    G = nx.DiGraph()

    # Add nodes and edges to the graph
    for node in graph_of_thought_model.nodes:
        G.add_node(node.id, label=node.content)
    for edge in graph_of_thought_model.edges:
        G.add_edge(edge.source_id, edge.target_id, label=edge.relationship)

    pos = nx.spring_layout(G)  # Generate positions for all nodes

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)  # Marks the end of the edge line
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=0.5, color="#888"),
        hoverinfo="none",
        mode="lines",
    )

    node_x = []
    node_y = []
    text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        text.append(G.nodes[node]["label"])

    node_trace = go.Scatter(
        x=node_x,
        
        
        y=node_y,
        mode="markers+text",
        hoverinfo="text",
        text=text,
        marker=dict(showscale=False, color="#1273de", size=10, line_width=2),
    )

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            showlegend=False,
            hovermode="closest",
            margin=dict(b=0, l=0, r=0, t=0),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        ),
    )

    fig.write_html(filename)
    print(f"Graph saved as {filename}")
