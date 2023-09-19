import tkinter as tk
from tkinter import ttk
from image.draw_coords_in_image import draw_coords_in_image
from logic import search_best_route, search_data_by_node_value
from data.get_graph_data import get_graph_data
def get_route_string(route):
    routeString = ""
    for item in route:
        node = item['node'].value
        routeString = routeString + str(node) + "->"

    return routeString

def get_nodes_data(route):
    nodes_data = []
    for i in route:
        d = search_data_by_node_value(i['node'].value)
        nodes_data.append(d)
    return nodes_data

def click_handler_btn_graph():
    image = draw_coords_in_image('image/city.jpeg', get_graph_data())
    image.show()

def click_handler():
    origin = origin_cbx.get()
    destination = destination_cbx.get()    

    if(origin == "" or destination == "") : return
    
    route = search_best_route(origin, destination)
    if(len(route) == 0) :
        message.configure(text="Ruta óptima calculada: " + "No existe ruta para llegar al destino", foreground="red")
        return
    
    #Show route string
    routeString = get_route_string(route)
    routeString = routeString.strip("->")
    message.configure(text="Ruta óptima calculada: " + str(routeString), foreground="black")
    
    #Show route in image
    nodes_data = get_nodes_data(route)    
    image = draw_coords_in_image('image/city.jpeg', nodes_data)
    image.show()
    
    
windows = tk.Tk()
windows.title("Find the optimal route")

# Origin Combobox 
origin_text = ttk.Label(windows, text="Origin:")
origin_text.pack()
origin_options = tuple(f'v{i}' for i in range(1, 50))
origin_cbx = ttk.Combobox(windows, values=origin_options)
origin_cbx.pack()
origin_cbx.bind("<<ComboboxSelected>>", None)

# Destination Combobox 
destination_text = ttk.Label(windows, text="Destination:")
destination_text.pack()
destination_options = tuple(f'v{i}' for i in range(1, 50))
destination_cbx = ttk.Combobox(windows, values=destination_options)
destination_cbx.pack()
destination_cbx.bind("<<ComboboxSelected>>", None)

# Image
city_label = tk.Label(windows)
city_label.pack()
# Crear el botón de calcular ruta óptima
btn = ttk.Button(windows, text="Best route", command=click_handler)
btn.pack(pady=20)

btn_graph = ttk.Button(windows, text="See graph", command=click_handler_btn_graph)
btn_graph.pack(pady=20)

# Crear el panel de mensajes de texto
message = ttk.Label(windows, text="")
message.pack()

windows.mainloop()
