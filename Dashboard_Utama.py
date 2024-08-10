import streamlit as st
import pandas as pd
import plotly.express as px

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="BUNG DANI | LUMBUNG DATA ALUMNI PIA (2021-2024)", page_icon=":mortar_board:")

#Judul aplikasi
st.title(':mortar_board: BUNG DANI')
st.caption('Lumbung Data Alumni MAS Al Irsyad (2021 - 2024)')

#Memuat data terlebih dahulu
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

#Menghitung jumlah alumni yang studi lanjut
@st.cache_data
def status_alumni(df):
  data = df.groupby(['Angkatan', 'Status'])['Nama'].count().reset_index()
  data.rename(columns={'Nama': 'Jumlah Studi Lanjut'}, inplace=True)
  data.replace(to_replace='[null]', value='Belum Mengisi', inplace=True)
  return data

#Statistik Status Angkatan
@st.cache_data
def statistik_alumni_lintas_angkatan(df):
  data = df.groupby('Angkatan')['Status'].count().reset_index()
  data['Studi Lanjut'] = df[df['Status'] == 'Studi Lanjut'].groupby('Angkatan')['Status'].count().reset_index()['Status']
  data['Lainnya'] = df[df['Status'] == 'Lainnya'].groupby('Angkatan')['Status'].count().reset_index()['Status']
  data['Belum Mengisi'] = df[df['Status'] == '[null]'].groupby('Angkatan')['Status'].count().reset_index()['Status']
  data.rename(columns={'Status': 'Total'}, inplace=True)
  data.fillna(0, inplace=True)
  data['Persentase Keterisian Tracing'] = (data['Studi Lanjut'] + data['Lainnya']) / data['Total'] * 100 
  data = data[['Angkatan', 'Studi Lanjut', 'Lainnya', 'Belum Mengisi', 'Persentase Keterisian Tracing', 'Total']]
  return data

#Soal 1: Apakah ada peningkatan angka penerimaan jumlah lulusan yang studi lanjut setiap angkatan?
@st.cache_data
def tren_jumlah_studi_lanjut(df):
  data = df[df['Status'] == 'Studi Lanjut'].groupby('Angkatan')['Nama'].count().reset_index()
  data.rename(columns={'Nama': 'Jumlah Studi Lanjut'}, inplace=True)
  return data

#Soal 2: Bagaimana tren setiap angkatan pada memilih kategori kampus (negeri, swasta)?
@st.cache_data
def tren_kategori_kampus(df):
  data = df[(df['Kategori'] != '-') & (df['Kategori'] != '[null]')].groupby(['Angkatan', 'Kategori'])['Nama'].count().reset_index()
  data.rename(columns={'Nama': 'Jumlah Alumni'}, inplace=True)
  return data

#Soal 3: Bagaimana tren ranah kuliah (umum atau agama) yang diambil pada setiap angkatan?
@st.cache_data
def tren_ranah_kuliah(df):
  data = df[(df['Ranah'] != '[null]') & (df['Ranah'] != '[unknown]') & (df['Ranah'] != '-')].groupby(['Angkatan', 'Ranah'])['Nama'].count().reset_index()
  data.rename(columns={'Nama': 'Jumlah Alumni'}, inplace=True)
  return data

#Soal 4: Bagaimana tren peningkatan penerimaan berdasarkan jalur masuk (snbp, snbt, mandiri) pada setiap angkatan?
@st.cache_data
def tren_jalur_penerimaan(df):
  data = df[(df['Jalur Penerimaan'] != '[null]') & (df['Jalur Penerimaan'] != '-')].groupby(['Angkatan', 'Jalur Penerimaan'])['Nama'].count().reset_index()
  data.rename(columns={'Nama': 'Jumlah Alumni'}, inplace=True)
  return data

#Soal 5: Apa saja jenjang yang diambil oleh kebanyakan alumni? sarjana kah atau diploma?
@st.cache_data
def distribusi_jenjang_studi(df):
  data = df[(df['Jenjang'] != '[null]') & (df['Jenjang'] != '-')].groupby(['Jenjang', 'Angkatan'])['Nama'].count().reset_index()
  data.rename(columns={'Nama': 'Jumlah Alumni'}, inplace=True)
  return data

