class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,value): #Specialfunktion som returnerar True eller False om värdet finns eller inte
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")

# --- Hjälp Funktioner ---
def putta(p, newvalue):
    if p == None:  # if there is empty space in the bottom.
        return Node(newvalue)

    if newvalue < p.value:   #Smaller? paced on the left
        p.left = putta(p.left, newvalue)

    elif newvalue > p.value: #Larger? placed on the right
        p.right = putta(p.right, newvalue)

    return p

def finns(p,key): #Funktion som gör själva jobbet att söka efter ett värde (Används bara när man söker)
        if p == None: 
            return False
        if key == p.value: 
            return True
        if key < p.value: 
            return finns(p.left,key)
        if key > p.value: 
            return finns(p.right,key)

def skriv(p):
    if p != None:
        #Travel down the left side
        skriv(p.left)
        
        #Print the current node's word
        print(p.value)
        
        #Travel down the right side
        skriv(p.right)