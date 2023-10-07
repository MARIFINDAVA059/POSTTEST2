"""
NAMA     : MUHAMMAD ARIFIN DAVA
NIM      : 2309116059
KElAS    : SISTEM INFORMASI-B  (23)

POSTTEST 2
TEMA     : Coffee Shop  ( RumahKita Coffee Shp[] )
"""

# Import library PrettyTable untuk membuat tabel yang rapi dan simpel.
from prettytable import PrettyTable

# Menentukan Menu kopi dengan menggunakan dictionary.
menu = {
   # Membuat daftar Menu coffee dan non coffee disertai harga dari tiap minuman.
   "Espresso":  27500 ,      
   "Cappuccino":  30000 ,
   "Mocha":  35000 ,
   "Macchiato":  37500 ,
   "Redvelvet Latte":  40000 ,
   "Matcha Latte":  35000 
}

# Inisialisasi dictionary untuk menyimpan pesanan customer dan catatan kasir.
customer_orders = {}        # Function orderan customer
cashier_records = []        # Function catatan kasir

# Username dan Password yang digunakan untuk login kasir
cashier_username = "dapa"   # Nama saya sendiri
cashier_password = "059"    # Password merupakan NIM saya

# Function untuk menampilkan menu kepada customer.
def display_menu():
   # Membuat tabel menggunakan PrettyTable.
   table = PrettyTable(["Menu", "Price"])  # Kolom pertama daftar Menu, Kolom kedua Harga Menu
   for item, price in menu.items():
      table.add_row([item, price])         # Menambahkan Baris pada PrettyTable
   print("Coffee Shop Menu")               # Instruksi untuk print Judul Daftar Menu
   print(table)                            # Instruksi untuk print PrettyTable

# Function yang akan ditampilkan kepada customer
def customer_interface():
   while True:
      display_menu()  # Menampilkan daftar menu beserta harga tiap menu
      customer_name = input("Enter your name (or 'X' to exit): ")   # Customer menginput nama customer
      if customer_name == 'X':    
         break        # Ketika Customer Mengisi X untuk keluar program, akan menampilkan total bill
      customer_order = {}
      while True:
         coffee = input("Enter a coffee item (or 'X' to finish): ") # Customer menginput Coffee yang akan diorder (penulisan harus sesuai)
         if coffee == 'X':
            break     # Ketika Customer Mengisi X untuk keluar program, akan menampilkan total bill
         if coffee in menu:
               quantity = int(input(f"How many {coffee}s would you like? "))   # Customer memilih ingin membeli berapa Coffee
               customer_order[coffee] = quantity                               # Untuk menyimpan orderan Coffee
         else:
               print("Invalid coffee selection. Please choose from the menu.") # Tampilan Ketika penulisan nama Coffee tidak sesuai
      customer_orders[customer_name] = customer_order                          # Untuk menyimpan nama customer
      print("Order placed successfully.")                                      # Tampilan ketika order berhasil dan tersimpan ke dictionary

      # Proses pembayaran
      total_bill = sum(menu[coffee] * quantity for coffee, quantity in customer_order.items()) # Perhitungan utk transaksi harga Coffee
      print(f"Your total bill is Rp. {total_bill:.2f}")                # Menampilkan total harga Coffee
      payment = float(input("Enter the payment amount: "))          # Customer diminta menginput total uang yang dibayarkan
      if payment >= total_bill:                                     # Jika customer menginput uang lebih dari harga, menampilkan kembalian
         change = payment - total_bill
         print(f"Payment successful. Your change is Rp. {change:.2f}") # Menampilkan uang kembalian untuk customer
      else:
         print("Insufficient payment. Please pay the full amount.") # Menampilkan pembayaran gagal ketika uang customer tidak cukup dan kembali ke menu tampilan awal customer

# Function untuk tampilan kasir.
def cashier_interface():
   while True:
      username = input("Enter your username: ")    # Kasir menginput nama (dapa)
      password = input("Enter your password: ")    # Kasir menginput password (059)
      if username == cashier_username and password == cashier_password: # Mengecek apakah kasir menginput data yang benar
         break
      else:
         print("Invalid credentials. Please try again.")                # Ketika kasir gagal login, program akan terus berulang
   while True:                                # Ketika login berhasil maka akan melanjutkan program
      print("Cashier Interface")              # Tampilan kasir
      print("1. View Orders")                
      print("2. Calculate Bills")
      print("3. Mark Orders as Paid")
      print("4. Total Transaction")
      print("5. Exit")
      choice = input("Enter your choice: ")   # Kasir memilih program yang ingin dijalankan

       if choice == '1':                       # Menampilkan orderan yang ada
         display_orders()
      elif choice == '2':                     # Menghitung tagihan yang ada
         calculate_bills()
      elif choice == '3':                     # Menghapus orderan yang sudah dibayarkan customer
         mark_orders_as_paid()
      elif choice == '4':                     # Menampilkan total penjualan Coffee Shop
         display_total_bills()
      elif choice == '5':                     # Mengupdate orderan customer
         update_customer_order()
      elif choice == '6':                     # Menghentikan program dan kembali ke tampilan awal Coffe Shop
         break
      else:
         print("Invalid choice. Please try again.") # Ketika menginput tidak sesuai (1/2/3/4/5)

