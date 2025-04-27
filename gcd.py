import streamlit as s
c1, c2 = s.columns(2)
with c1:
    s.write("hi Ms.")
with c2:
    s.header("priyadharshini\n goto side bar")
    s.sidebar.subheader("are you lucky? select any opiton in side bar")
o=s.sidebar.selectbox("select", ["1", "2"])

if o == "1":
    with s.form("enter the details"):
        n=s.text_input("enter your luck number")
        sub=s.form_submit_button("submit pannu")
        if sub:
            st.success("u r lucky because surya is your prand")
    
elif o == "2":
     with s.form("enter the details"):
        g=s.text_input("enter your luck number")
        f=s.form_submit_button("submit pannu")
        if f:
            s.success("u r lucky because surya is your prand")

