import streamlit as st
import pandas as pd
import os

st.title("User Information Form")

# Input fields
name = st.text_input("Enter your name:")
father = st.text_input("Enter your father's name:")
address = st.text_area("Enter your permanent address:")
mobile = st.number_input("Enter mobile number:", step=1, format="%d")
email = st.text_input("Enter your email:")

# Submit button
if st.button("Submit"):
    st.subheader("Your Details:")
    st.markdown(f"*Name:* {name}")
    st.markdown(f"*Father's Name:* {father}")
    st.markdown(f"*Address:* {address}")
    st.markdown(f"*Mobile Number:* {mobile}")
    st.markdown(f"*Email:* {email}")

    # Save to CSV
    data = {
        "Name": [name],
        "Father's Name": [father],
        "Address": [address],
        "Mobile": [mobile],
        "Email": [email]
    }

    df = pd.DataFrame(data)

    if os.path.exists("form_data.csv"):
        df.to_csv("form_data.csv", mode='a', header=False, index=False)
    else:
        df.to_csv("form_data.csv", index=False)

    st.success("Your data has been saved successfully!")
    