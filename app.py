import streamlit as st
import pandas as pd

def load_csv(csv_file, vin_column):
    df = pd.read_csv(csv_file)
    if vin_column not in df.columns:
        st.error(f"VIN column '{vin_column}' not found in the CSV file.")
        return None
    return df

st.title('VIN Reconciliation Tool')

uploaded_file_1 = st.file_uploader("Choose the first CSV file", type='csv')
vin_column_1 = st.text_input("Enter the VIN column name for the first CSV file", value="VIN")

uploaded_file_2 = st.file_uploader("Choose the second CSV file", type='csv')
vin_column_2 = st.text_input("Enter the VIN column name for the second CSV file", value="VIN")

if uploaded_file_1 is not None and uploaded_file_2 is not None and vin_column_1 and vin_column_2:
    df1 = load_csv(uploaded_file_1, vin_column_1)
    df2 = load_csv(uploaded_file_2, vin_column_2)

    if df1 is not None and df2 is not None:
        vin_set_1 = set(df1[vin_column_1].unique())
        vin_set_2 = set(df2[vin_column_2].unique())

        unique_to_file_1 = vin_set_1 - vin_set_2
        unique_to_file_2 = vin_set_2 - vin_set_1

        st.write("VINs unique to the first CSV file:", unique_to_file_1)
        st.write("VINs unique to the second CSV file:", unique_to_file_2)
