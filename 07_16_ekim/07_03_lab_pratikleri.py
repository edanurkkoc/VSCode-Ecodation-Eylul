
sirket={
    "departman":{
        "yazılım":["ali","memet"],
        "muasebe":["irem","elif"]
                },
    "calisanSayisi":100,
    "ceo":"Ali Kemal",
    "telefonlar":{
        "istanbul":"02126656656",
        "ankara":"0321456"
                 },
    "sirketArabalari":["i20","renault megan","ford focus"],
    "sirketArabalari2":{
            "i20":True,
            "renault megan":False,
            "ford focus":True
                       }
}
"""
print(sirket["ceo"])
print(sirket["calisanSayisi"])
print(sirket["telefonlar"]["ankara"])
print(sirket["sirketArabalari"][0])
print(sirket["departman"]["muasebe"][1])
"""
"""
#birinin sorusu
ad="edanur kocakoc"
adSoyadList=ad.split()
print(adSoyadList[0])
print(adSoyadList[1])
dSamples={
    adSoyadList[0]:adSoyadList[1]
}
print(dSamples)
"""
for key,value in sirket["sirketArabalari2"].items():
    if value==False:
        cvp=input(f"otoparktaki araba{key} almak ister misin 1/0: ")
        if cvp=="1":
            sirket["sirketarabalari2"][2]=True
print(sirket["sirketArabalari2"])







