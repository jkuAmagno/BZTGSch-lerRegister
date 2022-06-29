# BZTGSch-lerRegister
Ein Schülerverwaltungs Programm für den Unterricht an der BBS Haarentor der Klasse FA2C.

# Inhaltsverzeichniss
1. [Plannung](#Planung)
     1. [Programm Idee](#PlanungProgrammIdee)
     2. [GUI](#PlanungGUI)
     3. [Datenbank](#PlanungDatenbank)
          1. [ERM](#ERM)
          2. [Datenmodell](#Datenmodell)
     5. [Aufgabenverteilung](#PlanungAufgabenverteilung)
2. [Durchführung](#Durchführung)
     1. [GUI](#DurchführungGUI)
     2. [Datenbank](#DurchführungDatenbank)
3. [Überprüfung](#Überprüfung)
     1. [Datenbank Services](#ÜberprüfungDatenbankServices)
5. [Act?Wird es in der Doku benötigt?](#Act)



<a name="Planung"></a>  
## Planung
<a name="PlanungProgrammIdee"></a> 
### Programm Idee: 
Das Programm soll in der Lage sein für Schulen die Klassen, Lehrer und Schüler zu verwalten. Dazu soll es möglich sein diese anzuglegen und anzuzeigen. Es soll aber nicht möglich sein diese zu löschen aus zeitlichen gründen. In der GUI wird es möglich sein eine Klasse auszuwählen und anzuzeigen. 

<a name="PlanungGUI"></a> 
### GUI
Die GUI ist in 3 Fenster unterteilt. Dem Haupfenster, Schülerfenster und dem Klassenfenster.  

#### Hauptfenster
Im Hauptfenster befindet sich eine Liste der in der Datenbank verfügbaren Klassen. Die Liste wird angezeigt, wenn Sie auf „Update“ klicken, und wenn Sie eine Klasse aus der Liste auswählen, werden die Schüler und Lehrer für diese Klasse angezeigt.

// TODO Bild ändern 420 ist nicht so gut in einer Doku. Plus vielleicht ein Gif draus machen

![image](https://user-images.githubusercontent.com/23700090/176032764-c9f3276b-96db-4745-be95-701ac701eaca.png)

#### Schülerfenster
Wenn auf "Schüler hinzufügen" geklickt wird öffnet sich das Schülerfenster. Hier kann der Name, Alter eingegeben werden oder den Schüler einer Klasse zuweisen.  
Das zuweisen der Klasse erfolgt indem auf eine Klasse in der rechten Tabelle geklickt wird.

![image](https://user-images.githubusercontent.com/23700090/176033394-ca7ff8f9-06bd-470a-99e8-7cc62c51ad9e.png)

#### Klassenfenster
Das Klassenfenster wird geöffnet indem auf den Knopf "Klasse hinzufüben" geklickt wird. Hier muss erst der Klassenname eingegeben werden dann der Lehrer ausgewählt werden. 

![image](https://user-images.githubusercontent.com/23700090/176034086-f4cedcdf-e907-4202-8561-539ef12ee030.png)


<a name="PlanungDatenbank"></a> 
### Datenbank
Da das Programm Schulen, Klassen, Leherer und Schüler verwalten soll benötigen wir 4 Tabellen je eine für jeden dieser Punkte. Hierbei sollte eine Klasse immer zu einer Schule gehören. Ein Lehrer leitet eine Klasse und Schüler sind einer Klasse zugewiesen. Die einzelnen Attribute jeder Tabelle können im Datenmodell nachgeschaut werden.  

<a name="ERM"></a>  
### ERM: 
Als erstes wurde ein ERM erstellt das die verschiedenen Beziehnungen der Tabellen anzeigt.
![image](https://user-images.githubusercontent.com/23700090/175651691-e1aa23f4-e13a-4a4c-8895-118429741f20.png)

<a name="Datenmodell"></a>
### Datenmodell:
Als nächstes wurde das Datenmodell erstellt und die Attribute der Tabellen hinzugefügt.
![image](https://user-images.githubusercontent.com/23700090/175788152-a03a0482-1f85-43cb-9ad5-df04576cc873.png)

Als das Team zufrieden war wurde mit der Umsetzung begonnen. 
<a name="PlanungAufgabenverteilung"></a> 
### Aufgabenverteilung
- Keno: Datenbankplanung und Entwicklung / Doku
- Mohammad, Justin: GUI + Logik

<a name="Durchführung"></a> 
## Durchführung

<a name="DurchführungGUI"></a> 
### GUI
Für jedes Fenster wurde eine Datei erstellt. In dieser Datei werden alle ListBoxen, Entrys, Buttons und Labels mit Tkinter erstellt. 

[Beispiel Schülerfenster](https://github.com/jkuAmagno/BZTGSch-lerRegister/blob/main/NewStudentView.py)

Die Funktionalität der einzelnen Fenster steht in der [MainViewCodeBehind](https://github.com/jkuAmagno/BZTGSch-lerRegister/blob/main/MainViewCodeBehind.py) Datei.
![image](https://user-images.githubusercontent.com/23700090/176378373-1058e73f-0291-4179-ad6c-832b97549cd1.png)

<a name="DurchführungDatenbank"></a> 
### Datenbank
Zur erstellung der Datenbank wurde ein kleines Script in Python geschrieben das das die einzelnen Tabellen erstellt. Als Sprache wurde Python vorgegen und für die Datenbank wurde SQLite3 gewählt da hierfür Tutorials zur Verfügung gestellt bekommen haben.   
[Link zum Skriptfile](https://github.com/jkuAmagno/BZTGSch-lerRegister/blob/main/Services/CreateDatabase.py)

Im unteren Bild wird die Datenbank erstellt. Es wurden mehrere Methoden dazu geschrieben. Die erste erstellt die Datenbank und löscht die alte falls eine vorhanden ist. Dann werden die einzelnen Tabellen erstellt. In der letzten Methode werden Daten zum Testen in die Datenbank geschrieben. Diese kann für die Produktion auskommentiert werden. 

![image](https://user-images.githubusercontent.com/23700090/175788934-f04cb068-a7d7-4c9a-abaa-ac3319f2aa17.png)

Um Daten in die Tabellen zu schreiben und zu lesen wurden für jede Tabelle ein Service geschrieben. Ein Service ist immer eine Klasse die nur Methoden enthält um mit den Tabellen in der Datenbank zu arbeiten.
Hier als Beispiel der Service für die StudentTabelle.

[Link zum Student Service](https://github.com/jkuAmagno/BZTGSch-lerRegister/blob/main/Services/StudentService.py)

![image](https://user-images.githubusercontent.com/23700090/175789111-44807d72-795a-4933-89b2-28bf6c857d68.png)

<a name="Überprüfung"></a> 
## Überprüfung

<a name="ÜberprüfungDatenbankServices"></a> 
### Datenbank Services 

Hier wurde wieder für jede Methode in dem jeweiligen Service eine Test Methode geschrieben womit überprüft wurde ob die Servicemethode wie gewünscht funktioniert.

Ist es gewollt eine Methode zu Testes da Sie geändert oder neugeschrieben wurde muss hierfür eine Test Funktion geschrieben und unter dem Kommentar "# Call specific  Tests Here" aufgerufen werden. 

Es wurde auf Unit Test etc. verzichtet da wir keine Erfahrung mit diesen in Python haben und die Zeit dafür zu knapp war. 
Beispiel:
![PythonDatabaseTests](https://user-images.githubusercontent.com/23700090/175646719-65808b84-6194-4a27-b3c4-6d582e4f9a1e.gif)

<a name="Act"></a> 
## Act
Wenn etwas nicht funktioniert hat mussten wir Dinge anpassen. Das war Hauptsächlich nötig wenn die GUI eine Methode von der Datenbank benötigte die wir vorher nicht berücksichtigt hatten. Ein 2 Grund war Aufgaben neuverteilung durch Krankheit. Ansonsten musste nichts angepasst werden. 