# Function untuk menampilkan semua pesanan customer kepada kasir.
def display_orders():
   table = PrettyTable(["Customer", "Order"])       # Membuat PrettyTable nama customer dan orderannya   (READ)
   for customer, order in customer_orders.items():  
      table.add_row([customer, order])
   print("Customer Orders")
   print(table)                                     # Menampilkan nama customer dan orderannya

# Function untuk menghitung tagihan orderan
def calculate_bills():
   for customer, order in customer_orders.items(): 
      total_bill = sum(menu[coffee] * quantity for coffee, quantity in order.items()) # Menghitung orderan yang ada
      cashier_records.append((customer, order, total_bill))                           # Menambahkan hitungan tagihan ke dictionary (CREATE)
   print("Bills calculated and recorded successfully.")                               # Menampilkan tagihan sudah dihitung dan dicatat

# Function untuk mengupdate orderan customer
def update_customer_order():
   customer_name = input("Enter the customer's name to update their order: ")          # Menginput nama customer yang ingin diubah orderannya
   if customer_name in customer_orders:
      print(f"Current order for {customer_name}: {customer_orders[customer_name]}")    # Menampilkan orderan customer 
      new_order = {}
      while True:
         coffee = input("Enter a coffee item to update (or 'X' to finish updating): ") # Memilih coffe yang ingin di update
         if coffee == 'X':                                                             # Kembali ke menu sebelumnya ketika input "X"
            break
         if coffee in menu:                                                            # Ketika Coffee terdapat dalam menu melanjutkan program
            new_quantity = int(input(f"How many {coffee}s would you like? "))          # Menginput jumlah Coffee yang ingin diganti
            new_order[coffee] = new_quantity                                           # Update Coffee               (UPDATE)      
         else: 
            print("Invalid coffee selection. Please choose from the menu.")            # Tampilan ketika salah menginput Coffee
      customer_orders[customer_name] = new_order
      print(f"Order for {customer_name} has been updated successfully.")
   else:
      print("Customer not found. Please check the name.")

# Function untuk menghapus pesanan sebagai sudah dibayar oleh kasir.
def mark_orders_as_paid():
   customer_name = input("Enter the customer's name to clear their order when paid: ")  # Menginput nama customer yang telah membayar orderan
   if customer_name in customer_orders:
      del customer_orders[customer_name]                          # Delete orderan yang telah dibayar  (DELETE)
      print(f"{customer_name}'s order has been marked as paid.")  # Menampilkan tampilkan orderan telah dibayar
   else:
      print("Customer not found. Please check the name.")         # Ketika nama customer tidak ditemukan maka akan kembali

# Function untuk menghitung total transaksi Coffee Shop
def display_total_bills():
   total_bills = sum(record[2] for record in cashier_records)     # Mengambil data orderan yang telah dicatat
   print(f"Total Coffee Shop Transaction : Rp. {total_bills:.2f}   Alhamdulillah :) ") # Menampilkan total transaksi Coffee Shop

# Bagian utama program. ( tampilan awal program )
def main_menu():
   while True:
      menu = PrettyTable()                                    # Membuat PrettyTable
      menu.field_names = ["Option", " RumahKita Coffee Shop"] # Membuat Judul table
      menu.add_row(["1", "Customer Interface"])
      menu.add_row(["2", "Cashier Interface"])
      menu.add_row(["3", "Exit"])
      print(menu)
      choice = input("Enter your choice: ")                   # Menginput pilihan untuk menjalankan program

      if choice == '1':                               # Menjalankan program sebagai customer
         customer_interface()
      elif choice == '2':                             # Menjalankan program sebagai kasir
         cashier_interface()
      elif choice == '3':                             # Menghentikan / keluar dari program
         print("Terima kasih telah berkunjung ke RumahKita CoffeShop")
         break
      else:
         print("Invalid choice. Please try again.")   # Ketika input user tidak sesuai (1/2/3)

if __name__ == '__main__':    # Menjalankan Program Utama Coffee Shop 
   main_menu()
