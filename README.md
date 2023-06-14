# Trabajo práctico - Sistemas Contínuos - Ejercicio 4: Modelo de Lotka-Volterra

## Autores
- Giungi Agustin
- Rojo Jonathan

## Archivos
En el presente repositorio se encuentran 2 archivos:

- LoktaVolterra.py: contiene todo el funcionamiento del modelo
- Reporte.pdf: contiene el reporte del trabajo realizado

## Uso
   Para obtener una vista de ayuda de como utilizar los parametros opcionales se puede utilizar
   python3 LotkaVolterra.py -h

   Parámetros opcionales:
   "-i", "--interval", help = "Interval max. Default = 50. The sistem will also stop when the amount of preys or depredators reach less than 0.005"
   "-s", "--step", help = "Size of the step. Default = 0.01"
   "-d", "--depredator", type = int, help = "Starting amount of depredators. Default = 2"
   "-p", "--prey", type = int, help = "Starting amount of preys. Default = 2"
   "-r", help = "Growth rate of prey in the absence of predators. Default = 3"
   "-a", help = "Predation coefficient. Default = 2"
   "-b", help = "Growth rate of the number of predators. Default = 1"
   "-m", help = "Predator mortality rate. Default = 2"