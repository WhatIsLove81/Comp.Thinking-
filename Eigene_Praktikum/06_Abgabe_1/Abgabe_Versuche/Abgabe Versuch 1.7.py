def getRautenGroesse(rauten_groesse):
    wahl_groesse = None 

    while wahl_groesse is None or not (3 <= wahl_groesse <= 10):
        try:
            wahl_groesse = int(input('Bitte geben Sie die gewünschte Rautengröße (3-10)ein: '))
            if 3 <= wahl_groesse <= 10 :
                print(f'Sie haben eine Rautengröße von {wahl_groesse} gewählt.')
                break
            else:
                print(f'Fehler: Der eigegebene Wert({wahl_groesse}) muss zwischen 3 und einschließlich 10 liegen.')
        except ValueError:
            print(f'Fehler: Der eingegebene Wert muss eine ganze Zahl sein die zwischen 3 und einschließlich 10 liegt.')

    def printRaute(): 

#-------Leerzeichen Funktion-------------------------------------------------------------------------------------------------------------
        def printSpace(anzahl_spaces):
            print(" " * anzahl_spaces, end="")

#-------Rauten Funktion------------------------------------------------------------------------------------------------------------------
        def printRauteObereHaelfte():
            for zeilen_num in range(1, rauten_groesse + 1 , 1):
                fuehrendeLeerzeichen = rauten_groesse - zeilen_num
                mittlereLeerzeichen = 2 * zeilen_num - 1

                printSpace(fuehrendeLeerzeichen)
                print("*", end="")

                if mittlereLeerzeichen > 0:
                    printSpace(mittlereLeerzeichen)
                    print("*", end="")
        
                print()

        def printRauteUntereHaelfte():
            for zeilen_num in range(rauten_groesse, 0, -1): # rauten_groesse -1 ist auch eine option
                fuehrendeLeerzeichen = rauten_groesse - zeilen_num
                mittlereLeerzeichen = 2 * zeilen_num - 1

                printSpace(fuehrendeLeerzeichen)
                print("*", end="")

                if mittlereLeerzeichen > 0:
                    printSpace(mittlereLeerzeichen)
                    print("*", end="")
        
                print()
            
#-------ober-/untere Hälfte Aufrufen---------------------------------------------------------------------------------------------------------
        printRauteObereHaelfte()
        printRauteUntereHaelfte()

#---Ganze Rautenfunktion aufrufen--------------------------------------------------------------------------------------------------------        
    printRaute()

rauten_groesse = int(input('Bitte geben Sie die gewünschte Rautengröße (3-10) erneut ein: '))
getRautenGroesse(rauten_groesse)