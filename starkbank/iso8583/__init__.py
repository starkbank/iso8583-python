encoding = "ascii"


def getEncoding():
    return encoding


from .template.visa import visa
from .template.mastercard import mastercard


template = mastercard


def getTemplate():
    return template


from .message import parse, unparse
