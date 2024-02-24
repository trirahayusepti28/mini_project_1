import os
os.system("cls")

print('''
+==================================================================================================+
|                                   SISTEM PEMINJAMAN BARANG                                       |
+==================================================================================================+
''')

class InventarisBarang:
    def __init__(self):
        self.inventaris_barang = {}

    def tambah_barang(self, id_barang, nama_barang, jumlah, kondisi, lokasi, nama_pemilik):
        if id_barang not in self.inventaris_barang:
            self.inventaris_barang[id_barang] = {
                'id_barang': id_barang,
                'nama_barang': nama_barang,
                'jumlah': jumlah,
                'kondisi': kondisi,
                'lokasi': lokasi,
                'nama_pemilik': nama_pemilik
            }
            print("-- Barang berhasil ditambahkan --")
        else:
            print("ID barang sudah ada.")

    def tampilkan_semua_barang(self):
        if self.inventaris_barang:
            print("\nDaftar Barang:")
            print("+=======+======================+===========+====================+======================+======================+")
            print("| ID    | Nama Barang          | Jumlah    |      Kondisi       |        Lokasi        |     Nama Pemilik    |")
            print("+=======+======================+===========+====================+======================+======================+")
            for id_barang, detail_barang in self.inventaris_barang.items():
                print(f"| {id_barang:<5} | {detail_barang['nama_barang']:<20} | {detail_barang['jumlah']:<9} | {detail_barang['kondisi']:<18} | {detail_barang['lokasi']:<20} | {detail_barang['nama_pemilik']:<20} |")
            print("+=======+======================+===========+====================+======================+======================+")
        else:
            print("-- Inventaris barang kosong --.")

    def cari_barang(self, id_barang):
        if id_barang in self.inventaris_barang:
            detail_barang = self.inventaris_barang[id_barang]
            print(f"\nBarang dengan ID {id_barang} ditemukan:")
            print("+=======+======================+===========+====================+======================+======================+")
            print("| ID    | Nama Barang          | Jumlah    |      Kondisi       |        Lokasi        |     Nama Pemilik    |")
            print("+=======+======================+===========+====================+======================+======================+")
            print(f"| {detail_barang['id_barang']:<5} | {detail_barang['nama_barang']:<20} | {detail_barang['jumlah']:<9} | {detail_barang['kondisi']:<18} | {detail_barang['lokasi']:<20} | {detail_barang['nama_pemilik']:<20} |")
            print("+=======+======================+===========+====================+======================+======================+")
            return detail_barang
        else:
            print(f"Barang dengan ID {id_barang} tidak ditemukan.")
            return None

    def update_barang(self, id_barang, field, value, nama_pemilik=None):
        if id_barang in self.inventaris_barang:
            if field in self.inventaris_barang[id_barang]:
                if field == 'nama_pemilik':
                    self.inventaris_barang[id_barang][field] = value
                    print("-- Data pemilik barang berhasil diperbarui --.")
                else:
                    self.inventaris_barang[id_barang][field] = value
                    print("-- Data barang berhasil diperbarui --.")
            else:
                print("-- Field yang dimasukkan tidak valid --.")
        else:
            print("-- Tidak ada barang dengan ID tersebut --")

    def hapus_barang(self, id_barang):
        if id_barang in self.inventaris_barang:
            del self.inventaris_barang[id_barang]
            print("-- Barang berhasil dihapus dari inventaris --")
        else:
            print("-- Tidak ada barang dengan ID tersebut --")


# Fungsi main untuk menjalankan program
def main():
    inventaris = InventarisBarang()

    while True:
        print("\n=== Sistem Peminjaman Barang ===")
        print("1. Tambah Barang")
        print("2. Tampilkan Semua Barang")
        print("3. Cari Barang")
        print("4. Update Barang")
        print("5. Hapus Barang")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")

        if pilihan == "1":
            while True:
                id_barang = input("Masukkan ID Barang (harus angka): ")
                if not id_barang.isdigit():
                    print("ID Barang harus berupa angka.")
                else:
                    break  # Keluar dari loop saat ID barang sesuai

            nama_barang = input("Masukkan Nama Barang: ")
            while True:
                jumlah = input("Masukkan Jumlah: ")
                if not jumlah.isdigit():
                    print("Jumlah harus berupa angka.")
                else:
                    jumlah = int(jumlah)
                    break  # Keluar dari loop saat jumlah sesuai

            kondisi = input("Masukkan Kondisi: ")
            lokasi = input("Masukkan Lokasi: ")
            nama_pemilik = input("Masukkan Nama Pemilik Barang: ")  

            inventaris.tambah_barang(id_barang, nama_barang, jumlah, kondisi, lokasi, nama_pemilik)  

        elif pilihan == "2":
            inventaris.tampilkan_semua_barang()

        elif pilihan == "3":
            id_barang = input("Masukkan ID Barang yang ingin dicari: ")
            inventaris.cari_barang(id_barang)

        elif pilihan == "4":
            id_barang = input("Masukkan ID Barang yang ingin diperbarui: ")
            field = input("Masukkan field yang ingin diperbarui (nama_barang/jumlah/kondisi/lokasi/nama_pemilik): ")
            value = input("Masukkan nilai baru: ")
            inventaris.update_barang(id_barang, field, value)

        elif pilihan == "5":
            id_barang = input("Masukkan ID Barang yang ingin dihapus: ")
            inventaris.hapus_barang(id_barang)

        elif pilihan == "6":
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


# Menjalankan program utama
if __name__ == "__main__":
    main()