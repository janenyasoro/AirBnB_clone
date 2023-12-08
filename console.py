#!/usr/bin/python3
"""This defines the HBnB console."""
import cmd
import re
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Defines the HBNBcommmand interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb)"
    __classes = {
            "BaseModel"
   }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self,arg):
        """Quit command to exit the program."""
        return True

    def do_E0F(self, arg):
        """End of File signal to exit the program."""
        print("")
        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()

