from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from.forms import*
from django.shortcuts import render,redirect
import joblib
from .k import *




x_train=[text for text,intent in training_data]
y_train=[intent for text,intent in training_data]

from sklearn. feature_extraction.text import CountVectorizer
from sklearn .naive_bayes import MultinomialNB
CountVectorizer=CountVectorizer()
X_train=CountVectorizer.fit_transform(x_train)
model=MultinomialNB()
model.fit(X_train,y_train)



chat_history = [] 
def chatbot(request):
    form=ChatForm()

    response = None  # Initialize response with a default value
    if request.method == 'POST':
         
         form = ChatForm(request.POST)
         if form.is_valid():
            user_message = form.cleaned_data['message']
            user_input = CountVectorizer.transform([user_message])
            p = model.predict(user_input)[0]
            response = responses.get(p, "I'm sorry, I didn't understand that.")


            chat_history.append(("You", user_message))
            chat_history.append(("Bot", response))
    return  render(request,'home.html',{'form': form, 'chat_history':   chat_history})


# Create your views here.
