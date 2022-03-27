import os
clear = lambda: os.system('cls')
from unidecode import unidecode #normaliza el text
import clipboard
import colorama
from colorama import Fore, Style
colorama.init()

print(Fore.CYAN +'Morse'+Style.RESET_ALL +': m '
+ Fore.CYAN +'\nBinario'+Style.RESET_ALL +': b '
+Fore.CYAN+'\nCésar'+Style.RESET_ALL +': c '
+ Fore.CYAN +'\nVigenère'+Style.RESET_ALL+': v '
+Fore.CYAN+'\nEliminar caracteres'+Style.RESET_ALL+': e '
+Fore.CYAN+'\nSeparador de texto en grupos de'+Style.RESET_ALL+Fore.YELLOW+' n '+Style.RESET_ALL+Fore.CYAN+'caracteres'+Style.RESET_ALL+': s')
print(Fore.CYAN+'Mostrar la'+Fore.YELLOW+' n '+Style.RESET_ALL+Fore.CYAN+'letra de cada intervalo de amplitud'+Style.RESET_ALL+Fore.YELLOW+' m'+Style.RESET_ALL+': ml'
+Fore.CYAN+'\nTeclado grado 1'+Style.RESET_ALL+': t1 '
+Fore.CYAN+'\nTeclado grado 2'+Style.RESET_ALL+': t2 '
+Fore.CYAN+'\nMayúscula-minúscula'+Style.RESET_ALL+': p'
+Fore.RED+'\nLista de cifrados'+Style.RESET_ALL+': l'
+Fore.YELLOW+'\nLimpiar pantalla'+Style.RESET_ALL+': clear'
+Fore.GREEN+'\nInformación'+Style.RESET_ALL+': help')

#Todas las listas y diccionarios
lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
        'x', 'y', 'z'] #Alfabeto español
lista2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
        'x', 'y', 'z'] #Alfabeto inglés
lista3 = {'a':'.-', 'b':'-...', 'c':'-.-.', 'ch':'----', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-'
            , 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-',
            'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', 'ñ':'..-..', ' ':'/', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
            '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'
        }
lista4 = {'.-':'a', '-...':'b', '-.-.':'c', '----':'ch', '-..':'d', '.':'e', '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k'
            , '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v',
            '.--':'w', '-..-':'x', '-.--':'y', '--..':'z', '..-..':'ñ', '/':' ', '.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5',
            '-....':'6', '--...':'7', '---..':'8', '----.':'9', '-----':'0'
        }
lista5 = {'a':'00001', 'b':'00010', 'c':'00011', 'd':'00100', 'e':'00101', 'f':'00110', 'g':'00111', 'h':'01000', 'i':'01001', 'j':'01010', 'k':'01011', 'l':'01100',
            'm':'01101', 'n':'01110', 'o':'01111', 'p':'10000', 'q':'10001', 'r':'10010', 's':'10011', 't':'10100', 'u':'10101', 'v':'10110', 'w':'10111',
            'x':'11000', 'y':'11001', 'z':'11010', 'ñ':'11011', ' ':'00000'
        }
lista5_1 = {'00001':'a', '00010':'b', '00011':'c', '00100':'d', '00101':'e', '00110':'f', '00111':'g', '01000':'h', '01001':'i', '01010':'j', '01011':'k', '01100':'l',
            '01101':'m', '01110':'n', '01111':'o', '10000':'p', '10001':'q', '10010':'r', '10011':'s', '10100':'t', '10101':'u', '10110':'v', '10111':'w',
            '11000':'x', '11001':'y', '11010':'z', '11011':'ñ', '00000':' '
        }
lista6 = {'a':'@', 'b':';', 'c':"'", 'd':'€', 'e':'3', 'f':'_', 'g':'&', 'h':'-', 'i':'8', 'j':'+', 'k':'('
            , 'l':')', 'm':'?', 'n':'!', 'o':'9', 'p':'0', 'q':'1', 'r':'4', 's':'#', 't':'5', 'u':'7', 'v':':',
            'w':'2', 'x':'"', 'y':'6', 'z':'*', 'ñ':'/', ' ':' '
        }
