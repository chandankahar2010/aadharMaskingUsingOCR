import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Dense,Embedding,LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint
import os
import pickle
import numpy as np

file=open('C:/Users/chandan/Desktop/object_detection/object_detection/smart_compose/pride and prejudice.txt','r',encoding='utf8')
lines=[]
for i in file:
    lines.append(i)

data=""
for i in lines:
    data = ' '.join(lines)

data = data.replace('\n','').replace('\r','').replace('\ufeff','').replace('\"','').replace('\"','')
data  = data.split()
data = ' '.join(data)

tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
pickle.dump(tokenizer,open('C:/Users/chandan/Desktop/object_detection/object_detection/smart_compose/token.pkl','wb'))
sequence_data = tokenizer.texts_to_sequences([data])[0]

vocab_size=len(tokenizer.word_index)+1

sequences = []
for i in range(3,len(sequence_data)):
    words = sequence_data[i-3:i+1]
    sequences.append(words)

sequences = np.array(sequences)

x=[]
y=[]
for i in sequences:
    x.append(i[0:3])
    y.append(i[3])
x = np.array(x)
print(x.shape)
y = np.array(y)
print(y.shape)

# y=to_categorical(y,num_classes=vocab_size)

# model = Sequential()
# model.add(Embedding(vocab_size,10,input_length=3))
# model.add(LSTM(1000))
# model.add(Dense(1000,activation='relu'))
# model.add(Dense(vocab_size,activation='softmax'))

# checkpoint = ModelCheckpoint('C:/Users/chandan/Desktop/object_detection/object_detection/smart_compose/next_words.h5',monitor='loss',verbose=1,save_best_only=True)
# model.compile(loss=tf.keras.losses.categorical_crossentropy,optimizer=Adam(learning_rate=0.001))
# model.fit(x,y,batch_size=60,epochs=100,callbacks=[checkpoint])

model = tf.keras.models.load_model('C:/Users/chandan/Desktop/object_detection/object_detection/smart_compose/next_words.h5')
tokenizer = pickle.load(open('C:/Users/chandan/Desktop/object_detection/object_detection/smart_compose/token.pkl','rb'))
def predict_next_words(model,tokenizer,text):
    sequence = tokenizer.texts_to_sequences([text])
    sequence = np.array(sequence)
    preds = np.argmax(model.predict(sequence))
    predicted_word = ""
    for key,value in tokenizer.word_index.items():
        if value==preds:
            predicted_word = key
            break

    print('predicted_word_is--->',predicted_word)
    return predicted_word

while(True):
    text=input('Enter your lines: ')

    if(text=='0'):
        print('executaion completed')
        break
    else:
        text = text.split(" ")
        text = text[-3:]
        print('text is ---->',text)

        predict_next_words(model,tokenizer,text)