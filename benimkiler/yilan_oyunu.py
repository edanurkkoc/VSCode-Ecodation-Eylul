#TURTLE KÜTÜPANESİ:Kodları kullanarak grafiksel tasarımlar yapmayı ve kodların çalışma mantığını görsel bi rşekilde görmemizi sağlar
#ONKEYPRESS:1.fonks 2. ise atanması gereken değer(yön tuşu)
import turtle
import time #çalışması için bekleme süresi oluşturur 
import random #yem yendiği zaman random bi yerde tekrar gözüksün
#oyun ekranı oluşturma
oyunEkranı=turtle.Screen()
oyunEkranı.tracer(0)
oyunEkranı.setup(600,600)
oyunEkranı.bgcolor("black")

#Yılan oluşturma
yılan=turtle.Turtle()
yılan.shape("square")
yılan.color("red")
yılan.speed(0)
yılan.penup()#yılanın arkada bıraktığı izi siliyo
yılan.goto(-200,0)
yılan.yön="dur"

#Yemi oluşturma
yem=turtle.Turtle()
yem.shape("square")
yem.color("yellow")
yem.speed(0)
yem.penup()#yılanın arkada bıraktığı izi siliyo
yem.goto(0,0)
yem.yön="dur"

#Yılanın areketlerini oluşturma
def yukarı():
    if yılan.yön!="aşağı":
        yılan.yön="yukarı"
def aşağı():
    if yılan.yön!="yukarı":
        yılan.yön="aşağı"
def sağ():
    if yılan.yön!="sol":
        yılan.yön="sağ"
def sol():
    if yılan.yön!="sağ":
        yılan.yön="sol"
#Yılanın areketlerini tuşlara atıyoruz
oyunEkranı.listen()
oyunEkranı.onkeypress(yukarı,"w")
oyunEkranı.onkeypress(aşağı,"s")
oyunEkranı.onkeypress(sağ,"d")
oyunEkranı.onkeypress(sol,"a")

oyunEkranı.onkeypress(yukarı,"Up")
oyunEkranı.onkeypress(aşağı,"Down")
oyunEkranı.onkeypress(sağ,"Right")
oyunEkranı.onkeypress(sol,"Left")

#Şimdi yılanın areketleri için fonksiyon yazıyoruz
def hareket_et():
    if yılan.yön=="yukarı":
        y = yılan.ycor()
        yılan.sety(y+20)
    if yılan.yön=="aşağı":
        y = yılan.ycor()
        yılan.sety(y-20)
    if yılan.yön=="sağ":
        x = yılan.xcor()
        yılan.setx(x+20)
    if yılan.yön=="sol":
        x = yılan.xcor()
        yılan.setx(x-20)
bölümler=[]
while True:
    oyunEkranı.update()
    
    
    if yılan.xcor()>290 or yılan.xcor()<-290 or yılan.ycor()>290 or yılan.ycor()<-290:
        time.sleep(1)
        yılan.goto(-200,0)
        yılan.yön="dur"

    #kenara çarptığı zaman sıfırlansın
        for i in bölümler:
            i.goto(2000,2000)
         
        bölümler.clear()
          


    if yılan.distance(yem)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)  
        yem.goto(x,y)

        yeniBölüm=turtle.Turtle()
        yeniBölüm.speed(0)
        yeniBölüm.shape("square")
        yeniBölüm.penup()
        yeniBölüm.color("red")
        bölümler.append(yeniBölüm)
    #yem yediği zaman büyümesi
    for i in range(len(bölümler)-1,0,-1):
        x=bölümler[i-1].xcor()
        y=bölümler[i-1].ycor()
        bölümler[i].goto(x,y)

    if len(bölümler)>0:
        x=yılan.xcor()
        y=yılan.ycor()
        bölümler[0].goto(x,y)
    
    hareket_et()

    #kendine çarptığı zaman sıfırlansın
    for i in bölümler:
        if i.distance(yılan)<20:
            time.sleep(1)
            yılan.goto(-200,0)
            yılan.yön="dur"

            #aynı skorla devam etmek için
            for i in bölümler:
                i.goto(2000,2000)
            #yılanın parçalarını buraya atıyoruz
            bölümler.clear()



    time.sleep(0.1)


    