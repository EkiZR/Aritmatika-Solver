from prettytable import PrettyTable

def menu():
	table = PrettyTable(["No", "Menu"])
	table.add_row(["1", "Barisan Aritmatika"])
	table.add_row(["2", "Jika info suku hanya 2"])
	table.add_row(["3", "Deret Aritmatika"])
	print(table)

menu()
print("")
pilih = input("Pilih menu : ")
print("")

def aritmatika1():
	print("Barisan Aritmatika")
	print("-------------------------------------")
	Un = int(input("Masukan Suku ke-n : "))
	a = int(input("Masukan Suku Pertama :  "))
	b = int(input("Masukan Bedanya ⏩ (U2-U1) : "))
	print("Un = a + (n-1)b")
	print("U{} = {} + ({}-1){}".format(Un, a, Un, b))
	print("U{} = {} + {}.{}".format(Un, a, Un - 1, b))
	print("U{} = {} + {}".format(Un, a, (Un - 1) * b))
	hasilakhir = a + (Un - 1) * b
	print("U{} = {}".format(Un, hasilakhir))
	print("")
	back = str(input("Ketik ('y') jika ingin lihat menu lain : "))

	if back == ('y'):
		menu()
		pilih = int(input("Masukan Nomor Menu : "))
	if pilih == 1:
		return aritmatika1()
	if pilih == 2:
		return aritmatika2()
	if pilih == 3:
		return aritmatika3()


def aritmatika2():
	print("------------------------------")
	info1 = int(input("Masukan Suku ke-n : "))
	print("------------------------------")
	info2 = int(input("Masukan Suku ke-n : "))
	print("------------------------------")
	print("U{} = ".format(info1))
	print("U{} = ".format(info2))
	print("-------------------------------------")
	hasil1 = int(input("Masukan Nilai U{} : ".format(info1)))
	print("-------------------------------------")
	hasil2 = int(input("Masukan Nilai U{} : ".format(info2)))
	print("-------------------------------------")
	print("")

	print("U{} = {}".format(info1, hasil1))
	print("a + {}-1 = {}".format(info1, hasil1))
	print("a + {}b = {}".format(info1 - 1, hasil1))
	print("")
	print("U{} = {}".format(info2, hasil2))
	print("a + {}-1 = {}".format(info2, hasil2))
	print("a + {}b = {}".format(info2 - 1, hasil2))
	print("")
	print("Mencari Nilai b............(Metode eliminasi)")
	print("")
	print("a + {}b = {}".format(info2 - 1, hasil2))
	print("a + {}b = {}".format(info1 - 1, hasil1))
	print("__________________--")
	print("    {}b = {}".format(hasil2 - hasil1, (info2 - 1) - (info1 - 1)))
	print("      b = ", hasil2 - hasil1, "/", (info2 - 1) - (info1 - 1))
	nb = hasil2 - hasil1
	i21 = (info2 - 1) - (info1 - 1)
	nilaib = int(nb / i21)
	print("      b = ", (nilaib))
	print("")
	print("mencari nilai a............(Metode Substitusi)")
	print("a + {}b = {}".format(info1 - 1, hasil1))
	print("a + {}.{} = {}".format(info1 - 1, nilaib, hasil1))
	print(" a +", (info1 - 1) * nilaib, "= ", hasil1)
	print("     a =", hasil1, "-", (info1 - 1) * nilaib)
	print("     a =", hasil1 - (info1 - 1) * nilaib)
	print("")
	hasilakhir = int(input("Tentukan Suku ke-? : "))
	hasilakhir1 = hasilakhir - 1
	nilaia = hasil1 - (info1 - 1) * nilaib
	print("a + ( n - 1 ) b")
	print(nilaia, "+ (", hasilakhir, "- 1 ).", nilaib)
	print(nilaia, "+ (", hasilakhir - 1, ").", nilaib)
	print(nilaia, "+", hasilakhir1 * nilaib)
	print(nilaia + hasilakhir1 * nilaib)
	print("")
	print("Maka suku ke -", hasilakhir, "adalah", nilaia + hasilakhir1 * nilaib)
	print("")
	back = str(input("Ketik ('y') jika ingin lihat menu lain : "))
	if back == ('y'):
		menu()
		pilih = int(input("Masukan Nomor Menu : "))
	if pilih == 1:
		return aritmatika1()
	if pilih == 2:
		return aritmatika2()
	if pilih == 3:
		return aritmatika3()


def aritmatika3():
	print("")
	print("Deret Aritmatika")
	print("-------------------------------------")
	Sn = int(input("Tentukan jumlah n suku pertama : "))
	print("-------------------------------------")
	a = int(input("Masukan suku pertama barisan : "))
	print("-------------------------------------")
	b = int(input("beda ⏩ [itung sendiri U2-U1] : "))
	print("-------------------------------------")
	print("")
	print("Sn = n/2(2a + (n-1)b)")
	print("S{} = {}/2(2.{} + ({}-1)({})".format(Sn, Sn, a, Sn, b))
	print("S{} = {}({} + {}.({})".format(Sn, Sn / 2, 2 * a, Sn - 1, b))
	print("S{} = {}({} + {})".format(Sn, Sn / 2, 2 * a, ((Sn - 1) * b)))
	print("S{} = {}({})".format(Sn, Sn / 2, 2 * a + (Sn - 1) * b))
	nilaiakhir = int((Sn / 2) * (2 * a + (Sn - 1) * b))
	print("S{} = {}".format(Sn, nilaiakhir))
	print("")
	print("Jadi, Jumlah {} suku pertamanya adalah {}.".format(Sn, nilaiakhir))
	print("")
	back = str(input("Ketik ('y') jika ingin lihat menu lain : "))
	if back == ('y'):
		menu()
		pilih = int(input("Masukan Nomor Menu : "))
	if pilih == 1:
		return aritmatika1()
	if pilih == 2:
		return aritmatika2()
	if pilih == 3:
		return aritmatika3()


if pilih == ('1'):
	aritmatika1()

elif pilih == ('2'):
	aritmatika2()

elif pilih == ('3'):
	aritmatika3()
else:
	print("Menu tidak ada")
