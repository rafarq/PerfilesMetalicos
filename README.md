# Descripción
Este programa, es una utilidad de línea de comandos escrita en Python para buscar y visualizar datos de perfiles metálicos para la construcción. Los datos de los perfiles se leen de un archivo `perfiles.json` que debe estar en la misma ruta que el archivo `.py`.

El programa admite dos argumentos opcionales: `-perfil` y `-valor`.  

1. `-perfil`: se utiliza para especificar el nombre del perfil metálico que se desea buscar.
2. `-valor`: se utiliza para especificar un valor específico del perfil que se quiere buscar.

Si se proporcionan estos argumentos en la línea de comandos, el programa buscará el perfil y valor indicados y mostrará los resultados en pantalla.

Si no se proporcionan estos argumentos en la línea de comandos, el programa entrará en modo interactivo y preguntará al usuario qué perfil y valor quiere buscar.

El programa siempre imprimirá al principio la descripción y la información del autor. Y en caso de no proporcionar argumentos en la línea de comandos, mostrará la lista de perfiles disponibles antes de pedir las entradas al usuario.

## Como funciona

### Instalación

En primer lugar instala las dependencias con el comando

```
pip install -r requirements.txt
```

Comprueba que el fichero perfiles.py está junto al fichero perfiles.json que contiene todos los datos de los perfiles metálicos.

### Uso

El programa se invoca con el parámetro `-perfil` para indicar qué perfil se quiere ver y opcionalmente el parámetro `-valor` si solo se desea obtener un valor concreto para dicho perfil
```
python perfiles.py -perfil IPN80
python perfiles.py -perfil IPN80 -valor p
```

## Valores disponibles para cada tipo de perfil
#### Perfiles IPN
Los valores disponibles son estos:

-"Perfil": Este es el nombre o identificación del perfil.  
-"h": altura de la viga.  
-"b": anchura de la viga.  
-"e-r": espesor del alma.  
-"e1": espesor del ala en el encuentro con el alma.  
-"e2": espesor del ala en eje del agujero.  
-"r1": radio de curvatura del borde del ala.  
-"h1": altura de la parte plana del alma.  
-"u": perímetro de la sección de la viga.  
-"A": área de la sección transversal de la viga.  
-"Sx": momento elástico de media sección al eje X.  
-"Ix": momento de inercia respecto al eje X.  
-"Wx": módulo resistente de la sección respecto al eje X.  
-"ix": radio de giro respecto al eje X.  
-"Iy": momento de inercia respecto al eje Y.  
-"Wy": módulo resistente de la sección respecto al eje Y.  
-"iy": radio de giro respecto al eje Y.  
-"It": módulo de torsión de inercia.  
-"Ia": módulo de alabeo de la sección.  
-"w": gramil, ditancia entre ejes de agujeros.  
-"a": diámetro dek agujero del roblón normal.  
-"p": peso en kg por metro.   
-"cm": condiciones del mercado para el perfil (P - existencia permanente; C - Consultar).  

#### Perfiles IPE
Los valores disponibles son estos:

-"Perfil": Este es el nombre o identificación del perfil.  
-"h": altura de la viga.  
-"b": anchura de la viga.  
-"e": espesor del alma.  
-"e1": espesor del ala en el encuentro con el alma.  
-"r1": radio de curvatura del borde del ala.  
-"h1": altura de la parte plana del alma.  
-"u": perímetro de la sección de la viga.  
-"A": área de la sección transversal de la viga.  
-"Sx": momento elástico de media sección al eje X.  
-"Ix": momento de inercia respecto al eje X.  
-"Wx": módulo resistente de la sección respecto al eje X.  
-"ix": radio de giro respecto al eje X.  
-"Iy": momento de inercia respecto al eje Y.  
-"Wy": módulo resistente de la sección respecto al eje Y.  
-"iy": radio de giro respecto al eje Y.  
-"It": módulo de torsión de inercia.  
-"Ia": módulo de alabeo de la sección.  
-"w": gramil, ditancia entre ejes de agujeros.  
-"a": diámetro dek agujero del roblón normal.  
-"e2":   
-"p": peso en kg por metro.  
-"cm": condiciones del mercado para el perfil (P - existencia permanente; C - Consultar).  


#### Perfiles HEA-HEB-HEM
Los valores disponibles son estos:


-"Perfil": Este es el nombre o identificación del perfil.  
-"h": altura de la viga.  
-"b": anchura de la viga.  
-"e": espesor del alma.  
-"e1": espesor del ala en el encuentro con el alma.  
-"r1": radio de curvatura del borde del ala.  
-"h1": altura de la parte plana del alma.  
-"u": perímetro de la sección de la viga.  
-"A": área de la sección transversal de la viga.  
-"Sx": momento elástico de media sección al eje X.  
-"Ix": momento de inercia respecto al eje X.  
-"Wx": módulo resistente de la sección respecto al eje X.  
-"ix": radio de giro respecto al eje X.  
-"Iy": momento de inercia respecto al eje Y.  
-"Wy": módulo resistente de la sección respecto al eje Y.  
-"iy": radio de giro respecto al eje Y.  
-"It": módulo de torsión de inercia.  
-"Ia": módulo de alabeo de la sección.  
-"w": gramil, ditancia entre ejes de agujeros.  
-"w1": distancia entre el eje del agujero a la mitad restante del ala
-"a": diámetro dek agujero del roblón normal.  
-"p": peso en kg por metro.  
-"cm": condiciones del mercado para el perfil (P - existencia permanente; C - Consultar).  

