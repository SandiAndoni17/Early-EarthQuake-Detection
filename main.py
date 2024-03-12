'''
Newly Earthquake Detection Application
'''
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
    print(f"Dirasaekan {result['dirasakan']}")

if __name__ == '__main__':

    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)

