import streamlit as st
num1= st.number_input("Input First Number")
num2= st.number_input("Input Second Number")
def LCM(a,b):
    greater=max(a,b)
    while(True):
        if(greater % int(a)==0 and greater % int(b)==0):
            lcm = greater
            break
        greater = greater +1
    return lcm    

ans=0
if st.button("Submit"):
    ans=LCM(num1,num2)
st.write("LCM :",ans)