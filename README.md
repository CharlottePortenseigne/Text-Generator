# Text-Generator
This project is an Automatic Text Generator in Python 3.
It takes 50 words and predicts the 51st words or more.


# Installation
to clean the Data library
- Numpy 1.22.1
$ `pip install numpy`
- String
$ `pip install strings`
- Re 2021.11.10
$ `pip install regex`

to save the model library
- Pickle 5
$ `pip install pickle5`

Neural Network library
- TensorFlow 2
Requires the latest pip
$ 'pip install --upgrade pip'

Current stable release for CPU and GPU
pip install tensorflow
- Keras 2.7.0
$ `pip install keras`

Natural Language Processing library
- NLTK 3.6.7
$ `pip install nltk`
- SpaCy 3.2.1
$ `pip install spacy`

Deployment
- Flask 2.0.2
$ `pip install Flask`


# Project Development
The corpus is based of 18 English texts of the Gutemberg Project (Emma from Austen, Persuasion from Austen, Sens from Austen, the bible, Blake's poems, the stories from Bryant, Busterbrown from Burgess, Alice from Caroll, Ball from Chesterton, Brown from Chesterton, Thrusday from Chesterton, Parents from Edgeworth, Moby dick from Melville, Paradise from Milton, Caesar from Shakespeare, Hamlet from Shakespeare, Macbeth from Shakespeare and Leaves from Whitman), so thousands of pages.

Then, we cleaned the corpus by taking out the punctation, select only alphanumeric characters and put everything in lower case. The corpus merge all the texts, tokenized the corpus and made a dictionary of words from it.
A LSTM model Predictive model is made with 6 layers (Embedding, LSTM, Dropout, LSTM, Dropout, Dense, Dense). The model is saved with pickle.

In addition of that, to test the model we compare the Part-of-Speech of the original text and the Part-of-Speech of the predictive sentence.Then, we visualize the linguistics features of the original sentence and the predictive sentence.

Finally, we do a local deployment of the predictive sentence. The first page is the welcome page, then you can add the number of predictive words that you want on the URL.