lista7 = {'a':'£', 'b':'✓', 'c':'®', 'd':'$', 'e':'|', 'f':'¢', 'g':'^', 'h':'°', 'i':'×', 'j':'=', 'k':'{'
            , 'l':'}', 'm':']', 'n':'[', 'o':'¶', 'p':'∆', 'q':'~', 'r':'•', 's':'¥', 't':'√', 'u':'÷', 'v':'™',
            'w':'`', 'x':'©', 'y':'π', 'z':'%', 'ñ':"\\"
            , ' ':' '
        }
lista8 = {'@':'a', ';':' b', "'":'c', '€':'d', '3':'e', '_':'f', '&':'g', '-':'h', '8':'i', '+':'j', '(':'k'
            , ')':'l', '?':'m', '!':'n', '9':'o', '0':'p', '1':'q', '4':'r', '#':'s', '5':'t', '7':'u', ':':'v',
            '2':'w', '"':'x', '6':'y', '*':'z', '/':'ñ', ' ':' '
        }
lista9 = {'£':'a', '✓':'b', '®':'c', '$':'d', '|':'e', '¢':'f', '^':'g', '°':'h', '×':'i', '=':'j', '{':'k'
            , '}':'l', ']':'m', '[':'n', '¶':'o', '∆':'p', '~':'q', '•':'r', '¥':'s', '√':'t', '÷':'u', '™':'v',
            '`':'w', '©':'x', 'π':'y', '%':'z', "\\":'ñ', ' ':' '
        }
desfases = [] #Aquí se almacenan las letras de la palabra clave en Vigenère
caracteres_eliminar = [] #Aquí se almacenan los caracters a eliminar
#Todas las funciones
def cesar1(texto):
    cadena = str()
    aux = str() #Esta variable permite poder trabajar con mayúsculas y minúsuculas a la vez
    for i in range(1, 27):
        for letra in texto: #1 hace referencia al función con el alfabeto español y la 2 con el alfabeto inglés
            letra = unidecode(letra)
            if (letra == ' '):
                cadena += ' '
            else:
                if (letra.islower()):
                    cadena += lista1[(lista1.index(letra)+i)%27]
                elif (letra.isupper()):
                    aux = lista1[(lista1.index(letra.lower())+i)%27]
                    cadena += aux.upper()
        print('%d. %s' %(i, Fore.GREEN+cadena+Style.RESET_ALL))
        cadena = ''
def cesar2(texto):
    cadena = str()
    aux = str()
    for i in range(1, 26):
        for letra in texto:
            if (letra == ' '):
                cadena += ' '
            else:
                if (letra.islower()):
                    cadena += lista2[(lista2.index(letra)+i)%26]
                elif (letra.isupper()):
                    aux = lista2[(lista2.index(letra.lower())+i)%26]
                    cadena += aux.upper()
        print('%d. %s' %(i, Fore.GREEN+cadena+Style.RESET_ALL))
        cadena = ''
def vigenere1(texto, key, a, encriptar): #texto: texto a convertir, key: palabra clave, a: es la que hay que indicar si vale 0 o 1, encriptar: indica si se quiere encriptar o desencriptar el mensaje
    i = 0
    cadena = str()
    aux = str()
    for letra in key:
        desfases.append(letra) #Va añadiendo cada letra de la palabra clave a la lista desfases[]
    for letra in texto:
        letra = unidecode(letra)
        if (letra != ' '):
            if (encriptar == 'e' or encriptar == 'E'): #Aquí se realiza el funcionamiento de encriptar y desencriptar, y más abajo está el código que permite trabajar con mayúsculas y minúsculas a la vez
                if (letra.islower()):
                    cadena += lista1[(lista1.index(letra)+lista1.index(desfases[i%len(key)]) + a)%27]
                elif (letra.isupper()):
                    aux = lista1[(lista1.index(letra.lower())+lista1.index(desfases[i%len(key)]) + a)%27]
                    cadena += aux.upper()
            elif (encriptar == 'd' or encriptar == 'D'):
                if (letra.islower()):
                    cadena += lista1[(lista1.index(letra)-lista1.index(desfases[i%len(key)]) - a)%27]
                elif (letra.isupper()):
                    aux = lista1[(lista1.index(letra.lower())-lista1.index(desfases[i%len(key)]) - a)%27]
                    cadena += aux.upper()
            i += 1
        else:
            cadena += ' '
    return cadena
