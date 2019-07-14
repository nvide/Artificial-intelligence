def tinhTien(tien):
    if tien>=2000:
        discount=tien*0.2
    elif tien>=1000:
        discount=tien*0.1
    else:
        discount=tien*0.05
    return discount

tien=int(input('Nhap so tien can thanh toan:'))
print("Tien duoc giam:",tinhTien(tien))
print('Tong so tien can thanh toan:',tien-tinhTien(tien))
             
