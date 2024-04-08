# Importar librerías
import cv2
from ultralytics import YOLO

# Función para dibujar los bounding boxes en el frame
def plot_boxes(results, frame):
    for result in results:
        boxes = result.boxes.cpu().numpy()
        xyxys = boxes.xyxy
        label = boxes.cls
        
        etiqueta = 0
        name_etiqueta = 'person'
        
        # Iterar sobre las coordenadas de los bounding boxes
        for indice, xyxy in enumerate(xyxys):
            # Verificar si el índice corresponde a la posición con cero (persona) en la lista de números
            if label[indice] == etiqueta:
                # Dibujar el bounding box solo si corresponde a una posición con cero
                cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0, 255, 0), 2)
                
                # Agregar label "person" en la parte superior izquierda del bounding box
                cv2.putText(frame, name_etiqueta, (int(xyxy[0]), int(xyxy[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

# Función principal
def main():
    # Cargar el modelo YOLOv8
    model = YOLO('yolov8s.pt')

    # Lectura de imagen de la cámara
    cap = cv2.VideoCapture(0)

    # Bucle a través de los frames del video
    while cap.isOpened():
        # Leer un frame del video
        success, frame = cap.read()
        
        frame = cv2.flip(frame, 1)

        if success:
            # Realizar inferencia YOLOv8 en el frame
            results = model(frame)
                
            # Visualizar los resultados en el frame
            plot_boxes(results, frame)
        
            # Mostrar el frame anotado
            cv2.imshow("YOLOv8 Inference", frame)

            # Romper el bucle si se presiona 'q'
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Romper el bucle si se alcanza el final del video
            break

    # Liberar el objeto de captura de video y cerrar la ventana de visualización
    cap.release()
    cv2.destroyAllWindows()

# Ejecutar la función principal si este script se ejecuta directamente
if __name__ == "__main__":
    main()
