import osmnx as ox

place_name = "Medellín, Colombia"
graph = ox.graph_from_place(place_name, network_type="drive")

ox.plot_graph(graph)