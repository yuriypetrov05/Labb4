def makechildren_v1(aktuellt_ord, svenska, gamla):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

    for i in range(len(aktuellt_ord)): #Dubbel for loop går igenom bokstäverna i orden
        for bokstav in alfabet:  #Sen för varje bokstav den går igenom alfabetet
            if bokstav == aktuellt_ord[i]: #ifall bokstaven finns i orden
                continue  #gå vidare

            nytt_ord = aktuellt_ord[:i] + bokstav + aktuellt_ord[i+1:]  #sätt in det nya bokstaven och behåll de gamla

            if nytt_ord in svenska and nytt_ord not in gamla:
                gamla.put(nytt_ord)
                
                #I version 1 skriver vi bara ut barnet direkt på skärmen!
                print(nytt_ord)


from bintreeFile import Bintree  

def main():
    svenska = Bintree()
    gamla = Bintree()
    
    try: #Denn igentligen behövs ej, ta bort?
        with open("word3.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                svenska.put(word)
    except FileNotFoundError:#Behövs ej igentligen.
        print("Filen finns inte!")
        return

    #Fråga bara efter startord
    startord = input("Startord: ").strip().lower()
    
    gamla.put(startord)
    
    print(f"Barnen till {startord} är:")
    makechildren_v1(startord, svenska, gamla)

if __name__ == "__main__":
    main()