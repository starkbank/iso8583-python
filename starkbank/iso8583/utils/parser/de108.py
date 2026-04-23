from .tlvParser import TlvParser, TlvElementConfig


class ParseDe108(TlvParser):

    def __init__(self, encoding=None):
        super().__init__(encoding=encoding, dataElement=TlvElementConfig.DE108)
