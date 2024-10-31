class Handler:
    def __init__(self, output_widget):
        self.__output_widget = output_widget  # widget instance
        self.__command_found = False

    def is_function_implemented(self, name):
        implemented_functions = ["stinky", "exit", "clear", "whoami", "hello"]
        for n in implemented_functions:
            if n == name:
                self.__command_found = True
                return getattr(self, n)()  # dynamicly call the methods by its name from array

        if self.__command_found is False:
            self.__output_widget.append(
                '<font color="red">Unknown command, implemented commands: "stinky", "clear" and "exit"</font>')

    #todo: implement function that check if the def from array is really implemented
    #todo: also implement security check features :)

    def stinky(self):
        self.__output_widget.append("NUUH, I think BETY is the stinkiest!")

    @staticmethod
    def exit():
        exit(1)

    def whoami(self):
        self.__output_widget.append("You are NEO, currently, you are trapped in THE MATRIX...")

    def hello(self):
        ascii_art = """\
    ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░         ░▒▓██████▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓████████▓▒░ ░▒▓██████▓▒░   ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓████████▓▒░ ░▒▓████████▓▒░  ░▒▓██████▓▒░
    """
        self.__output_widget.append(f"<pre style='font-family:Courier; white-space: pre-wrap;'>{ascii_art}</pre>")

    def clear(self):
        self.__output_widget.clear()
        self.__output_widget.append("Output cleared, you may continue in your silly activities.")
