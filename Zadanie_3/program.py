import Zadanie_3.calculations.pakiet

wart_pocz = float(input("Podaj wartość początkową: "))
oprocent = float(input("Podaj aktuane oprocentowanie: "))
okres = float(input("Podaj okres lokaty w latach: "))

print("Wartość lokaty wzrośnie do: ", Zadanie_3.calculations.pakiet.wartosc_lokaty(wart_pocz,oprocent,okres))

