
database = { 'Id_karyawan'  : [123,456,789,147],
             'nama_karyawan': ['josep','bambang','dara','suep'],
             'jabatan'      : ['staf','senior','junior','SPV'],
             'gaji'         : [100,200,150,500],
             'kpi'          : [95,85,74,63]

}

#=======================READING===========================================
def angka4():
    print(" ")
    print('===============Report Data Karyawan===================')
    print('pilih untuk melanjutkan proses!')

    def tampilkan_data():
        print(' ')
        print(f''''========================== # Data Base Karyawan # =======================================''')
        print("{: <15} {: <15} {: <15} {: <15} {: <15}".format('| Id Karyawan', ' | Nama Karyawan', ' | Jabatan', '  | Gaji', '   | KPI'))
        print('-----------------------------------------------------------------------------------------')
        for i in range(len(database['Id_karyawan'])):
            # print(i)
            print(f'''| {database['Id_karyawan'][i]:<15}| {database['nama_karyawan'][i]:<15}| {database['jabatan'][i]:<15}| {database['gaji'][i]:<15}| {database['kpi'][i]:<15}''')

    def tampilan_data_2():
        print(' ')
        input_id = input('masukan id karyawan: ')
        while True:
            if input_id.isnumeric():
                t_d = int(input_id)
                counter = 0
                for i in database['Id_karyawan']:
                    if t_d == i:
                        index_find = database['Id_karyawan'].index(t_d)
                        print(' ')
                        print(f'Berikut adalah hasil pencarian data dengan ID Karyawan : {input_id}')
                        print('````````````````````````````````````````````````````````````')
                        print(f''''========================== # Data Base Karyawan # =====================================|''')
                        print("{: <15} {: <15} {: <15} {: <15} {: <15}".format('| Id Karyawan', ' | Nama Karyawan', ' | Jabatan', '  | Gaji', '   | KPI'))
                        print('----------------------------------------------------------------------------------------|')

                        print(f'''| {database['Id_karyawan'][index_find]:<15}| {database['nama_karyawan'][index_find]:<15}| {database['jabatan'][index_find]:<15}| {database['gaji'][index_find]:<15}| {database['kpi'][index_find]:<15}''')
                        print('----------------------------------------------------------------------------------------|')
                        break
                    else:
                        counter += 1
            
                if counter == len(database['Id_karyawan']):
                    print('')
                    print('------------------------------------------')
                    print('Maaf Data yang Anda Cari Tidak Ditemukan:(')
                    print('------------------------------------------')
                    break                      
                else:
                    break
            else:
                print('')
                print('------------------------------------')
                print('Ulangi Input ID dalam Bentuk Angka!!')
                print('-------------------------------------')
                break
        
    while True:
        print('.......................................................')
        lanjutkan = input('TAMPILKAN DATA = 1, MENCARI = 2 BACK = 0: ')
        if lanjutkan == '1':
            tampilkan_data()
        elif lanjutkan == '2':
            tampilan_data_2()
        elif lanjutkan == '0':
            main_menu()                       
        else:
            
            print('--------------------------')
            print('Masukan Angka yang Benar!!')
            print('--------------------------')
            print(' ')

