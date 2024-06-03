import pyautogui as pyau
import time
import sys

if len(sys.argv) != 1:
    print("Usage: python3 testTidio.py")
    sys.exit(1)


def setupInicial():
    selecionar("chatBubble")
    selecionar("caixaTexto")
    pyau.typewrite("Alexandre\n")
    time.sleep(.5)
    selecionar("revenda")
    selecionar("dentista")
    time.sleep(12)
    selecionar("fazerPedido")
    selecionar("caixaTexto")
    escrever("Fo Fa")
    escrever("alexandreffaria@me.com")
    escrever("31933006786")
    
   
def selecionar(objeto):
    if objeto == "chatBubble":
        coord = (1860,997)
    if objeto == "caixaTexto":
        coord = (1573,980)
    if objeto == "finalizarPedido":
        coord = (1737,890)  
    if objeto == "fazerPedido":
        coord = (1649,858)
    if objeto == "pd":
        coord = (1698,799) 
    if objeto == "livro":
        coord = (1722,843) 
    if objeto == "revenda":
        coord = (1658,712)
    if objeto == "dentista":
        coord = (1615,831) 
        
    pyau.moveTo(coord) 
    pyau.click()
    time.sleep(2)

def escrever(palavras):
    pyau.typewrite(f"{palavras}\n")
    time.sleep(2.5)

def todosOsProdutos(qtdAzul, qtdRosa, qtdVerde, qtdLaranja, qtdLivro):
    setupInicial()

    selecionar("pd")
    selecionar("caixaTexto")
    
    escrever(qtdRosa)
    escrever(qtdAzul)
    escrever(qtdLaranja)
    escrever(qtdVerde)

    selecionar("livro")
    selecionar("caixaTexto")
    escrever(qtdLivro)
    selecionar("finalizarPedido")

todosOsProdutos(qtdAzul=5,qtdRosa=5,qtdLaranja=0,qtdVerde=10,qtdLivro=5)

time.sleep(5)