
import sys

class lz77:
    """
       Esta classe comprime uma sequêencia de caracteres usando
       o algoritmo LZ77 como descrito em

       Esta é uma implementação didática, para exemplificar
       o funcionamento do algoritmo, e não possui nenhum tipo de
       otimização, por isso seu desempenho em situações reais
       deve ser muito abaixo do esperado.
    """
    def __init__(self, window_size = 65535, buffer_size=255):
        """
           Carrega os parâmetros de tamanho de janela e buffer
           de look-ahead
        """
        self.window_size = window_size
        self.buffer_size = buffer_size
    def encode(self, str):
        """
            Aplica o algoritmo LZ77 na cadeia de entrada, gerando
            uma lista de "tuplas" na saída. Cada tupla corresponde
            a (posição, tamanho, literal) onde posição é a posição
            relativa da cadeia encontrada na janela, tamanho é o
            tamanho dessa cadeia e literal é o símbolo que segue
            a cadeia nessa sequência.
        """
        ret = []
        i = 0
        while i < len(str):
            begin_window = i-self.window_size
            if begin_window < 0:
                begin_window = 0
            window = str[begin_window:i]
            buffer = str[i:i+self.buffer_size]
            tuple = (0, 0, str[i])
            # Este "loop" é o "coração" do algoritmo. Aqui procuramos
            # a maior sequência dentro da janela (window) que case
            # com o início do buffer. A implementação atual simplesmente
            # procura por ocorrências de substrings cada vez menores
            # do buffer até encontrar alguma. Implementações mais
            # eficientes usariam um dicionário de prefixos, uma trie
            # ou uma tabela de espalhamento.
            for size in range(len(buffer), 0, -1):
                index = window.rfind(buffer[0:size])
                if index >= 0:
                    literal = '' # a string vazia representa
                                 # o final do arquivo.
                    if i + size < len(str):
                        literal = str[i+size]
                    tuple = (len(window)-index-1, size, literal)
                    break
            i = i + tuple[1] + 1
            ret = ret + [tuple]
        return ret
    def decode(self, list):
        """
            A decodificação é extremamente simples: basta copiar a
            subsequência indicada pela tupla para o final da sequência
            de saída e acrescentar o novo carácter literal.
        """
        ret = ''
        for tuple in list:
            pos = len(ret) - tuple[0] - 1
            ret = ret + ret[pos:pos+tuple[1]] + tuple[2]
        return ret

if __name__ == "__main__":
    str = 'abracadabra'
    encoder = lz77(4,4)
    encoded = encoder.encode(str)
    print (encoded)

    decoder = lz77(8,4)
    decoded = decoder.decode(encoded)
    print (decoded)