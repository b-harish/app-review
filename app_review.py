import streamlit as st
import pandas as pd
from utils import *
from authenticate import *

st.title('App Review Analyzer')


uploaded_file = None
if check_password():
    # Ref: https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
    st.subheader('Upload Reviews')
    uploaded_file = st.file_uploader('Choose file containing app reviews')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, index_col='ID')

    st.subheader('Reviews uploaded!')
    # display 10% of records by default
    default_rows = int(df.shape[0] * 0.1)
    num_rows = st.slider('Number of reviews to display?', 0, df.shape[0], default_rows)
    st.write(df.iloc[0:num_rows])

    records = get_contradicting_app_reviews(df, 'Text', 'Star')
    
    st.subheader('Result')
    st.subheader(f'{records.shape[0]} contradicting reviews found!')

    default_rows = int(records.shape[0] * 0.1)
    num_rows = st.slider('Number of contradicting reviews to display?', 0, records.shape[0], default_rows)
    st.write(records.iloc[0:num_rows])