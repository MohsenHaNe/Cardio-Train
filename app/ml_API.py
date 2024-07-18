from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class columns(BaseModel):
    
    age : int
    gender : int
    height : int
    weight : float
    ap_hi  : int
    ap_lo  : int
    cholesterol : int
    gluc : int
    smoke : int
    alco : int
    active : int

# load  Model

model = pickle.load(open('model.sav','rb'))

@app.post('/cardio_prediction')
def prediction(input_parameters:columns):
    
    input_data = input_parameters.json()
    input_dict = json.loads(input_data)
    
    ag = input_dict['age']
    gndr = input_dict['gender']
    hight = input_dict['height']
    wight = input_dict['weight']
    aphi = input_dict['ap_hi']
    aplo = input_dict['ap_lo']
    choles = input_dict['cholesterol']
    glc = input_dict['gluc']
    smk = input_dict['smoke']
    alc = input_dict['alco']
    actv = input_dict['active']
    
    input_list = [ag,gndr,hight,wight,aphi,aplo,choles,glc,smk,alc,actv]
    
    pred = model.predict([input_list])
    
    if pred[0] == 0:
        print('Not Cardio')
    else:
        print('Cardio')
    