# 🤖 Intelligent NLP Chatbot

This project is an **intent detection chatbot** developed using Natural Language Processing (NLP) techniques.
It classifies user inputs into predefined intents and generates appropriate responses through a trained deep learning model.

---

## 🚀 Features

* Intent classification using a trained neural network model
* Text preprocessing with tokenization and sequence padding
* Supports multiple intents including:

  * Greeting
  * Goodbye
  * Help
  * Weather queries
  * Time queries
  * Course information
  * Identity questions
  * Thanks
* Interactive user interface built with Gradio

---

## 🧠 Technologies Used

* Python
* TensorFlow / Keras
* Scikit-learn
* Gradio
* NLP techniques (TF-IDF, N-grams, tokenization)

---

## 📂 Dataset

A custom dataset was fully designed and manually created from scratch by the author for intent classification tasks. No pre-existing datasets were used.

The dataset consists of multiple intent categories, each containing approximately 50 diverse example sentences to ensure robustness and generalization. In total, the dataset includes around 400 samples.

To maintain fairness and avoid bias, the dataset was carefully balanced across all intent classes. The data was split into training (80%) and testing (20%) sets for reliable model evaluation.

This approach provides full control over the data and ensures that the model is trained on task-specific, high-quality examples.

---

## 📂 Project Structure

```
.
├── app.py                         # Gradio application interface
├── model.h5                      # Trained model
├── tokenizer.pkl                 # Tokenizer for preprocessing
├── label_encoder.pkl             # Label encoder for intent mapping
├── requirements.txt              # Dependencies
├── intelligent_nlp_chatbot.ipynb # Full project notebook
```

---

## 🌐 Live Demo

👉 Try the chatbot here:
https://huggingface.co/spaces/hacerdilarakivrak/intelligent-nlp-chatbot

---

## ⚙️ How It Works

1. The user inputs a message
2. The text is converted into numerical sequences using a tokenizer
3. Sequences are padded to a fixed length (`max_len = 7`)
4. The trained model predicts the corresponding intent
5. The system returns a predefined response

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/hacerdilarakivrak/intelligent-nlp-chatbot.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python app.py
```

---

## 📓 Project Notebook

The complete project, including preprocessing, model training, and interface development, is available in:

`intelligent_nlp_chatbot.ipynb`

---


## 👩‍💻 Author

Hacer Dilara Kıvrak

---

## 📄 License

This project is developed for educational purposes.
