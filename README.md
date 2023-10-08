# POSTTEST2
POST TEST 2 (PRAKTIKUM) MUHAMMAD ARIFIN DAVA 2309116059- SISTEM INFORMASI-B 23

TUGAS :
Buat sebuah program yang didalamnya:
terdapat 2 role, yaitu pembeli dan admin. (Dapat berupa role lain, misal pasien dan admin)
Menu untuk role admin bisa melakukan CRUD (Create, Read, Update, Delete)
Menu untuk role pembeli hanya dapat melakukan transaksi. (Aktivitas role lainnya bisa disesuaikan. Contoh role pasien dapat mendaftarkan diri untuk antrian)
Dengan ketentuan:
Membuat flowchart
Memiliki tampilan yang dapat dimengerti user
Mengumpulkan melalui github. Yang dikumpulkan di classroom adalah link repository nya.  Membuat file README.md yang didalamnya terdapat gambar flowchart dan penjelasan output beserta screenshoot output.
Nilai tambahan (Bersifat Opsional) :
menggunakan PrettyTable


Flowchart :
![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/a4561046-82db-4ea5-9bde-69abff407871)

Penjelasan Program :
Program sistem manajemen Coffee Shop dengan menu customer (Customer Interface) dan kasir (Cashier Interface). Program ini dibuat menggunakan Python dan menggunakan PrettyTable untuk membuat tampilan yang rapi dan bersih. Program ini menggabungkan beberapa konsep dasar pemrograman seperti penggunaan dictionary, list, penggunaan fungsi, penggunaan loop, serta konsep CRUD (Create, Read, Update, Delete) sederhana.

Berikut adalah penjelasan rinci dari program tersebut:

Import Library:

Program mengimpor modul PrettyTable untuk membuat tampilan tabel yang rapi dan simpel.
Menu Coffee:

Program menentukan menu kopi beserta harga dari tiap minuman menggunakan dictionary dengan nama menu.
Inisialisasi Dictionary:

Program menginisialisasi dua dictionary: customer_orders untuk menyimpan pesanan pelanggan dan cashier_records untuk mencatat pesanan yang sudah dibayar oleh pelanggan.
Username dan Password Kasir:

Terdapat username (cashier_username) dan password (cashier_password) yang digunakan untuk login kasir. Ini digunakan untuk memvalidasi login saat kasir mengakses antarmuka kasir.
Customer Interface:

Fungsi customer_interface memungkinkan pelanggan untuk melihat daftar menu, mengisi pesanan mereka, dan melakukan pembayaran. Pelanggan dapat memesan beberapa kopi sekaligus dan menginput jumlahnya.
Cashier Interface:

Fungsi cashier_interface digunakan oleh kasir untuk mengakses antarmuka kasir. Kasir akan diminta untuk menginput username dan password sebelum dapat mengakses antarmuka kasir.
Antarmuka kasir menawarkan beberapa opsi, termasuk melihat pesanan pelanggan, menghitung tagihan, menandai pesanan sebagai sudah dibayar, menampilkan total transaksi Coffee Shop, mengupdate pesanan pelanggan, dan keluar dari antarmuka kasir.
Display Orders:

Fungsi display_orders menampilkan pesanan pelanggan beserta nama pelanggan ke dalam tabel menggunakan PrettyTable. Ini memungkinkan kasir untuk melihat pesanan yang ada.
Calculate Bills:

Fungsi calculate_bills menghitung total tagihan untuk setiap pesanan pelanggan dan mencatatnya ke dalam cashier_records.
Mark Orders as Paid:

Fungsi mark_orders_as_paid memungkinkan kasir untuk menandai pesanan pelanggan sebagai sudah dibayar dan menghapusnya dari daftar pesanan aktif.
Update Customer Order:

Fungsi update_customer_order memungkinkan kasir untuk memperbarui pesanan pelanggan dengan menghapus pesanan lama dan menggantinya dengan pesanan baru.
Display Total Bills:

Fungsi display_total_bills menghitung total transaksi seluruh pesanan yang sudah dibayar dan menampilkannya.
Main Menu:

