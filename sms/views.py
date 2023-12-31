from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
import pickle
import nltk
nltk.download('punkt')

nltk.download('stopwords')
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

class SmsView(APIView):
    
    def preprocess_text(self,text):
        # Lower Case
        text = text.lower()

        # Tokenization
        text = nltk.word_tokenize(text)

        # Removing Special Characters
        y = []
        for i in text:
            if i.isalnum():
                y.append(i)

        text = y[:]
        y.clear()

        # Stopwrds, punc and stemming
        for i in text:
            if i not in stopwords.words('english') and i not in string.punctuation:
                i = ps.stem(i)
                y.append(i)


        return " ".join(y)

    def get(self, request):
        sms = Sms.objects.all()
        serializer = SmsSerializer(sms, many=True)
        
        return Response({
            "status": 200,
            "payload": serializer.data,
        })
        
    def post(self, request):
        try:
            serializer = SmsSerializer(data=request.data)
            
            if serializer.is_valid():
                try:
                    vectorizer_path = 'nlp/vectorizer.pkl'
                    model_path = 'nlp/multinomialNB_model.pkl'

                    # Load the pickled files
                    with open(model_path, 'rb') as model_file:
                        model = pickle.load(model_file)

                    with open(vectorizer_path, 'rb') as vectorizer_file:
                        vectorizer = pickle.load(vectorizer_file)
                except Exception as e:
                    print(f"Error in loading pickle files: {e}")
                    return Response({
                        "status": 500,
                        "error": "Internal Server Error",
                    })
                sms = serializer.validated_data['sms']
                print("sms: ", sms)
                transformed_sms = self.preprocess_text(sms)
                vector_input = vectorizer.transform([transformed_sms])
                result = model.predict(vector_input)[0]
                
                ans = "Nothing Yet"
                if result==1:
                    ans = "Spam"
                else:
                    ans = "Not Spam"
                 
                # Save the serializer with the predicted label
                serializer.save(label=ans)
                   
                return Response({
                    
                    "status": 200,
                    "payload": {
                        "prediction": ans,
                    },
                })
            else:
                return Response({
                    "status": 400,
                    "errors": serializer.errors,
                })
        except Exception as e:
            print(f"Error in post method: {e}")
            return Response({
                "status": 500,
                "error": "Internal Server Error",
            })