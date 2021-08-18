def gera_primo(numero):

    import random

    def fatorando_2(n):
        k = 0
        q = n
        while q % 2 == 0:
            q //= 2
            k += 1
        return k, q

    def Miller_Rabin(numero, base):

        if numero % 2 == 0 or numero == 1:
            return 'composto'
        base = (base % numero)
        if base == 0 or base == 1:
            return 'inconclusivo'

        k, q = fatorando_2(numero-1)

        r = pow(base, q, numero)
        if r == 1 or r == numero-1:
            return 'inconclusivo'

        i = 0

        while True:
            r = pow(r, 2, numero)
            i += 1

            if r == 1 or i == k:
                return 'composto'
            if r == numero-1:
                return 'inconclusivo'

    while True:
        primo = random.randint(10**numero, 10**(numero+2))
        base = random.randint(2, primo-1)

        for _ in range (0,10):
            if Miller_Rabin(primo, base) == 'inconclusivo':
                return primo
            


def Euclides_estendido(a, b):

    x_antigo, y_antigo = 1, 0
    x_novo, y_novo = 0, 1
    Dividendo, Divisor = a, b
    while Divisor != 0:
        Quociente, Resto = divmod(Dividendo, Divisor)

        x_antigo, x_novo = x_novo, (x_antigo - Quociente*x_novo)
        y_antigo, y_novo = y_novo, (y_antigo - Quociente*y_novo)
        Dividendo, Divisor = Divisor, Resto

    return Dividendo, x_antigo, y_antigo


def gera_chaves():

    e = 7
    p = gera_primo(50)
    q = gera_primo(50)

    n = p * q
    phi = (p - 1)*(q - 1)


    mdc, d, _ = Euclides_estendido(e, phi)

    _,inversoP,_ = Euclides_estendido(p,q)
    _,inversoQ,_ = Euclides_estendido(q,p)

    while True:
        if mdc == 1:
            break
        e = e + 2

    FormReduzidaD = d%(p-1) #Forma reduzida d mod p-1
    FormReduzidaD2 = d%(q-1) #Forma reduzida d mod q-1

    d = d%phi #Forma reduzida d mod phi n
    

    return n, d, e, phi, p, q, FormReduzidaD, FormReduzidaD2, inversoP, inversoQ


def encriptar(frase, n, e):

    frase_criptografada = []
    blocos_lista = []

    símbolos_para_códigos = {'0': 111, '1': 112, '2': 113, '3': 114, '4': 115,
                             '5': 116, '6': 117, '7': 118, '8': 119, '9': 121, '=': 122, '+': 123,
                             '-': 124, '/': 125, '*': 126, 'a': 127, 'b': 128, 'c': 129, 'd': 131,
                             'e': 132, 'f': 133, 'g': 134, 'h': 135, 'i': 136, 'j': 137, 'k': 138,
                             'l': 139, 'm': 141, 'n': 142, 'o': 143, 'p': 144, 'q': 145, 'r': 146,
                             's': 147, 't': 148, 'u': 149, 'v': 151, 'w': 152, 'x': 153, 'y': 154,
                             'z': 155, 'á': 156, 'à': 157, 'â': 158, 'ã': 159, 'é': 161, 'ê': 162,
                             'í': 163, 'ó': 164, 'ô': 165, 'õ': 166, 'ú': 167, 'ç': 168, 'A': 169,
                             'B': 171, 'C': 172, 'D': 173, 'E': 174, 'F': 175, 'G': 176, 'H': 177,
                             'I': 178, 'J': 179, 'K': 181, 'L': 182, 'M': 183, 'N': 184, 'O': 185,
                             'P': 186, 'Q': 187, 'R': 188, 'S': 189, 'T': 191, 'U': 192, 'V': 193,
                             'W': 194, 'X': 195, 'Y': 196, 'Z': 197, 'Á': 198, 'À': 199, 'Â': 211,
                             'Ã': 212, 'É': 213, 'Ê': 214, 'Í': 215, 'Ó': 216, 'Ô': 217, 'Õ': 218,
                             'Ú': 219, 'Ç': 221, ',': 222, '.': 223, '!': 224, '?': 225, ';': 226,
                             ':': 227, '_': 228, '(': 229, ')': 231, '"': 232, '#': 233, '$': 234,
                             '%': 235, '@': 236, ' ': 237, '\n': 238}

    for y in frase:
        frase_criptografada.append(símbolos_para_códigos[y])
    print(frase_criptografada)

    for x in frase_criptografada:
        blocos_lista.append(pow(x, e, n))
    print(blocos_lista)

    return blocos_lista


def descriptar(blocos_lista, n, d):

    códigos_para_símbolos = {111: '0', 112: '1', 113: '2', 114: '3', 115: '4',
                             116: '5', 117: '6', 118: '7', 119: '8', 121: '9', 122: '=', 123: '+',
                             124: '-', 125: '/', 126: '*', 127: 'a', 128: 'b', 129: 'c', 131: 'd',
                             132: 'e', 133: 'f', 134: 'g', 135: 'h', 136: 'i', 137: 'j', 138: 'k',
                             139: 'l', 141: 'm', 142: 'n', 143: 'o', 144: 'p', 145: 'q', 146: 'r',
                             147: 's', 148: 't', 149: 'u', 151: 'v', 152: 'w', 153: 'x', 154: 'y',
                             155: 'z', 156: 'á', 157: 'à', 158: 'â', 159: 'ã', 161: 'é', 162: 'ê',
                             163: 'í', 164: 'ó', 165: 'ô', 166: 'õ', 167: 'ú', 168: 'ç', 169: 'A',
                             171: 'B', 172: 'C', 173: 'D', 174: 'E', 175: 'F', 176: 'G', 177: 'H',
                             178: 'I', 179: 'J', 181: 'K', 182: 'L', 183: 'M', 184: 'N', 185: 'O',
                             186: 'P', 187: 'Q', 188: 'R', 189: 'S', 191: 'T', 192: 'U', 193: 'V',
                             194: 'W', 195: 'X', 196: 'Y', 197: 'Z', 198: 'Á', 199: 'À', 211: 'Â',
                             212: 'Ã', 213: 'É', 214: 'Ê', 215: 'Í', 216: 'Ó', 217: 'Ô', 218: 'Õ',
                             219: 'Ú', 221: 'Ç', 222: ',', 223: '.', 224: '!', 225: '?', 226: ';',
                             227: ':', 228: '_', 229: '(', 231: ')', 232: '"', 233: '#', 234: '$',
                             235: '%', 236: '@', 237: ' ', 238: '\n'}

    decriptados = []

    for x in blocos_lista:
        decriptados.append(pow(x,d, n))
    print(decriptados)

    decriptados_texto = []

    for v in decriptados:
        decriptados_texto.append(códigos_para_símbolos[v])

    return "".join(decriptados_texto)


n, d, e, phi, p, q, FormReduzidaD, FormReduzidaD2, inversoP, inversoQ = gera_chaves()


(descriptar(encriptar('Olá Git Hub',n,e),n,d))