# ===============================menu create====================================================
def angka1():
    print('===============Masukan Data Karyawan===================')
    print('pilih untuk melanjutkan proses!')
    
    def masukan_data():
        print(' ')
        input_integer = input("Masukan ID Karyawan : ")

        kata_list = list(input_integer)
        interger = [char.isnumeric() for char in kata_list]
        # print(interger)

        if False in interger:
            print(' ')
            print('Silakan Input Dalam Bentuk Angka!!')
            print(' ')
            angka1()
        
        input_id = int(input_integer)
        
        counter = 0
        for i in database['Id_karyawan']:
            if input_id == i:

                database['Id_karyawan'].index(input_id)
                print(' ')
                print('----------------------')
                print("!!!maaf ID suda ada!!!")
                print('----------------------')
                print(' ')
                break
            else:
                counter +=1
                
        if counter == len(database['Id_karyawan']):
            input_nama = input("masukan nama karyawan : ").lower()
            input_jabatan = input("masukan jabatan : ").lower()
            while True:
                input_gaji = input("masukan data gaji : ")
                if input_gaji.isnumeric():
                    input_gaji_int = int(input_gaji)
                    break
                else:
                    print('_______________________________________________')
                    print('silakan masukan lagi Gaji dalam bentuk "ANGKA" ')
                    print('```````````````````````````````````````````````')

            while True:
                input_kpi = input("masukan nilai KPI : ")
                if input_kpi.isnumeric():
                    input_kpi_int = int(input_kpi)
                    break
                else:
                    print('_______________________________________________')
                    print('silakan masukan lagi KPI dalam bentuk "ANGKA" ')
                    print('```````````````````````````````````````````````')


                        
            while True:
                print('')
                input_pasti = input('Apakah Anda Yakin??  \nYA=1  \nNO= 0 \nPilih Angka: ')
                if input_pasti == '1':    
                    database['Id_karyawan'].append(input_id)
                    database['nama_karyawan'].append(input_nama)
                    database['jabatan'].append(input_jabatan)
                    database['gaji'].append(input_gaji_int)
                    database['kpi'].append(input_kpi_int)
                    print('............................................')
                    print('Data Berhasil di Tambahkan di Database Kami:)')
                    print('````````````````````````````````````````````')
                    break
                elif input_pasti == '0':
                    main_menu()
                    break
                else:
                    print(' ')
                    print('Masukan Angka yang Benar!!')
                    print(' ')

    while True:
        print('.......................................................')     
        lanjutkan = input('MENAMBAHKAN DATA = 1,BACK = 0: ')
        if lanjutkan == '1':
            masukan_data()
        elif lanjutkan == '0':
            main_menu()        
        else:
            print('--------------------------------')
            print('Silakan Masukan Angka yang benar')
            print('`````````````````````````````````')  
            print(' ')
            
            
# ===========================================menu update===================================================

