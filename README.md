# ProgettoCinema
Progetto del corso di Fondamenti di Informatica del CdL in Ingegneria dell'Informazione 2020/2021.
Il seguente è un programma della categoria di gestione dati.
Si tratta di un programma che permette la gestione dei dati di un cinema (in questo caso specifico di un multisala)

## Struttura
  - “main.py”: è il programma principale, necessario per l’esecuzione del programma
  - “funzioni.py”: contiene alcune tra le funzioni create per il funzionamento del programma
  - “utenti.txt”: contiene i dati (username e password) dei vari utenti che si sono registrati all’interno del programma
  - “tariffe.txt”: contiene una lista in cui si trovano i nomi delle tariffe (giorni della settimana e ridotti) e il prezzo di quest’ultime
  - “listafilm.txt”: è un file che contiene titolo, giorno, ora e sala di proiezione di tutti gli spettacoli inseriti all’interno del programma
  - Inoltre, ogni volta che un utente aggiunge uno spettacolo, viene creato un file di testo che “simula” i posti occupati e quelli disponibili all’interno di una sala, la quale è impostata di default a 180 posti (12 File x 15 Posti)
  
## Funzionamento
Il programma è composto da svariati menù (realizzati attraverso dei cicli while) che proporranno diverse scelte all’utente.
Una volta avviato, l'utente potrà scegliere di registrarsi o di effettuare l'accesso nella sua area personale, e da qui potrà:
  - Effettuare il logout
  - Visualizzare, aggiungere, modificare o eliminare gli spettacoli nel proprio "archivio". 
  Come precedentemente descritto, nel momento dell’aggiunta di uno spettacolo, viene creato un file di testo che simula una sala, inoltre i dati relativi a questo spettacolo vengono aggiunti al file “listafilm.txt”; il programma non è tuttavia pensato per avere in programmazione più spettacoli con lo stesso titolo del film.
  Se si decide di modificare uno spettacolo, sarà possibile scegliere quale dato in particolare modificare.
  Se invece decide di eliminare uno spettacolo, verranno eliminati i dati di quest’ultimo dal file “listafilm.txt” e attraverso l’uso di una libreria di sistema (os), verrà eliminato anche il file associato alla sala dello spettacolo
  - Modificare l’importo di una tariffa selezionata
  - "Staccare" un biglietto: questa operazione stampa su schermo (a seconda del numero di posti richiesti), la fila, il posto e il costo del biglietto per ogni persona
  - Inoltre è possibile, in molti punti del programma, tornare alla sezione precedente
Il funzionamento del programma è analizzato in maniera più dettagliata all’interno del codice 
