class Classy():
    def __init__(self):
        self.items = []

    #This function adds the item to the items list.
    def fancy(self,item):
        self.items.append(item)
        # return (self.items)
    #This function gets the classiness.
    def get_classiness(self):
        classiness = 0
        for stuff in range (len(self.items)):
            if self.items[stuff].lower() == "tophat":
                classiness +=2
            elif self.items[stuff].lower() == "bowtie":
                classiness +=4
            elif self.items[stuff].lower() == "monocle":
                classiness +=5
            else:
                classiness +=0

        return classiness





me = Classy()
print(me.get_classiness())
me.fancy('mat')
me.fancy('Tophat')
print(me.get_classiness())
me.fancy('bowtie')
me.fancy('MoNOcle')
me.fancy("fan")
print(me.get_classiness())