def angka2():
    print('===============Mengubah Data Karyawan===================')
    print('pilih untuk melanjutkan proses!')
    def merubah_data():
        print(' ')
        input_id = input('masukan id karyawan: ')
        print(' ')
        while True:
            if input_id.isnumeric():
                t_u = int(input_id)
                counter = 0
                for i in range(len(database['Id_karyawan'])):

                    def input_ubah2():
                        print(' ')
                        ubah_input_karyawan = input('Masukan Nama Baru: ')
                        while True:
                            A = input('Apakah Anda Yakin Mengubah Nama diatas? \nYes = 1 \nNo = 0 \nPilih Angka: ')
                            if A =='1':
                                index = database['Id_karyawan'].index(i)
                                database['nama_karyawan'][index] = ubah_input_karyawan
                                print(' ')
                                print('data telah di ubah')
                                main_menu_ubah()
                            elif A == '0':
                                angka2()   
                            else:
                                print(' ')
                                print('!!harap memasukan sesuai angka di atas!!')
                                print(' ')
                                    
                    def input_ubah3():
                        print(' ')
                        ubah_input_jabatan = input('Masukan Jabatan Baru: ')
                        while True:
                            A = input('Apakah Anda Yakin Mengubah Jabatan Diatas? \nYes = 1 \nNo = 0 \nPilih Angka: ')
                            if A =='1':
                                index = database['Id_karyawan'].index(i)
                                database['jabatan'][index] = ubah_input_jabatan
                                print(' ')
                                print('Data Telah Diubah')
                                main_menu_ubah()
                            elif A == '0':
                                angka2()   
                            else:
                                print(' ')
                                print('!!harap memasukan sesuai angka di atas!!')
                                print(' ')
                                    
                    def input_ubah4():
                        while True:
                            print(' ')
                            ubah_gaji = input('Masukan Gaji Baru: ')
                            if ubah_gaji.isnumeric():
                                input_ubah_gaji = int(ubah_gaji)
                                while True:
                                    A = input('Apakah Anda Yakin Mengubah Gaji diatas? \nYes = 1 \nNo = 0 \nPilih Angka: ')
                                    if A =='1':
                                        index = database['Id_karyawan'].index(i)
                                        database['gaji'][index] = input_ubah_gaji
                                        print(' ')
                                        print('data telah di ubah')
                                        main_menu_ubah()
                                    elif A == '0':
                                        angka2()   
                                    else:
                                        print(' ')
                                        print('!!harap memasukan sesuai angka di atas!!')
                                        print(' ')
                                
                            else:
                                print('_______________________________')
                                print('!!!Inputan Hanya Untuk Angka!!!')
                                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                                print(' ')
                                    
                    def input_ubah5():
                        print(' ')
                        while True:
                            ubah_kpi = input('Masukan KPI Baru: ')
                            if ubah_kpi.isnumeric():
                                input_ubah_kpi = int(ubah_kpi)
                                while True:
                                    A = input('Apakah Anda Yakin Mengubah KPI diatas? \nYes = 1 \nNo = 0 \nPilih Angka: ')
                                    if A =='1':
                                        index = database['Id_karyawan'].index(i)
                                        database['kpi'][index] = input_ubah_kpi
                                        print(' ')
                                        print('data telah di ubah')
                                        main_menu_ubah()
                                    elif A == '0':
                                        angka2()
                                        
                                    else:
                                        print(' ')
                                        print('!!harap memasukan sesuai angka di atas!!')
                                        print(' ')
                                
                            else:
                                print('_______________________________')
                                print('!!!Inputan Hanya Untuk Angka!!!')
                                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                                print(' ')
                                
                    def main_menu_ubah():
                        print(' ')
                        print('===============Merubah Data Base Karyawan===================')
                        print('1.','Nama Karyawan')
                        print('2.','jabatan')
                        print('3.','Gaji')
                        print('4.','KPI')
                        print('5.','Kembali')

                        input_main_menu_ubah = input('Silakan pilih menu dengan input angka 1-5:')
                                
                        while True:
                            
                            if input_main_menu_ubah == '1':
                                input_ubah2()
                                
                            elif input_main_menu_ubah == '2':
                                input_ubah3()
                                
                            elif input_main_menu_ubah == '3':
                                input_ubah4()
                                
                            elif input_main_menu_ubah == '4':
                                input_ubah5()
                                
                            elif input_main_menu_ubah == '5':
                                angka2()
                            else:
                                print('Silakan Ulangi Sesuai Angka Diatas!!')



                    if t_u == database['Id_karyawan'][i]:
                        while True:
                            counter = 0
                            for i in database['Id_karyawan']:
                                if t_u == i:
                                    index_find = database['Id_karyawan'].index(t_u)
                                    print(' ')
                                    print(f'Berikut adalah hasil pencarian data dengan ID Karyawan : {input_id}')
                                    print('````````````````````````````````````````````````````````````')
                                    print(f''''========================== # Data Base Karyawan # =====================================|''')
                                    print("{: <15} {: <15} {: <15} {: <15} {: <15}".format('| Id Karyawan', ' | Nama Karyawan', ' | Jabatan', '  | Gaji', '   | KPI'))
                                    print('----------------------------------------------------------------------------------------|')

                                    print(f'''| {database['Id_karyawan'][index_find]:<15}| {database['nama_karyawan'][index_find]:<15}| {database['jabatan'][index_find]:<15}| {database['gaji'][index_find]:<15}| {database['kpi'][index_find]:<15}''')
                                    print('----------------------------------------------------------------------------------------|')
                                    break
                                else:
                                    counter += 1

                            B = input('Apakah Anda Yakin Mengubah Data diatas? \nYes = 1 \nNo = 0 \nPilih Angka: ')

                            if B == '1':
                                main_menu_ubah()                                
                            elif B == '0':
                                angka2()        
                            else:
                                print(' ')
                                print('!!harap memasukan sesuai angka di atas!!')
                                print(' ')
                        
                    else:        
                        counter +=1
                
                if counter == len(database['Id_karyawan']):
                    print(" ")
                    print('..........................................................')
                    print('Maaf ID yang Anda Input Tidak Tersedia di Data Base kami:)')
                    print('"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
                    print(" ")
                    break
            
            else:
                print('')
                print('------------------------------------')
                print('Ulangi Input ID dalam Bentuk Angka!!')
                print('-------------------------------------')
                break

#--------------------------------------------------------------------------------
    while True:
        print('.......................................................')
        lanjutkan = input('MERUBAH DATA = 1,BACK = 0: ')
        if lanjutkan == '1':
            merubah_data()
        elif lanjutkan == '0':
            main_menu()
        else:
            print(' ')
            print('--------------------------------')
            print('Silakan Masukan Angka yang benar')
            print('`````````````````````````````````')  
            print(' ')


# #######################################MENU DELETE############################################

def angka3():
    print('===============Menghapus Data Karyawan===================')
    print('pilih untuk melanjutkan proses!')
    def hapus_data():
        print(' ')
        input_id = input('masukan id karyawan: ')
        while True:
            if input_id.isnumeric():
                t_h = int(input_id) 
                counter = 0
                for i in range(len(database['Id_karyawan'])):
                    if t_h == database['Id_karyawan'][i]:
                        while True:
                            B = input('Apakah Anda Yakin Menghapus Data Ini? \nYes = 1 \nNo = 0 \nPilih Angka: ')
                            if B == '1':
                                del database ['Id_karyawan'][i]
                                del database['nama_karyawan'][i]
                                del database['jabatan'][i]
                                del database['gaji'][i]
                                print(' ')
                                print('Data Berhasil di hapus')
                                break
                            elif B == '0':
                                angka3()
                            else:
                                print('Masukan Angka Sesuai di Atas!!')
                        break
                    else:
                        counter +=1
                        if counter == len(database['Id_karyawan']):
                            print('------------------------------------------')
                            print('Maaf Data di Data Base Kami Tidak Tersedia')
                            print('------------------------------------------')
                            print(' ')
                
                break
            else:
                print(' ')
                print('------------------------------------')
                print('Ulangi Input ID dalam Bentuk Angka!!')
                print('------------------------------------')
                break
            
    while True:
        print('.......................................................')
        lanjutkan = input('MENGHAPUS DATA = 1,BACK = 0: ')
        if lanjutkan == '1':
            hapus_data()
        elif lanjutkan == '0':
            main_menu()
        else:
            print(' ')
            print('--------------------------------')
            print('Silakan Masukan Angka yang benar')
            print('````````````````````````````````')  
            print(' ')
            
def angka5():
    while True:
        C = input('Apakah Anda Yakin Mengubah Nama diatas? \nYes = 1 \nNo = 0 \nPilih Angka: ')
        if C =='1':
            print('===============EXIT===================')
            print('===========TERIMA KASIH================')
            exit()  

        elif C == '0':
            print('')
            main_menu()  
        else:
            print(' ')
            print('!!harap memasukan sesuai angka di atas!!')
            print(' ')

def main_menu ():
    print('===============Data Base Karyawan===================')
    print('1.','Report Data Karyawan')
    print('2.','Menambahkan Data Karyawan')
    print('3.','Mengubah Data Karyawan')
    print('4.','Menghapus Data Karyawan')
    print('5.','Exit')
    print(' ')
    input_main_menu = input('Silakan pilih menu dengan input angka 1-5:')
    print(' ')

    if input_main_menu == '2':
        angka1()
    elif input_main_menu == '3':
        angka2()
    elif input_main_menu == '4':
        angka3()
    elif input_main_menu == '1':
        angka4()
    elif input_main_menu == '5':
        angka5()
    else:
        print(' ')
        print('--------------------------------')
        print('Silakan Masukan Angka yang benar')
        print('`````````````````````````````````')  
        print(' ')
        main_menu()

main_menu()
    
