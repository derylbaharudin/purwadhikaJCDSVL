# Name : Deryl Baharudin
# Purwadhika Data Science and Machine Learning
# Video Learning After Office

# Sistem Informasi Rumah Sakit

dataPasien = {
    1:['A1','A2','B1','B2','C1','C2'],
    2:['Daud Marfuah S.','Deryl si kasep','Nurjannah Hestiah','Qomaruddin adjah','Budi doremifasol','Ando separuh aku'],
    3:[3243782390541278,1278542389547876,7623905489129034,6745927415490212,2389437812094378,9365284725399521],
    4:[12,32,43,49,28,55],
    5:['Rawat Inap','Rawat Jalan','Rawat Inap','Rawat Jalan','Rawat Jalan','Operasi'],
}

nama_kolom = {
    1:'ID',
    2:'NAMA PASIEN',
    3:'NOMOR KTP',
    4:'UMUR',
    5:'PERAWATAN'
}

def main_menu():
    while True:
        print('''
        ========== Data Pasien Rumah Sakit Deryl ==========
        1. Report Data Pasien Rumah Sakit
        2. Registrasi Pasien Baru
        3. Update Data Pasien
        4. Hapus Data Pasien
        5. Exit
        ===================================================
        ''')
        pilihan = input('Silahkan pilih menu [1-5]: ')
        if pilihan == '1':
            pilihan1()
        elif pilihan == '2':
            pilihan2()
        elif pilihan == '3':
            pilihan3()
        elif pilihan == '4':
            pilihan4()
        elif pilihan == '5':
            print('Sampai Jumpa!')
            print('Program Selesai.')
            selesai()
        else:
            print(f'*****Pilihan {pilihan} tidak ada dalam daftar!*****')

def pilihan1():
    while True:
        print('''
        ++++++++++ Report Data Pasien Rumah Sakit ++++++++++
        1. Report Seluruh Data Pasien
        2. Report Data Tertentu
        3. Kembali ke Menu Utama
        ++++++++++++++++++++++++++++++++++++++++++++++++++++
        ''')
        pilihan1 = input('Silahkan pilih menu [1-3]: ')
        if pilihan1 == '1':
            reportSeluruh()
        elif pilihan1 == '2':
            reportTertentu()
        elif pilihan1 == '3':
            main_menu()
        else:
            print(f'*****Pilihan {pilihan1} tidak ada dalam daftar!*****')

def reportSeluruh():
    table = 'Id\t| Nama Pasien\t\t| Nomor KTP\t\t| Umur\t| Perawatan\t|\n\n'
    for i in range(len(dataPasien[1])):
        for j in range(1,len(dataPasien)+1):
            data = dataPasien[j][i]
            table += f'{data}\t| '
        table += '\n'
    print(table)

def reportTertentu():
    table = 'Id\t| Nama Pasien\t\t| Nomor KTP\t\t| Umur\t| Perawatan\t|\n\n'
    cari_id = input('Masukan Id Pasien yang akan dicari: ').upper()
    try:
        index_id = dataPasien[1].index(cari_id)
        for i in range(1,len(dataPasien)+1):
            data = dataPasien[i][index_id]
            table += f'{data}\t| '
        print(table)
    except ValueError as VE:
        print(f'Maaf, Id {cari_id} Tidak Ada dalam Database Pasien Rumah Sakit')

def pilihan2():
    while True:
        print('''
        ++++++++++ Registrasi Pasien Baru ++++++++++
        1. Tambah Data Pasien Baru
        2. Kembali ke Menu Utama
        ++++++++++++++++++++++++++++++++++++++++++++
        ''')
        pilihan2 = input('Silahkan pilih menu [1-2]: ')
        if pilihan2 == '1':
            tambahPasien()
        elif pilihan2 == '2':
            main_menu()
        else:
            print(f'*****Pilihan {pilihan2} tidak ada dalam daftar!*****')

def tambahPasien():
    while True:
        id_baru = input('Masukan id Pasien: ').title()
        if id_baru in dataPasien[1]:
            print(f'Data {id_baru} sudah ada.')
        else:
            break
    
    while True:
        nik_baru = int(input('Masukan NIK Pasien: '))
        if len(str((nik_baru))) == 16:
            break
        else:
            print('Format Nomor KTP tidak sesuai (16 angka)!')
    
    nama_baru = input('Masukan Nama Pasien: ').title()
    umur_baru = int(input('Masukan Umur Pasien: '))
    perawatan_baru = input('Masukan Jenis Perawatan Pasien: ').title()
    list_update = [id_baru, nama_baru, nik_baru, umur_baru, perawatan_baru]
        
    while True:
        dataUpdate = input('Apakah data akan disimpan [Y/N]: ').upper()
        if dataUpdate == 'Y':
            print('Data Tersimpan')
            break
        elif dataUpdate == 'N':
            print('Data Tidak Tersimpan')
            pilihan2()
        else:
            print(f'Pilihan {dataUpdate} tidak tersedia!')
        
    for i, item in enumerate(list_update):
        dataPasien[i+1].append(item)
    
    pilihan2()

