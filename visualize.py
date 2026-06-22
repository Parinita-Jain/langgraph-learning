# visualize.py

from graph import app

png_data = app.get_graph().draw_mermaid_png()

with open("graph.png", "wb") as f:
    f.write(png_data)

print("Graph saved as graph.png")