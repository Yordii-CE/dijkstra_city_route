import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def get_data_by_name(graph_data, name):
    node_data = None
    for i in graph_data:
        if i['name'] == name:
            node_data = i
    return node_data

def draw_coords_in_image(image_path, graph_data):
     # Carga la imagen
    img = mpimg.imread(image_path)

    # Crea la figura y el gráfico
    fig, ax = plt.subplots()

    # Muestra la imagen
    ax.imshow(img)
    plt.axis('off')   

    # Dibuja el punto rojo en las coordenadas dadas y agrega el número
    for i, coord in enumerate(graph_data):    
        x, y, connections = coord['x'], coord['y'], coord['connections']
        color = 'ro'
        if i == 0: color = 'go'
        if i == len(graph_data) - 1: color = 'go'
        
        ax.plot(x, y, color, markersize=15)
        
        ax.text(x, y, str(coord['name']), color='white', fontsize=8, ha='center', va='center')


        #Draw line connection
        if(len(connections) > 0):
            for c in connections:
                connectedNode = get_data_by_name(graph_data, c[0])
                if connectedNode == None : continue
                cx, cy = connectedNode['x'], connectedNode['y']
                
                ax.annotate('', xy=(cx, cy), xytext=(x,y),
                    arrowprops=dict(arrowstyle='->', color='blue', linewidth=2),
                    annotation_clip=False)
                
                # Calcula el punto medio entre las coordenadas inicial y final
                punto_medio = ((x + cx) / 2,
                            (y + cy) / 2)

                # # Agrega el texto en el punto medio de la línea
            
                ax.text(punto_medio[0], punto_medio[1], str(c[1]), color='black', fontsize=10,
                            ha='center', va='center', fontweight='bold')
                
    # Muestra el gráfico con los puntos y números dibujados
    #plt.show()
    return plt