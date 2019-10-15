thisdict = {
    "Marka" : "Ford",
    "Model" : "Mustang",
    "ÜretimYılı" : "1980"
}

# print(thisdict)
#
#
# print(thisdict["Model"])
#
# a = thisdict.get("Model")
# print(a)
#
# thisdict["ÜretimYılı"] = 1970
#
# print(thisdict.get("ÜretimYılı"))
#
# for i,k in thisdict.items():
#     print(" Anahtar Kelimeniz = " + i + " Değeriniz ise = "+ k)

# if "Model" in thisdict:
#     print("Evet model bulunmakta")

# print(len(thisdict))

# thisdict["Rengi"] = "Mavi" # Ekleme işlemi yapar
# # print(thisdict)

# thisdict.pop("Model") # Silme işlemini yapar
# print(thisdict)

# thisdict.popitem() # Son anahtar kelime ve değerini siler
# print(thisdict)

# del thisdict["Marka"] # istediğiniz anahtar kelime ve değerini siler
# print(thisdict)

# thisdict.clear()
# print(thisdict)

# benimSozluk = thisdict.copy()
# print(benimSozluk)

# benimSozuluk = dict(thisdict)
# print(benimSozuluk)
# #
# # # Ailemiz = {
# # #     "Baba" : {
# # #         "Adı" : "Mahmut",
# # #         "Yaşı" : "49"
# # #     },
# # #     "Anne" : {
# # #         "Adı" : "Selin",
# # #         "Yaşı" : "45"
# # #     },
# # #     "Çocuk" : {
#         "Adı" : "Burak",
#         "Yaşı" : "18"
#     }
# }
#
# print(Ailemiz)

# Baba = {}
# Anne = {}
# Ailemiz = {"Baba" : Baba, "Anne": Anne}