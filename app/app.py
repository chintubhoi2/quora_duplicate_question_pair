import streamlit as st
import helper
import pickle

model = pickle.load(open(r'C:\Users\bhoic\OneDrive\Desktop\quora\model.pkl','rb'))
scaler = pickle.load(open(r'C:\Users\bhoic\OneDrive\Desktop\quora\scaler.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    query = scaler.transform(query)
    result = model.predict(query)[0]
    print(result)
    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicat')