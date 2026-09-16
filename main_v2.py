from bintreeFile import Bintree  
from linkedQFile import LinkedQ 

def makechildren(aktuellt_ord, q, svenska, gamla, slutord):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

    #Loopa igenom varje position i ordet(för ett 3-bokstavsord med index 0,1,2)
    for i in range(len(aktuellt_ord)): #dubbel for loop
        for bokstav in alfabet:
            if bokstav == aktuellt_ord[i]:
                continue

            #Exempel: om ord="söt", i=0, bokstav="n" -> "" + "n" + "öt" = "nöt"
            nytt_ord = aktuellt_ord[:i] + bokstav + aktuellt_ord[i+1:]

            #Kontrollera 1: Är det ett riktigt svenskt ord?
            #Kontrollera 2: Har vi undvikit det tidigare? (Förhindrar eviga cykler)
            if nytt_ord in svenska and nytt_ord not in gamla:
                
                #Markera ordet som besökt DIREKT så ingen annan gren lägger till det
                gamla.put(nytt_ord)
                
                #Om vi precis skapade slutordet är vi klara!
                if nytt_ord == slutord:
                    return True
                    
                #Annars lägger vi det längst bak i kön så vi kan söka från det senare
                q.enqueue(nytt_ord)

def main():
    svenska = Bintree()
    gamla = Bintree()
    q = LinkedQ()
    
    try:
        with open("word3.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                svenska.put(word)
    except FileNotFoundError:
        print("Filen finns inte!")
        return

    #Ta in start och slut från användaren
    startord = input("Startord: ").strip().lower()
    slutord = input("Slutord: ").strip().lower()

    q.enqueue(startord)
    gamla.put(startord)

    hittad = False
    #BFS-slinga: Fortsätt så länge det finns ord kvar i kön.
    while not q.is_empty():
        aktuellt_ord = q.dequeue()

        #Låt makechildren generera barn och kolla om vi når i mål
        if makechildren(aktuellt_ord, q, svenska, gamla, slutord):
            print(f"Det finns en väg till {slutord}")
            hittad = True
            break  #Bryt while-loopen, vi är klara!
            
    if not hittad:
        print(f"Det fanns ingen väg från {startord} till {slutord}")

if __name__ == "__main__":
    main()
        

