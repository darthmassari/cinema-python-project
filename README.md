# Cinema
Progetto in Python del corso di Fondamenti di Informatica del CdL in Ingegneria dell'Informazione 2020/2021.   
Il seguente è un programma della categoria di gestione dati, che permette la gestione delle proiezioni di un cinema (in questo caso un multisala)   
Il programma si presenta con interfaccia a linea di comando, non essendo dotato di GUI

## Struttura
- **src**: contiene i file python per eseguire il programma
- **resources**: contiene le risorse del programma
  
## Funzionamento
Il programma è composto da svariati menu che proporranno diverse scelte all’utente.
Una volta avviato, l'utente potrà scegliere di registrarsi o di effettuare l'accesso nella sua area personale, e da qui potrà:
- **Visualizzare, aggiungere, modificare o eliminare spettacoli**   
Come precedentemente descritto, nel momento dell’aggiunta di uno spettacolo, viene creato un file di testo che simula una sala, inoltre i dati relativi a questo spettacolo vengono aggiunti al file **listafilm.txt**  
Se si decide di modificare uno spettacolo, sarà possibile scegliere quale dato in particolare modificare.   
Se invece decide di eliminare uno spettacolo, verranno eliminati i dati di quest’ultimo dal file **listafilm.txt** e attraverso l’uso di una libreria di sistema (os), verrà eliminato anche il file associato alla sala dello spettacolo
- **Modificare l’importo di una tariffa selezionata**
- **Staccare un biglietto**   
Questa operazione stampa su schermo (a seconda del numero di posti richiesti), la fila, il posto e il costo del biglietto per ogni persona
- **Effettuare il logout**
- **Tornare alla sezione precedente**

## Alcune note
- Il programma è documentato in maniera più dettagliata all’interno del codice 
- Il programma non permette l'inserimento di uno spettacolo con titolo del film già presente 
- Il programma è stato sviluppato con scarse conoscenze di programmazione
