import requests
from bs4 import BeautifulSoup

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
})
def ekstraksi_data():
    """
    Tanggal :17 Februari 2024
    Waktu : 23:47:28 WIB
    Magnitude :4.1
    Kedalaman: 10 km
    Lokasi :8.38 LS - 114.49 BT
    Pusat gempa : berada dilaut 12 km BaratDaya Jembrana
    Dirasakan : Dirasakan (Skala MMI): III Banyuwangi, III Jembrana
    :return:
    """
    url = 'https://www.bmkg.go.id/'
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"}
    url = 'https://www.bmkg.go.id/'  # Sesuaikan URL
    response = session.get(url)

    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())

    hasil = dict()
    hasil['tanggal'] = '17 Februari 2024'
    hasil ['waktu'] =  '23:47:28 WIB'
    hasil ['magnitudo'] =  '4.1 MMI'
    hasil ['lokasi'] = {'ls':8.38, 'bt':114.49 }
    hasil['pusat'] = 'Pusat gempa berada dilaut 12 km BaratDaya Jembrana'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III Banyuwangi, III Jembrana'

    return  hasil

def tampilkan_data(result):
    print('Gempa Terakhir bedasarkan data BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi :LS= {result['lokasi']['ls']},BT= {result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")

