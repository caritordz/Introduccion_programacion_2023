#Bibliotecas


#Entrada de datos
#Declaracion de variables

aciertos = 0


#Proceso 

def cuestionario ():
    preguntas = [
    
    "1. Herramienta de programación, parecido al lenguaje español utilizado para crear código:\
    a) IDE   b) Pseudocódigo   c) Compilador     d) ANSI / ISO: "

    "2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y \
    forma determinados.    a) Información     b) Datos     c) Programa     d) Código:"

    "3. Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo.\
    a) IEEE     b) IDE     c) ANSI/ISO     d) VSCode: "

    "4. Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema.\
    a) Proceso     b) Solución     c) Función     d) Algoritmo "

    " 5. Conjunto de elementos que se relacionan para cumplir una función determinada.\
    a) Estructura     b) Datos     c) Operación     d) Sistema"
    
    "6. Componente de un IDE que se encarga de traducir el código fuente a código máquina.\
     a) Depurador     b) Editor de Texto     c) Terminal de Salida     d) Compilador/Intérprete"

    "7. Elemento que se usa para almacenar una cantidad donde cambia su valor.\
     a) Constante     b) Variable     c) Librería     d) Tipo de Dato"

    "8. Conjunto de símbolos, letras, números que no tienen un significado.\
     a) Datos     b) Estructura     c) Información     d) Sistema"

    "9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento.\
     a) Filosofía     b) Sociología     c) Lógica     d) Argumentación"

    "10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto.\
     a) Evento     b) Estándar     c) Calidad     d) Productividad"

    "11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico.\
     a) Estructura     b) Sistema     c) Objeto     d) Virtual"

    "12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar.\
     a) Operaciones/Cálculos     b) Sintaxis     c) Programa de Computadora     d) Comando"
    
    
    ]

    respuestas_correctas = [ "b", "b", "c", "d", "d","d","b", "a", "c", "b","a","c" ]
        
    respuestas_usuario = []

    print("Escribe tus respuestas")

#Inicio del cuestionario 

    for i, pregunta in enumerate(preguntas):
        print(pregunta)
        respuesta = input("Ingresa el inciso correcto:  ")
        respuestas.usuario.append(respuestas_usuario)

    aciertos = 0

    for i in range(len(respuestas_correctas)):
        if respuestas_correctas [i] == respuestas_usuario [i]:
            aciertos += 1
    
    print("Tus aciertos: ", aciertos)
    print("calificacion final: ", (aciertos * 10) /12)







