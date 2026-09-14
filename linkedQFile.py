class Node:
    def __init__(self, value):
        self.value = value
        self.next = None #Detta är pilen, den pekar inte på någonting i början

class LinkedQ: #basically kopierar metoder från arrayQ förutom att använder None istället
    def __init__(self):
        self.__first = None
        self.__last = None

    def is_empty(self):
        #Kön är tom om pilen inte pekar på en Node
        return self.__first is None

    def enqueue(self, item):
        new_node = Node(item) #Skapa NY låda med värdet (item)

        if self.is_empty():
            #Representerar Fall 1: Kön är tom. Pilar pekar på Ny Node
            self.__first = new_node
            self.__last =  new_node
        else:
            #Fall 2: Det finns redan något i kön
            #__last pekar på nya noden
            self.__last.next = new_node
            #Uppdatera
            self.__last = new_node

    #När objekt A ska bort, __first pilen ska istället peka på objekt B
    def dequeue(self):
        #spara värden från första lådan (A)
        chosen_value = self.__first.value
        #flytta fram kön i ett steg
        self.__first = self.__first.next
        return chosen_value




