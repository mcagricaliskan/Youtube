import qrcode


QR = qrcode.make("Mehmet Çağrı Çalışkan")
QR.save("ilkQR.png")


# qr = qrcode.QRCode(
#     version=1 , # 1-40 arasında olabilir. # Ne kadar uzun veriniz varsa o kadar büyük olmalı
#     error_correction= qrcode.constants.ERROR_CORRECT_M,
#     box_size=5, #Genel Büyüklük
#     border=1, # QR etrafındaki boşluk
# )
#
# qr.add_data("Python, nesne yönelimli, yorumlamalı, birimsel (modüler) ve etkileşimli yüksek seviyeli bir programlama dilidir.[3]Girintilere dayalı basit sözdizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır. Bu da ona söz diziminin ayrıntıları ile vakit yitirmeden programlama yapılmaya başlanabilen bir dil olma özelliği kazandırır.Modüler yapısı, sınıf dizgesini (sistem) ve her türlü veri alanı girişini destekler. Hemen hemen her türlü platformda çalışabilir. (Unix , Linux, Mac, Windows, Amiga, Symbian). Python ile sistem programlama, kullanıcı arabirimi programlama, ağ programlama, web programlama, uygulama ve veritabanı yazılımı programlama gibi birçok alanda yazılım geliştirebilirsiniz. Büyük yazılımların hızlı bir şekilde prototiplerinin üretilmesi ve denenmesi gerektiği durumlarda da C ya da C++ gibi dillere tercih edilir.")
# qr.make(fit=True)
#
# QRresim = qr.make_image(fill_color = "black", back_color = "white")
# QRresim.save("Ücüncü.png")