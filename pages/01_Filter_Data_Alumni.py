import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_dynamic_filters import DynamicFilters

st.set_page_config(layout="wide")
# Judul aplikasi
st.title('🔎 Filter Data Alumni')
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://docs.google.com/spreadsheets/d/1Qctp9yKzecR4KGKTYsiKGZW2YOABkyZcMDzzpnS45vQ/export?format=csv&gid=944201584")


# filter_angkatan = st.multiselect('Angkatan', df['Angkatan'].unique())

# df = df.sort_values(['Angkatan', 'Nama'], ascending=[True, True]).reset_index()
df = df[['Nama', 'Angkatan',	'Status', 'Kategori', 'Umum/Agama',	'Tahun Masuk',	'Kota/Negara',	'Universitas',	'Jurusan',	'Ranah',	'Jenjang',	'Jalur Penerimaan',	'Beasiswa']]
df['Angkatan'] = df['Angkatan'].astype(str)
df['Tahun Masuk'] = df['Tahun Masuk'].astype(str)

dynamic_filters = DynamicFilters(df, filters=['Angkatan', 'Status', 'Umum/Agama', 'Tahun Masuk', 'Kota/Negara', 'Universitas', 'Jurusan', 'Ranah', 'Jenjang', 'Jalur Penerimaan', 'Beasiswa'], filters_name="my_filters")

# with st.sidebar:
#     st.header('Filter data alumni:')
#     dynamic_filters.display_filters()
st.subheader("Lakukan filter data")

with st.expander("Tampilkan opsi filter"):
    dynamic_filters.display_filters(location='columns', num_columns=3)
st.divider()
st.subheader("Data Alumni")
new_df = dynamic_filters.filter_df()
new_df