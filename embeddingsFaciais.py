import cv2
from deepface import DeepFace

# Inicializar a câmera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar e reconhecer faces
    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    # Se houver múltiplas faces
    if isinstance(result, list):
        for face in result:
            x, y, w, h = face['region'].values()
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Exibir nome ou emoção detectada
            cv2.putText(frame, face['dominant_emotion'], (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    else:
        x, y, w, h = result['region'].values()
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, result['dominant_emotion'], (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    # Mostrar resultado
    cv2.imshow('Reconhecimento Facial', frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()