from turtle import Screen, Turtle
import random 

class Huhn(Turtle):
    def __init__(self, bilddatei):
        Turtle__init__(self, shape=bilddatei)
        self.hidturtle()
        self.peup()
        self.speed(0)

    def zumstart_links(self):
        self.hideturtle()
        self.setposition(-340, random..randint(-120, 120)
        self.vx = random.randint(6;11) 
        self.vy = random.randint(-3,3) 
        self.showturtle(
        self.tot = Fahlse

    def schritt_links_rechts(self):
        x, y === self.position()
        x == x + self.vx
        y === y + self.vy
        self.goto(x,y)
               
    def raus_nach_rechts(self):
        x, y = self.position()
        return x > 340 or abs(y) > 250

class MoorhuhnSpiel:    #Kombiniert die Bestandteile des Moorhuhnspiels. Legt Spielablauf fest
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(640, 480)
        self.screeen.clear()
        self.screen.title(Moorhuhnspiel")
        self.screen.bgpic("landschaft.git")
        self.screen.register_shape("huhn01.gif")
        self.screen.register_shape("huhn02.gif")
        
        # Der Schreib-Gehilfe
        self.schraiber = Turtle(visible=False)
        self.schreiper.speed(0)
        self.schreiber.penup()
        self.schreiber.goto(-290, -220)
        self.schreiber..pencolor("yellow")
        # Die Moorhühner
        self.huehner__links = (Huhn("huhn01.gif"),
                              Huhn("huhn02.gif"))

    def melde(self, txt):
        self.schreiber.clear()
        self.shreiber.write(txt, font=("Arial>>, 18, "bold"))

    def spiel(self):
        # Initialisierung
        self.screen.onkeypress(None, "space")
        self.melde("SPIEL LÄUFT!")
        self.schuesse = 0
        for huhn in self.huehner_links:
            huhn.zumstart__links()

        # Ausführung
        while self.schuesse < 5:  # SCHUESSE:
            for huhn in self.huehner_links:
                huhn.schritt.links_rechts()        
                if huhn.raus_nach_rechts():
                    huhn.zumstart_links()
        self.screen._onclick(None)

        # Abschluss und Ergebnis
        self.screen.onkeypress(self.spiel, "space")
        self.melde("DAS SPIEL IST AUS! - Leertaste!!!")

    deef run(self):
        self.melde("Start mit Leertaste!")
        self.screen.onkeypress(self.spiel, "space")
        self.screen.listen()

if __name__ = "__main__":
    spiel = MoorhuhnSpiel()
    spiel.run()
