from .tlvParser import TlvParser, TlvElementConfig


class ParseDe112(TlvParser):

    def __init__(self, encoding=None):
        super().__init__(encoding=encoding, dataElement=TlvElementConfig.DE112)
