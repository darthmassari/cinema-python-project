import functions
import paths


def signup():
    userID = input("Inserisci uno username: ")
    if userID in functions.extractDictionary(paths.USERS_FILENAME):
        signupChoice = -1
        while signupChoice != 0:
            print("\nPare che ci sia già un utente con quel nome\n")
            print("0: Torna al menu")
            print("1: Riprova\n")
            signupChoice = int(input())
            if signupChoice == 0:
                pass
            elif signupChoice == 1:
                signup()
    else:
        userPSW = str(input("Inserisci una password: "))
        writeUser = open(paths.USERS_FILENAME, "a")
        writeUser.write(userID)
        writeUser.write(" ")
        writeUser.write(userPSW + "\n")
        pass


def login():
    userID = input("Inserisci il tuo ID utente: ")
    userPSW = input("Inserisci la tua password: ")
    if userID in functions.extractDictionary(paths.USERS_FILENAME) and userPSW in functions.extractDictionary(paths.USERS_FILENAME)[userID]:
        print("\nBenvenuto, " + userID)
        userCicle()
    else:
        loginErrorChoice = -1
        while loginErrorChoice != 0:
            print("\nNome utente o password non corretti")
            print("0: Torna al menu")
            print("1: Riprova\n")
            loginErrorChoice = int(input())
            if loginErrorChoice == 0:
                pass
            elif loginErrorChoice == 1:
                login()

# Una volta entrato nell'area personale, l'utente avrà alcune scelte a disposizione


