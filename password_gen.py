import streamlit as st
import pandas as pd
import numpy as np
import  random
import string

char=list(string.ascii_uppercase+string.ascii_lowercase+string.digits+"!@#$%^&*()")

def pwd_gen(l):
    
    random.shuffle(char)

    temp=random.sample(char,l)

    #random.shuffle(temp)

    return ''.join(temp)


st.title('Password Genrator')
l=st.slider('Pick a length of password', 8, 32)
st.header('Genrated Password :')
st.text(pwd_gen(l))
