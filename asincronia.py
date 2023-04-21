import asyncio
import random

async def correr_caballo(numero_caballo):
    velocidad = random.randint(1, 5)  # Velocidad aleatoria entre 1 y 5
    print(f"Caballo {numero_caballo} con velocidad {velocidad} iniciando la carrera")
    for paso in range(1, 11):
        await asyncio.sleep(1)  # Esperar un segundo entre cada paso
        print(f"Caballo {numero_caballo} ha dado el paso {paso}")
    print(f"Caballo {numero_caballo} ha llegado a la meta")
    return numero_caballo

async def main():
    tareas = []
    for i in range(1, 6):
        tarea = asyncio.create_task(correr_caballo(i))
        tareas.append(tarea)
    resultados = await asyncio.gather(*tareas)
    print(f"El ganador es el caballo {resultados[0]}")

asyncio.run(main())