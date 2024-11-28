import json
import plotly.graph_objects as go

# # Parse the JSONL content
# jsonl_content = """
# {"type": "node", "data": {"id": "1", "label": "Máy A", "x": 100, "y": 50}}
# {"type": "node", "data": {"id": "2", "label": "Nóng thiết bị AB", "x": 250, "y": 150}}
# {"type": "node", "data": {"id": "3", "label": "Sản phẩm bất thường mã ABC", "x": 450, "y": 150}}
# {"type": "arrow", "data": {"source": "1", "target": "2", "label": ""}}
# {"type": "arrow", "data": {"source": "2", "target": "3", "label": "Biên độ nhiệt 5°C"}}
# {"type": "arrow", "data": {"source": "2", "target": "3", "label": "Tốc độ máy dao động 0.9"}}
# """

# # Corrected input
# jsonl_content = """
# {"type": "node", "data": {"id": "1", "label": "CNC", "x1": -100, "y1": 0, "x2": 0, "y2": 50}}
# {"type": "node", "data": {"id": "2", "label": "Đầu khoan cứng", "x1": 100, "y1": 0, "x2": 200, "y2": 50}}
# {"type": "node", "data": {"id": "3", "label": "Lệch 0.5mm", "x1": 100, "y1": -150, "x2": 200, "y2": -100}}
# {"type": "node", "data": {"id": "4", "label": "Sản phẩm kém chất lượng", "x1": 300, "y1": -150, "x2": 400, "y2": -100}}
# {"type": "node", "data": {"id": "5", "label": "Máy dao động nhiều", "x1": 100, "y1": -300, "x2": 200, "y2": -250}}
# {"type": "arrow", "data": {"id": "a1", "label": "Vấn đề", "x1": 0, "y1": 25, "x2": 100, "y2": 25}}
# {"type": "arrow", "data": {"id": "a2", "label": "", "x1": 150, "y1": 0, "x2": 150, "y2": -100}}
# {"type": "arrow", "data": {"id": "a3", "label": "", "x1": 200, "y1": -125, "x2": 300, "y2": -125}}
# {"type": "arrow", "data": {"id": "a4", "label": "", "x1": 200, "y1": -275, "x2": 350, "y2": -275, "x3": 350, "y3": -150}}
# """

# Trial input
jsonl_content = """
{"type": "node", "data": {"id": "1", "label": "Máy A", "x1": -50, "y1": -50, "x2": 50, "y2": 0}}\n{"type": "node", "data": {"id": "2", "label": "Nóng thiết bị AB", "x1": -100, "y1": -25, "x2": 0, "y2": 25}}\n{"type": "node", "data": {"id": "3", "label": "Biến đổi nhiệt 5°C", "x1": 50, "y1": -25, "x2": 150, "y2": 25}}\n{"type": "node", "data": {"id": "4", "label": "Sản phẩm bất thường nhiệt ABC", "x1": 200, "y1": -25, "x2": 350, "y2": 25}}\n{"type": "arrow", "data": {"id": "1", "label": "", "x1": 0, "y1": 0, "x2": -100, "y2": 0}}\n{"type": "arrow", "data": {"id": "2", "label": "Tốc độ máy dao động 0.9", "x1": 0, "y1": 0, "x2": 100, "y2": 0}}\n{"type": "arrow", "data": {"id": "3", "label": "", "x1": 150, "y1": 0, "x2": 200, "y2": 0}}\n
"""
# Parse nodes and arrows
nodes = {}
arrows = {}

for line in jsonl_content.strip().split("\n"):
    item = json.loads(line)
    if item["type"] == "node":
        nodes[item["data"]["id"]] = {
            "label": item["data"]["label"],
            "x1": item["data"]["x1"],
            "y1": item["data"]["y1"],
            "x2": item["data"]["x2"],
            "y2": item["data"]["y2"],
        }

    elif item["type"] == "arrow":
        arrows[item["data"]["id"]] = {
            "label": item["data"]["label"],
            "x1": item["data"]["x1"],
            "y1": item["data"]["y1"],
            "x2": item["data"]["x2"],
            "y2": item["data"]["y2"]
        }
        # Add x3 and y3 if they exist in the data
        if "x3" in item["data"] and "y3" in item["data"]:
            arrows[item["data"]["id"]]["x3"] = item["data"]["x3"]
            arrows[item["data"]["id"]]["y3"] = item["data"]["y3"]
        else:
            arrows[item["data"]["id"]]["x3"] = None
            arrows[item["data"]["id"]]["y3"] = None



