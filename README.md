# BZTGSch-lerRegister
Ein SchülerProgramm für den unterricht

# Inhaltsverzeichniss
1. [Datenbank](#Datenbank)
   1. [Plannung](#Plannung)
   2. [ERM](#ERM)
2. [Fazit](#Fazit)

## Datenbank <a name="Datenbank"></a>  
### Plannung: <a name="Plannung"></a> 
Ziel was es eine Datenbank zu erstellen die Klassen, Schüler, Schulen und Lehrer verwaltet. Es wurde daraufhin eine Datenbank erstellt die 4 Tabellen enthält.

1. Schools
  - Hat eine Id
  - Hat einen Namen
  - Stadt
  - ZIP
  - Straßenname + Hausnummer
  
2. Classes
  - Hat eine Id
  - Jede Klasse hat einen Lehrer
  - Jede Klasse gehört zu einer Schule
  - Hat einen Namen
  
3. Teachers
  - Hat eine Id
  - Vornamen
  - Nachnamen
  - Alter
  
4. Students
  - Hat eine Id
  - Gehört zu einer Klasse
  - Vornamen
  - Nachnamen
  - Alter

<h3>ERM:</h3> <a name="ERM"></a>  

![image](https://user-images.githubusercontent.com/23700090/175651691-e1aa23f4-e13a-4a4c-8895-118429741f20.png)

Wie in dem Bild gezeigt. Gibt es eine Schule die mehrere Klassen haben kann. Diese Klassen haben immer einen Lehrer und mehrere Schüler.

<h2>Erstellung der Datenbank:</h2>
Zur erstellung der Datenbank wurde ein kleines Script geschrieben das das die Tabellen erstellt. Zum Testen wurde auch noch eins geschrieben das die Tabellen mit Testdaten füllt.

// ToDo: Code des Scriptes hier zeigen.

Um Daten in die Tabellen zu schreiben und zu lesen wurden für jede Tabelle ein Service geschrieben. Ein Service ist immer eine Class die nur Methoden enthält um mit den Tabellen in der Datenbank zu arbeiten.
Hier als Beispiel der Service für die StudentTabelle.

//ToDo: Service Code hier einfügen.

<h2>Testen der Services:</h2>

Hier wurde wieder für jede Funktion in dem Service eine Test Funktion geschrieben womit überprüft wurde ob die Methode wie gewünscht funktioniert.

Ist es gewollt eine Methode zu Testes da Sie geändert oder neugeschrieben wurde muss hierfür eine Test Funktion geschrieben und unter dem Kommentar "# Call specific  Tests Here" aufgerufen werden. 

Es wurde auf Unit Test etc. verzichtet da wir keine Erfahrung mit diesen in Python haben und die Zeit dafür zu knapp war. 
Beispiel:
![PythonDatabaseTests](https://user-images.githubusercontent.com/23700090/175646719-65808b84-6194-4a27-b3c4-6d582e4f9a1e.gif)

## Fazit <a name="Fazit"></a>  
