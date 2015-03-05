
#Author:  Nadia Barbosa


# [1]

class Geometry(object): #initial class
    count = 0
    def __init__(self):
        self.uniqueID = Geometry.count
        print self.uniqueID
        Geometry.count = Geometry.count +1
        
# [2]

class Point(Geometry): #subclass for points
    def __init__(self, x, y):
        Geometry.__init__(self)
        self.x = x
        self.y = y
    
    def __str__(self): # to list points
        return "(%s, %s)"%(self.x, self.y)
    
    def equality(self, otherpoint): # use if to test equality
        if self.x == otherpoint.x and self.y == otherpoint.y:
            return "True"
        else:
            return "False"
            
    def identify(self, otherpoint): # use if to test uniqueIDs
        if self.uniqueID == otherpoint.uniqueID:
            return "True"
        else:
            return "False"

    def distance(self, otherpoint): # calculates distance using distance formula
        import math
        dist = math.sqrt(((self.x-otherpoint.x)**2)+((self.y-otherpoint.y)**2))
        return dist           
    

        
#-----------------------------------------
    
#[3]
    
def main(): #calls classes and method to print script on colsole

    print "Unique IDs:"
    P1=Point(5,3)
    P2=Point(2,7)
    P3=Point(2,7)
    print
    print "Points"
    print P1, P2, P3
    print
    print "Equality - Do points have same XY coordinates?"
    print "   Between P1 & P2: " + P1.equality(P2) #calling equality method
    print "   Between P1 & P3: " + P1.equality(P3)
    print "   Between P2 & P3: " + P2.equality(P3)
    print
    print "Identity - Do points have matching unique IDs?"
    print "   Between P1 & P2: " + P1.identify(P2) #calling identify method
    print "   Between P1 & P3: " + P1.identify(P3)
    print "   Between P2 & P3: " + P2.identify(P3)
    print
    print "Distance - What is the distance between each point?"
    print "   Between P1 & P2: " + str(P1.distance(P2)) #calling distance method
    print "   Between P1 & P3: " + str(P1.distance(P3))
    print "   Between P2 & P3: " + str(P2.distance(P3))
   
main()
    



        



