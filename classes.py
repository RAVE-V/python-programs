class animal:
    def __init__(self,colour,legs):
        self.colour=colour
        self.legs=legs
    
        ammu=cat(self)
        

class cat(animal):
    def sound():
        print "meeow"
        

ammu = animal("white",4)
print (ammu.colour)
print ammu.sound()
