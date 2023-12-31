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
            return 45000
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
