## Como funciona

### Instalación

En primer lugar instala las dependencias con el comando

```
pip install -r requirements.txt
```

Comprueba que el fichero perfiles.py está junto al fichero perfiles.json que contiene todos los datos de los perfiles metálicos.

### Funcionamiento

El programa se invoca con el parámetro -perfil para indicar qué perfil se quiere ver y opcionalmente el parámetro -valor si solo se desea obtener un valor concreto para dicho perfil
```
python perfiles.py -perfil IPN80
python perfiles.py -perfil IPN80 -valor p
```

Los valores disponibles son estos:

"Perfil": Este es el nombre o identificación del perfil.
"h": altura de la viga.
"b": anchura de la viga.
"e-r": espesor del alma
"e1": espesor del ala en el encuentro con el alma
"e2": espesor del ala en eje del agujero.
"r1": radio de curvatura del borde del ala.
"h1": altura de la parte plana del alma.
"u": perímetro de la sección de la viga.
"A": área de la sección transversal de la viga.
"Sx": momento elástico de media sección al eje X.
"Ix": momento de inercia respecto al eje X.
"Wx": módulo resistente de la sección respecto al eje X.
"ix": radio de giro respecto al eje X.
"Iy": momento de inercia respecto al eje Y.
"Wy": módulo resistente de la sección respecto al eje Y.
"iy": radio de giro respecto al eje Y.
"It": módulo de torsión de inercia.
"Ia": módulo de alabeo de la sección.
"w": gramil, ditancia entre ejes de agujeros.
"a": diámetro dek agujero del roblón normal.
"p": pero por metro.
"cm": condiciones del mercado para el perfil (P - existencia permanente; C - Consultar).
