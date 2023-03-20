# print('===============Data Base Karyawan===================')

# print('1.','Menambahkan Data Karyawan')
# print('2.','Mengubah Data Karyawan')
# print('3.','Menghapus Data Karyawan')
# print('4.','Report Data Karyawan')
# print('5.','Exit')

# while True:
#     input_angka = (int(input('Silakan Pilih Menu dalam Angka 1-5:')))
#     if input_angka == 1:
#         print('===============Masukan Data Karyawan===================')
#         print('masukan data karyawan jika data tidak tersedia harap isi 0')
#         Id_karyawan = []
#         nama_karyawan = []
#         jabatan = []
#         gaji = []

#         def masukkan_data():
#             input_id = int(input("masukan Id_karyawan : "))
#             Id_karyawan.append({'Id_karyawan' : input_id})
#             # print(input_id)

#             input_nama = input("masukan nama_karyawan : ")
#             nama_karyawan.append({'nama_karyawan' : input_nama})
#             # print(input_nama)

#             input_jabatan = input("masukan jabatan : ")
#             jabatan.append({'jabatan' : input_jabatan})
#             # print(input_jabatan)

#             input_gaji = int(input("masukan data gaji : "))
#             gaji.append({'jabatan' : input_gaji})
#             # print(input_gaji)
            
#         masukkan_data() 



#     if input_angka == 2:
#         print('===============Mengubah Data karyawan===================')
#     if input_angka == 3:
#         print('===============Menghapus Data karyawan===================')
#     if input_angka == 4:
#         print('===============Report Data karyawan===================')
#     else:
#         quit()


# while True:
#     user_input = input("Masukkan bilangan bulat: ")
#     if user_input.isnumeric():
#         integer_input = int(user_input)
#         break
#     else:
#         print("Input harus berupa bilangan bulat. Silakan coba lagi.")

# print("Bilangan bulat yang dimasukkan adalah:", integer_input)


# input_id = input("Masukan ID Karyawan : ")

# kata_list = list(input_id)
# comp = [char.isnumeric() for char in kata_list]
# print(comp)

# input_id = input("Masukan ID Karyawan : ")

# interger = int(input_id)

# if False:
#     print("slah")

# print(interger)

num = int(input("Masukkan angka antara 1 dan 10: "))
while num < 1 or num > 10:
    num = int(input("Masukkan angka antara 1 dan 10: "))
print("Angka yang dimasukkan adalah:", num)


