#STANDARD VARIABLES
startscherm = True

#SETUP
def setup():
    global logo
    global evil32
    global bungee32
    global startknop
    size(1280,720)
    bgImg = loadImage("img/achtergrond.jpg")
    background(bgImg)
    noStroke()
    logo = loadImage("img/Skelet.png")
    evil32 = createFont("data/Evil_Empire.otf", 32)
    bungee32 = createFont("data/Bungee-Regular.ttf", 32)
    startknop = loadImage("img/Start knop.png")
    
def draw():
    if startscherm:
        #LOGO
        image(logo,555,10,200,220)
        #ESCAPE THE BOARD
        textFont(evil32)
        textSize(70)
        fill(250,250,250)
        text("Escape The Board", 415,320)
        #START KNOP
        image(startknop,403,370,476,120) #3,97
        textFont(bungee32)
        #VRAAG INVOEREN EN EXIT
        fill("#AEAEAE")
        text("Vraag Invoeren", 489,570)
        fill("#FF686B")
        text("EXIT", 596,640)
        #TEAM 4
        textSize(25)
        fill(250,250,250)
        text("Team 4", 1150,700)
        
