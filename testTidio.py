import pyautogui as pyau
import time
import sys

if len(sys.argv) != 1:
    print("Usage: python3 testTidio.py")
    sys.exit(1)


def setupInicial():
    pyau.moveTo(1860,997) # Chat bubble
    pyau.click()
    time.sleep(1)
    pyau.moveTo(1573,980) # Text input
    pyau.click()
    time.sleep(1)
    pyau.typewrite("Alexandre\n")
    time.sleep(.5)
    pyau.moveTo(1658,712) # Click Revenda
    pyau.click()
    time.sleep(1)
    pyau.moveTo(1615,831) # Click Dentista
    pyau.click()
    time.sleep(12)
    pyau.moveTo(1649,858) # Click Fazer Pedido
    pyau.click()
    time.sleep(3)
    pyau.moveTo(1573,980)
    pyau.click()
    time.sleep(1)
    pyau.typewrite("Fo Fa\n")
    time.sleep(2.5)
    pyau.typewrite("alexandreffaria@me.com\n")
    time.sleep(2.5)
    pyau.typewrite("31933006786\n")
    time.sleep(2.5)
   



def todosOsProdutos(azul, rosa, verde, laranja, livro):
    setupInicial()
    

