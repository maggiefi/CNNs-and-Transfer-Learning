import streamlit as st

def local_css(file):
	with open(file) as f:
		st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

