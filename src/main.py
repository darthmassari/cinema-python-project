import funzioni
import os

REPOSITORY_BASE = "resources"
MOVIES_PATH = REPOSITORY_BASE + "/" + "movies"
DATA_PATH = REPOSITORY_BASE + "/" + "data"
UTENTI_FILENAME = DATA_PATH + "/" + "utenti.txt"
TARIFFE_FILENAME = DATA_PATH + "/" + "tariffe.txt"
LISTAFILM_FILENAME = DATA_PATH + "/" + "listafilm.txt"

def registrazione():
    userID = input("Inserisci uno username: ")
    if userID in funzioni.estraiDizionario(UTENTI_FILENAME):
        sceltaReg = -1
        while sceltaReg != 0:
            print("\nPare che ci sia già un utente con quel nome\n")  
            print("0: Torna al menu")                                 
            print("1: Riprova\n")                                     
            sceltaReg = int(input())
            if sceltaReg == 0:
                pass
            elif sceltaReg == 1:
                registrazione()
    else:
        userPSW = str(input("Inserisci una password: "))            
        scriviUtente = open(UTENTI_FILENAME, "a")                      
        scriviUtente.write(userID)                                  
        scriviUtente.write(" ")                                     
        scriviUtente.write(userPSW + "\n")
        pass
                                     
def login():                         
    userID = input("Inserisci il tuo ID utente: ")
    userPSW = input("Inserisci la tua password: ")
    if userID in funzioni.estraiDizionario(UTENTI_FILENAME) and userPSW in funzioni.estraiDizionario(UTENTI_FILENAME)[userID]:
       print("\nBenvenuto, " + userID)        
       cicloUtente()                          
    else:                                     
        sceltaErr = -1                        
        while sceltaErr != 0:
            print("\nNome utente o password non corretti")
            print("0: Torna al menu")
            print("1: Riprova\n")
            sceltaErr = int(input())
            if sceltaErr == 0:
                pass
            elif sceltaErr == 1:
                login()

