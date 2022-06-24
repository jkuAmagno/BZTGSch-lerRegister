# BZTGSch-lerRegister

Ein SchülerProgramm für den unterricht

Datenbank Plannung:
Ziel was es eine Datenbank zu erstellen die Klassen, Schüler, Schulen und Lehrer verwaltet. Es wurde daraufhin eine Datenbank erstellt die 4 Tabellen enthält.

1. Schools
2. Classes
3. Teachers
4. Students

//ToDo: Bild hier einfügen.

Wie in dem Bild gezeigt. Gibt es eine Schule die mehrere Klassen haben kann. Diese Klassen haben immer einen Lehrer und mehrere Schüler.

Erstellung der Datenbank:
Zur erstellung der Datenbank wurde ein kleines Script geschrieben das das die Tabellen erstellt. Zum Testen wurde auch noch eins geschrieben das die Tabellen mit Testdaten füllt.

// ToDo: Code des Scriptes hier zeigen.

Um Daten in die Tabellen zu schreiben und zu lesen wurden für jede Tabelle ein Service geschrieben. Ein Service ist immer eine Class die nur Methoden enthält um mit den Tabellen in der Datenbank zu arbeiten.
Hier als Beispiel der Service für die StudentTabelle.

//ToDo: Service Code hier einfügen.

Testen der Services:
Hier wurde wieder für jede Funktion in dem Service eine Test Funktion geschrieben womit überprüft wurde ob die Methode wie gewünscht funktioniert.

Ist es gewollt eine Methode zu Testes da Sie geändert oder neugeschrieben wurde muss hierfür eine Test Funktion geschrieben und unter dem Kommentar "# Call specific  Tests Here" aufgerufen werden. 

Es wurde auf Unit Test etc. verzichtet da wir keine Erfahrung mit diesen in Python haben und die Zeit dafür zu knapp war. 
Beispiel:
![PythonDatabaseTests](https://user-images.githubusercontent.com/23700090/175646719-65808b84-6194-4a27-b3c4-6d582e4f9a1e.gif)


