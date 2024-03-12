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
    try:

    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"}
      # Sesuaikan URL
        content = session.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span',{'class':'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        ls = None
        bt = None
        pusat = None
        dirasakan = None



        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            i = i+1


    # print(response.status_code)
    # soup = BeautifulSoup(response.content, 'html.'parser')
    # print(soup.prettify())

    hasil = dict()
    hasil['tanggal'] = tanggal
    hasil ['waktu'] =  waktu


    hasil ['magnitudo'] =  magnitudo
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