#Una volta entrato nell'area personale, l'utente avrà alcune scelte a disposizione
def cicloUtente():                               
    sceltaUtente = -1
    while sceltaUtente != 0:
        print("\nSeleziona una sezione ")
        print("0: Logout")
        print("1: Gestione spettacoli ")
        print("2: Modifica prezzi tariffe")
        print("3: Staccare un biglietto\n")
        sceltaUtente = int(input())
        print("")

        # Logout, il programma torna nel ciclo precedente
        if sceltaUtente == 0:                 
            pass                              

        # Menu gestione degli spettacoli
        elif sceltaUtente == 1:               
            sceltaSpettacolo = -1
            while sceltaSpettacolo != 0:
                print("GESTIONE SPETTACOLI")
                print("0: Indietro")
                print("1: Lista degli spettacoli")
                print("2: Aggiungi uno spettacolo")
                print("3: Mofifica uno spettacolo")
                print("4: Elimina uno spettacolo\n")
                sceltaSpettacolo = int(input())

                # Indietro
                if sceltaSpettacolo == 0:
                    pass

                # Lista spettacoli    
                elif sceltaSpettacolo == 1:         
                    print("")                       
                    funzioni.listaFilm()                    
                    print("")
                    sceltaUtente = 1

                # Aggiunta di uno spettacolo
                elif sceltaSpettacolo == 2:
                    scriviFilm = open(LISTAFILM_FILENAME, "a")     # Apre il file contenente i dati di tutti gli spettacoli
                    
                    titoloSpettacolo = str(input("\nInserisci il nome del film: "))
                    titoloSpettacolo_ = titoloSpettacolo.replace(" ", "_")      # Eventuali spazi vengono sostituiti da "_"
                    scriviFilm.write(titoloSpettacolo_)                     
                    scriviFilm.write(" ")                                   

                    giornoFilm = str(input("Inserisci il giorno della settimana: "))
                    giornoFilmLower = giornoFilm.lower().replace("ì", "i")     # Le maiuscole vengono rese minuscole
                    scriviFilm.write(giornoFilmLower)                         
                    scriviFilm.write(" ")

                    orarioFilm = str(input("Inserisci l'orario: "))
                    scriviFilm.write(orarioFilm)
                    scriviFilm.write(" ")

                    salaFilm = str(input("Inserisci il numero della sala: "))
                    scriviFilm.write(salaFilm)
                    scriviFilm.write(" ")

                    capienzaSala = str(180)                   # Capienza standard delle sale a 180 posti
                    scriviFilm.write(capienzaSala)
                    scriviFilm.write("\n")
                    scriviFilm.close()                          # Il file viene chiuso
                    fileSalaFilm = MOVIES_PATH + "/" + titoloSpettacolo_ + ".txt"   # Viene creato il file composto da titolo + .txt, contiene la rappresentazione dei posti nella sala
                    funzioni.nuovaSala(fileSalaFilm)                   
                    print("\nProiezione aggiunta con successo!\n")

                # Modifica di uno spettacolo                        
                elif sceltaSpettacolo == 3:                
                    print("\nQuale film vuoi modificare?")
                    funzioni.listaFilm()
                    print("")
                    sceltaModFilm = int(input())
                    print("")                                            
                    copiaTabella = list(funzioni.estraiTabella(LISTAFILM_FILENAME))  # Copia della tabella degli spettacoli, permette di modificare i singoli valori dello spettacolo selezionato

                    for i in range(len(copiaTabella)):          # i = numero di riga della tabella
                        if sceltaModFilm == i + 1:              # Se l'input dell'utente corrisponde al numero della riga di uno spettacolo,
                            print("Cosa vuoi modificare?")      # viene chiesto quale elemento modificare
                            print("1: Titolo")
                            print("2: Giorno")
                            print("3: Orario")
                            print("4: Sala")
                            print("")
                            sceltaModFilm_2 = int(input())      # Per ogni elemento inserito, viene memorizzato un nuovo elemento della
                            print("")                           # copia della tabella nella posizione [numero riga][elemento della riga]

                            if sceltaModFilm_2 == 1:
                                aggTitFilm = str(input("Inserisci il nuovo titolo: "))
                                copiaTabella[i][0] = aggTitFilm.replace(" ", "_")
                                fileSalaFilm = aggTitFilm + ".txt"
                                funzioni.nuovaSala(fileSalaFilm)

                            elif sceltaModFilm_2 == 2:
                                aggGioFilm = input("Inserisci il nuovo giorno: ")
                                copiaTabella[i][1] = aggGioFilm

                            elif sceltaModFilm_2 == 3:
                                aggOraFilm = input("Inserisci il nuovo orario: ")
                                copiaTabella[i][2] = aggOraFilm

                            elif sceltaModFilm_2 == 4:
                                aggSalaFilm = input("Inserisci la nuova sala: ")
                                copiaTabella[i][3] = aggSalaFilm

                            aggiornaFilm = open(LISTAFILM_FILENAME, "w")         # Apre il file della lista degli spettacoli in modalità di scrittura:
                            for line in copiaTabella:                         # Il contenuto del file viene sovrascritto con la copia della tabella
                                for arg in line:                              
                                    aggiornaFilm.write(arg)                   
                                    aggiornaFilm.write(" ")
                                aggiornaFilm.write("\n")
                            aggiornaFilm.close()
                            print("\nProiezione modificata con successo!\n")
                        else:
                            pass

                # Eliminazione di uno spettacolo                                  
                elif sceltaSpettacolo == 4:
                    print("\nQuale spettacolo vuoi eliminare?\n")
                    funzioni.listaFilm()                                       
                    print("")
                    sceltaCancTariffa = int(input())
                    copiaTabella = list(funzioni.estraiTabella(LISTAFILM_FILENAME))    # Copia della tabella con la lista degli spettacoli
                                                                        
                    for i in range(len(copiaTabella)):      # i = numero di riga della tabella

                        if sceltaCancTariffa == i + 1:
                            fileSalaFilm = copiaTabella[i][0] + ".txt"  # fileSalaFilm prende come valore la stringa del titolo del film + ".txt"
                            os.remove(fileSalaFilm)                     # Il file viene eliminato
                                                                        
                            del copiaTabella[i]                         # Viene eliminata anche la linea riferita allo spettacolo dalla copia della tabella,
                            aggiornaFilm = open(LISTAFILM_FILENAME, "w")
                            for line in copiaTabella:                   # Viene aperto il file con la lista delle proiezioni in modalità
                                for arg in line:                        # scrittura, che viene aggiornato con la nuova lista degli spettacoli 
                                    aggiornaFilm.write(arg)             
                                    aggiornaFilm.write(" ")
                                aggiornaFilm.write("\n")
                            aggiornaFilm.close()
                            print("\nProiezione eliminata con successo!")

                        else:
                            pass

        # Modifica prezzi tariffe
        elif sceltaUtente == 2:
            print("\nQuale tariffa vuoi modificare?")           
            f = 1                                                           # f aggiunge numerazione alla lista delle tariffe,
            for nomeTariffa in funzioni.estraiDizionario(TARIFFE_FILENAME):    # definita come dizionario del tipo "[nome tariffa][prezzo]"
                print(str(f) + ":", nomeTariffa)
                f = f + 1
            print("")

            copiaDizionario = dict(funzioni.estraiDizionario(TARIFFE_FILENAME))  # Copia del dizionario delle tariffe
            sceltaModTariffa = int(input())

            if sceltaModTariffa == 1:                                       # Per ogni giorno, modifica l'importo
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

            modTariffa = open(TARIFFE_FILENAME, "w")
            for chiave in copiaDizionario:                  # Il file contenente le tariffe viene aggiornato
                modTariffa.write(chiave)
                modTariffa.write(" ")
                modTariffa.write(copiaDizionario[chiave] + "\n")
            modTariffa.close()

        # Stampa di un biglietto                                    
        elif sceltaUtente == 3:
            sceltaTicket = -1
            while sceltaTicket != 0:
                print("Per quale spettacolo?\n")       
                funzioni.listaFilm()                # Viene stampata la lista dei film
                print("")
                sceltaTicket = int(input())
                copiaTabella = list(funzioni.estraiTabella(LISTAFILM_FILENAME))    # Copia della tabella degli spettacoli

                for i in range(len(copiaTabella)):
                    tariffaTicket = copiaTabella[i][1]
                    titoloFilmTicket = str(copiaTabella[i][0]) + ".txt"

                    if sceltaTicket == i + 1:
                        numTicket = int(input("\nInserisci il numero di biglietti: "))   # Viene chiesto il numero di biglietti
                        print("")
                        for nomeTariffa in funzioni.estraiDizionario(TARIFFE_FILENAME):              
                            if tariffaTicket == nomeTariffa:                                                                                      # Se il nome del giorno di proiezione coincide con quello del nome di una tariffa,
                                funzioni.modificaSala(titoloFilmTicket, numTicket, str(funzioni.estraiDizionario(TARIFFE_FILENAME)[nomeTariffa]))    # allora viene stampato il biglietto con il prezzo riferito al giorno di proiezione

                        copiaTabella[i][4] = int(copiaTabella[i][4]) - numTicket     # La copia della tabella viene modificato sottraendo il numero di biglietti richiesti
                        copiaTabella[i][4] = str(copiaTabella[i][4])                 # e viene convertito in stringa per effettuare la scrittura
                        aggiornaFilm = open(LISTAFILM_FILENAME, "w")                    

                        for line in copiaTabella:
                            for arg in line:                       # Il file con la lista degli spettacoli viene aggiornato
                                aggiornaFilm.write(arg)
                                aggiornaFilm.write(" ")
                            aggiornaFilm.write("\n")
                        aggiornaFilm.close()
                break

# --------------------------------------------------------------------------------------
# Viene definito il menu principale, dal quale si può effettuare l'accesso o registrarsi
scelta_menu = -1        
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
