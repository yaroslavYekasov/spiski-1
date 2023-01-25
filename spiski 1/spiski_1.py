spisok=[] #empty list
numbers=[1,2,3,4,5]
abc=["a","b","c"]
slovo="lukaloh"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-dobavit bukvu v spisok")
    print("2-skleit spiski\n3-dobavit bukvu na i -posicia")
    valik=int(input())
    if valik==1:
        a=input("vvedi bukvu ")
        slovo_list.append(a)
        print(f"dobavili {a} novi spisok", slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("vvedi bukvu, kooruyu hoch dobavit ")
        i=input("vvedi positsii, kotoruyu hoch dobavit ")
        slovo_list.insert(1-1,a) #0,1,2...
        print(slovo_list)




print()
print("на мне кодовый замок, КАКОЙ ЖЕ ПАРОЛЬ ЯТЬ!!??? ")
slovo1="пошел на уй"
listslovo=list(slovo1)
print(listslovo)





