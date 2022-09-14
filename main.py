#Importamos la libreria random para que genere un numero del 0 a 10.
import random 
#Importamos la libreria tiempio para temporizar la trivia
import time
#Iniciamos la trivia en true
iniciar_trivia=True
intentos=0
#numero_carga=0
#Creamos constantes de colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
#Amarillo en negrita con el 1
YELLOW = '\033[1;33m'
BLUE = '\033[34m'
#Morado en negrita con el 1
MAGENTA = '\033[1;35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0;m'
puntaje=0
#puntaje=random.randint(0,10)
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
#print(GREEN+"Este texto será verde"+RESET)
#print("\033[1;33m"+"fred"+'\033[0;m') 
print(RED+ "          Bienvenido a mi Trivia Futbolera \n" + RESET)
time.sleep(1)
print(GREEN+ "Pondremos a prueba tus conocimientos futboleros " + RESET)

print ("Empezaste con: ", puntaje, " puntos")
#print ("Tienes " , puntaje, "puntos \n")abs
nombre=input("Ingresa tu nombre: " )
#edad=input("Ingresa tu edad: " )

# Es importante dar instrucciones sobre cómo jugar:
print ("\nMuy bien " ,(MAGENTA+ nombre + RESET)  , " responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

# OJO, el \n al final de la línea 2 es para dar un "salto de línea"
while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0

  print(YELLOW+"\nIntento número:" + RESET, YELLOW+str(intentos)+RESET  )
  #input("Presiona Enter para continuar ")
  
  for numero_carga in range (5,0,-1):
   print ("Por favor espera " ,CYAN+str(numero_carga), "segundos"+RESET)
   time.sleep(1)

  print (GREEN+"\n1)¿Qué pais fué el campeón del mundial Sudáfrica 2010? \n "+RESET)
  print ("a) Brasil")
  print ("b) Holanda")
  print ("c) España")
  print ("d) Uruguay")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  
  respuesta_1 = input("\n Tu respuesta: ").lower()
  
  while respuesta_1 not in ("a", "b", "c", "d","x"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "a":
    print(RED+ "Incorrecto!", nombre, "Brasil no fue el campeón " + RESET)
    puntaje-=2
   # print("Tienes " , puntaje , "puntos")
  elif respuesta_1 == "d":
    print(RED+ "Incorrecto!", nombre, "Uruguay no fue el campeón " + RESET)
    puntaje-=2
   # print("Tienes " , puntaje, "puntos")
  elif respuesta_1 == "b":
    print(RED+ "Incorrecto!", nombre, "Holanda no fue el campeón " + RESET)
    puntaje-=2
  #  print("Tienes " , puntaje, "puntos")
  elif respuesta_1 == "x":
    bonus_1=50
    puntaje=puntaje + bonus_1
    
    print(BLUE+"Esto es un bonus secreto , has ganado: " ,str (bonus_1), " puntos." + RESET )
    #print (nombre, "tienes", puntaje, "puntos")
  
  else:
    puntaje+=10
    print(CYAN+ "Muy bien ", nombre, "! España fue el campeón del mundial Sudafrica 2010 " + RESET)
    #print("Muy bien", nombre, "!")
    
  print(nombre , "llevas " , puntaje, "puntos")
  
  #time.sleep(2)
 # para ayudarnos a imaginar que vamos jugando
  print("Espera...")
  time.sleep(1)
  #puntaje = puntaje +20  # Imaginaremos que ganó 20 puntos en el desarrollo de la trivia


  # Pregunta 2
  print (GREEN+"\n2)¿Quién es el futbolista con más balones de oro ganados? \n"+RESET)
  print ("a) Ronaldinho")
  print ("b) Messi")
  print ("c) Cristiano Ronaldo")
  print ("d) Neymar")
  
  respuesta_2 = input("\n Tu respuesta: ").lower()
  
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  
  if respuesta_2 == "a":
    print(RED+ "Incorrecto! Ronaldinho no es la respuesta correcta " + RESET)
    puntaje-=2
   # print("Tienes " , puntaje , "puntos")
  elif respuesta_2 == "c":
    print(RED+ "Incorrecto! Cristiano Ronaldo no es la respuesta correcta " + RESET)
    puntaje-=2
   # print("Tienes " , puntaje, "puntos")
  elif respuesta_2 == "d":
    print(RED+ "Incorrecto! Neymar no es la respuesta correcta " + RESET)
    puntaje-=2
  #  print("Tienes " , puntaje, "puntos")
  
  else:
    puntaje+=10
    print(CYAN+ "Muy bien! Messi es el futbolista con más balones de oro ganados " + RESET)
    #print("Muy bien", nombre, "!")
    
  print(nombre , "llevas " , puntaje, "puntos")
  #time.sleep(2)
  print("Espera...")
  time.sleep(1)
  
  # Pregunta 3
  print (GREEN+"\n3)¿Qué futbolista fue el ganador de la bota de oro del mundial Rusia 2018? \n"+RESET)
  print ("a) Lukaku")
  print ("b) Kane")
  print ("c) MBappé")
  print ("d) Cristiano Ronaldo")
  
  respuesta_3 = input("\n Tu respuesta: ").lower()
  
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "a":
    print(RED+"Incorrecto!", nombre, "Lukaku no fue el ganador"+RESET)
    puntaje-=2
   # print("Tienes " + str(puntaje), "puntos")
  elif respuesta_3 == "c":
    print(RED+"Incorrecto!", nombre, "Mbappe no fue el ganador"+RESET)
    puntaje-=2
    #print("Tienes " + str(puntaje), "puntos")
  elif respuesta_3 == "d":
    print(RED+"Incorrecto!", nombre, "Cristiano Ronaldo no fue el ganador"+RESET)
    puntaje-=2
  else:
     puntaje+=10
     print(CYAN+"Correcto! Harry Kane fue el goleador"+RESET)

  print(nombre , "llevas " , puntaje, "puntos")
  #time.sleep(2)
  print("Espera...")
  time.sleep(1)

  
  # input("\nPresiona una tecla para continuar")
  # Pregunta 3
  
  print (GREEN+"\n4) ¿Quién es el máximo goleador en la historia de los mundiales?\n"+RESET)
  print ("a) Ronaldo")
  print ("b) Gerd Muller")
  print ("c) Pele")
  print ("d) Miroslav Klose")
  # Almacenamos la respuesta del usuario en la variable "respuesta_4"
  respuesta_4 = input("\nTu respuesta: ").lower()
  
  while respuesta_4 not in ("a", "b", "c", "d","p"):
    respuesta_4 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_4 == "c":
    print (RED+"Totalmente incorrecto! ..."+RESET)
    puntaje-=2
  elif respuesta_4 == "a":
    print (RED+"..."+RESET)
    puntaje-= 2
  elif respuesta_4 == "b":
    print (RED+"Incorrecto! ..."+RESET)
    puntaje-= 2
  elif respuesta_4 == "p":
    
    bonus_2=20
    puntaje=puntaje+bonus_2
    print(BLUE+"Esto es un bonus secreto , has ganado: " ,str (bonus_2), " puntos." + RESET )
    #print (nombre, "tienes", puntaje, "puntos")
  else:
    print (CYAN+"Correcto! ..."+RESET)
    puntaje+=10 
    
  for numero_carga in range (5,0,-1):
   variable=random.randint(0,10)
  sumar=variable+puntaje
  
  print("Tienes " , puntaje , " puntos ... \nAhora deja que la suerte haga su trabajo ")
  time.sleep(2)
 # print("Ganaste ", sumar)
  print("\nGracias a la suerte ganaste: " ,CYAN+ str(variable) + RESET," puntos")
 # print("Excelente, has obtenido", sumar, "puntos ")
  print(RED+"\nGracias por jugar mi trivia, alcanzaste los " , sumar, "puntos"+RESET)

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero" ,(MAGENTA+ nombre + RESET) , " que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False 
  #exit()
    # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.

"""
for numero_carga in range (5,0,-1):
 print ("Por favor espera " ,numero_carga, "segundos")
 time.sleep(1)
 """
 # input("Presiona Enter para continuar")
# Pregunta 1



