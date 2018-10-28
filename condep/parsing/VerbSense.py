from enum import Enum
from typing import List

class VerbSense:

    verb_sense_id = None

    def __init__(self, verb_name:str, arguments:list):
        self.verb_name = verb_name
        self.arguments = arguments

        assert(isinstance(arguments,list))

    def get_verb_subject(self):
        return [arg for arg in self.arguments if arg.type == 'PAG'][0]

    def get_verb_object(self):
        return [arg for arg in self.arguments if arg.type == 'PPT'][0]

    def get_argument_by_type(self, argument_type:str):
        return [arg for arg in self.arguments if arg.type == argument_type][0]

    def set_argument_by_type(self, argument_type:str, argument_name:str):
        existing = [arg for arg in self.arguments if arg.type == argument_type]
        if existing:
            existing[0].argument = argument_name
        else:
            self.arguments.append(VerbArgumentInstance(None, argument_type, argument_name))


class VerbArgument:
    def __init__(self, description, type):
        self.description = description
        self.type = type

class VerbArgumentInstance(VerbArgument):
    def __init__(self, description:str, type:str, argument:str):
        self.description = description
        self.type = type
        self.argument = argument