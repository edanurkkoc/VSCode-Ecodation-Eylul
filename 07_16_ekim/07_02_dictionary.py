pDiliOzellikleri={
    "programlama dili":"pyton",
    "seviye":"yüksek",
    "interpreter":True,
    "version":"3.10"

}

kronBike={
    "jant":23,
    "renk":("sarı","kırmız"),
    "vites":24,
    "karbon-çelik":["karbon","çelik"],
    "turu":"bisiklet"
}
print(kronBike)
print(type(kronBike))
print(kronBike["turu"])
print(kronBike.keys())
for i in kronBike.keys():
    print(i)
    
print(kronBike.values())
for i in kronBike.values():
    print(type(i)," ",i)

#override ->Üzerine yazma
kronBike={
    "jant":23,
    "renk":("sarı","kırmız"),
    "vites":24,
    "karbon-çelik":["karbon","çelik"],
    "turu":"bisiklet",
    "jant":21
}
#print(kronBike)
kronBike["vites"]=21#yerine bunu atıyo,
kronBike["sele"]="T.M"#son satıra bunu ekliyor
del kronBike["kadro"]#bu satırı temizliyo
for key,value in kronBike.items():
    print(key,value)
    #print(key)
    #print(value)
kronBike.clear()#boş bir dctionary ile karşılaşırız,{};epsini siliyo yani
print(kronBike)

#value ve keyleri sırasıyla yazdıran kod
pDiliOzellikleri={
    "programlama dili":"pyton",
    "seviye":"yüksek",
    "interpreter":True,
    "version":"3.10"
}
myList=list(pDiliOzellikleri.keys())
myList.sort()#artan alfabetik sıraya göre sıralıyo
#myList.sort(reverse=True) ->Burda ise azalan alfabetik sıraya göre sıralıyo
for i in myList:
    print(pDiliOzellikleri[i])#print(i,pDiliOzellikleri[i]) bu da key dillerini yazar


