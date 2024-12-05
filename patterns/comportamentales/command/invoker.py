from .command import Command


class Invoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        result = command.execute()
        self.history.append(command)
        return result

    def undo_last_command(self):
        if self.history:
            command = self.history.pop()
            return command.undo()
        return "No hay comandos para deshacer."