import osmnx as ox

place_name = "Medellín, Colombia"
G = ox.graph_from_place(place_name, network_type="drive")

# ox.plot_graph(G)

ox.plot_graph(G, node_size=1, node_color="red")

def style_unvisited_edge(edge):        
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 0.2
    G.edges[edge]["linewidth"] = 0.5

def style_visited_edge(edge):
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

for edges in G.edges:
    style_visited_edge(edges)