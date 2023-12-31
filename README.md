# kelompok-4
Kelompok 4 - Studi Kasus Pembelian Tiket Bioskop
LAPORAN
PENERAPAN GUI PADA OOP: PEMBELIAH TIKET BIOSKOP

ANGGOTA KELOMPOK 4:
Afrizal tuasikal 		: 5220411262
Auxylium B.E. Bunga 	: 5220411260
Didi Wahidi 			: 5190411142
Didik sukma putra 		: 5220411270
Raisul Gibran 		: 5220411251



KELAS E
PRODI INFORMATIKA
FAKULTAS SAINS DAN TEKNOLOGI
UNIVERSITAS TEKNOLOGI YOGYAKARTA
2023/2024
KATA PENGANTAR

Puji syukur kami panjatkan kepada Tuhan Yang Maha Esa, karena atas limpahan rahmatnya penyusun dapat menyelesaikan makalah ini tepat waktu tanpa ada halangan yang berarti dan sesuai dengan harapan.
Ucapan terima kasih kami sampaikan kepada ibu Irma Handayani, S.Kom., M.Cs., sebagai dosen pengampu mata kuliah Pengembanggan Berorientasi Objek Praktik dan terimakasi kepada asisten dosen yang telah memberikan arahan dan pemahaman dalam menyusun makalah ini.
Kami menyadari bahwa dalam penyusunan makalah ini masih banyak kekurangan karena keterbatasan kami. Maka dari itu penyusun sangat mengharapkan kritik dan saran untuk menyempurnakan makalah ini. Semoga apa yang ditulis dapat bermanfaat bagi semua pihak yang membutuhkan. 
 
DAFTAR ISI

KATA PENGANTAR	ii
DAFTAR ISI	iii
BAB I PENDAHULUAN	1
1.1.	Latar Belakang	1
1.2.	Rumus Masalah	1
1.3.	Tujuan	1
BAB II DASAR TEORI	2
2.1.	GUI	2
BAB III PEMBAHASAAN	3
3.1.	SOURS CODE	3
3.2.	Fitur-fitur	6
3.2.2.	Pemilihan calendar	7
3.2.3.	Pemilihan Film	8
3.2.4.	Penyimpanan Data	8
3.2.5.	 Melihat Data Pembeli	8
3.2.6.	 Perhitungan Total Penjualan	9
3.2.7.	Message Box	9
BAB IV PENUTUP	10
4.1.	Kesimpulan	10
 

 
BAB I
PENDAHULUAN
1.1.	Latar Belakang
Dalam era digital seperti saat ini, pemesanan tiket bioskop dapat dilakukan dengan mudah melalui aplikasi berbasis GUI. Aplikasi ini memungkinkan pengguna untuk memilih film yang ingin ditonton dan memilih jadwal yang tersedia, serta melakukan pembayaran tiket secara online. Oleh karena itu, kami membuat laporan ini untuk membahas tentang GUI pemesanan tiket bioskop yang dapat membantu pengguna dalam melakukan pemesanan tiket secara mudah dan efisien. Dalam laporan ini, kami akan membahas tentang fitur-fitur yang harus ada dalam GUI pemesanan tiket bioskop, perancangan sistem informasi, desain grafis, dan pengembangan aplikasi. Semoga laporan ini dapat memberikan informasi yang bermanfaat bagi pembaca.
Pengembangan aplikasi pemesanan tiket bioskop juga melibatkan penggunaan teknologi terkini, seperti Python dan tkinter, untuk membuat aplikasi yang efisien dan mudah dikelola. Hal ini mencakup perancangan sistem informasi, desain grafis, dan pengembangan aplikasi, yang menciptakan aplikasi yang dapat dijalankan melalui platform seperti Colab. Dengan demikian, aplikasi ini dapat diperkenalkan untuk berbagai platform, termasuk perangkat seluler, memudahkan pengguna dalam melakukan pemesanan tiket bioskop secara digital.

1.2.	Rumus Masalah
-	Menambahkan validasi input pada form pembeli, seperti memastikan bahwa umur dan nomor kontak yang dimasukkan adalah angka.
-	Menambahkan fitur untuk menghitung total penjualan berdasarkan film yang dibeli.

1.3.	Tujuan
-	Tujuan dari pengembangan GUI pemesanan tiket bioskop adalah untuk memberikan pengalaman pengguna yang mudah dan efisien.


 
BAB II
DASAR TEORI

