class Handler:
    def __init__(self, output_widget):
        self.__output_widget = output_widget  # widget instance
        self.__command_found = False
        self.__imp_func_getter = None

    def is_function_implemented(self, name, second_part):
        implemented_functions = ["exit", "clear", "whois", "help"]
        self.__imp_func_getter = implemented_functions
        for n in implemented_functions:
            if n == name:
                self.__command_found = True
                return getattr(self, n)(second_part)  # dynamic method call by its name from array

        if self.__command_found is False:
            self.__output_widget.append(
                '<font color="red">Unknown command, implemented commands: "exit", "clear", "whois, and "help"</font>')

    # todo: implement function that check if the def from array is really implemented
    # todo: also implement security check features :)

    # TODO: implement journal kind of command
    # TODO: make whois use database query instead of getting info from nested dict.

    def help(self, _):
        self.__output_widget.append("Available commands are: %s" % self.__imp_func_getter)

    @staticmethod
    def exit(_):
        exit(1)

    def whois(self, command_flag):
        # nested dictionary, kind of dynamic? maybe I will redo this whole function
        # for now only for testing, real function should have query asking on database, which I do not have yet
        flags = {
            "n": {  # → flag key
                "dict": {  # → start of flag_info
                    "ryu": "The best husband ever",
                    "bety": "Best wife.",
                    "anakin": "The youngling killer!"
                },
                "error_msg": "Please try to use \"whois -n <name>\", or use \"whois --help\"."
            },  # → end of flag info
            "i": {  # → flag key
                "dict": {
                    "ryu": "Male, MORAVÁK",
                    "bety": "Female, ČEŠKO",
                    "anakin": "He ded"
                },
                "error_msg": "Please try to use \"whois -i <name>\", or use \"whois --help\"."
            }
        }

        # help dictionary
        help_dict = {
            "n": "  -n    Retrieve information about a specified name.",
            "i": "  -i    Retrieve information about a specified person.",
            "--help": "  --help    Show this help message."
        }

        if not command_flag:
            self.__output_widget.append("You are NEO! Currently, you are trapped in THE MATRIX...")
            return

        # check if flag starts with -, then remove it and forward it to the next iteration
        raw_flag = command_flag[0][1:] if command_flag[0].startswith('-') else None

        # iteration with flags :)
        # flag_key is the key, aka n, i...
        # flag_info is the nested dict, to which the flag_key point.
        # aka flag_key = n, flag_info = { "dict": { "ryu": "The best husband ever", "bety": ....
        for flag_key, flag_info in flags.items():
            if raw_flag == flag_key:  # ← find out, if flag is in dictionary as a key aka -n → n
                target_dict = flag_info["dict"]
                #  ↑ get correct dict inside of flags, if for loops stops on n, it looks for dict on "n" key
                if len(command_flag) == 2:
                    name = command_flag[1]
                    if name in target_dict:
                        self.__output_widget.append(target_dict[name])
                    else:
                        self.__output_widget.append("Name not found.")
                else:
                    self.__output_widget.append(flag_info["error_msg"])
                return  # no flag found → return

        # whois --help if case ↓:
        if command_flag[0] == "--help" and len(command_flag) == 1:
            self.__output_widget.append("Usage: whois -n <name> or whois -i <name> or whois --help")
            self.__output_widget.append("Flags:")
            for help_text in help_dict.values():
                self.__output_widget.append(help_text)
        else:
            self.__output_widget.append(
                "whoami does not have \"%s\" flag option, use \"--help\" flag for more information." % command_flag[0]
            )

    def clear(self, _):
        self.__output_widget.clear()
        self.__output_widget.append("Output cleared, you may continue in your silly activities.")
