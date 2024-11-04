''' parktek dasar pemograman '''
import datetime
date = datetime.datetime.now()
menu_kopi = {
    'AR': {'name': 'Americano', 'harga': 15000},
    'CP': {'name': 'Cappucino', 'harga': 20000},
    'ES': {'name': 'Espresso', 'harga': 25000},
}

order_list = []
print("=" *40)
print("=========== MENU COFFEE CUY ============")
print("=" *40)
print(f"{'Kode':<10}{'Nama':<18}{'Harga'}")

for i, item in menu_kopi.items():
    print(f"{i:<9}|{item['name']:<17}|Rp {item['harga']}")
print("")
# # proses
nama = input('pesanan atas nama siapa: ')
banyak = int(input("Jumlah varian menu : "))
for i in range(banyak):
    print(f"Cup -", i+1)
    order_user = input("Masukan Kode Menu : ").upper()
    if order_user in menu_kopi:
        qty = int(input("Masukan Jumlah : "))
        total = qty * menu_kopi[order_user]['harga']
        order_list.append([menu_kopi[order_user]['name'], qty, menu_kopi[order_user]['harga'], total])
        print("")
    else:
        print("Maaf, menu yang anda pilih tidak tersedia")

print("=" *41)
print("=========== STRUK PEMBAYARAN ============")
print(f"Nama Pembeli :{nama}" )
print(f"Tanggal      :{date.day}/{date.month}/{date.year}")
print("=" *41)
print(f"{'No':<5}{'Kode':<21}{'Menu':<10}{'Harga'}")
for i, item in enumerate(order_list):
    print(f"{i+1:<5}{item[0]:<21}{item[1]:<10}{item[2]}")
print("=" *41)
total = sum([item[3] for item in order_list])
pajak = total * 0.1
harga_bayar = total + pajak
print(f"Pajak : Rp {int(pajak)}")
print(f"Total : Rp {int(harga_bayar)}")
bayar = int(input("uang bayar: Rp "))
kembalian = bayar - harga_bayar
print(f"kembalian: Rp {int(kembalian)}")
