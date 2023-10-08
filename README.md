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
Program menginisialisasi dua dictionary: customer_orders untuk menyimpan orderan customer dan cashier_records untuk mencatat orderan yang sudah dibayar oleh customer.

Username dan Password Kasir:
Terdapat username (cashier_username) dan password (cashier_password) yang digunakan untuk login kasir. Ini digunakan untuk memvalidasi login saat kasir mengakses tampilan kasir.

Customer Interface:
Function customer_interface memungkinkan customer untuk melihat daftar menu, mengisi orderan mereka, dan melakukan pembayaran. Pelanggan dapat memesan beberapa kopi sekaligus dan menginput jumlahnya.
Terdapat juga tampilan untuk mengisi uang yang akan dibayar dan juga uang kembalian setelah pembayaran.

Cashier Interface:
Function cashier_interface digunakan oleh kasir untuk mengakses tampilan kasir. Kasir akan diminta untuk menginput username dan password sebelum dapat mengakses tampilan kasir.
tampilan kasir menawarkan beberapa opsi, termasuk melihat orderan customer, menghitung tagihan, menandai orderan sebagai sudah dibayar, menampilkan total transaksi Coffee Shop, mengupdate orderan customer, dan keluar dari tampilan kasir.

Display Orders:
Function display_orders menampilkan orderan customer beserta nama customer ke dalam tabel menggunakan PrettyTable. Ini memungkinkan kasir untuk melihat orderan yang ada.

Calculate Bills:
Function calculate_bills menghitung total tagihan untuk setiap orderan customer dan mencatatnya ke dalam cashier_records.

Mark Orders as Paid:
Function mark_orders_as_paid memungkinkan kasir untuk menandai orderan customer sebagai sudah dibayar dan menghapusnya dari daftar orderan.

Update Customer Order:
Function update_customer_order memungkinkan kasir untuk memperbarui orderan customer dengan menghapus orderan lama dan menggantinya dengan orderan baru.

Display Total Bills:
Function display_total_bills menghitung total transaksi seluruh orderan yang sudah dibayar dan menampilkannya.

Main Menu:
Function main_menu adalah fungsi utama program yang menampilkan menu utama Coffee Shop dengan opsi untuk memilih tampilan customer, tampilan kasir, atau keluar dari program.

Penanganan Input salah :
Program melakukan penanganan input yang salah dengan menampilkan pesan kesalahan dan memberikan kesempatan untuk mencoba lagi.
Program ini mencakup konsep dasar pemrograman dan membuat alur kerja yang cukup intuitif antara customer dan kasir. Program ini memungkinkan customer untuk memesan kopi dan kasir untuk mengelola orderan dan transaksi secara efisien


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
jika telah berhasil login maka akan muncul tampilan kasir interface, kasir dapat memilih 6 fitur kasir yang tertera pada output
kasir diminta input antara (1/2/3/4/5/6)

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/d126a7c8-4c25-46ee-a440-e1f997140641)

Berikut tampilan ketika login salah karena username dan password tidak sesuai, maka akan terus looping hingga username dan password benar

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/a662e350-6110-4d4d-a73e-46c0a3fa9e00)

Ketika user menginput "1" maka akan menampilkan (CRUD = READ) orderan yang telah diorder beserta jumlah orderannya, dan akan kembali looping 
ke tampilan awal kasir untuk memilih fitur
( KETIKA TIDAK ADA ORDERAN MAKA HANYA AKAN MUNCUL PRETTYTABLE TANPA ISI TABEL )

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/21882e0c-bc09-4219-a11e-b02dfda98562)

Ketika user menginput "2" maka akan melakukan penghitungan semua orderan yang ada, yang nantinya digunakan pada bagian total transaction
fitur ini menambahkan hitungan tagihan menggunakan create yaitu append ( CRUD = CREATE )
dan akan kembali looping ke tampilan awal kasir untuk memilih fitur 

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/79ad01b8-e1c8-4c88-a104-3d9fd5c16216)

Ketika user menginput "3" maka akan muncul tampilan untuk menginput nama customer yang ingin ditandain bahwa customer telah membayar (CRUD = DELETE),
setelah nama customer diinput maka akan muncul tampilan (nama customer) order telah terbayar, dan akan kembali looping ke tampilan awal kasir untuk memilih fitur

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/bb589f93-43b4-4f28-bc24-32f46d22aa21)

Setelah user menandai nama customer yang telah membayar, maka orderan customer tersebut tidak akan ditampilkan lagi, dapat di cek menggunakan section "1" dan akan tampil bahwa
orderan dengan nama customer "dary" yang awalnya ada, sekarang sudah tidak ada


![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/ea515a1f-fa7d-439d-b33e-4a1479b89d5c)

Ketika user menginput nama customer yang salah akan muncul tampilan, customer tidak ada, silahkan cek kembali nama customer, dan akan kembali looping ke tampilan awal kasir untuk memilih fitur

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/3e8bb879-8b4d-4345-a3f9-40c4d61c0d2b)

Ketika user menginput "4" maka akan muncul tampilan total transaksi yang ada, yang telah dihitung pada function "2" yaitu perhitungan orderan

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/243d75d0-1fad-467b-888f-f727aa9a2793)

Ketika user menginput "5" maka akan muncul tampilan untuk menginput nama customer yang ingin di update orderannya ( CRUD = UPDATE ), akan muncul tampilan orderan customer tersebut,
user diminta untuk menginput nama coffee yang ingin diedit, jika nama coffee sesuai akan muncul pilihan input jumlah orderan yang ingin diganti seperti contoh diatas

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/48c7412a-e903-462f-acfb-09a51dcf561a)

dapat di cek pada section "1" untuk mengecek jumlah orderan setelah diubah, yang awalnya Mocha : 3 dan Espresso : 2, menjadi Mocha : 4 dan Espresso : 4

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/48576a74-2888-4029-a36c-30ce5dc7f9ff)

Ketika orderan dihapus dengan menggunakan section "3" maka pada section "1" tidak ada isi orderan pada tabel

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/6b64796a-f3be-466b-8962-d7e6975ca88c)

Ketika memilih "6" pada section, maka akan keluar dari section kasir dan kembali ke tampilan awal menggunakan break

![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/6d14356d-54ed-4fd1-84bb-a40d9d33e71c)

ketika memilih section "4" maka akan muncul tampilan, pilihan salah, coba lagi.


![image](https://github.com/MARIFINDAVA059/POSTTEST2/assets/147223413/4f62b1e1-6bf0-4e3f-a0e6-c597e8cac555)

Ketika user memilih section "3" maka akan keluar dari program menggunakan break , akan muncul tampilan" Terima kasih telah berkunjung ke RumahKita CoffeShop ", dan program berhenti


























