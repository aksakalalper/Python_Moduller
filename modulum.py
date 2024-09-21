class KareAlma(): 
    def __init__(self,sayi):
        self.sayi=sayi
    def Sonuc(self):
        return self.sayi**2
        
     


def yardim (x):
    print('modul uzerindeki sayi integer ve sayilar dizisine erisebilirsiniz. ')
    
sayi=10

sayilar=[1,2,3]

kisiler={
"isim":"ahmet",
"yas":25,
"sehir":"izmir"
}
print('modul eklendi.')

sayi2=KareAlma(5)
sayi3=sayi2.Sonuc()
print(sayi3)


