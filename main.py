def makechildren(aktuell_ord, q, svenska, gamla, slutord):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

    #Loopa igenom varje position i ordet(för ett 3-bokstavsord med index 0,1,2)
    for i in range(len(aktuell_ord)): #dubbel for loop
        for bokstav in alfabet:
            if bokstav == aktuellt_ord[i]:
                continue