# vsc_rebuttal_trainer.py

import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="VSC Rebuttal Trainer", layout="centered")
df = pd.read_csv("vsc_rebuttals.csv")

st.title("🚘 VSC Objection Rebuttal Trainer")
st.write("Flip through real objections and proven rebuttals. Tap to reveal.")

if "index" not in st.session_state:
    st.session_state.index = random.randint(0, len(df) - 1)

if st.button("🔄 New Objection"):
    st.session_state.index = random.randint(0, len(df) - 1)

card = df.iloc[st.session_state.index]

st.subheader("❗ Objection:")
st.markdown(f"**{card['Objection']}**")

if st.button("🎯 Show Rebuttal"):
    st.success(card['Rebuttal'])

st.markdown("---")
st.caption("Powered by AI + Streamlit. Built for closers.")
