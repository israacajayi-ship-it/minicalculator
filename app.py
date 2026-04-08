import streamlit as st

st.title("simple addition app")
# st.write("my favourite game")
# st.write("my favourite verse")
# st.write("my favourite app")

num1=st.number_input("enter first number")
num2=st.number_input("enter second number")


if st.button("Add"):
    result=num1+num2
    st.write("Answer:", result) 