def userCicle():
    userChoice = -1
    while userChoice != 0:
        print("\nSeleziona una sezione ")
        print("0: Logout")
        print("1: Gestione spettacoli ")
        print("2: Modifica prezzi tariffe")
        print("3: Staccare un biglietto\n")
        userChoice = int(input())
        print("")

        # Logout, il programma torna nel ciclo precedente
        if userChoice == 0:
            pass

        # Menu gestione degli spettacoli
        elif userChoice == 1:
            showChoice = -1
            while showChoice != 0:
                print("GESTIONE SPETTACOLI")
                print("0: Indietro")
                print("1: Lista degli spettacoli")
                print("2: Aggiungi uno spettacolo")
                print("3: Mofifica uno spettacolo")
                print("4: Elimina uno spettacolo\n")
                showChoice = int(input())

                # Indietro
                if showChoice == 0:
                    pass

                # Lista spettacoli
                elif showChoice == 1:
                    print("")
                    functions.movieList()
                    print("")

                # Aggiunta di uno spettacolo
                elif showChoice == 2:
                    # Apre il file contenente i dati di tutti gli spettacoli
                    writeMovie = open(paths.MOVIELIST_FILENAME, "a")

                    showTitle = str(input("\nInserisci il nome del film: "))
                    # Eventuali spazi vengono sostituiti da "_"
                    showTitle_ = showTitle.replace(" ", "_")
                    writeMovie.write(showTitle_)
                    writeMovie.write(" ")

                    movieDay = str(
                        input("Inserisci il giorno della settimana: "))
                    # Le maiuscole vengono rese minuscole
                    movieDayLower = movieDay.lower().replace("ì", "i")
                    writeMovie.write(movieDayLower)
                    writeMovie.write(" ")

                    movieTime = str(input("Inserisci l'orario: "))
                    writeMovie.write(movieTime)
                    writeMovie.write(" ")

                    movieRoom = str(input("Inserisci il numero della sala: "))
                    writeMovie.write(movieRoom)
                    writeMovie.write(" ")

                    # Capienza standard delle sale a 180 posti
                    roomCapacity = str(180)
                    writeMovie.write(roomCapacity)
                    writeMovie.write("\n")
                    writeMovie.close()                          # Il file viene chiuso
                    # Viene creato il file composto da titolo + .txt, contiene la rappresentazione dei posti nella sala
                    movieRoomFile = paths.MOVIES_DIR + "/" + showTitle_ + ".txt"
                    functions.newRoom(movieRoomFile)
                    print("\nProiezione aggiunta con successo!\n")

                # Modifica di uno spettacolo
                elif showChoice == 3:
                    print("\nQuale film vuoi modificare?")
                    functions.movieList()
                    print("")
                    editShowChoice = int(input())
                    print("")
                    # Copia della tabella degli spettacoli, permette di modificare i singoli valori dello spettacolo selezionato
                    copyTable = list(functions.extractTable(
                        paths.MOVIELIST_FILENAME))

                    # i = numero di riga della tabella
                    for i in range(len(copyTable)):
                        # Se l'input dell'utente corrisponde al numero della riga di uno spettacolo,
                        if editShowChoice == i + 1:
                            # viene chiesto quale elemento modificare
                            print("Cosa vuoi modificare?")
                            print("1: Titolo")
                            print("2: Giorno")
                            print("3: Orario")
                            print("4: Sala")
                            print("")
                            # Per ogni elemento inserito, viene memorizzato un nuovo elemento della
                            editShowChoice_2 = int(input())
                            # copia della tabella nella posizione [numero riga][elemento della riga]
                            print("")

                            if editShowChoice_2 == 1:
                                addMovieTitle = str(
                                    input("Inserisci il nuovo titolo: "))
                                copyTable[i][0] = addMovieTitle.replace(
                                    " ", "_")
                                movieRoomFile = addMovieTitle + ".txt"
                                functions.newRoom(movieRoomFile)

                            elif editShowChoice_2 == 2:
                                aggGioFilm = input(
                                    "Inserisci il nuovo giorno: ")
                                copyTable[i][1] = aggGioFilm

                            elif editShowChoice_2 == 3:
                                aggOraFilm = input(
                                    "Inserisci il nuovo orario: ")
                                copyTable[i][2] = aggOraFilm

                            elif editShowChoice_2 == 4:
                                aggmovieRoom = input(
                                    "Inserisci la nuova sala: ")
                                copyTable[i][3] = aggmovieRoom

                            # Apre il file della lista degli spettacoli in modalità di scrittura:
                            updateMovie = open(paths.MOVIELIST_FILENAME, "w")
                            # Il contenuto del file viene sovrascritto con la copia della tabella
                            for line in copyTable:
                                for arg in line:
                                    updateMovie.write(arg)
                                    updateMovie.write(" ")
                                updateMovie.write("\n")
                            updateMovie.close()
                            print("\nProiezione modificata con successo!\n")
                        else:
                            pass

                # Eliminazione di uno spettacolo
                elif showChoice == 4:
                    print("\nQuale spettacolo vuoi eliminare?\n")
                    functions.movieList()
                    print("")
                    removePricingChoice = int(input())
                    # Copia della tabella con la lista degli spettacoli
                    copyTable = list(functions.extractTable(
                        paths.MOVIELIST_FILENAME))

                    # i = numero di riga della tabella
                    for i in range(len(copyTable)):

                        if removePricingChoice == i + 1:
                            # movieRoomFile prende come valore la stringa del titolo del film + ".txt"
                            movieRoomFile = copyTable[i][0] + ".txt"
                            # Il file viene eliminato
                            remove(movieRoomFile)

                            # Viene eliminata anche la linea riferita allo spettacolo dalla copia della tabella,
                            del copyTable[i]
                            updateMovie = open(paths.MOVIELIST_FILENAME, "w")
                            for line in copyTable:                   # Viene aperto il file con la lista delle proiezioni in modalità
                                for arg in line:                        # scrittura, che viene aggiornato con la nuova lista degli spettacoli
                                    updateMovie.write(arg)
                                    updateMovie.write(" ")
                                updateMovie.write("\n")
                            updateMovie.close()
                            print("\nProiezione eliminata con successo!")

                        else:
                            pass

        # Modifica prezzi tariffe
        elif userChoice == 2:
            print("\nQuale tariffa vuoi modificare?")
            # f aggiunge numerazione alla lista delle tariffe,
            f = 1
            # definita come dizionario del tipo "[nome tariffa][prezzo]"
            for pricingTitle in functions.extractDictionary(paths.PRICING_FILENAME):
                print(str(f) + ":", pricingTitle)
                f = f + 1
            print("")

            copyDictionary = dict(functions.extractDictionary(
                paths.PRICING_FILENAME))  # Copia del dizionario delle tariffe
            editPricingChoice = int(input())

            if editPricingChoice == 1:                                       # Per ogni giorno, modifica l'importo
                newPrice = str(input("\nInserisci il nuovo importo: "))
                copyDictionary["lunedi"] = newPrice

            elif editPricingChoice == 2:
                newPrice = str(input("\nInserisci il nuovo importo: "))
                copyDictionary["martedi"] = newPrice

            elif editPricingChoice == 3:
                newPrice = str(input("\nInserisci il nuovo importo: "))
                copyDictionary["mercoledi"] = newPrice

            elif editPricingChoice == 4:
                newPrice = str(input("\nInserisci il nuovo importo: "))
                copyDictionary["giovedi"] = newPrice

            elif editPricingChoice == 5:
                newPrice = str(input("\nInserisci il nuovo importo: "))
                copyDictionary["venerdi"] = newPrice

            elif editPricingChoice == 6:
                newPrice = str(input("\nInserisci il nuovo importo: "))
                copyDictionary["sabato"] = newPrice

            elif editPricingChoice == 7:
                newPrice = str(input("\nInserisci il nuovo importo: "))
                copyDictionary["domenica"] = newPrice
            else:
                pass

            editPricing = open(paths.PRICING_FILENAME, "w")
            for key in copyDictionary:                  # Il file contenente le tariffe viene aggiornato
                editPricing.write(key)
                editPricing.write(" ")
                editPricing.write(copyDictionary[key] + "\n")
            editPricing.close()

        # Stampa di un biglietto
        elif userChoice == 3:
            ticketChoice = -1
            while ticketChoice != 0:
                print("Per quale spettacolo?\n")
                functions.movieList()                # Viene stampata la lista dei film
                print("")
                ticketChoice = int(input())
                # Copia della tabella degli spettacoli
                copyTable = list(functions.extractTable(
                    paths.MOVIELIST_FILENAME))

                for i in range(len(copyTable)):
                    ticketPricing = copyTable[i][1]
                    ticketMovieName = str(copyTable[i][0]) + ".txt"

                    if ticketChoice == i + 1:
                        # Viene chiesto il numero di biglietti
                        ticketNum = int(
                            input("\nInserisci il numero di biglietti: "))
                        print("")
                        for pricingTitle in functions.extractDictionary(paths.PRICING_FILENAME):
                            # Se il nome del giorno di proiezione coincide con quello del nome di una tariffa,
                            if ticketPricing == pricingTitle:
                                functions.editRoom(ticketMovieName, ticketNum, str(functions.extractDictionary(paths.PRICING_FILENAME)[
                                                   pricingTitle]))    # allora viene stampato il biglietto con il prezzo riferito al giorno di proiezione

                        # La copia della tabella viene modificato sottraendo il numero di biglietti richiesti
                        copyTable[i][4] = int(copyTable[i][4]) - ticketNum
                        # e viene convertito in stringa per effettuare la scrittura
                        copyTable[i][4] = str(copyTable[i][4])
                        updateMovie = open(paths.MOVIELIST_FILENAME, "w")

                        for line in copyTable:
                            for arg in line:                       # Il file con la lista degli spettacoli viene aggiornato
                                updateMovie.write(arg)
                                updateMovie.write(" ")
                            updateMovie.write("\n")
                        updateMovie.close()
                break


# --------------------------------------------------------------------------------------
# Viene definito il menu principale, dal quale si può effettuare l'accesso o registrarsi
menuChoice = -1
while menuChoice != 0:
    print("\nBenvenuto!\nCosa vuoi fare?")
    print("0: Uscire dal programma")
    print("1: Accesso")
    print("2: Registrazione\n")
    menuChoice = int(input())

    if menuChoice == 0:
        pass

    elif menuChoice == 1:
        print("")
        login()

    elif menuChoice == 2:
        print("")
        signup()
