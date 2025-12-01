# Sistema de Detecção e Reconhecimento Facial 🧑‍💻

## 📌 Descrição
Este projeto implementa um sistema de **detecção e reconhecimento facial** em tempo real, utilizando:
- **TensorFlow/Keras** para modelos pré-treinados (ex.: ResNet50).
- **OpenCV** para captura de vídeo e detecção de faces.
- **DeepFace** para reconhecimento facial baseado em embeddings.

O sistema é capaz de:
- Detectar múltiplas faces em uma imagem ou vídeo.
- Reconhecer pessoas específicas a partir de um **dataset de imagens**.
- Exibir o nome da pessoa reconhecida diretamente na tela.

---

## 🚀 Tecnologias Utilizadas
- [Python 3.8+](https://www.python.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [OpenCV](https://opencv.org/)
- [DeepFace](https://github.com/serengil/deepface)
- [NumPy](https://numpy.org/)

---

## 📂 Estrutura do Projeto


---

## ⚙️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/reconhecimento-facial.git
   cd reconhecimento-facial

   python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

- Adicione imagens das pessoas que deseja reconhecer dentro da pasta dataset/, cada pessoa em uma subpasta com seu nome.
- Execute o código:
python main.py
- O sistema abrirá a webcam e exibirá:
- Retângulos ao redor das faces detectadas.
- O nome da pessoa reconhecida (baseado no dataset).
Pressione q para encerrar a execução.📖 Exemplo de Uso- Adicione fotos de Bruno, Maria e João no dataset.
- Ao rodar o sistema, ele detectará e reconhecerá cada pessoa em tempo real.
🔑 Observações- Quanto mais imagens por pessoa, melhor a precisão.
- É recomendado usar fotos variadas (ângulos, iluminação).
- O DeepFace suporta diferentes modelos de embeddings (VGG-Face, Facenet, OpenFace, DeepFace, Dlib, ArcFace).
👨‍💻 AutorProjeto desenvolvido por Bruno Braat, como parte de estudos em Machine Learning e Visão Computacional.
