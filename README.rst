Performance Test EmbASP
=======================

I test realizzati per il confronto del tempo di esecuzione tra l’implementazione Java e quella Python del framework EmbASP, comprendono:
Gli eseguibili di DLV e Clingo. 
Gli script che utilizzano il framework per la risoluzione di 2 problemi di test, uno riguardante sudoku e l’altro la 3-colorabilità, in 2 versioni perfettamente equivalenti ma scritte rispettivamente una in linguaggio java e l’altra in linguaggio python.
I file dei programmi ASP per la soluzione dei 2 problemi (“sudoku”, “3-colorabilità”), in 2 varianti, la prima per una risoluzione generica del problema, (vengono utilizzati dagli script precedentemente citati che si occupano, tramite l’utilizzo del framework, di passare i predicati di input al processo), e l’altra con già la presenza al loro interno di predicati che rappresentano l’input del problema, (vengono utilizzati direttamente dagli eseguibili Clingo e DLV, per l’ottenimento del solo tempo di calcolo dei 2 risolutori), ovviamente i predicati di input di entrambi le versioni sono i medesimi.
Il file di script, scritto in linguaggio Python, che si occupa, per ogni test di eseguirlo 10 volte, la versione java, quella python e il solo solver, successivamente memorizza i valori, ne esegue una media, e calcola la differenza dei tempi tra le versioni java e python con quella del solo solver. Infine salva tutti i valori ottenuti in un file csv ordinati in “tabelle”.
Tutti i valori temporali ottenuti sono espressi in nanosecondi.