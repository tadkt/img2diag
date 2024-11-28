# Generating a Draw.io (XML) structure based on the provided elements and connections

def generate_drawio(elements, connections):
    # Base structure for Draw.io file
    drawio_base = """<mxfile host="app.diagrams.net">
  <diagram name="Diagram">
    <mxGraphModel dx="1400" dy="1400" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
    """

    # Add elements to the Draw.io structure
    element_template = """<mxCell id="{id}" value="{label}" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
        <mxGeometry x="{x}" y="{y}" width="160" height="60" as="geometry" />
      </mxCell>
    """
    for element in elements:
        drawio_base += element_template.format(
            id=element["id"],
            label=element["label"],
            x=element["x"],
            y=element["y"]
        )

    # Add connections to the Draw.io structure
    connection_template = """<mxCell id="{id}" edge="1" parent="1" source="{source}" target="{target}">
        <mxGeometry relative="1" as="geometry" />
      </mxCell>
    """
    for idx, connection in enumerate(connections, start=len(elements) + 1):
        drawio_base += connection_template.format(
            id=idx, source=connection["source"], target=connection["target"]
        )

    # Close the Draw.io structure
    drawio_base += """
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
    """
    return drawio_base


# Provided data
elements = [
    {"id": "1", "label": "Vấn đề: bị cháo dây", "x": 100, "y": 50},
    {"id": "2", "label": "Máy A", "x": 100, "y": 150},
    {"id": "3", "label": "Nóng thiết bị AB", "x": 250, "y": 150},
    {"id": "4", "label": "Biến đổi nhiệt 5°C", "x": 400, "y": 150},
    {"id": "5", "label": "Sản phẩm bất thường mã ABC", "x": 550, "y": 150},
    {"id": "6", "label": "Tốc độ máy dao động 0,9", "x": 400, "y": 250}
]

connections = [
    {"source": "1", "target": "2"},
    {"source": "2", "target": "3"},
    {"source": "3", "target": "4"},
    {"source": "4", "target": "5"},
    {"source": "4", "target": "6"}
]

# Generate the Draw.io XML
drawio_content = generate_drawio(elements, connections)

# Save the Draw.io content to a file
drawio_file_path = "generated_diagram.drawio"
with open(drawio_file_path, "w", encoding="utf-8") as file:
    file.write(drawio_content)

drawio_file_path
