###########################
# save this as app.py
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Welcome!"
#############################
# import joblib
# from flask import Flask
# from tensorflow import keras
# import pickle

# app = Flask(__name__)

# # route set as
# @app.route("/")

# model = keras.models.load_model("prediction_model.h5")
# texts_model = joblib.load("texts_model.joblib")
# # loading
# with open('tokenizer.pickle', 'rb') as handle:
#     tokenizer = pickle.load(handle)

# def generate_text_seq(model=model, tokenizer=tokenizer, n_words=3, text_seq_length=51):
#       lines = []
#       for i in range(text_seq_length, len(tokenizer)):
#             seq = tokenizer[i-text_seq_length:i]
#             line = ' '.join(seq)
#             lines.append(line)
#             if i > 200000:
#                   break

#         seed_text = lines[0]
#         text = []
#         for _ in range(n_words): # how many words you want to generate
#           encoded = tokenizer.texts_to_sequences([seed_text])[0]
#           encoded = pad_sequences([encoded], maxlen = text_seq_length, truncating = 'pre')

#           y_predict = model.predict_classes(encoded) # return the interger value of the word

#           predicted_word = ''
#         for word, index in tokenizer.word_index.items(): # find the word by the integer word
#             if index == y_predict:
#                 predicted_word = word
#                 break
#         seed_text = seed_text + ' ' + predicted_word
#         text.append(predicted_word)
#       return ' '.join(text)
############################
from flask import Flask
from tensorflow import keras
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

model = keras.models.load_model("prediction_model.h5")
with open('tokenizer.pickle', 'rb') as handle:
  tokenizer = pickle.load(handle)
with open('seq_length.pickle', 'rb') as handle:
  seq_length = pickle.load(handle)
with open('lines.pickle', 'rb') as handle:
  lines = pickle.load(handle)

@app.route("/")
def hello():
    return "Welcome to the matrix!"

@app.route("/<n_words>")
#def generate_text_seq(model, tokenizer, text_seq_length, seed_text, n_words):
def generate_text_seq(seed_text=lines[0],n_words=3):
      model = keras.models.load_model("prediction_model.h5")
      with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
      with open('seq_length.pickle', 'rb') as handle:
        seq_length = pickle.load(handle)
      with open('lines.pickle', 'rb') as handle:
        lines = pickle.load(handle)
      text = []
      for _ in range(int(n_words)):
        encoded = tokenizer.texts_to_sequences([seed_text])[0]
        encoded = pad_sequences([encoded], maxlen = seq_length, truncating = 'pre')
        y_predict = model.predict_classes(encoded)
        predicted_word = ''
        for word, index in tokenizer.word_index.items():
              if index == y_predict:
                    predicted_word = word
                    break
        seed_text = seed_text + ' ' + predicted_word
        text.append(predicted_word)
        gen_text = str(' '.join(text))
      return lines[0] + ' ' + gen_text
      
      
      #generate_text_seq(lines[0], 3)

if __name__ == '__main__':
      app.run(host='127.0.0.1',port=5001,debug=True)
# def pred():
#     return "-deal of the- is the same Part-of-Speech as -daughers of a-"