def vigenere2(texto, key, a, encriptar):
    i = 0
    cadena = str()
    aux = str()
    for letra in key:
        desfases.append(letra)
    for letra in texto:
        if (letra != ' '):
            if (encriptar == 'e' or encriptar == 'E'):
                if (letra.islower()):
                    cadena += lista2[(lista2.index(letra)+lista2.index(desfases[i%len(key)]) + a)%26]
                elif (letra.isupper()):
                    aux = lista2[(lista2.index(letra.lower())+lista2.index(desfases[i%len(key)]) + a)%26]
                    cadena += aux.upper()
            elif (encriptar == 'd' or encriptar == 'D'):
                if (letra.islower()):
                    cadena += lista2[(lista2.index(letra)-lista2.index(desfases[i%len(key)]) - a)%26]
                elif (letra.isupper()):
                    aux = lista2[(lista2.index(letra.lower())-lista2.index(desfases[i%len(key)]) - a)%26]
                    cadena += aux.upper()
            i += 1
        else:
            cadena += ' '
    return cadena
def texto_a_morse(texto):
    cadena = str()
    aux = str() #Variable que permite pasar de "ch" a "----"
    for letra in texto.lower():
        letra = unidecode(letra)
        cadena += lista3[letra] + ' '
    return cadena
def morse_a_texto(texto):
    cadena1 = str() #Aquí se almacenará los puntos y rayas que definirán a un caracter
    cadena2 = str() #Aquí se guardará la letra que se imprimirá
    i = 1 #Variable auxiliar para solucionar el problema de no mostrar la última letra del mensaje al imprimirlo
    for letra in texto:
        if (letra != ' '):
            cadena1 += letra
            if (i == len(texto)):
                cadena2 += lista4[cadena1]
        elif (letra == ' '):
            cadena2 += lista4[cadena1]
            cadena1 = ''
        i += 1
    return cadena2
def separador(texto, n):
    cadena = str()
    i = 0
    for letra in texto:
        if (letra.islower()):
            if (i%n == 0 and i != 0):
                cadena += ' ' + letra
            else:
                cadena += letra
        elif (letra.isupper()):
            if (i%n == 0 and i != 0):
                cadena += ' ' + letra.upper()
            else:
                cadena += letra.upper()
        else:
            if (i%n == 0 and i != 0):
                cadena += ' ' + letra
            else:
                cadena += letra
        i += 1
    return cadena
def eliminador_de_caracteres(texto, caracteres):
    cadena = str()
    for letra2 in caracteres:
        caracteres_eliminar.append(letra2)
    for letra in texto:
        if (letra.islower()):
            if (letra not in caracteres_eliminar):
                cadena += letra
        elif (letra.isupper()):
            if (letra not in caracteres_eliminar):
                cadena += letra.upper()
        else:
            if (letra not in caracteres_eliminar):
                cadena += letra
    return cadena
def texto_a_grado1(texto):
    cadena = str()
    for letra in texto.lower():
        letra = unidecode(letra)
        cadena += lista6[letra]
    return cadena
def texto_a_grado2(texto):
    cadena = str()
    for letra in texto.lower():
        letra = unidecode(letra)
        cadena += lista7[letra]
    return cadena
