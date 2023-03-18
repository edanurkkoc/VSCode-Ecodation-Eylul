""" 
youtube abone sayısında çıktı anında son ek ekleme 
-izlenme 18000 → 18 B Abone 
-izlenme 1800000 → 1.8 Mn Abone 
-izlenme 1800000000 → 1.8 Ml Abone
"""
izlenme=18950
if 1000<=izlenme<=999999:
    print(f"{izlenme//1000}B")
elif 1000000<=izlenme<=999999999:
    print(f"{(izlenme//1000)/1000}Mn")
elif 1000000000<=izlenme<=99999999999:
    print(f"{(izlenme//1000000)/1000}Ml")
