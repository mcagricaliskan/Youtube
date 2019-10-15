# metin1 = "Selamlar. Benim adım"
# metin2 = "Çağrı ve Yotube videoları çekiyorum."
#
#
# print(metin1 + " " + metin2)
#
# print("{} {}".format(metin1,metin2))


# Sıcaklık = 38
# Nem = "%68"
# HavaDurumu = "Güneşli"
#
# print("Bugün hava sıcaklığı {} derece ve nem oranı {}. Bugünün hava durumu ise {}".format(Sıcaklık,Nem,HavaDurumu))
# print("Bugün hava sıcaklığı " + str(Sıcaklık) + " derece ve nem oranı " + Nem + ". Bugünün hava durumu ise " + HavaDurumu )
# print(f"Bugün hava sıcaklığı {Sıcaklık} derece ve nem oranı {Nem}. Bugünün hava durumu ise {HavaDurumu}")
#
# sayı1 = 100
# sayı2 = 200
#
# print("{} ile {} toplamı = {} \n {} in karesi {} ve {} karesi {}".format(sayı1,sayı2,sayı1+sayı2,sayı1,sayı1**2,sayı2,sayı2**2))
#
# print(f"{sayı1} ile {sayı2} toplamı = {sayı1 + sayı2} \n {sayı1} in karesi {sayı1**2} ve {sayı2}in karesi {sayı2**2}")



def sayı1():
    return 100
def sayı2():
    return 200


print(f"{sayı1()} sayısı ile {sayı2()} sayısının toplamı = {sayı1() + sayı2()}")

print(f"{(lambda x: x**2)(123421)}")