2.1.	GUI
GUI (Graphical User Interface), adalah antarmuka pada sistem operasi atau komputer yang menggunakan menu grafis agar mempermudah para pengguna-nya untuk berinteraksi dengan komputer atau sistem operasi.
Jadi, GUI merupakan antarmuka pada sistem operasi komputer yang menggunakan menu grafis. Menu grafis ini maksudnya terdapat tampilan yang lebih ditekankan untuk membuat sistem operasi yang user-friendly agar para pengguna lebih nyaman menggunakan komputer. Menu grafis adalah grafis-grafis atau gambar-gambar dan tampilan yang tujuannya untuk memudahkan para pengguna menggunakan sistem operasi. Kelebihan/keutamaan dan kekurangan dari GUI:

Kelebihan GUI:
1.	Desain Grafis lebih menarik.
2.	GUI memungkinkan user untuk berinteraksi dengan komputer secara lebih baik.
3.	Memudahkan pengguna. 
4.	Menarik minat pengguna.
5.	Resolusi gambar yang tinggi.
Kekurangan GUI :
1.	Memakan memory yang sangat besar. 
2.	Bergantung pada perangkat keras.
3.	Membutuhkan banyak tempat pada layar komputer.
4.	Tidak fleksibel.
GUI pemesanan tiket bioskop merupakan aplikasi berbasis antarmuka grafis yang memungkinkan pengguna untuk memilih film, jadwal, kursi, serta melakukan pembayaran tiket secara online. Dalam pengembangan GUI pemesanan tiket bioskop, perlu diperhatikan beberapa aspek, seperti perancangan sistem informasi, desain grafis, dan pengembangan aplikasi. Perancangan sistem informasi harus efisien dan efektif dalam mengelola informasi tentang tiket, pelanggan, dan transaksi. Desain grafis yang menarik dan mudah digunakan sangat penting untuk menarik konsumen dan memudahkan penggunaan aplikasi. Sedangkan pengembangan aplikasi pemesanan tiket bioskop berbasis mobile adalah solusi yang diperlukan untuk memudahkan pemesanan tiket di tempat dan kapan saja. Dalam pengembangan aplikasi ini, penggunaan teknologi terkini seperti Python dan tkinter dapat membantu dalam membuat aplikasi yang efisien dan mudah dikelola.
Dalam pengembangan GUI pemesanan tiket bioskop, juga perlu diperhatikan beberapa fitur yang harus ada dalam aplikasi, seperti pemesanan tiket, data pelanggan, laporan penjualan, antarmuka yang menarik, dan validasi input. Fitur-fitur tersebut harus disediakan dalam GUI pemesanan tiket bioskop untuk memberikan pengalaman pengguna yang baik dan memudahkan proses pemesanan tiket bioskop. Validasi input sangat penting dalam memastikan data yang diinput benar, sedangkan penggunaan dropdown dapat memudahkan pengguna dalam memilih opsi yang sesuai. Laporan penjualan juga harus disajikan dengan baik untuk memudahkan pengguna dalam melihat laporan penjualan tiket bioskop secara akurat dan efisien. Desain grafis yang menarik dan mudah digunakan juga sangat penting untuk menarik konsumen dan memudahkan penggunaan aplikasi.

 
	
BAB III
PEMBAHASAAN

3.1.	SOURS CODE
import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import tkinter.messagebox as messagebox