#Soal 6: Berapa banyak alumni yang mendapatkan beasiswa? (Lintas Angkatan)
@st.cache_data
def jumlah_alumni_beasiswa(df):
  data = df[(df['Status'] == 'Studi Lanjut')].groupby('Beasiswa')['Nama'].count().reset_index()
  data.rename(columns={'Nama': 'Jumlah Alumni'}, inplace=True)
  # data['Beasiswa'].replace(to_replace='[null]', value='Belum Mengisi', inplace=True)
  # data['Beasiswa'].replace(to_replace='-', value='Bekerja', inplace=True)
  data['Beasiswa'].replace(to_replace='[unknown]', value='Tidak mencantumkan data', inplace=True)
  return data

#Soal 7: Berapa banyak alumni yang mendapatkan beasiswa? (Per Angkatan)
@st.cache_data
def jumlah_alumni_beasiswa_per_angkatan(df):
#   data = df[(df['Status'] == 'Studi Lanjut') & (df['Angkatan'] == angkatan)].groupby(['Beasiswa'])['Nama'].count().reset_index()
#   data.rename(columns={'Nama': 'Jumlah Alumni'}, inplace=True)
#   data['Beasiswa'].replace(to_replace="[unknown]", value="Tidak mencantumkan data")
#   return data
  data = df[(df['Status'] == 'Studi Lanjut')].groupby(['Beasiswa', 'Angkatan'])['Nama'].count().reset_index()
  data.rename(columns={'Nama': 'Jumlah Alumni'}, inplace=True)
  data['Beasiswa'].replace(to_replace="[unknown]", value="Tidak mencantumkan data")
  return data

#Soal 8: Siapa saja yang mendapatkan beasiswa?


#Soal 9: Apa univ yang banyak diambil pada lintas angkatan?
@st.cache_data
def jumlah_alumni_per_universitas_dan_angkatan(df):
  data = df[df['Status'] == 'Studi Lanjut'].groupby(['Universitas', 'Angkatan'])['Nama'].count().reset_index()
  data.rename(columns={'Nama': 'Jumlah Alumni'}, inplace=True)
  data.replace(to_replace='[null]', value='Belum Mengisi', inplace=True)
  return data

#Soal 10: Jurusan apa yang terdapat banyak alumni di sana?
@st.cache_data
def jumlah_alumni_per_jurusan_dan_angkatan(df):
  data = df[df['Status'] == 'Studi Lanjut'].groupby(['Jurusan', 'Angkatan'])['Nama'].count().reset_index()
  data.rename(columns={'Nama': 'Jumlah Alumni'}, inplace=True)
  data.replace(to_replace='[null]', value='Belum Mengisi', inplace=True)
  return data

#Pertanyaan 11: Kota mana yang banyak menjadi sasaran alumni?
@st.cache_data
def jumlah_alumni_per_kota_dan_angkatan(df):
  data = df[(df['Status'] == 'Studi Lanjut')].groupby(['Kota/Negara', 'Angkatan'])['Nama'].count().reset_index()
  data.rename(columns={'Nama': 'Jumlah Alumni'}, inplace=True)
  data.replace(to_replace='[null]', value='Belum Mengisi', inplace=True)
  return data

df = load_data("https://docs.google.com/spreadsheets/d/1Qctp9yKzecR4KGKTYsiKGZW2YOABkyZcMDzzpnS45vQ/export?format=csv&gid=944201584")

