from funzioniTesina import *       #Contiene le funzioni che verranno utilizzate nel programma
import os                          #Libreria utile all'eliminazione di file

                                                 #Questa funzione permette la registrazione all'interno del programma
def registrazione():
    userID = input("Inserisci uno username: ")          #La funzione chiede all'utente uno username

    if userID in estraiDizionario("utenti.txt"):
        sceltaReg = -1
        while sceltaReg != 0:
            print("\nPare che ci sia già un utente con quel nome\n")  #Se lo username risulta già presente tra gli utenti
            print("0: Torna al menu")                                 #già registrati, il programma permette di tornare al menu
            print("1: Riprova\n")                                     #oppure riprovare la procedura
            sceltaReg = int(input())
            if sceltaReg == 0:
                pass
            elif sceltaReg == 1:
                registrazione()

    else:
        userPSW = str(input("Inserisci una password: "))            #Se lo username non risulta già registrato, allora
        scriviUtente = open("utenti.txt", "a")                      #Il programma chiede di inserire una password e
        scriviUtente.write(userID)                                  #completa la procedura di registrazione aggiungendo
        scriviUtente.write(" ")                                     #l'utente tra gli utenti registrati
        scriviUtente.write(userPSW + "\n")
        pass


                                     #Quesa funzione permette di effettuare il login all'interno del programma
def login():                         #chiedendo all'utente il suo username e la sua password
    userID = input("Inserisci il tuo ID utente: ")
    userPSW = input("Inserisci la tua password: ")

    if userID in estraiDizionario("utenti.txt") and userPSW in estraiDizionario("utenti.txt")[userID]:
       print("\nBenvenuto, " + userID)        #Se il nome utente e la password inseriti combaciano con quelli di un utente
       cicloUtente()                          #registrato nel programma, viene effettuato il login

    else:                                     #altrimenti il programma permette di scegliere se tornare al menu o di
        sceltaErr = -1                        #riprovare con la procedura di autenticazoione
        while sceltaErr != 0:
            print("\nNome utente o password non corretti")
            print("0: Torna al menu")
            print("1: Riprova\n")
            sceltaErr = int(input())
            if sceltaErr == 0:
                pass
            elif sceltaErr == 1:
                login()


