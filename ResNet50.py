import cv2
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image

# 1. Carregar modelo pré-treinado (ResNet50 com pesos do ImageNet)
model = ResNet50(weights='imagenet')

# 2. Inicializar o classificador de faces (Haar Cascade do OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 3. Abrir a câmera ou vídeo
cap = cv2.VideoCapture(0)  # 0 = webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Converter para escala de cinza (detecção de faces)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Desenhar retângulo ao redor da face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Recortar a face detectada
        face_img = frame[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (224, 224))  # tamanho esperado pelo ResNet50

        # Pré-processar a imagem
        x_img = image.img_to_array(face_img)
        x_img = np.expand_dims(x_img, axis=0)
        x_img = preprocess_input(x_img)

        # Classificação da face (usando ResNet50 como exemplo)
        preds = model.predict(x_img)
        # Aqui você pode usar decode_predictions ou treinar sua própria rede para reconhecimento específico

    # Mostrar resultado
    cv2.imshow('Reconhecimento Facial', frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()