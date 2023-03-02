import main

# Estrae da un file selezionato un dizionario
# Usato per estrarre dati da un dizionario (Utenti, tariffe, ecc)
def estraiDizionario(nomeFile):         
    dict = {}                           
    apriFile = open(nomeFile, "r")         
    for line in apriFile:                  
        (chiave, valore) = line.split()     # Divide la chiave (nome) e il valore (password/prezzo) e li aggiunge al dizionario vuoto
        dict[str(chiave)] = valore           
    apriFile.close()
    return dict                         

# Ha la stessa funzione della precedente, ma vengono estratti più valori
# che vengono aggiunti ad ogni riga della tabella
# Usata per operare sul file della lista degli spettacoli
def estraiTabella(nomeFile):            
    tab = []                            
    apriFile = open(nomeFile, "r")      
    for line in apriFile:
        (titolo_film, giorno_film, orario_film, sala_film, capienza_film) = line.split()
        riga = [titolo_film, giorno_film, orario_film, sala_film, capienza_film]
        tab.append(riga)
    apriFile.close()
    return tab

# Identica alla precedente, ma sostituisce nel titolo i "_" con degli spazi
# Usata soprattutto per visualizzare la lista dei film
def estraiTabella2(nomeFile):              
    tab = []                                
    apriFile = open(nomeFile, "r")          
    for line in apriFile:                   
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

# Stampa su schermo la lista dei film
# che viene contornata da trattini e barre verticali (- , |)
def listaFilm():                  
    print("-" * 79)               
    print("|   Titolo" + 35*" " + "Giorno     Orario   Sala  Posti  |")
    print("-" * 79)
    n = 0                           # n numera ogni spettacolo
    for i in estraiTabella2(main.LISTAFILM_FILENAME):
        n = n + 1
        print("|",n, "%-39s  %-10s  %-6s %3s %7s   |" % (i[0], i[1], i[2], i[3], i[4]))
    print("-" * 79)

# Crea la sala di uno spettacolo
def nuovaSala(nomeFile):       
    numFile = 12               
    numPosti = 15
    creaSala = open(nomeFile, "w")
    for i in range(numFile):
        fila = "0 " * numPosti      # Vengono aggiunti tanti "0" che stanno ad indicare se un posto è disponibile
        creaSala.write(fila)        # se un posto è occupato, viene utilizzato "1".
        creaSala.write("\n")        # Nel momento della creazione della sala, tutti i posti sono disponibili
    creaSala.close()

# Prende in ingresso il file della sala di uno spettacolo, il numero di biglietti richiesti e il prezzo del biglietto
def modificaSala(fileSala, numTicket, prezzoTicket):   
    tab = []                                           
    leggiSala = open(fileSala, "r")
    for riga in leggiSala:                # Viene creata una tabella di posti, con valore "0" o "1"
        posti = riga.split()
        tab.append(posti)
    leggiSala.close()

    for m in range(numTicket):         # Per ogni biglietto richiesto
        i = 0                          # i = numero di fila
        disponibilita = False          # Il ciclo continua finchè un posto non è disponibile

        for line in tab:
            if disponibilita == False:  
                i = i + 1
                n = 0                  # n = numero di posto

                for item in line:
                    n = n + 1
                    if item == "1":         
                        pass
                    elif item == "0":         
                        disponibilita = True
                        tab[i - 1][n - 1] = "1"             # Il posto disponibile viene convertito in "occupato"
                        aggiornaSala = open(fileSala, "w")

                        for linea in tab:                   # Il file della sala viene aggiornato
                            for elemento in linea:
                                aggiornaSala.write(elemento)
                                aggiornaSala.write(" ")
                            aggiornaSala.write("\n")
                        aggiornaSala.close()
                        break
            else:
                break
        print("Fila", i, "Posto", n, "Prezzo", prezzoTicket + "€\n")