col1, col2 = st.columns(2)
with col1:
  st.header("Sekilas Tentang Portal")
  st.markdown('''
    Portal ini digunakan untuk melihat statistik dan pemetaan alumni mulai angkatan 30 (Alqatras - 2020/2021) sampai 33 (Manzigard - 2023-2024). Adapun fitur yang dapat digunakan masih terbatas pada:
    - Melihat ringkasan statistik berdasarkan:
      - [Peningkatan Alumni Studi Lanjut](#peningkatan-jumlah-studi-lanjut-tiap-angkatan)
      - [Jenjang Kuliah](#apa-kebanyakan-jenjang-yang-mereka-ambil)
      - [Kategori Kampus](#bagaimana-sebaran-alumni-berdasarkan-kategori-kampus)
      - [Jalur Penerimaan](#apa-jalur-penerimaan-yang-mereka-gunakan)
      - [Kampus yang Diminati](#bagaimana-sebaran-alumni-berdasarkan-kategori-kampus)
      - [Jurusan yang Diminati](#mana-sasaran-jurusan-kebanyakan-alumni)
      - [Ranah Peminatan](#apa-ranah-peminatan-yang-alumni-minati)
      - [Kota / Negara](#mana-kota-yang-banyak-tersebar-alumni)
      - [Penerima Beasiswa](#bagaimana-presentase-alumni-yang-mendapat-beasiswa)
    - Ringkasan statistik ini disusun berdasarkan angkatan atau lintas angkatan. Jika Anda ingin melihat data alumni secara lebih detail, silakan gunakan fitur [Filter Data Alumni](Filter_Data_Alumni) atau menu yang tersedia di sidebar.
  ''')
with col2:
  st.header("Cara Pemakaian")
  st.markdown('''
  Fitur:
    - **Melihat jumlah masing-masing data:** Letakkan kursor Anda di atas garis/kota grafik
    - **Urutkan berdasarkan kolom (pada tabel):** Tekan bagian header kolom beberapa kali dan lihat perubahannya. Sesuaikan dengan kebutuhan Anda.
    - **Fitur Full Screen, Pencarian, dan Unduh Data:** Letakkan kursor Anda pada bagian atas tabel. Klik berdasarkan kebutuhan Anda. 
  
  ### Kritik, Saran, Laporan Masalah
  Jika Anda menemukan kritik, saran, atau masalah, jangan sungkan untuk menghubungi kami melalui Whatsapp [Developer](https://wa.me/628779897434).
  ''')

st.header('Disclaimer Akurasi Data')
soal0 = statistik_alumni_lintas_angkatan(df)
# soal0
# Buat kolom baru untuk menampilkan progress bar sebagai teks
soal0["Progress Bar"] = soal0["Persentase Keterisian Tracing"].apply(
    lambda x: f"[{'█' * int(x/10)}{'░' * int((100-x)/10)}] {x}%"
)

# Tampilkan DataFrame dengan kolom "Progress Bar"
st.dataframe(soal0, hide_index=False)
st.text("Data terakhir diupdate pada 2023")
st.divider()

col1, col2 = st.columns(2)
with col1:
#Jawaban soal 1
  st.subheader('Peningkatan Jumlah Studi Lanjut Tiap Angkatan')
  soal1 = tren_jumlah_studi_lanjut(df)
  st.line_chart(data=soal1, x="Angkatan", y="Jumlah Studi Lanjut")

with col2:
#Jawaban Soal 5
  st.subheader('Apa Kebanyakan Jenjang yang Mereka Ambil?')
  def distribusi_jenjang_studi_chart():
    soal5 = distribusi_jenjang_studi(df)
    heatmap_data = soal5.pivot_table(index='Angkatan', columns='Jenjang', values='Jumlah Alumni', fill_value=0)
    fig = px.imshow(heatmap_data)
    st.plotly_chart(fig)

  distribusi_jenjang_studi_chart()

col1, col2 = st.columns(2)
with col1:
  st.subheader("Bagaimana Sebaran Alumni Berdasarkan Kategori Kampus?")
  #Jawaban Soal 2
  @st.cache_data
  def tren_kategori_kampus_chart():
      soal2 = tren_kategori_kampus(df)
      heatmap_data = soal2.pivot_table(index='Angkatan', columns='Kategori', values='Jumlah Alumni', fill_value=0)

      fig = px.imshow(heatmap_data)
      st.plotly_chart(fig)

  tren_kategori_kampus_chart()

