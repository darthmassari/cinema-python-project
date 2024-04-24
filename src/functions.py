import paths

# Estrae da un file selezionato un dizionario
# Usato per estrarre dati da un dizionario (Utenti, tariffe, ecc)


def extractDictionary(fileName):
    dict = {}
    openFile = open(fileName, "r")
    for line in openFile:
        # Divide la chiave (nome) e il valore (password/prezzo) e li aggiunge al dizionario vuoto
        (key, value) = line.split()
        dict[str(key)] = value
    openFile.close()
    return dict

# Ha la stessa funzione della precedente, ma vengono estratti più valori
# che vengono aggiunti ad ogni riga della tabella
# Usata per operare sul file della lista degli spettacoli


def extractTable(fileName):
    tab = []
    openFile = open(fileName, "r")
    for line in openFile:
        (movie_title, movie_day, movie_time,
         movie_room, movie_capacity) = line.split()
        row = [movie_title, movie_day, movie_time, movie_room, movie_capacity]
        tab.append(row)
    openFile.close()
    return tab

# Identica alla precedente, ma sostituisce nel titolo i "_" con degli spazi
# Usata soprattutto per visualizzare la lista dei film


def extractTable2(fileName):
    tab = []
    openFile = open(fileName, "r")
    for line in openFile:
        (movie_title, movie_day, movie_time,
         movie_room, movie_capacity) = line.split()
        movieTitle = str(movie_title).replace("_", " ")
        row = [movieTitle, movie_day, movie_time, movie_room, movie_capacity]
        tab.append(row)
    openFile.close()
    return tab


def extractTitle(fileName):
    openFile = open(fileName, "r")
    for line in openFile:
        (movie_title, movie_day, movie_time,
         movie_room, movie_capacity) = line.split()
    openFile.close()
    return movie_title

# Stampa su schermo la lista dei film
# che viene contornata da trattini e barre verticali


def movieList():
    print("-" * 79)
    print("|   Titolo" + 35*" " + "Giorno     Orario   Sala  Posti  |")
    print("-" * 79)
    n = 0                           # n numera ogni spettacolo
    for i in extractTable2(paths.MOVIELIST_FILENAME):
        n = n + 1
        print("|", n, "%-39s  %-10s  %-6s %3s %7s   |" %
              (i[0], i[1], i[2], i[3], i[4]))
    print("-" * 79)

# Crea la sala di uno spettacolo


def newRoom(fileName):
    rowNum = 12
    seatNum = 15
    createRoom = open(fileName, "w")
    for i in range(rowNum):
        # Vengono aggiunti tanti "0" che stanno ad indicare se un posto è disponibile
        row = "0 " * seatNum
        # se un posto è occupato, viene utilizzato "1".
        createRoom.write(row)
        # Nel momento della creazione della sala, tutti i posti sono disponibili
        createRoom.write("\n")
    createRoom.close()

# Prende in ingresso il file della sala di uno spettacolo, il numero di biglietti richiesti e il prezzo del biglietto


def editRoom(roomFile, ticketNum, ticketPrice):
    tab = []
    readRoom = open(roomFile, "r")
    for row in readRoom:                # Viene creata una tabella di posti, con valore "0" o "1"
        seats = row.split()
        tab.append(seats)
    readRoom.close()

    for m in range(ticketNum):         # Per ogni biglietto richiesto
        i = 0                          # i = numero di fila
        available = False          # Il ciclo continua finchè un posto non è disponibile

        for line in tab:
            if available == False:
                i = i + 1
                n = 0                  # n = numero di posto

                for item in line:
                    n = n + 1
                    if item == "1":
                        pass
                    elif item == "0":
                        available = True
                        # Il posto disponibile viene convertito in "occupato"
                        tab[i - 1][n - 1] = "1"
                        updateRoom = open(roomFile, "w")

                        for line in tab:                   # Il file della sala viene aggiornato
                            for element in line:
                                updateRoom.write(element)
                                updateRoom.write(" ")
                            updateRoom.write("\n")
                        updateRoom.close()
                        break
            else:
                break
        print("row", i, "Posto", n, "Prezzo", ticketPrice + "€\n")
