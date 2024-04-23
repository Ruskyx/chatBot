def doppia_lettera(str):
    risultato = ''
    for lettera in str:
        risultato += lettera * 2
    return risultato

def funzione_segreta(a, b):
    # Scrivi qui il tuo codice!
    result = str(a) + str(b)
    return int(result)    
print(doppia_lettera("Ciao"))
print(funzione_segreta(1, 2))
print(funzione_segreta("Ciao, ", "Mondo!"))