with col2:
  st.subheader("Apa Jalur Penerimaan yang Mereka Gunakan?")
  #Jawaban Soal 4
  def tren_jalur_penerimaan_chart():
      soal4 = tren_jalur_penerimaan(df)
      heatmap_data = soal4.pivot_table(index='Angkatan', columns='Jalur Penerimaan', values='Jumlah Alumni', fill_value=0)
      fig = px.imshow(heatmap_data)
      st.plotly_chart(fig)

  tren_jalur_penerimaan_chart()

col1, col2 = st.columns(2)
with col1:
  st.subheader('Mana Sasaran Kampus Kebanyakan Alumni?')
  #Jawaban Soal 9
  jumlah_alumni_per_univ = jumlah_alumni_per_universitas_dan_angkatan(df)
  univ_terpopuler = jumlah_alumni_per_univ.pivot_table(index='Universitas', columns='Angkatan', values='Jumlah Alumni', fill_value=0)
  univ_terpopuler['Lintas Angkatan'] = univ_terpopuler.sum(axis=1)
  univ_terpopuler = univ_terpopuler.sort_values('Lintas Angkatan', ascending=False)
  univ_terpopuler

with col2:
  st.subheader('Mana Sasaran Jurusan Kebanyakan Alumni?')
  #Jawaban Soal 10
  jumlah_alumni_per_jurusan = jumlah_alumni_per_jurusan_dan_angkatan(df)
  jurusan_terpopuler = jumlah_alumni_per_jurusan.pivot_table(index='Jurusan', columns='Angkatan', values='Jumlah Alumni', fill_value=0)
  jurusan_terpopuler['Lintas Angkatan'] = jurusan_terpopuler.sum(axis=1)
  jurusan_terpopuler = jurusan_terpopuler.sort_values('Lintas Angkatan', ascending=False)
  jurusan_terpopuler

st.subheader("Apa ranah peminatan yang alumni minati?")
#Jawaban Soal 3
@st.cache_data
def tren_ranah_kuliah_chart():
    soal3 = tren_ranah_kuliah(df)
    heatmap_data = soal3.pivot_table(index='Angkatan', columns='Ranah', values='Jumlah Alumni', fill_value=0)

    fig = px.imshow(heatmap_data)
    st.plotly_chart(fig)

tren_ranah_kuliah_chart()


st.subheader('Mana Kota yang Banyak Tersebar Alumni?')
#Jawaban Soal 10
jumlah_alumni_per_kota = jumlah_alumni_per_kota_dan_angkatan(df)
kota_terpopuler = jumlah_alumni_per_kota.pivot_table(index='Kota/Negara', columns='Angkatan', values='Jumlah Alumni', fill_value=0)
kota_terpopuler['Lintas Angkatan'] = kota_terpopuler.sum(axis=1)
kota_terpopuler = kota_terpopuler.sort_values('Lintas Angkatan', ascending=False)
kota_terpopuler

col1, col2 = st.columns(2)
with col1:
  st.subheader('Bagaimana Presentase Alumni yang Mendapat Beasiswa?')
  #Jawaban Soal 6
  def jumlah_alumni_beasiswa_chart():
      soal6 = jumlah_alumni_beasiswa(df)

      fig = px.pie(soal6, values="Jumlah Alumni", names="Beasiswa")
      st.plotly_chart(fig)

  jumlah_alumni_beasiswa_chart()

with col2:
  st.subheader('Berapa Jumlah Penerima Beasiswa Setiap Angkatan?')
  #Jawaban Soal 7
  jumlah_alumni_beasiswa_per_angkatan = jumlah_alumni_beasiswa_per_angkatan(df)
  jumlah_alumni_beasiswa_tabel = jumlah_alumni_beasiswa_per_angkatan.pivot_table(index='Beasiswa', columns='Angkatan', values='Jumlah Alumni', fill_value=0)
  jumlah_alumni_beasiswa_tabel['Lintas Angkatan'] = jumlah_alumni_beasiswa_tabel.sum(axis=1)
  jumlah_alumni_beasiswa_tabel = jumlah_alumni_beasiswa_tabel.sort_values('Lintas Angkatan', ascending=False)
  jumlah_alumni_beasiswa_tabel

#Jawaban Soal 8



#Jawaban Soal 11
