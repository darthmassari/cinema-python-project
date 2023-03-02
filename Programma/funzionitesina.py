def estraiDizionario(nomeFile):         #Questa funzione serve per estrarre da un file selezionato un dizionario, viene
                                        #usato per estrarre i dati degli utenti in fasi di registrazione e login e per estrarre
    dict = {}                           #le tariffe con i prezzi corrispondenti
    apriFile = open(nomeFile, "r")      #Viene aperto il file in modalità di lettura
    for line in apriFile:               #e per ogni linea
        (chiave, valore) = line.split() #divido la chiave (nome) e il valore (password/prezzo)
        dict[str(chiave)] = valore      #e li aggiungo al dizionario vuoto
    apriFile.close()
    return dict                         #restituisce il dizionario


def estraiTabella(nomeFile):            #Ha lo stesso funzionamento della funzione precedente, ma vengono estratti più valori
    tab = []                            #i quali vengono aggiunti ad ogni riga della tabella
    apriFile = open(nomeFile, "r")      #Viene usata per operare sul file della lista degli spettacoli
    for line in apriFile:
        (titolo_film, giorno_film, orario_film, sala_film, capienza_film) = line.split()
        riga = [titolo_film, giorno_film, orario_film, sala_film, capienza_film]
        tab.append(riga)
    apriFile.close()
    return tab


def estraiTabella2(nomeFile):               #funzione identica alla precedente, ma sostituisce nel titolo del film
    tab = []                                #i "_" con degli spazi
    apriFile = open(nomeFile, "r")          #Viene usata soprattutto per visualizzare la lista dei film, la quale viene "abbellita"
    for line in apriFile:                   #con una funzione successiva
        (titolo_film, giorno_film, orario_film, sala_film, capienza_film) = line.split()
        titoloFilm = str(titolo_film).replace("_", " ")
        riga = [titoloFilm, giorno_film, orario_film, sala_film, capienza_film]
        tab.append(riga)
    apriFile.close()
    return tab


def estraiTitolo(nomeFile):
    apriFile = open(nomeFile, "r")
    for line in apriFile:
        (titolo_film, giorno_film, orario_film, sala_film, capienza_film) = line.split()
    apriFile.close()
    return titolo_film


def listaFilm():                  #è la funzione che stampa su schermo la lista dei film
    print("-" * 79)               #la quale viene contornata da trattini e barre verticali (- , |)
    print("|   Titolo" + 35*" " + "Giorno     Orario   Sala  Posti  |")
    print("-" * 79)
    n = 0                         #la variabile n serve per numerare ogni spettacolo
    for i in estraiTabella2("listafilm.txt"):
        n = n + 1
        print("|",n, "%-39s  %-10s  %-6s %3s %7s   |" % (i[0], i[1], i[2], i[3], i[4]))
    print("-" * 79)


def nuovaSala(nomeFile):       #è la funzione che serve per la creazione della sala di uno spettacolo
    numFile = 12               #vengono definite il numero di file e di posti
    numPosti = 15
    creaSala = open(nomeFile, "w")
    for i in range(numFile):
        fila = "O " * numPosti      #vengono aggiunti tanti "0" che stanno ad indicare se un posto è disponibile
        creaSala.write(fila)        #se un posto è occupato, viene utilizzata "X".
        creaSala.write("\n")        #Nel momento della creazione della sala, tutti i posti sono disponibili
    creaSala.close()


def modificaSala(fileSala, numTicket, prezzoTicket):   #se si sceglie di stampare un biglietto, questa funzione prende in ingresso il file della sala di uno
    tab = []                                           #spettacolo, il numero di biglietti richiesti e il prezzo del biglietto
    leggiSala = open(fileSala, "r")
    for riga in leggiSala:                #viene creata una tabella di posti, con valore "X" o "0"
        posti = riga.split()
        tab.append(posti)
    leggiSala.close()

    for m in range(numTicket):         #il ciclo si ripete per ogni biglietto richiesto
        i = 0                          #vengono definiti due contatori: i per la fila e successivamente n per il posto
        disponibilita = False         #il ciclo continua finchè un posto non è disponibile

        for line in tab:
            if disponibilita == False:  #per ogni riga, se non c'è la disponibilità, si controlla la riga successiva
                i = i + 1
                n = 0

                for item in line:
                    n = n + 1
                    if item == "X":         #se il posto non è disponibile passa al prossimo
                        pass
                    elif item == "O":           #se il posto è disponibile, c'è disponibilità e quindi successivamente i cicli si interromperanno
                        disponibilita = True
                        tab[i - 1][n - 1] = "X"             #il posto disponibile viene convertito in "occupato"
                        aggiornaSala = open(fileSala, "w")

                        for linea in tab:                     #il file della sala viene aggiornato
                            for elemento in linea:
                                aggiornaSala.write(elemento)
                                aggiornaSala.write(" ")
                            aggiornaSala.write("\n")
                        aggiornaSala.close()
                        break
            else:
                break
        print("Fila", i, "Posto", n, "Prezzo", prezzoTicket + "€\n")   #Al termine stampa fila, posto e prezzo di ogni biglietto