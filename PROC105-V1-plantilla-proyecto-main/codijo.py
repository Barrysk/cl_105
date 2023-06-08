import os
import cv2

# Establecer ruta de la carpeta de imágenes
folder_path = "Images"

# Crear una lista vacía para almacenar las imágenes
images = []

# Verificar cada archivo en la carpeta
for file in os.listdir(folder_path):
    # Separar el nombre y la extensión del archivo
    file_name, file_extension = os.path.splitext(file)
    
    # Verificar si la extensión del archivo coincide con la extensión de la imagen
    if file_extension.lower() in ['.jpg', '.jpeg', '.png']:
        # Concatenar la ruta y el nombre del archivo
        file_path = os.path.join(folder_path, file)
        print(file_path)  # Comprobar el nombre del archivo
        
        # Agregar el archivo a la lista de imágenes
        images.append(file_path)

# Obtener la cantidad de imágenes
count = len(images)

# Leer la primera imagen de la lista
frame = cv2.imread(images[0])

# Obtener el ancho, alto y canales de la imagen
height, width, channels = frame.shape
size = (width, height)
print(size)  # Comprobar el tamaño

# Crear el objeto VideoWriter
video_name = "Project.mp4"
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = 0.8
video_writer = cv2.VideoWriter(video_name, fourcc, fps, size)

# Agregar imágenes al VideoWriter
for i in range(0, count):
    # Leer cada imagen
    image = cv2.imread(images[i])
    
    # Agregar la imagen al video
    video_writer.write(image)

# Liberar recursos
video_writer.release()

print("Listo")  # Mensaje de finalización
