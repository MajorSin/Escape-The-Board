import Router

#Spel gereed stellen.
def setup():
    #Grootte van het spel.
    size(1280, 720)
    
    #Stijl.
    noStroke()
    noCursor()
    
    #Achtergrond inladen.
    global background_image
    background_image = loadImage('images/horror-background.jpg')
    
    #Standaard font inladen.
    global font
    font = createFont('Arial', 50)
    
    #Gereed stellen wat nodig is in Main.
    Router.prep()

#Ververst elke keer wat getekent wordt.
def draw():
    #Dit ververst de achtergrond.
    background(background_image)
    
    #Standaard font tekst.
    textFont(font)
    
    #Toont het gehele scherm van de UserInput.
    Router.display_screen()
    
def mousePressed():
    Router.mousePressed()
    
def keyPressed():
    Router.keyPressed()
