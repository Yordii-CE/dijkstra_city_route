import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pyperclip


# Image Handler click
def onclick(event):
    if event.xdata is not None and event.ydata is not None:   
        coordenada_x = round(event.xdata, 2)
        coordenada_y = round(event.ydata, 2)
        
        coordenadas = {'x': coordenada_x, 'y': coordenada_y}
        #Copy to clipboard
        pyperclip.copy(str(coordenadas) + ",") 
        print(coordenadas)

img_path = 'ciudad.jpeg'

# Read image
img = mpimg.imread(img_path)

# Create figure and graphic
fig, ax = plt.subplots()

ax.imshow(img)
plt.axis('off')
fig.canvas.mpl_connect('button_press_event', onclick)

# Show the image
plt.show()