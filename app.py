
import streamlit as st
import joblib
model=joblib.load('spam-ham')
st.title('spam ham classifier')
ip=st.text_input('enter the message')
op=model.predict([ip])
if st.button('predict'):
  st.title(op[0])
