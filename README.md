# kelompok-4
Kelompok 4 - Studi Kasus Pembelian Tiket Bioskop
LAPORAN
PENERAPAN GUI PADA OOP: PEMBELIAH TIKET BIOSKOP

ANGGOTA KELOMPOK 4:
Afrizal tuasikal 		: 5220411262
Auxylium B.E. Bunga 		: 5220411260
Didi Wahidi 			: 5190411142
Didik sukma putra 		: 5220411270
Raisul Gibran 			: 5220411251

Kode Python tersebut merupakan implementasi dari sebuah aplikasi kasir pembelian tiket film bioskop. Aplikasi ini menggunakan library tkinter untuk antarmuka pengguna dan csv untuk menyimpan data pembeli. Kode tersebut terdiri dari class SistemTiket yang mengatur seluruh fungsionalitas aplikasi. Selain itu, terdapat metode-metode seperti pilih_film, save_data, lihat_data, total_penjualan, dan fungsi bantuan seperti jam_tayang dan harga untuk melakukan perhitungan terkait film yang dipilih.

Kode tersebut dapat dijalankan untuk membuat aplikasi kasir pembelian tiket film bioskop dengan antarmuka sederhana menggunakan Python dan library tkinter serta csv. Aplikasi ini memiliki fitur-fitur berikut:

1. input data pembeli. 
   Aplikasi menampilkan Window untuk mengimput data pembeli seperti nama, umur, nomor kontak, tanggal pembelian, dan film yang di inginkan
2. Pemilihan Kalender. 
   Dari pemilihan tanggal beli yang membuka DropDown agar memunculkan pilihan tanggal untuk menyimpan data pembelian yang dilakukan pada saat itu. Untuk memunculkan calendar
   harus download library tkcalendar dulu dengan perintah “pip install tkcalendar”. Library ini akan otomatis memilih tepat pada hari pembelian.4. Pemilihan Film
   Pengguna dapat memilih film melalui tombol "Pilih Film" yang membuka jendela baru dengan pilihan film beserta jam tayang dan harga.
5. Melihat Data Pembeli. 
   Aplikasi juga memungkinkan pengguna untuk melihat data pembeli yang telah disimpan dalam bentuk tabel ketika mengkilk “Lihat Data Pembeli” dan akan mengakse file CSV.
6. Perhitungan Total Penjualan
   Aplikasi dapat menghitung total penjualan berdasarkan data pembeli yang tersimpan ketka mengklik “Total Penjualan”.
7. peringatan Message Box. 
   Kotak pesan ini digunakan untuk memberikan informasi atau pemberitahuan kepada pengguna terkait dengan input yang diberikan atau hasil dari operasi yang dilakukan. Sebagai
   contoh, dalam metode save_data, terdapat penggunaan messagebox.showerror untuk menampilkan pesan error jika terdapat kesalahan dalam input umur dan nomor kontak. Selain
   itu, pesan error juga ditampilkan jika pengguna mencoba untuk menyimpan data tanpa memilih film terlebih dahulu.

Beberapa Kelebihan:
1. Mudah. 
   Kasir jadi lebih mudah dalam mengelola data pembeli dan tidak perlu menginput harga dan jam tanyan secara manual karena ada method pada code tersebut yang mengatur otomatis
   harga dan jam tayang sebuah film yang di pilih.
2. Pengolahan Data. 
   Data akan tersimpan dan walaupun programnya di close dan dijalankan kembali maka kasir dapat mengakses data yang tersimpan tampa takut data akan hilang akibat program di
   hentikan.
3. Penggunaan GUI. 
   Pengguan GUI pada aplikasi ini cukup terorganisir dimana untuk memilih film dan memunjulkan data menggunakan window lain dapat meningkatkan kemudahan karena tampilan input
   dan memunjulkan data tidak dilakukan pada satu window agar tampilan window lebih jelas dan tidak membingungkan. 
