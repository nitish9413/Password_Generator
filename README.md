# Password_Generator

## [Try](https://nitish9413-password-generator-password-gen-e9dids.streamlitapp.com/)

### Modules Used
1. Random
2. String
3. Streamlit

___

## Code
### Import Required Modules 
```Python
import random
import string
import streamlit as st
```

### Create a function pwd_gen() which will generate a Password

#### In char , We have stored lowercase and uppercase letters along with numbers and symbols. this function takes length as input paramter
```Python
char=list(string.ascii_uppercase+string.ascii_lowercase+string.digits+"!@#$%^&*()")

def pwd_gen(l):
    random.shuffle(char)
    temp=random.sample(char,l)
    return ''.join(temp)
```
___

## UI part
#### We are going to create basic UI for our application

```Python
st.title('Password Generator')
```
#### Now we need Length of the password as input from User for that we have created slider ( Min. length 8 & Max. 32) stored input in variable l

```Python
l=st.slider('Pick a length of password', 8, 32)
```

#### Now Display the Generated Password

```Python
st.header('Genrated Password :')
st.text(pwd_gen(l))
```
___

#UI:
![alt text](https://github.com/nitish9413/Password_Generator/blob/main/UI.png "Application UI")
___

# How to use

#### Clone this repo

```Python
git clone https://github.com/nitish9413/Password_Generator.git
cd Password_Generator
```

#### Run below command in terminal
```Python
streamlit run password_gen.py
```

