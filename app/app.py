import streamlit as st
import pickle

# import Model
model = pickle.load(open('Model.pkl','rb'))


# create app
def main():
  st.header('Cardio prediction')
  # inputs
  age = st.slider('input your Age',0,65)
  gender = st.slider('what is your gender',1,2)
  height = st.slider('Enter your height',0,250)
  weight = st.slider('Enter your weight',0.0,300.0)
  ap_hi = st.slider('Enter your ap_hi',0,160200)
  ap_lo = st.slider('Enter your ap_lo',0,110000)
  cholesterol = st.slider('Enter your cholesterol',0,5)
  gluc = st.slider('gluc؟',0,3)
  smoke = st.slider('Do you Smoke?',0,1)
  alco = st.slider('Do you have alchohol ? ',0,1)
  active = st.slider('Are you activate?',0,1)

  inputs = [[age,gender,height,weight,gender,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active]]

  if st.button('Predict'):
    res = model.predict(inputs)
    if res[0] == 0 :
      print('Not Cardio')
    else : 
      print(' Cardio')
    


# run app
if __name__ == "__main__": # --> streamlit run app.py
  main()