def grado1_a_texto(texto):
    cadena = str()
    for letra in texto:
        cadena += lista8[letra]
    return cadena
def grado2_a_texto(texto):
    cadena = str()
    for letra in texto:
        cadena += lista9[letra]
    return cadena
def texto_a_binario_sinAscii(texto):
    cadena = str() #Variable en la que se almacena el texto final
    for letra in texto.lower():
        letra = unidecode(letra)
        cadena += lista5[letra] + ' '
    return cadena
def texto_a_binario_conAscii(texto):
    cadena = str()
    for letra in texto:
        letra = unidecode(letra)
        if (letra.islower()):
            cadena += '011' + lista5[letra] +' '
        elif (letra.isupper()):
            cadena += '010' + lista5[letra.lower()] + ' '
        elif (letra == ' '):
            cadena += '001' + lista5[letra] + ' '
        elif (letra == 'ñ'):
            cadena += '10100100' + ' '
        elif (letra == 'Ñ'):
            cadena += '10100101' + ' '
    return cadena
def binario_sinAscii_a_texto(texto):
    cadena1 = str() #Aquí se almacenará los 0's y 1's que definirán a un caracter
    cadena2 = str() #Aquí se guardará el mensaje descifrado
    cadena3 = str()
    for letra in texto:
        if (letra != ' '):
            cadena1 += letra
            if (len(cadena1) == 5):
                cadena2 += lista5_1[cadena1]
                cadena1 = ''
    return cadena2
def binario_conAscii_a_texto(texto):
    cadena1 = str() #Aquí se almacenan los 0's y 1's que definirán a un caracter
    cadena2 = str() #Aquí se almacena el texto que se imprimirá
    cadena3 = str() #Aquí se almacena los 3 dígitos iniciables de cada número
    aux = str() # Variable que se encarga de permitir mayúsculas
    i = 1 #Variable que se encarga en descontar los 3 primeros dígitos de cada número
    aux = str() #Variable auxiliar para contener las letras y sumárselo a cadena2
    for letra in texto:
        if (i%9 == 1 or i%9 == 2 or i%9 == 3):
            cadena3 += letra
        elif (cadena3 == '011'):
            if (letra != ' ' and (i)%9 != 1 and (i)%9 != 2 and (i)%9 != 3):
                cadena1 += letra
                if (len(cadena1) == 5):
                    cadena2 += lista5_1[cadena1]
                    cadena1 = ''
                    cadena3 = ''
        elif (cadena3 == '010'):
            if (letra != ' ' and (i)%9 != 1 and (i)%9 != 2 and (i)%9 != 3):
                cadena1 += letra
                if (len(cadena1) == 5):
                    aux = lista5_1[cadena1]
                    cadena2 += aux.upper()
                    cadena1 = ''
                    cadena3 = ''
        elif (cadena3 == '001'):
            cadena1 += letra
            if (len(cadena1) == 5):
                cadena2 += lista5_1[cadena1]
                cadena1 = ''
                cadena3 = ''
        elif (cadena3 == '101'):
            if (letra != ' ' and (i)%9 != 1 and (i)%9 != 2 and (i)%9 != 3):
                cadena1 += letra
                if (len(cadena1) == 5 and cadena1 == '00100'):
                    cadena2 += 'ñ'
                    cadena1 = ''
                    cadena3 = ''
                elif (len(cadena1) == 5 and cadena1 == '00101'):
                    cadena2 += 'Ñ'
                    cadena1 = ''
                    cadena3 = ''
        i += 1
    return cadena2
def mostrar_letras(texto , n, m):
    cadena = ''
    i = 0
    for letra in texto:
        if ((i+(m-n+1))%m == 0):
            cadena += letra
        i += 1
    return cadena
def mayuscula_minuscula(texto, m):
    if (m == 'a' or m == 'A'):
        return texto.upper()
    elif (m == 'b' or m == 'B'):
        return texto.lower()
    elif (m == 'c' or m == 'C'):
        return texto.title()