Fungsi main_menu adalah fungsi utama program yang menampilkan menu utama Coffee Shop dengan opsi untuk memilih antarmuka pelanggan, antarmuka kasir, atau keluar dari program.
Penanganan Input:

Program melakukan penanganan input yang salah dengan menampilkan pesan kesalahan dan memberikan kesempatan untuk mencoba lagi.
Program ini mencakup konsep dasar pemrograman dan membuat alur kerja yang cukup intuitif antara pelanggan dan kasir. Program ini memungkinkan pelanggan untuk memesan kopi dan kasir untuk mengelola pesanan dan transaksi secara efisien.

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/a96078cf-c8df-412d-bf85-c065b29e7b62)
note : Program menggunakan bahasa Inggris
diawal program akan tampil output nama Coffee shop dan user diminta untuk memilih opsi menjadi customer atau kasir

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/453e8e03-9e1f-4ca0-a9e0-750780ab4c24)
Ketika User memilih sebagai customer akan tampil daftar menu Coffee Shop lengkap beserta harga, user diminta menginput nama
( TERDAPAT OPSI X UNTUK KELUAR DARI MENU CUSTOMER )

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/22520c50-4b81-4814-86a8-7e2b00585a4e)
Ketika User menginput X maka akan kembali ke tampilan awal program

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/884bdf4c-b169-4cb9-9156-42d5d9160fbe)
Setelah menginput nama, user diminta menginput orderan Coffee yg ingin dipesan ( NAMA COFFEE HARUS SESUAI DENGAN YANG ADA DI MENU )
( TERDAPAT OPSI X UNTUK KELUAR DARI MENU CUSTOMER )

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/02f00383-3747-442e-9f85-4762c9a86b90)
Ketika user menginput nama Coffee yang tidak sesuai maka akan muncul tampilan berikut dan akan looping ke bagian pemilihan menu

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/675da1b0-a88a-4a27-a73f-940aa237f30f)
Setelah menginput nama menu akan muncul tampilan input jumlah orderan

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/28dc06ea-7823-4c1a-bc8b-ae81ef2f96cf)
Kemudian user akan looping ke pemilihan menu lagi

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/b1b4226e-03b8-42f4-a5c2-d23bb02f0606)
Setelahnya jika user memilih untuk memesan orderan lagi, akan tampil output seperti sebelumnya dan jika telah selesai order
akan looping ke pemilihan menu, user dapat mengakhiri pemilihan menu dengan cara menginput "X"

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/691aa9ec-12d3-4135-acd4-acafe58a7018)
Ketika user menginput "X" akan tampil output total bill user kemudian user diminta untuk menyebutkan uang yang akan dibayar

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/070da394-c517-496d-baa9-f0a0e0632651)
Ketika uang yang akan dibayar user >= total bill, maka akan muncul tampilan transaksi berhasil dan akan tampil output
uang kembalian dari transaksi dan akan looping ke tampilan awal customer yaitu menginput nama, user dapat mengorder kembali,
namun jika user ingin keluar dari menu customer, user dapat menginput "X"

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/e6ca0e58-6f18-471a-b14f-d73f220bed4b)
Ketika uang yang dibayar user tidak cukup, maka akan tampil seperti diatas dan kembali looping ke menu customer, user dapat mengorder kembali,
namun jika user ingin keluar dari menu customer, user dapat menginput "X"

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/1fbdd563-819e-4fcb-92b3-6c539e1c057c)
Ketika user menginput "X" maka user akan kembali ke tampilan awal program, dan bisa memilih untuk kembali ke user interface / kasir interface /
exit program.. Ketika user memilih untuk kasir interface, akan muncul tampilan login, user diminta untuk menginput username dan password

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/04769907-d6e6-450a-b7b2-592178a88210)
username untuk kasir sendiri adalah : ( untuk username dan password harus sesuai, jika salah maka akan terus looping di bagian login )
username : dapa ( nama saya )
password : 059  ( nim saya )
jika telah berhasil login maka akan muncul tampilan