def cicloUtente():                               #Una volta entrato nell'area personale, l'utente avrà alcune scelte a disposizione
    sceltaUtente = -1
    while sceltaUtente != 0:
        print("\nSeleziona una sezione ")
        print("0: Logout")
        print("1: Gestione spettacoli ")
        print("2: Modifica prezzi tariffe")
        print("3: Staccare un biglietto\n")
        sceltaUtente = int(input())
        print("")

        if sceltaUtente == 0:                 #Se si decide di effettuare il logout, semplicemente il programma uscirà dal ciclo
            pass                              #e tornerà nel ciclo precedente, ossia il menu principale

        elif sceltaUtente == 1:               #Si entra nel menu della gestione degli spettacoli
            sceltaSpettacolo = -1
            while sceltaSpettacolo != 0:
                print("GESTIONE SPETTACOLI")
                print("0: Indietro")
                print("1: Lista degli spettacoli")
                print("2: Aggiungi uno spettacolo")
                print("3: Mofifica uno spettacolo")
                print("4: Elimina uno spettacolo\n")
                sceltaSpettacolo = int(input())

                if sceltaSpettacolo == 0:
                    pass

                elif sceltaSpettacolo == 1:         #Il programma richiama la funzione listafilm,
                    print("")                       #stampando così la lista degli spettacoli
                    listaFilm()
                    print("")
                    sceltaUtente = 1

                                                              # Se si decide di aggiungere uno spettacolo,
                elif sceltaSpettacolo == 2:
                    scriviFilm = open("listafilm.txt", "a")   #il programma apre il file contenente i dati di tutti gli spettacoli
                                                              #chiedendo titolo, giorno ora e sala di proiezione
                    titoloSpettacolo = str(input("\nInserisci il nome del film: "))
                    titoloSpettacolo_ = titoloSpettacolo.replace(" ", "_")  #eventuali spazi vengono sostituiti dal carattere "_" in modo tale
                    scriviFilm.write(titoloSpettacolo_)                     #da considerare il titolo come un unico elemento: questa operazione è necessaria
                    scriviFilm.write(" ")                                   #per quando si andrà a visualizzare la lista degli spettacoli

                    giornoFilm = str(input("Inserisci il giorno della settimana: "))
                    giornoFilmLower = giornoFilm.lower().replace("ì", "i")     #le maiuscole vengono rese minuscole per evitare errori in alcune funzioni,
                    scriviFilm.write(giornoFilmLower)                          #così come le i accentate
                    scriviFilm.write(" ")

                    orarioFilm = str(input("Inserisci l'orario: "))
                    scriviFilm.write(orarioFilm)
                    scriviFilm.write(" ")

                    salaFilm = str(input("Inserisci il numero della sala: "))
                    scriviFilm.write(salaFilm)
                    scriviFilm.write(" ")

                    capienzaSala = str(180)                   #la capienza standard delle sale è impostata a 180 posti
                    scriviFilm.write(capienzaSala)
                    scriviFilm.write("\n")
                    scriviFilm.close()                        #il file viene chiuso
                    fileSalaFilm = titoloSpettacolo_ + ".txt" #e viene creato un file che prende il titolo del film come nome aggiungendo la stringa ".txt"
                    nuovaSala(fileSalaFilm)                   #e contiene una rappresentazione dei posti all'interno della sala
                    print("\nProiezione aggiunta con successo!\n")

                                                            #Se si decide di modificare uno spettacolo
                elif sceltaSpettacolo == 3:                 #Il programma chiede all'utente quale film vuole modificare e stampa la lista degli spettacoli
                    print("\nQuale film vuoi modificare?")
                    listaFilm()
                    print("")
                    sceltaModFilm = int(input())
                    print("")                                            #Creo una copia della tabella degli spettacoli, in modo tale da poter
                    copiaTabella = list(estraiTabella("listafilm.txt"))  #modificare i singoli valori riferiti allo spettacolo selezionato

                    for i in range(len(copiaTabella)):                   #Il parametro i assume come valore il numero della riga della tabella
                        if sceltaModFilm == i + 1:                       #Se l'input dell'utente corrisponde al numero della riga dello spettacolo selezionato,
                            print("Cosa vuoi modificare?")               #Il programma chiede quale elemento dello spettacolo modificare
                            print("1: Titolo")
                            print("2: Giorno")
                            print("3: Orario")
                            print("4: Sala")
                            print("")
                            sceltaModFilm_2 = int(input())               #Per ogni elemento inserito, viene memorizzato un nuovo elemento della
                            print("")                                    #copia della tabella nella posizione "[numero riga][elemento della riga]"

                            if sceltaModFilm_2 == 1:
                                aggTitFilm = str(input("Inserisci il nuovo titolo: "))
                                copiaTabella[i][0] = aggTitFilm.replace(" ", "_")
                                fileSalaFilm = aggTitFilm + ".txt"
                                nuovaSala(fileSalaFilm)

                            elif sceltaModFilm_2 == 2:
                                aggGioFilm = input("Inserisci il nuovo giorno: ")
                                copiaTabella[i][1] = aggGioFilm

                            elif sceltaModFilm_2 == 3:
                                aggOraFilm = input("Inserisci il nuovo orario: ")
                                copiaTabella[i][2] = aggOraFilm

                            elif sceltaModFilm_2 == 4:
                                aggSalaFilm = input("Inserisci la nuova sala: ")
                                copiaTabella[i][3] = aggSalaFilm

                            aggiornaFilm = open("listafilm.txt", "w")         #Dopodichè, avendo una copia della tabella con i parametri modificati,
                            for line in copiaTabella:                         #posso aprire il file della lista degli spettacoli in modalità di scrittura:
                                for arg in line:                              #in questo modo il contenuto del file viene eliminato, e attraverso un
                                    aggiornaFilm.write(arg)                   #ciclo viene scritta riga per riga il contenuto della copia della tabella
                                    aggiornaFilm.write(" ")
                                aggiornaFilm.write("\n")
                            aggiornaFilm.close()
                            print("\nProiezione modificata con successo!\n")
                        else:
                            pass

                                                                      #Se si decide di elminare uno spettacolo
                elif sceltaSpettacolo == 4:
                    print("\nQuale spettacolo vuoi eliminare?\n")
                    listaFilm()                                       #Come in precedenza, il programma stampa la lista degli spettacoli
                    print("")
                    sceltaCancTariffa = int(input())
                    copiaTabella = list(estraiTabella("listafilm.txt")) #Allo stesso modo, viene creata una copia della tabella con la lista degli spettacoli
                                                                        #e viene effettuato un ciclo in cui i assume il numero della riga del film selezionato
                    for i in range(len(copiaTabella)):

                        if sceltaCancTariffa == i + 1:
                            fileSalaFilm = copiaTabella[i][0] + ".txt"  #Questa variabile prende come valore la stringa del titolo del film e aggiunge ".txt"
                            os.remove(fileSalaFilm)                     #In questo modo, si ottiene il nome del file della sala riferita al film, il quale viene
                                                                        #eliminato utilizzando la libreria os
                            del copiaTabella[i]                         #Viene eliminata anche la linea riferita allo spettacolo selezionato dalla copia della tabella,
                            aggiornaFilm = open("listafilm.txt", "w")
                            for line in copiaTabella:                   #Come in precedenza, viene aperto il file con la lista delle proiezioni in modalità
                                for arg in line:                        #scrittura, il quale viene aggiornato con la lista degli spettacoli escludendo quello
                                    aggiornaFilm.write(arg)             #che è stato eliminato
                                    aggiornaFilm.write(" ")
                                aggiornaFilm.write("\n")
                            aggiornaFilm.close()
                            print("\nProiezione eliminata con successo!")

                        else:
                            pass


        elif sceltaUtente == 2:
            print("\nQuale tariffa vuoi modificare?")           #Se si decide di modificare una tariffa, il programma chiede di selezionarne una
            f = 1                                               #Viene definita una variabile (f) che serve per aggiungere una numerazione alla lista
            for nomeTariffa in estraiDizionario("tariffe.txt"): #delle tariffe, la quale è definita sotto forma di dizionario del tipo "[nome tariffa][prezzo]"
                print(str(f) + ":", nomeTariffa)
                f = f + 1
            print("")

            copiaDizionario = dict(estraiDizionario("tariffe.txt"))  #creo una copia del dizionario delle tariffe
            sceltaModTariffa = int(input())

            if sceltaModTariffa == 1:                                #per ogni giorno che è possibile selezionare, modifico l'importo di quest'ultimo
                nuovoPrezzo = str(input("\nInserisci il nuovo importo: "))
                copiaDizionario["lunedi"] = nuovoPrezzo

            elif sceltaModTariffa == 2:
                nuovoPrezzo = str(input("\nInserisci il nuovo importo: "))
                copiaDizionario["martedi"] = nuovoPrezzo

            elif sceltaModTariffa == 3:
                nuovoPrezzo = str(input("\nInserisci il nuovo importo: "))
                copiaDizionario["mercoledi"] = nuovoPrezzo

            elif sceltaModTariffa == 4:
                nuovoPrezzo = str(input("\nInserisci il nuovo importo: "))
                copiaDizionario["giovedi"] = nuovoPrezzo

            elif sceltaModTariffa == 5:
                nuovoPrezzo = str(input("\nInserisci il nuovo importo: "))
                copiaDizionario["venerdi"] = nuovoPrezzo

            elif sceltaModTariffa == 6:
                nuovoPrezzo = str(input("\nInserisci il nuovo importo: "))
                copiaDizionario["sabato"] = nuovoPrezzo

            elif sceltaModTariffa == 7:
                nuovoPrezzo = str(input("\nInserisci il nuovo importo: "))
                copiaDizionario["domenica"] = nuovoPrezzo
            else:
                pass

            modTariffa = open("tariffe.txt", "w")
            for chiave in copiaDizionario:                  #il file contenente le tariffe viene aggiornato
                modTariffa.write(chiave)
                modTariffa.write(" ")
                modTariffa.write(copiaDizionario[chiave] + "\n")
            modTariffa.close()

                                                       #Se l'utente decide di "staccare" un biglietto
        elif sceltaUtente == 3:
            sceltaTicket = -1
            while sceltaTicket != 0:
                print("Per quale spettacolo?\n")       #Viene stampata la lista dei film
                listaFilm()
                print("")
                sceltaTicket = int(input())
                copiaTabella = list(estraiTabella("listafilm.txt"))  #Viene creata una copia della tabella degli spettacoli

                for i in range(len(copiaTabella)):
                    tariffaTicket = copiaTabella[i][1]
                    titoloFilmTicket = str(copiaTabella[i][0]) + ".txt"

                    if sceltaTicket == i + 1:
                        numTicket = int(input("\nInserisci il numero di biglietti: "))   #Il programma chiede il numero di biglietti
                        print("")
                        for nomeTariffa in estraiDizionario("tariffe.txt"):              #Se il nome del giorno di proiezione coincide con quello del nome di una tariffa,
                            if tariffaTicket == nomeTariffa:                             # allora il programma stampa il biglietto con il prezzo riferito al giorno di proiezione
                                modificaSala(titoloFilmTicket, numTicket, str(estraiDizionario("tariffe.txt")[nomeTariffa]))     #usando questa funzione

                        copiaTabella[i][4] = int(copiaTabella[i][4]) - numTicket     #Il parametro della copia della tabella viene modificato sottraendo
                        copiaTabella[i][4] = str(copiaTabella[i][4])                 #Il numero dei biglietti richiesti e viene convertito in stringa per
                        aggiornaFilm = open("listafilm.txt", "w")                    #effettuare la scrittura

                        for line in copiaTabella:
                            for arg in line:                       #Il file con la lista degli spettacoli viene aggiornato
                                aggiornaFilm.write(arg)
                                aggiornaFilm.write(" ")
                            aggiornaFilm.write("\n")
                        aggiornaFilm.close()
                break

# --------------------------------------------------------------------------------------
scelta_menu = -1        #Viene definito il menu principale, dal quale si può effettuare l'accesso o registrarsi
while scelta_menu != 0:
    print("\nBenvenuto!\nCosa vuoi fare?")
    print("0: Uscire dal programma")
    print("1: Accesso")
    print("2: Registrazione\n")
    scelta_menu = int(input())

    if scelta_menu == 0:
        pass


    elif scelta_menu == 1:
        print("")
        login()


    elif scelta_menu == 2:
        print("")
        registrazione()
