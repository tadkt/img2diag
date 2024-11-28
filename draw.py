import json
import plotly.graph_objects as go

# Parse the JSONL content
jsonl_content = """
{"type": "node", "data": {"id": "1", "label": "Máy A", "x": 100, "y": 50}}
{"type": "node", "data": {"id": "2", "label": "Nóng thiết bị AB", "x": 250, "y": 150}}
{"type": "node", "data": {"id": "3", "label": "Sản phẩm bất thường mã ABC", "x": 450, "y": 150}}
{"type": "arrow", "data": {"source": "1", "target": "2", "label": ""}}
{"type": "arrow", "data": {"source": "2", "target": "3", "label": "Biên độ nhiệt 5°C"}}
{"type": "arrow", "data": {"source": "2", "target": "3", "label": "Tốc độ máy dao động 0.9"}}
"""

# Parse nodes and arrows
nodes = {}
arrows = []

for line in jsonl_content.strip().split("\n"):
    item = json.loads(line)
    if item["type"] == "node":
        nodes[item["data"]["id"]] = {
            "label": item["data"]["label"],
            "x": item["data"]["x"],
            "y": item["data"]["y"]
        }
    elif item["type"] == "arrow":
        arrows.append((item["data"]["source"], item["data"]["target"], item["data"]["label"]))

# Create plotly graph
edge_x = []
edge_y = []
edge_text = []
node_x = []
node_y = []
node_text = []

# Add nodes to plotly graph
for node_id, node_data in nodes.items():
    node_x.append(node_data["x"])
    node_y.append(node_data["y"])
    node_text.append(node_data["label"])

# Add edges to plotly graph
for source, target, label in arrows:
    x0, y0 = nodes[source]["x"], nodes[source]["y"]
    x1, y1 = nodes[target]["x"], nodes[target]["y"]
    
    edge_x.append(x0)
    edge_y.append(y0)
    edge_x.append(x1)
    edge_y.append(y1)
    edge_text.append(label)

# Create the figure
fig = go.Figure()

# Add edges as lines
fig.add_trace(go.Scatter(
    x=edge_x,
    y=edge_y,
    mode='lines+text',
    line=dict(width=2, color='black'),
    text=edge_text,
    textposition='top center',
    hoverinfo='text'
))

# Add nodes as scatter points
fig.add_trace(go.Scatter(
    x=node_x,
    y=node_y,
    mode='markers+text',
    marker=dict(color='blue', size=20),
    text=node_text,
    textposition='bottom center',
    hoverinfo='text'
))

# Update layout for better visuals
fig.update_layout(
    title="Flow Diagram",
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=False, zeroline=False),
    plot_bgcolor='white',
    margin=dict(l=0, r=0, t=40, b=0),
    autosize=True
)

# Show the figure
fig.show()
