import Main

#Spel gereed stellen.
def setup():
    #Grootte van het spel.
    size(1000, 1000)
    
    #Stijl.
    noStroke()
    noCursor()
    
    #Achtergrond inladen.
    global background_image
    background_image = loadImage('images/horror-background.jpg')

#Ververst elke keer wat getekent wordt.
def draw():
    #Dit ververst de achtergrond.
    background(background_image)
    
    #Standaard font tekst.
    textFont(createFont('Arial', 50))
    
    #Toont het gehele scherm van de UserInput.
    Main.data()
    
def mousePressed():
    Main.mousePressed()
    
def keyPressed():
    Main.keyPressed()
