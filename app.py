
import streamlit as st
import pandas as pd
import plotly.express as px

# Homepage
st.title('Selamat Datang di Program Affiliate "Investasi Dini"')
st.markdown('**Mulai menghasilkan dengan menjadi affiliate kami dan bantu orang lain belajar tentang investasi dini!**')
st.write('Bergabung dengan program affiliate kami dan dapatkan komisi untuk setiap penjualan eBook yang kamu referensikan.')
st.image('image/landing-page-image.png', use_column_width=True)

if st.button('Daftar Sebagai Affiliate'):
    st.write('Silahkan daftar dengan mengisi form pendaftaran.')

# Registrasi form
def show_signup_form():
    with st.form(key='signup_form'):
        username = st.text_input('Nama Pengguna')
        email = st.text_input('Email')
        password = st.text_input('Kata Sandi', type='password')
        submit_button = st.form_submit_button('Daftar')
        
        if submit_button:
            st.write(f'Pendaftaran berhasil untuk {username}!')

show_signup_form()

# Sample data for affiliate dashboard
data = {
    'Tanggal': ['2025-05-01', '2025-05-02', '2025-05-03'],
    'Jumlah Terjual': [10, 15, 20],
    'Komisi': [150000, 225000, 300000]
}

df = pd.DataFrame(data)

# Display the data table
st.write('Statistik Penjualan Anda:')
st.dataframe(df)

# Sales graph
fig = px.line(df, x='Tanggal', y='Jumlah Terjual', title='Grafik Penjualan Affiliate')
st.plotly_chart(fig)

# Commission graph
fig2 = px.bar(df, x='Tanggal', y='Komisi', title='Grafik Komisi Affiliate')
st.plotly_chart(fig2)

# Affiliate link
affiliate_link = "https://example.com/affiliate/uniqueID"
st.write('Bagikan link unik Anda untuk mulai menjual eBook:')
st.write(f'[Link Anda: {affiliate_link}](#)')
