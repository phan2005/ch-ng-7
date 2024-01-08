a=int(input("số tiền muốn đổi:"))
so_to_1=a//500000
tien_con_lai1=a%500000
so_to_2=tien_con_lai1//200000
tien_con_lai2=tien_con_lai1%200000
so_to_3=tien_con_lai2//100000
tien_con_lai3=tien_con_lai2%100000
so_to_4=tien_con_lai3//50000
tien_con_lai4=tien_con_lai3%50000
print("số tờ 500k:",so_to_1)
print("số tờ 200k:",so_to_2)
print("số tờ 100k:",so_to_3)
print("số tờ 50k:",so_to_4)
print("sô tiền thừa:",tien_con_lai4)