from starkbank.iso8583.version import IsoVersion
from starkbank.iso8583.utils.enum import LengthType, Encoding
from starkbank.iso8583.utils.parser import parseString, parseBitString, parseDE048, parseDE112, parseBin
from starkbank.iso8583.utils.parser import unparseString, unparseBitString, unparseDE048, unparseDE112, unparseBin

mastercard = {
    IsoVersion._1987: {
        "MTI": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE000": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE001": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE002": {
            "lengthType": LengthType.llvar,
            "limit": 19,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE003": {
            "lengthType": LengthType.fixed,
            "limit": 6,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE004": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE005": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE006": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE007": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE008": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE009": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE010": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE011": {
            "lengthType": LengthType.fixed,
            "limit": 6,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE012": {
            "lengthType": LengthType.fixed,
            "limit": 6,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE013": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE014": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE015": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE016": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE017": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE018": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE019": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE020": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE021": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE022": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE023": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE024": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE025": {
            "lengthType": LengthType.fixed,
            "limit": 2,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE026": {
            "lengthType": LengthType.fixed,
            "limit": 2,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE027": {
            "lengthType": LengthType.fixed,
            "limit": 1,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE028": {
            "lengthType": LengthType.fixed,
            "limit": 9,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE029": {
            "lengthType": LengthType.fixed,
            "limit": 9,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE030": {
            "lengthType": LengthType.fixed,
            "limit": 9,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE031": {
            "lengthType": LengthType.fixed,
            "limit": 9,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE032": {
            "lengthType": LengthType.llvar,
            "limit": 11,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE033": {
            "lengthType": LengthType.llvar,
            "limit": 11,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE034": {
            "lengthType": LengthType.llvar,
            "limit": 28,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE035": {
            "lengthType": LengthType.llvar,
            "limit": 37,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE036": {
            "lengthType": LengthType.lllvar,
            "limit": 104,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE037": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE038": {
            "lengthType": LengthType.fixed,
            "limit": 6,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE039": {
            "lengthType": LengthType.fixed,
            "limit": 2,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE040": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE041": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE042": {
            "lengthType": LengthType.fixed,
            "limit": 15,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE043": {
            "lengthType": LengthType.fixed,
            "limit": 40,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE044": {
            "lengthType": LengthType.llvar,
            "limit": 25,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE045": {
            "lengthType": LengthType.llvar,
            "limit": 76,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE046": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE047": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE048": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseDE048,
            "unparser": unparseDE048,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE049": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE050": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE051": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE052": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE053": {
            "lengthType": LengthType.fixed,
            "limit": 16,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE054": {
            "lengthType": LengthType.lllvar,
            "limit": 120,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE055": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseBin,
            "unparser": unparseBin,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE056": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE057": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE058": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE059": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE060": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE061": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE062": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE063": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE064": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE065": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE066": {
            "lengthType": LengthType.fixed,
            "limit": 1,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE067": {
            "lengthType": LengthType.fixed,
            "limit": 2,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE068": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE069": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE070": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE071": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE072": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE073": {
            "lengthType": LengthType.fixed,
            "limit": 6,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE074": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE075": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE076": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE077": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE078": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE079": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE080": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE081": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE082": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE083": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE084": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE085": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE086": {
            "lengthType": LengthType.fixed,
            "limit": 16,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE087": {
            "lengthType": LengthType.fixed,
            "limit": 16,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE088": {
            "lengthType": LengthType.fixed,
            "limit": 16,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE089": {
            "lengthType": LengthType.fixed,
            "limit": 16,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE090": {
            "lengthType": LengthType.fixed,
            "limit": 42,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE091": {
            "lengthType": LengthType.fixed,
            "limit": 1,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE092": {
            "lengthType": LengthType.fixed,
            "limit": 2,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE093": {
            "lengthType": LengthType.fixed,
            "limit": 5,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE094": {
            "lengthType": LengthType.fixed,
            "limit": 7,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE095": {
            "lengthType": LengthType.fixed,
            "limit": 42,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE096": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE097": {
            "lengthType": LengthType.fixed,
            "limit": 17,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE098": {
            "lengthType": LengthType.fixed,
            "limit": 25,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE099": {
            "lengthType": LengthType.llvar,
            "limit": 11,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE100": {
            "lengthType": LengthType.llvar,
            "limit": 11,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE101": {
            "lengthType": LengthType.llvar,
            "limit": 17,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE102": {
            "lengthType": LengthType.llvar,
            "limit": 28,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE103": {
            "lengthType": LengthType.llvar,
            "limit": 28,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE104": {
            "lengthType": LengthType.lllvar,
            "limit": 100,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE105": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE106": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE107": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE108": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE109": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE110": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE111": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE112": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseDE112,
            "unparser": unparseDE112,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE113": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE114": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE115": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE116": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE117": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE118": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE119": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE120": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE121": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE122": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE123": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE124": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE125": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE126": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE127": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE128": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
    },
    IsoVersion._1993: {
        "MTI": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE000": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE001": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE002": {
            "lengthType": LengthType.llvar,
            "limit": 19,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE003": {
            "lengthType": LengthType.fixed,
            "limit": 6,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE004": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE005": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE006": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE007": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE008": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE009": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE010": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE011": {
            "lengthType": LengthType.fixed,
            "limit": 6,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE012": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE013": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE014": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE015": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE016": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE017": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE018": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE019": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE020": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE021": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE022": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE023": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE024": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE025": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE026": {
            "lengthType": LengthType.fixed,
            "limit": 4,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE027": {
            "lengthType": LengthType.fixed,
            "limit": 1,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE028": {
            "lengthType": LengthType.fixed,
            "limit": 9,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE029": {
            "lengthType": LengthType.fixed,
            "limit": 9,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE030": {
            "lengthType": LengthType.fixed,
            "limit": 24,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE031": {
            "lengthType": LengthType.llvar,
            "limit": 23,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE032": {
            "lengthType": LengthType.llvar,
            "limit": 11,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE033": {
            "lengthType": LengthType.llvar,
            "limit": 11,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE034": {
            "lengthType": LengthType.llvar,
            "limit": 28,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE035": {
            "lengthType": LengthType.llvar,
            "limit": 37,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE036": {
            "lengthType": LengthType.lllvar,
            "limit": 104,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE037": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE038": {
            "lengthType": LengthType.fixed,
            "limit": 6,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE039": {
            "lengthType": LengthType.fixed,
            "limit": 2,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE040": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE041": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE042": {
            "lengthType": LengthType.fixed,
            "limit": 15,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE043": {
            "lengthType": LengthType.llvar,
            "limit": 99,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE044": {
            "lengthType": LengthType.llvar,
            "limit": 25,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE045": {
            "lengthType": LengthType.llvar,
            "limit": 76,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE046": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE047": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE048": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE049": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE050": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE051": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE052": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE053": {
            "lengthType": LengthType.fixed,
            "limit": 16,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE054": {
            "lengthType": LengthType.lllvar,
            "limit": 240,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE055": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseBin,
            "unparser": unparseBin,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE056": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE057": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE058": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE059": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE060": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE061": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE062": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE063": {
            "lengthType": LengthType.lllvar,
            "limit": 16,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE064": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE065": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE066": {
            "lengthType": LengthType.fixed,
            "limit": 1,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE067": {
            "lengthType": LengthType.fixed,
            "limit": 2,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE068": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE069": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE070": {
            "lengthType": LengthType.fixed,
            "limit": 3,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE071": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE072": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE073": {
            "lengthType": LengthType.fixed,
            "limit": 6,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE074": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE075": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE076": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE077": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE078": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE079": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE080": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE081": {
            "lengthType": LengthType.fixed,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE082": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE083": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE084": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE085": {
            "lengthType": LengthType.fixed,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE086": {
            "lengthType": LengthType.fixed,
            "limit": 16,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE087": {
            "lengthType": LengthType.fixed,
            "limit": 16,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE088": {
            "lengthType": LengthType.fixed,
            "limit": 16,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE089": {
            "lengthType": LengthType.fixed,
            "limit": 16,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE090": {
            "lengthType": LengthType.fixed,
            "limit": 42,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE091": {
            "lengthType": LengthType.fixed,
            "limit": 1,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE092": {
            "lengthType": LengthType.fixed,
            "limit": 2,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE093": {
            "lengthType": LengthType.llvar,
            "limit": 11,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE094": {
            "lengthType": LengthType.llvar,
            "limit": 11,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE095": {
            "lengthType": LengthType.llvar,
            "limit": 10,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE096": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE097": {
            "lengthType": LengthType.fixed,
            "limit": 17,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE098": {
            "lengthType": LengthType.fixed,
            "limit": 25,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE099": {
            "lengthType": LengthType.llvar,
            "limit": 11,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE100": {
            "lengthType": LengthType.llvar,
            "limit": 11,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE101": {
            "lengthType": LengthType.llvar,
            "limit": 17,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE102": {
            "lengthType": LengthType.llvar,
            "limit": 28,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE103": {
            "lengthType": LengthType.llvar,
            "limit": 28,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE104": {
            "lengthType": LengthType.lllvar,
            "limit": 100,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE105": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE106": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE107": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE108": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE109": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE110": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE111": {
            "lengthType": LengthType.lllvar,
            "limit": 12,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE112": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE113": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE114": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE115": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE116": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE117": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE118": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE119": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE120": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE121": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE122": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE123": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE124": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE125": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE126": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE127": {
            "lengthType": LengthType.lllvar,
            "limit": 999,
            "parser": parseString,
            "unparser": unparseString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
        "DE128": {
            "lengthType": LengthType.fixed,
            "limit": 8,
            "parser": parseBitString,
            "unparser": unparseBitString,
            "lengthEncoding": Encoding.cp500,
            "dataEncoding": Encoding.cp500
        },
    },
}
