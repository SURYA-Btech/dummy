import streamlit as s
from PIL import Image
c1, c2 = s.columns(2)
with c1:
    s.write("hi Ms.")
    i=Image.open("p.png")
    s.image(i,use_container_width=True)
with c2:
    s.header("priyadharshini\n goto side bar")
    s.sidebar.subheader("are you lucky? select any opiton in side bar")
o=s.sidebar.selectbox("select", ["1", "2"])

if o == "1":
    with s.form("enter the details"):
        n=s.text_input("enter your luck number")
        sub=s.form_submit_button("submit pannu")
        if sub:
            s.success("u r lucky because surya is your prand")
    
elif o == "2":
     with s.form("enter the details"):
        g=s.text_input("enter your luck number")
        f=s.form_submit_button("submit pannu")
        if f:
            s.success("u r lucky because surya is your prand")