class SistemTiket:
    def __init__(self, root):
        self.root = root
        self.file = "DataPembelianTiket.csv"
        self.font = 10
        tk.Label(root, text="KASIR PEMBELIAN TIKET FILM BIOSKOP", background="azure3",font=self.font).grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        tk.Label(root, text="Nama Pembeli:", font=self.font).grid(row=1, column=0, padx=10, pady=10, sticky=E)
        self.nama = tk.Entry(root, font=self.font, bd=5)
        self.nama.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        tk.Label(root, text="Umur Pembeli:", font=self.font).grid(row=2, column=0, padx=10, pady=10, sticky=E)
        self.umur = tk.Entry(root, font=self.font, bd=5)
        self.umur.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        tk.Label(root, text="No.Kontak:", font=self.font).grid(row=3, column=0, padx=10, pady=10, sticky=E)
        self.kontak = tk.Entry(root, font=self.font, bd=5)
        self.kontak.grid(row=3, column=1, padx=10, pady=10, sticky=W)
        tk.Label(root, text="Tanggal Beli:", font=self.font).grid(row=4, column=0, padx=10, pady=10, sticky=E)
        self.tgl_beli = DateEntry(root, date_pattern='dd/mm/y', width=12, font=self.font)
        self.tgl_beli.grid(row=4, column=1, padx=10, pady=10, sticky=W)
        self.film = tk.Button(root, text="Pilih Film", font=self.font, command=self.pilih_film)
        self.film.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(root, text="Simpan", font=self.font, command=self.save_data).grid(row=6, column=0, padx=10, pady=10, columnspan=2)
        tk.Button(root, text="Lihat Data Pembeli",font=self.font, command=self.lihat_data).grid(row=7, column=0, padx=10, pady=10, columnspan=2)
        
    def pilih_film(self):
        self.jendela_film = tk.Toplevel(self.root)
        self.jendela_film.title("Pilih Film")
        tk.Button(self.jendela_film, text="Siksa Neraka/ Jam: 15:30/ Harga: Rp70.000", background="Orange", font=self.font, command=lambda: set_film('Siksa Neraka')).grid(row=0, column=0,padx=10,pady=10)
        tk.Button(self.jendela_film, text="Layangan Putus/ Jam: 18:00/ Harga: Rp50.000", background="Orange",font=self.font,command=lambda: set_film('Layangan Putus')).grid(row=1, column=0,padx=10,pady=10)
        tk.Button(self.jendela_film, text="13 Bom Di Jakarta/ Jam: 21:00/ Harga: Rp45.000", background="Orange",font=self.font,command=lambda: set_film('13 Bom Di Jakarta')).grid(row=2, column=0,padx=10,pady=10)
        def set_film(film):
            self.pickpilh = film
            self.jendela_film.destroy()

    def save_data(self):
        nama = self.nama.get()
        umur_str = self.umur.get()
        kontak_str = self.kontak.get()
        try:
            umur = int(umur_str)
            kontak = int(kontak_str)
        except ValueError:
            messagebox.showerror("Error", "Umur dan No.Kontak harus berupa angka.")
            return
            
        if not hasattr(self, 'pickpilh'):
            messagebox.showerror("Error", "Silakan pilih film terlebih dahulu.")
            return        
        tgl_beli = self.tgl_beli.get_date().strftime('%d/%m/%Y')
        film = self.pickpilh
        harga = self.harga(film)
        jam_tayang = self.jam_tayang(film)
        with open(self.file, 'a', newline='') as file:
            fieldnames = ['Nama', 'Umur', 'No_tlp', 'Tanggal_Beli', 'Film', 'Harga', 'Jam_Tayang']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({
                'Nama': nama,
                'Umur': umur,
                'No_tlp': kontak,
                'Tanggal_Beli': tgl_beli,
                'Film': film,
                'Harga': harga,
                'Jam_Tayang': jam_tayang
            })
        self.clear()

    def jam_tayang(self, jdl_film):
        if jdl_film == 'Siksa Neraka':
            return '15:30'
        elif jdl_film == 'Layangan Putus':
            return '18:00'
        elif jdl_film == '13 Bom Di Jakarta':
            return '21:00'
        else:
            return ''

    def harga(self, jdl_film):
        if jdl_film == 'Siksa Neraka':
            return 70000
        elif jdl_film == 'Layangan Putus':
            return 50000
        elif jdl_film == "13 Bom Di Jakarta":
            return 40000
        else:
            return ''

    def clear(self):
        self.nama.delete(0, tk.END)
        self.umur.delete(0, tk.END)
        self.kontak.delete(0, tk.END)
        self.film.event_delete('')

    def lihat_data(self):
        self.jendela_info = tk.Toplevel(self.root)
        self.jendela_info.title("Info Pelanggan")
        self.tree = ttk.Treeview(self.jendela_info, columns=('No', 'Nama', 'Umur', 'No. Telp', 'Tanggal Beli', 'Film', 'Harga', 'Jam Tayang'))
        self.tree.heading('No', text='No')
        self.tree.heading('Nama', text='Nama')
        self.tree.heading('Umur', text='Umur')
        self.tree.heading('No. Telp', text='No. Telp')
        self.tree.heading('Tanggal Beli', text='Tanggal Beli')
        self.tree.heading('Film', text='Film')
        self.tree.heading('Harga', text='Harga')
        self.tree.heading('Jam Tayang', text='Jam Tayang')
        self.tree.column('#0', stretch=tk.NO, width=0)
        self.tree.column('No', stretch=tk.NO, width=40)
        self.tree.column('Nama', stretch=tk.NO, width=150)
        self.tree.column('Umur', stretch=tk.NO, width=80)
        self.tree.column('No. Telp', stretch=tk.NO, width=100)
        self.tree.column('Tanggal Beli', stretch=tk.NO, width=100)
        self.tree.column('Film', stretch=tk.NO, width=150)
        self.tree.column('Harga', stretch=tk.NO, width=100)
        self.tree.column('Jam Tayang', stretch=tk.NO, width=100)
        no = 0
        with open(self.file, 'r') as file:
            reader = csv.DictReader(file)
            for idx, row in enumerate(reader, start=1):
                no += 1
                self.tree.insert('', 'end', iid=idx, values=(no, row['Nama'], row['Umur'], row['No_tlp'], row['Tanggal_Beli'], row['Film'],row['Harga'], row['Jam_Tayang']))
        self.tree.pack(expand=YES, fill=BOTH)
        tk.Button(self.jendela_info, text='Total Penjualan', command=self.total_penjualan, font=self.font).pack(padx=5, pady=5)

    def total_penjualan(self):
        total = 0
        with open(self.file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                harga = int(row['Harga'])
                total += harga
        tk.Label(self.jendela_info, text=f'Total Penjualan: Rp{total:,}', background="royalblue1", font=self.font).pack(padx=5,pady=5)

root = tk.Tk()
root.title("Sistem Penjualan Tiket Bioskop")
root.state('zoomed')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
app = SistemTiket(root)
root.mainloop()

3.2.	Fitur-fitur 
Kode Python tersebut merupakan implementasi dari sebuah aplikasi kasir pembelian tiket film bioskop. Aplikasi ini menggunakan library tkinter untuk antarmuka pengguna dan csv untuk menyimpan data pembeli. Kode tersebut terdiri dari class SistemTiket yang mengatur seluruh fungsionalitas aplikasi. Selain itu, terdapat metode-metode seperti pilih_film, save_data, lihat_data, total_penjualan, dan fungsi bantuan seperti jam_tayang dan harga untuk melakukan perhitungan terkait film yang dipilih.
Kode tersebut dapat dijalankan untuk membuat aplikasi kasir pembelian tiket film bioskop dengan antarmuka sederhana menggunakan Python dan library tkinter serta csv. Aplikasi ini memiliki fitur-fitur berikut:

3.2.1.	Antarmuka Pengguna.











 

Aplikasi menampilkan antarmuka untuk memasukkan data pembeli, seperti nama, umur, nomor kontak, dan tanggal pembelian.

3.2.2.	 Pemilihan calendar
 
Gambar 3.2 pemilihan calendar
Dari pemilihan tanggal beli yang membuka jendela agar memunculkan pilihan tanggal untuk menyimpan data pembelian yang dilakukan pada saat itu. Untuk memunculkan calendar harus download library tkcalendar dulu dengan perintah “pip install tkcalendar” 
 
Gambar 3.3 install tkcalendar
3.2.3.	Pemilihan Film

 
Gambar 3.4 Pemilihan film
Pengguna dapat memilih film melalui tombol "Pilih Film" yang membuka jendela kecil dengan pilihan film beserta jam tayang dan harga.
3.2.4.	Penyimpanan Data

 
Gambar 2.5 pemyimpanan data
Data pembeli disimpan ke dalam file CSV setelah pengguna mengklik tombol "Simpan". Dan tabel pada inputan akan di bersihkan
3.2.5.	 Melihat Data Pembeli 
Gambar 3.6 Data Pembeli
Aplikasi juga memungkinkan pengguna untuk melihat data pembeli yang telah disimpan dalam bentuk tabel ketika mengkilk “Lihat Data Pembeli”
3.2.6.	 Perhitungan Total Penjualan
Bagan 1Gambar 3.7 Perhitungan Total
Aplikasi dapat menghitung total penjualan berdasarkan data pembeli yang tersimpan ketka mengklik “Total Penjualan”.
3.2.7.	 Message Box
Kotak pesan ini digunakan untuk memberikan informasi atau pemberitahuan kepada pengguna terkait dengan input yang diberikan atau hasil dari operasi yang dilakukan. Sebagai contoh, dalam metode save_data, terdapat penggunaan messagebox.showerror untuk menampilkan pesan error jika terdapat kesalahan dalam input umur dan nomor kontak. Selain itu, pesan error juga ditampilkan jika pengguna mencoba untuk menyimpan data tanpa memilih film terlebih dahulu.

 
BAB IV
PENUTUP

4.1.	 Kesimpulan
Pada kode ini menciptakan aplikasi kasir, pembelian tiket film bioskop yang menggunakan library tkinter untuk membuat antarmuka dan csv untuk menyimpan data pembeli. Aplikasi ini juga memiliki fitur-fitur seperti memilih film, menyimpan data pembeli, dan menampilkan data pembeli dalam layar kecil. Pada kode ini mencakup metode-metode seperti pilih_film, save_data, lihat_data, total_penjualan, dan fungsi bantuan seperti jam_tayang dan harga untuk melakukan perhitungan terkait film yang dipilih. Aplikasi ini dapat menghitung total penjualan berdasarkan data pembeli yang tersimpan dalam file CSV.
Secara keseluruhan, kode ini menunjukkan bagaimana mengembangkan aplikasi kasir pembelian tiket film bioskop menggunakan Python dan library tkinter serta csv.
