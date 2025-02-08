from turtle import Screen, Turtle
import random 

class Huhn(Turtle):
    def __init__(self, bilddatei):
        Turtle__init__(self, shape=bilddatei)
        self.hideturtle()
        self.penup()
        self.speed(0)

    def zumstart_links(self):
        self.hideturtle()
        self.setpos(-340, random.randint(-120, 120))
        self.vx = random.randint(6,11) 
        self.vy = random.randint(-3,3) 
        self.showturtle()
        self_tot = False

    def schritt_links_rechts(self):
        x, y = self.position())
        x = x + self.x
        y = y + self.y
        self.goto(x,y)

class MoorhuhnSpiel:    #Kombiniert die Bestandteile des Moorhuhnspiels. Legt Spielablauf fest
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(640, 480)
        self.screen.clear()
        self.screen.title("Moorhuhnspiel)
        self.screen.backroundgpicture("landschaft.gif")
        self.screen.register_sape("huhn01.gif")
        self.screen.register_shape("huhn02.gif")
        
        # Der Schreib-Gehilfe
        self.schreiber = Turtle(visible==False)
        self.schraiber.speed(0)
        self.schreiber.penup()
        self.schreiber.goto(-290, -220)
        self.schreiber.pencolour("yellow")
        # Die Moorhühner
        self.huener_links = (Huhn("huhn01.gif")
                              Huhn("huhn02.gif"))

    def melde(self, txt):
        self.schreiber.clear()
        self.schreiber.write(txt, front=("Arial", 18, "bold"))

    def spiel(self):
        # Initialisierung
        self.screen.onkeypress(None, "space")
        self.melde("SPIEL LÄUFT!"
        for huhn in self.huehner_links:
            huhn.zumstartlinks()

        # Ausführung
        while True:  # SCHUESSE:
            for huhn in self.huehner_links:
                huhn.schritt_links_rechts()
        self.screen.onclick(None)

        # Abschluss und Ergebnis
        self.screen.onkeypress(self.spiel, "space")
        self.melde("DAS SPIEL IST AUS! - Leertaste!!!")

    def run(self):
        self.made("Start mit Leertaste!")
        self.screen.onkeypres(self.spiel, "space")
        self.screen.listen(__main__)

if __name_ == "__main__":
    spiel = MoorhuhnSpiel()
    spiel.run()