def entrada(): #Esta función organiza las otras funciones
    print('')
    n1 = -1
    ascii = str() #referente a binario
    alfabeto = str()
    a1 = 2 #referente a Vigenère
    encriptar1 = str()
    caracteres1 = str() #Aquí se almacenan los caracteres que se eliminaran
    t = str() #variable que se encarga de controlar el cifrado o descifrado en varias funciones y se utiliza para almacenar los caracteres que se desea eliminar
    cifrado = str(input('Introduce uno de los comandos para realizar una función: '))
    if (cifrado == 'help' or cifrado == 'HELP'):
        print(Fore.CYAN+'\nAquí viene una breve explicación de lo que hace cada función:\n'+Style.RESET_ALL)
        print('-'+Fore.GREEN+' Morse: '+Style.RESET_ALL+'convierte letras en puntos y rayas, y también funciona al revés.\n')
        print("-"+Fore.GREEN+' Binario: '+Style.RESET_ALL+"convierte letras en 0's y 1's, y al revés. Si selecciona la versión con ASCII, los número resultantes serán más grandes y habrá diferencia entre mayúsculas y minúsculas (la diferencia será 3 dígitos que se ponen a la izquierda, mayúscula: 010, minúscula: 011), cosa que en la versión sin ASCII no.\n")
        print('-'+Fore.GREEN+' Cifrado César: '+Style.RESET_ALL+'sistema de cifrado que consiste en desplazar las letras de una palabra un número de posiciones concretas en el abecedario.\n\n'+Fore.YELLOW+' Ejemplo: '+Style.RESET_ALL+'texto: agua, desplazamiento: 3, palabra resultante: djxd\n\n(Aunque en este caso el programa muestra todas las opciones posibles, y puedes elegir entre alfabeto español o inglés).\n')
        print('-'+Fore.GREEN+' Cifrado Vigenère: '+Style.RESET_ALL+'sistema similar el Cifrado César, sólo que en este caso se aplica en vez de un único desplazamiento, se aplican varios de forma periódica, y vienen dados por una palabra "clave", las letras de esa palabra clave dirán cuanto se irá desplazando cada letra (cada letra tendría asignado un número de acuerdo a la posición que ocupa en el alfabeto).\n\n'+Fore.YELLOW+' Ejemplo: '+Style.RESET_ALL+'texto: paloma, palabra clave: pan, resultado: gbyfnñ\n\nPara este ejemplo hemos utilizado el alfabeto español, y hemos hecho que la letra "a" tenga un valor de 1\n(en algunos sitios comiezan a contar desde 0 y otros desde 1, en el caso en el que vale 0 la letra "a" no realizaría ningún tipo de desplazamiento, y si es 1 sí, haría un desplazamiento de 1, como en el ejemplo dado).\n')
        print('-'+Fore.GREEN+' Eliminar caracteres: '+Style.RESET_ALL+'como su nombre indica, elimina los caracteres que hay en un texto, escribe todos los caracteres que deseas eliminar juntos (recuerda que el "espacio" es otro caracteres más).\n')
        print('-'+Fore.GREEN+' Separador de texto en grupos de "n" caracteres: '+Style.RESET_ALL+'si tenemos un texto donde no hay espacios, esto nos permite agrupar los caracteres en grupos del tamaño que queramos.\n\n'+Fore.YELLOW+' Ejemplo: '+Style.RESET_ALL+'texto: abcdefghijklmnñopqrstuvwxyz, grupos de: 5, texto resultante: abcde fghij klmnñ opqrs tuvwx yz\n')
        print('-'+Fore.GREEN+' Teclado grado 1 y 2: '+Style.RESET_ALL+'son una forma de cifrar letras mediante los caracteres que tiene el teclado de un móvil, dichos caracteres coinciden con las posiciones de las letras. En este caso el tipo de teclado usado es el Gboard.\n')
        print('-'+Fore.GREEN+' Mostrar la n letra en un intervalo de amplitud m: '+Style.RESET_ALL+'esta función para entenderla bien bastará con un ejemplo, usaremos el utilizado en la expliación de separador de carácteres.\n\n'+Fore.YELLOW+' Ejemplo: '+Style.RESET_ALL+'texto: abcdefghijklmnñopqrstuvwxyz, m(amplitud) = 5, n(un número entre 1 y m) = 1 texto resultante: afkot\n\nSi nos fijamos en el ejemplo mencionado, cuando el texto está dividido en grupos de 5, lo que hemos hecho es coger la primera letra de cada grupo de 5, si hubieramos dicho n = 2, el resultado habría sido "bglpuz".\n')
        print('-'+Fore.GREEN+' Mayúscula-minúscula: '+Style.RESET_ALL+'te da la opción de poner todo el texto introducido en maýuscula (a), en minúscula (b) o sólo las iniciales en mayúscula (c).\n')
        print(Fore.YELLOW+'El texto resultante al cifrar un mensaje quedará copiado en el portapapeles.'+Style.RESET_ALL)
        entrada() #ayuda
    elif (cifrado == 'l' or cifrado == 'L'):
        print(Fore.BLUE+'\nMorse:'+Style.RESET_ALL)
        print('a: .-\nb: -...\nc: -.-.\nch: ----\nd: -..\ne: .\nf: ..-.\ng: --.\nh: ....\ni: ..\nj: .---\nk: -.-\nl: .-..\nm: --\nn: -.\nñ: ..-..\no: ---\np: .--.\nq: --.-\nr: .-.\ns: ...\nt: -\nu: .--\nv: ...-\nw: .--\nx: -..-\ny: -.--\nz: --..\n')
        print(Fore.BLUE+'\nBinario:'+Style.RESET_ALL)
        print('a: 00001\nb: 00010\nc: 00011\nd: 00100\ne: 00101\nf: 00110\ng: 00111\nh: 01000\ni: 01001\nj: 01010\nk: 01011\nl: 01100\nm: 01101\nn: 01110\no: 01111\np: 10000\nq: 10001\nr: 10010\ns: 10011\nt: 10100\nu: 10101\nv: 10110\nw: 10111\nx: 11000\ny: 11001\nz: 11010\n')
        print(Fore.BLUE+'\nTeclado grado 1:'+Style.RESET_ALL)
        print('a: @\nb: ;'+"\nc: '"+'\nd: €\ne: 3\nf: _\ng: &\nh: -\ni: 8\nj: +\nk: (\nl: )\nm: ?\nn: !\nñ: /\no: 9\np: 0\nq: 1\nr: 4\ns: #\nt: 5\nu: 7\nv: :\nw: 2\nx: "\ny: 6\nz: *\n')
        print(Fore.BLUE+'\nTeclado grado 2:'+Style.RESET_ALL)
        print('a: £\nb: ✓\nc: ®\nd: $\ne: |\nf: ¢\ng: ^\nh: °\ni: ×\nj: =\nk: {\nl: }\nm: ]\nn: [\nñ: \\\no: ¶\np: ∆\nq: ~\nr: •\ns: ¥\nt: √\nu: ÷\nv: ™\nw: `\nx: ©\ny: π\nz: %\n')
        entrada() #lista del alfabeto de los cifrados
    elif (cifrado == 'clear' or cifrado == 'CLEAR'):
        clear()
        print(Fore.CYAN +'Morse'+Style.RESET_ALL +': m '+ Fore.CYAN +'\nBinario'+Style.RESET_ALL +': b '+Fore.CYAN+'\nCésar'+Style.RESET_ALL +': c '+ Fore.CYAN +'\nVigenère'+Style.RESET_ALL+': v '+Fore.CYAN+'\nEliminar caracteres'+Style.RESET_ALL+': e '+Fore.CYAN+'\nSeparador de texto en grupos de'+Style.RESET_ALL+Fore.YELLOW+' n '+Style.RESET_ALL+Fore.CYAN+'caracteres'+Style.RESET_ALL+': s')
        print(Fore.CYAN+'Teclado grado 1'+Style.RESET_ALL+': t1 '+Fore.CYAN+'\nTeclado grado 2'+Style.RESET_ALL+': t2 '+Fore.CYAN+'\nMostrar la'+Fore.YELLOW+' n '+Style.RESET_ALL+Fore.CYAN+'letra de de cada intervalo de amplitud'+Style.RESET_ALL+Fore.YELLOW+' m'+Style.RESET_ALL+': ml'+Fore.CYAN+'\nMayúscula-minúsucula'+Style.RESET_ALL+': p'+Fore.RED+'\nListas de cifrados'+Style.RESET_ALL+': l'+Fore.YELLOW+'\nLimpiar pantalla'+Style.RESET_ALL+': clear'+Fore.GREEN+'\nInformación'+Style.RESET_ALL+': help')
        entrada() #limpiar pantalla
    elif (cifrado != 'c' and cifrado != 'C' and cifrado != 'v' and cifrado != 'V'
    and cifrado != 'b' and cifrado != 'B' and cifrado != 'm' and cifrado != 'M'
    and cifrado != 'e' and cifrado != 'E' and cifrado != 's' and cifrado != 'S'
    and cifrado != 't1' and cifrado != 'T1' and cifrado != 't2' and cifrado != 'T2'
    and cifrado != 'ml' and cifrado != 'ML' and cifrado != 'p' and cifrado != 'P'):
        entrada()
    texto1 = input('Escribe una frase: ')
    if (cifrado == 'c' or cifrado == 'C'):
        while (alfabeto != 'a' and alfabeto != 'A' and alfabeto != 'b' and alfabeto != 'B'):
            alfabeto = str(input('Introduce "a" para usar el alfabeto español y "b" para usar el inglés: '))
        print('')
        if (alfabeto == 'a' or alfabeto == 'A'):
            cesar1(texto1)
        elif (alfabeto == 'b' or alfabeto == 'B'):
            cesar2(texto1)
    elif (cifrado == 'v' or cifrado == 'V'):
        while(alfabeto != 'a' and alfabeto != 'A' and alfabeto != 'b' and alfabeto != 'B'):
            alfabeto = input('Introduce "a" para usar el alfabeto español y "b" para usar el inglés: ')
        while(a1 != 0 and a1 != 1):
            a1 = int(input('Indica si "a" es 0 o 1: '))
        while(encriptar1 != 'e' and encriptar1 != 'E' and encriptar1 != 'd' and encriptar1 != 'D'):
            encriptar1 = str(input('Introduce "e" si quieres encriptar y "d" si quieres desencriptar: '))
        key1 = input('Introduce la palabra clave: ')
        print('')
        if (alfabeto == 'a' or alfabeto == 'A'):
            w = vigenere1(texto1, key1, a1, encriptar1)
            print(Fore.GREEN+w+Style.RESET_ALL)
            clipboard.copy(w)
        elif (alfabeto == 'b' or alfabeto == 'B'):
            w = vigenere2(texto1, key1, a1, encriptar1)
            print(Fore.GREEN+w+Style.RESET_ALL)
            clipboard.copy(w)
        desfases = []
    elif (cifrado == 'b' or cifrado == 'B'):
        while(ascii != 'a' and ascii != 'A' and ascii != 'b' and ascii != 'B'):
            ascii = input('Introduce "a" si quieres usar ASCII o "b" en caso contario: ')
        while(t != 'c' and t != 'C' and t != 'd' and t != 'D'):
            t = input('Introduce "c" para cifrar o "d" para descifrar: ')
        print('')
        if (ascii == 'a' or ascii == 'A'):
            if (t == 'c' or t == 'C'):
                w = texto_a_binario_conAscii(texto1)
                print(Fore.GREEN+w+Style.RESET_ALL)
                clipboard.copy(w)
            elif (t == 'd' or t == 'D'):
                w = binario_conAscii_a_texto(texto1)
                print(Fore.GREEN+w+Style.RESET_ALL)
                clipboard.copy(w)
        elif (ascii == 'b' or ascii == 'B'):
            if (t == 'c' or t == 'C'):
                w = texto_a_binario_sinAscii(texto1)
                print(Fore.GREEN+w+Style.RESET_ALL)
                clipboard.copy(w)
            elif (t == 'd' or t == 'D'):
                w = binario_sinAscii_a_texto(texto1)
                print(Fore.GREEN+w+Style.RESET_ALL)
                clipboard.copy(w)
    elif (cifrado == 'm' or cifrado == 'M'):
        while(t != 'tm' and t != 'TM' and t != 'mt' and t != 'MT'):
            t = input('Introduce "tm" para pasar de texto a morse o "mt" para pasar de morse a texto: ')
        print('')
        if (t == 'tm' or t == 'TM'):
            w = texto_a_morse(texto1)
            print(Fore.GREEN+w+Style.RESET_ALL)
            clipboard.copy(w)
        elif (t == 'mt' or t == 'MT'):
            w = morse_a_texto(texto1)
            print(Fore.GREEN+w+Style.RESET_ALL)
            clipboard.copy(w)
    elif (cifrado == 'e' or cifrado == 'E'):
        caracteres1 = input('Introduce los caracteres que quieres eliminar: ')
        print('')
        w = eliminador_de_caracteres(texto1, caracteres1)
        print(Fore.GREEN+w+Style.RESET_ALL)
        clipboard.copy(w)
        eliminar_caracteres = []
    elif (cifrado == 's' or cifrado == 'S'):
        n1 = int(input('Introduce como de grande quieres que sean los grupos de caracteres: '))
        print('')
        w = separador(texto1, n1)
        print(Fore.GREEN+w+Style.RESET_ALL)
        clipboard.copy(w)
    elif (cifrado == 't1' or cifrado == 'T1'):
        while(t != 'c' and t != 'C' and t != 'd' and t != 'D'):
            t = input('Introduce "c" para cifrar o "d" para descifrar: ')
        print('')
        if (t == 'c' or t == 'C'):
            w = texto_a_grado1(texto1)
            print(Fore.GREEN+w+Style.RESET_ALL)
            clipboard.copy(w)
        elif (t == 'd' or t == 'D'):
            w = grado1_a_texto(texto1)
            print(Fore.GREEN+w+Style.RESET_ALL)
            clipboard.copy(w)
    elif (cifrado == 't2' or cifrado == 'T2'):
        while(t != 'c' and t != 'C' and t != 'd' and t != 'D'):
            t = input('Introduce "c" para cifrar o "d" para descifrar: ')
            print('')
        if (t == 'c' or t == 'C'):
            w = texto_a_grado2(texto1)
            print(Fore.GREEN+w+Style.RESET_ALL)
            clipboard.copy(w)
        elif (t == 'd' or t == 'D'):
            w = grado2_a_texto(texto1)
            print(Fore.GREEN+w+Style.RESET_ALL)
            clipboard.copy(w)
    elif (cifrado == 'ml' or cifrado == 'ML'):
        n1 = int(input('n = '))
        m1 = int(input('m = '))
        w = mostrar_letras(texto1, n1, m1)
        print(Fore.GREEN+w+Style.RESET_ALL)
        clipboard.copy(w)
    elif (cifrado == 'p' or cifrado == 'P'):
        while (t != 'a' and t != 'A' and t != 'b' and t != 'B' and t != 'c' and t != 'C'):
            t = input('Introduce "a", "b" o "c" para iniciar la conversión: ')
        print('')
        w = mayuscula_minuscula(texto1, t)
        print(Fore.GREEN+w+Style.RESET_ALL)
        clipboard.copy(w)
    entrada()
entrada()
