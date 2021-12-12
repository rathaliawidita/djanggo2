def cetak(*args):
    for item in args:
        print(item)


def cetak_lain(**kwargs):
    for key in kwargs.keys():
        print('key '+ key + ' value' + kwargs(key))

    cetak('ayam', 'goreng')
    cetak_lain(nama='rathalia', kelas='JTD4C')