import streamlit as st
st.title("My Streamlit App")
st.write("Welcome to my Streamlit application! This is a simple app that demonstrates the capabilities of Streamlit for building interactive web applications with Python.")
n = st.number_input("Enter a number:", value=1,step=1)

square = n ** 2
cube =n ** 3
fifth_power = n ** 5
st.write(f"The square of {n} is {square}.")
st.write(f"The cube of {n} is {cube}.")
st.write("The fifth power of {} is {}.".format(n, fifth_power))

