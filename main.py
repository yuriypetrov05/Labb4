def makechildren(aktuell_ord, q, svenska, gamla, slutord):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

    #Loopa igenom varje position i ordet(för ett 3-bokstavsord med index 0,1,2)
    for i in range(len(aktuell_ord)): #dubbel for loop
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