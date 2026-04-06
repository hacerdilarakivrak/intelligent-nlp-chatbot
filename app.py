import gradio as gr
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Modeli yükle
model = load_model("model.h5")

# Tokenizer'ı yükle
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Label encoder'ı yükle
with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Senin Colab'dan çıkan gerçek max_len değeri
max_len = 7

# Intent'lere göre cevaplar
responses = {
    "greeting": "Hello! How can I help you?",
    "goodbye": "Goodbye! Have a great day.",
    "help": "I can help you with greetings, time queries, weather queries, course information, identity questions, and thanks.",
    "time_query": "This looks like a time-related question.",
    "weather_query": "This looks like a weather-related question.",
    "course_info": "This looks like a course-related question.",
    "thanks": "You're welcome!",
    "identity": "I am an NLP-based intelligent chatbot."
}

# Intent tahmin fonksiyonu
def predict_intent(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len, padding="post")
    prediction = model.predict(padded, verbose=0)
    predicted_index = np.argmax(prediction)
    predicted_label = label_encoder.inverse_transform([predicted_index])[0]
    return predicted_label

# Chatbot cevap fonksiyonu
def chatbot_app(user_input):
    intent = predict_intent(user_input)
    response = responses.get(intent, "Sorry, I couldn't understand that.")
    return response

# Gradio arayüzü
demo = gr.Interface(
    fn=chatbot_app,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here...", label="You"),
    outputs=gr.Textbox(label="Chatbot Response"),
    title="Intelligent NLP Chatbot 🤖",
    description="An intent detection chatbot built using TensorFlow, TF-IDF, and N-gram models."
)

# Uygulamayı başlat
demo.launch()