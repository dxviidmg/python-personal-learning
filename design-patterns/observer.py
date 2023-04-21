# Clase observable
class ChatRoom:
    def __init__(self):
        self.observadores = set()
        self.mensajes = []

    def agregar_observador(self, observador):
        self.observadores.add(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, mensaje):
#        print('notificar_observadores', mensaje)
        self.mensajes.append(mensaje)
        for observador in self.observadores:
            observador.actualizar(self.mensajes)

    def enviar_mensaje(self, mensaje):
        self.notificar_observadores(mensaje)


# Clase observador
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes_recibidos = []

    def actualizar(self, mensajes):
        nuevos_mensajes = [mensaje for mensaje in mensajes if mensaje not in self.mensajes_recibidos]
        print(nuevos_mensajes)
        self.mensajes_recibidos.extend(nuevos_mensajes)
        print(f"Usuario {self.nombre}: {nuevos_mensajes}")


# Uso del patrón Observer
if __name__ == "__main__":
    chat_room = ChatRoom()

    usuario1 = Usuario("Juan")
    usuario2 = Usuario("María")

    chat_room.agregar_observador(usuario1)
    chat_room.agregar_observador(usuario2)

    chat_room.enviar_mensaje("Hola, ¿cómo están?")
    chat_room.enviar_mensaje("Bien, gracias. ¿Y tú?")
#    chat_room.enviar_mensaje("También bien, gracias por preguntar.")
