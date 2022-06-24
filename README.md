# BZTGSch-lerRegister
Ein Schülerverwaltungs Programm für den Unterricht an der BBS Haarentor der Klasse FA2C.

# Inhaltsverzeichniss
1. [Datenbank](#Datenbank)
   1. [Plannung](#Plannung)
   2. [ERM](#ERM)
   3. [Erstellung der Datenbank](#Datenbankerstellung)
   4. [Testen der Datenbank](#TestenDerDatenbank)
2. [Fazit](#Fazit)

<a name="Datenbank"></a>  
## Datenbank
<a name="Plannung"></a> 
### Plannung: 
Ziel was es eine Datenbank zu erstellen die Klassen, Schüler, Schulen und Lehrer verwaltet. Es wurde daraufhin eine Datenbank erstellt die 4 Tabellen enthält.
1. Schools
   1. Hat eine Id
   2. Hat einen Namen
   3. Stadt
   4. ZIP
   5. Straßenname + Hausnummer
  
2. Classes
   1. Hat eine Id
   2. Jede Klasse hat einen Lehrer
   3. Jede Klasse gehört zu einer Schule
   4. Hat einen Namen
  
3. Teachers
   1. Hat eine Id
   2. Vornamen
   3. Nachnamen
   4. Alter
  
4. Students
   1. Hat eine Id
   2. Gehört zu einer Klasse
   3. Vornamen
   4. Nachnamen
   5. Alter

<a name="ERM"></a>  
### ERM: 

![image](https://user-images.githubusercontent.com/23700090/175651691-e1aa23f4-e13a-4a4c-8895-118429741f20.png)

Wie in dem Bild gezeigt. Gibt es eine Schule die mehrere Klassen haben kann. Diese Klassen haben immer einen Lehrer und mehrere Schüler.

<a name="Datenbankerstellung"></a>
### Erstellung der Datenbank: 
Zur erstellung der Datenbank wurde ein kleines Script geschrieben das das die Tabellen erstellt. Zum Testen wurde auch noch eins geschrieben das die Tabellen mit Testdaten füllt.

// ToDo: Code des Scriptes hier zeigen.

Um Daten in die Tabellen zu schreiben und zu lesen wurden für jede Tabelle ein Service geschrieben. Ein Service ist immer eine Class die nur Methoden enthält um mit den Tabellen in der Datenbank zu arbeiten.
Hier als Beispiel der Service für die StudentTabelle.

//ToDo: Service Code hier einfügen.

<a name="TestenDerDatenbank"></a>
### Testen der Datenbank:

Hier wurde wieder für jede Funktion in dem Service eine Test Funktion geschrieben womit überprüft wurde ob die Methode wie gewünscht funktioniert.

Ist es gewollt eine Methode zu Testes da Sie geändert oder neugeschrieben wurde muss hierfür eine Test Funktion geschrieben und unter dem Kommentar "# Call specific  Tests Here" aufgerufen werden. 

Es wurde auf Unit Test etc. verzichtet da wir keine Erfahrung mit diesen in Python haben und die Zeit dafür zu knapp war. 
Beispiel:
![PythonDatabaseTests](https://user-images.githubusercontent.com/23700090/175646719-65808b84-6194-4a27-b3c4-6d582e4f9a1e.gif)

## Fazit <a name="Fazit"></a>  
