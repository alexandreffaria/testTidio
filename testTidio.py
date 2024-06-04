import pyautogui as pyau
import time
import argparse

def setupInicial():
    selecionar("chatBubble")
    pyau.hotkey('ctrl','r')
    time.sleep(5)
    selecionar("chatBubble")
    selecionar("caixaTexto")
    escrever("Alexandre")
    selecionar("revenda")
    selecionar("dentista")
    time.sleep(10)
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
    if objeto == "irParaPedido":
        coord = (1737,890)
    if objeto == "linkPedido":
        coord = (1675,770)
        
    pyau.moveTo(coord) 
    pyau.click()
    time.sleep(2)

def escrever(palavras):
    pyau.typewrite(f"{palavras}\n")
    time.sleep(2.5)

def todosOsProdutos(qtdAzul, qtdRosa, qtdLaranja, qtdVerde, qtdLivro):
    setupInicial()
    if qtdAzul > 0 or qtdRosa > 0 or qtdLaranja > 0 or qtdVerde > 0:
        selecionar("pd")
        selecionar("caixaTexto") 
        escrever(qtdAzul)
        escrever(qtdRosa)
        escrever(qtdLaranja)
        escrever(qtdVerde)

    if qtdLivro > 0:
        selecionar("livro")
        selecionar("caixaTexto")
        escrever(qtdLivro)

    selecionar("finalizarPedido")
    selecionar("irParaPedido")
    selecionar("linkPedido")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Teste de geração de pedidos.")
    parser.add_argument('--azul', type=int, required=True, help='Quantidade de porta dentes azuis')
    parser.add_argument('--rosa', type=int, required=True, help='Quantidade de porta dentes rosas')
    parser.add_argument('--laranja', type=int, required=True, help='Quantidade de porta dentes laranjas')
    parser.add_argument('--verde', type=int, required=True, help='Quantidade de porta dentes verdes')
    parser.add_argument('--livro', type=int, required=True, help='Quantidade de livros')

    args = parser.parse_args()

    qtdAzul = args.azul
    qtdRosa = args.rosa
    qtdLaranja = args.laranja
    qtdVerde = args.verde
    qtdLivro = args.livro

    todosOsProdutos(qtdAzul,qtdRosa,qtdLaranja,qtdVerde,qtdLivro)