def pilihan3():
    while True:
        print('''
        ++++++++++ Update Data Pasien ++++++++++
        1. Update Data Pasien
        2. Kembali ke Menu Utama
        ++++++++++++++++++++++++++++++++++++++++
        ''')
        pilihan3 = input('Silahkan pilih menu [1-2]: ')
        if pilihan3 == '1':
            updatedata()
        elif pilihan3 == '2':
            main_menu()
        else:
            print(f'*****Pilihan {pilihan3} tidak ada dalam daftar!*****')

def updatedata():
    while True:
        ubah_id = input('Masukan Id Pasien yang akan diubah: ').title()
        if ubah_id in dataPasien[1]:
            break
        else:
            print(f'Data {ubah_id} tidak ada.')
    
    table = 'Id\t| Nama Pasien\t\t| Nomor KTP\t\t| Umur\t| Perawatan\t|\n\n'
    index_id = dataPasien[1].index(ubah_id)
    for i in range(1,len(dataPasien)+1):
        data = dataPasien[i][index_id]
        table += f'{data}\t| '
    print(table)
    
    while True:
        dataUpdate = input('Tekan Y jika ingin lanjut update data dan N jika ingin cancel update [Y/N]: ').upper()
        if dataUpdate == 'Y':
            while True:
                kolom = input('Masukan Kolom yang akan diupdate: ').upper()
                if kolom in nama_kolom.values():
                    break
                else:
                    print(f'Tidak ada kolom {kolom} pada database Rumah Sakit')
            
            for i, item in enumerate(nama_kolom.values()):
                if kolom == item:
                    idx_col = i+1
            
            if (idx_col == 4):
                data_baru = int(input(f'Masukan {kolom.title()} Baru: '))
            elif (idx_col == 3):
                while True:
                    data_baru = int(input(f'Masukan {kolom.title()} Baru: '))
                    if len(str(data_baru)) == 16:
                        break
                    else:
                        print('Format Nomor KTP tidak sesuai (16 angka)!')
            else:
                data_baru = input(f'Masukan {kolom.title()} Baru: ').title()
            
            while True:
                dataupdate = input('Apakah data akan diupdate? [Y/N]: ').upper()
                if dataupdate == 'Y':
                    dataPasien[idx_col][index_id] = data_baru
                    print('Data Updated!')
                    pilihan3()
                elif dataupdate == 'N':
                    print('Data tidak diupdate!')
                    pilihan3()
                else:
                    continue
        elif dataUpdate == 'N':
            print('Data tidak diupdate.')
            pilihan3()
        else:
            continue

def pilihan4():
    while True:
        print('''
        ++++++++++ Hapus Data Pasien ++++++++++
        1. Hapus Data Pasien
        2. Kembali ke Menu Utama
        +++++++++++++++++++++++++++++++++++++++
        ''')
        pilihan4 = input('Silahkan pilih menu [1-2]: ')
        if pilihan4 == '1':
            hapusdata()
        elif pilihan4 == '2':
            main_menu()
        else:
            print(f'*****Pilihan {pilihan4} tidak ada dalam daftar!*****')

def hapusdata():
    while True:
        hapus_id = input('Masukan Id Pasien yang akan dihapus: ').title()
        if hapus_id in dataPasien[1]:
            break
        else:
            print(f'Data {hapus_id} tidak ada.')
    
    table = 'Id\t| Nama Pasien\t\t| Nomor KTP\t\t| Umur\t| Perawatan\t|\n\n'
    index_id = dataPasien[1].index(hapus_id)
    for i in range(1,len(dataPasien)+1):
        data = dataPasien[i][index_id]
        table += f'{data}\t| '
    print(table)
    
    while True:
        datahapus = input('Apakah Data akan dihapus? [Y/N]: ').upper()
        if datahapus == 'Y':
            for i in range(1,len(dataPasien)+1):
                dataPasien[i].pop(index_id)
            print('Data Berhasil Dihapus!')
            pilihan4()
        elif datahapus == 'N':
            print('Data tidak terhapus!')
            pilihan4()
        else:
            continue

def selesai():
    print('*******************************************************************')
    
# Mulai Program
main_menu()