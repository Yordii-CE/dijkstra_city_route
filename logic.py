import pandas as pd
from dijkstra.graph import Node
from dijkstra.dijkstra import Dijkstra
from data.get_graph_data import get_graph_data

pd.set_option('display.max_columns', None)

data =  get_graph_data()
nodes = []
    
#Name == Node.value
def search_data_by_node_value(value):
    dat = None
    for i in data:
        if i['name'] == value:
            dat = i

    return dat

def search_node_by_name(name):
    nod = None
    for i in nodes:
        if i.value == name:
            nod = i
    return nod 

def create_nodes():
    for i in data:
        node = Node(i['name'])
        nodes.append(node)

    for i in nodes:
        d = search_data_by_node_value(i.value)
        conn = []
        for k in d['connections']:
            nod = search_node_by_name(k[0])
            co = {'node' : nod, 'distance' : k[1]}
            conn.append(co)   
        i.connect(conn)

def search_best_route(initialNode, destinationNode):      
    create_nodes()
    initialNode = search_node_by_name(initialNode)
    destinationNode = search_node_by_name(destinationNode)

    dijkstra = Dijkstra(nodes)
    dijkstra.createRoutes(initialNode)
    route = dijkstra.getBestRoute(destinationNode)
    return route  