# Create plotly graph
edge_x1 = []
edge_y1 = []
edge_x2 = []
edge_y2 = []
edge_x3 = []
edge_y3 = []
edge_text = []
node_x1 = []
node_x2 = []
node_y1 = []
node_y2 = []
node_text = []

# Add nodes to plotly graph
for node_id, node_data in nodes.items():
    node_x1.append(node_data["x1"])
    node_x2.append(node_data["x2"])
    node_y1.append(node_data["y1"])
    node_y2.append(node_data["y2"])
    node_text.append(node_data["label"])

# Add edges to plotly graph
for arrow_id, arrow_data in arrows.items():
    edge_x1.append(arrow_data["x1"])
    edge_x2.append(arrow_data["x2"])
    edge_x3.append(arrow_data["x3"])
    edge_y1.append(arrow_data["y1"])
    edge_y2.append(arrow_data["y2"])
    edge_y3.append(arrow_data["y3"])
    edge_text.append(arrow_data["label"])

# Plot
fig = go.Figure()

for idx in range(len(node_x1)):
    fig.add_shape(type="rect", x0=node_x1[idx], y0=node_y1[idx], x1=node_x2[idx], y1=node_y2[idx])
    fig.add_trace(go.Scatter(x=[(node_x1[idx]+node_x2[idx])/2], y=[node_y2[idx]+10], text=[node_text[idx]], mode="text"))


# Use mode line+text
for idx in range(len(edge_x1)):
    if edge_x3[idx] is not None and edge_y3[idx] is not None:
        fig.add_shape(type="line", x0=edge_x1[idx], y0=edge_y1[idx], x1=edge_x2[idx], y1=edge_y2[idx])
        fig.add_trace(go.Scatter(x=[edge_x2[idx], edge_x3[idx]], y=[edge_y2[idx], edge_y3[idx]], mode="lines+markers+text",
                                marker=dict(
                                    size=10,  # Size of the arrow marker
                                    symbol="arrow-bar-up",  # Arrow marker type
                                    angleref="previous",  # Angle reference relative to the previous point
                                ),
                                # line=dict(color="black"),
                                text=[None, edge_text[idx]],
                                textposition="top center",
                                textfont=dict(size=12),))
        # fig.add_shape(type="line", x0=edge_x2[idx], y0=edge_y2[idx], x1=edge_x3[idx], y1=edge_y3[idx], label=dict(text=edge_text[idx]))
    else:
        # fig.add_shape(type="line", x0=edge_x1[idx], y0=edge_y1[idx], x1=edge_x2[idx], y1=edge_y2[idx], label=dict(text=edge_text[idx]))
        fig.add_trace(go.Scatter(x=[edge_x1[idx], edge_x2[idx]], y=[edge_y1[idx], edge_y2[idx]], mode="lines+markers+text",
                                marker=dict(
                                    size=10,  # Size of the arrow marker
                                    symbol="arrow-bar-up",  # Arrow marker type
                                    angleref="previous",  # Angle reference relative to the previous point
                                ),
                                # line=dict(color="black"),
                                text=[None, edge_text[idx]],
                                textposition="top center",
                                textfont=dict(size=12),))
fig.show()




# # Create the figure
# fig = go.Figure()

# # Add edges as lines
# fig.add_trace(go.Scatter(
#     x=edge_x,
#     y=edge_y,
#     mode='lines+text',
#     line=dict(width=2, color='black'),
#     text=edge_text,
#     textposition='top center',
#     hoverinfo='text'
# ))

# # Add nodes as scatter points
# fig.add_trace(go.Scatter(
#     x=node_x,
#     y=node_y,
#     mode='markers+text',
#     marker=dict(color='blue', size=20),
#     text=node_text,
#     textposition='bottom center',
#     hoverinfo='text'
# ))

# # Update layout for better visuals
# fig.update_layout(
#     title="Flow Diagram",
#     showlegend=False,
#     xaxis=dict(showgrid=False, zeroline=False),
#     yaxis=dict(showgrid=False, zeroline=False),
#     plot_bgcolor='white',
#     margin=dict(l=0, r=0, t=40, b=0),
#     autosize=True
# )

# # Show the figure
# fig.show()
# print(f"Edge x1: {edge_x1}")
# print(f"Edge x3: {edge_x3}")
# print(f"Edge text: {edge_text}")
# print(f"Edge y3: {edge_y3}")
# print(f"Node x1: {node_x1}")