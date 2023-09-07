from .base import Template
from ..version import IsoVersion
from ..utils.field import Field
from ..utils.enum import Encoding
from ..utils.header import VisaHeaderRule
from ..utils.length import FixedLengthRule, VariableLengthRule
from ..utils.parser import ParseBcdString, ParseBitmap, ParseString, ParseBin, ParseBitmapFormat, ParseBitString, \
    ParseUndefined, ParseHexadecimal, ParseDataset


visa = {
    IsoVersion._1987: Template(headerRule=VisaHeaderRule(), fields=[
        Field(
            name="MTI",
            lengthRule=FixedLengthRule(limit=4),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE000",
            lengthRule=FixedLengthRule(limit=8),
            parsingRule=ParseBitmap(offset=0),
        ),
        Field(
            name="DE001",
            lengthRule=FixedLengthRule(limit=8),
            parsingRule=ParseBitmap(offset=64),
        ),
        Field(
            name="DE002",
            lengthRule=VariableLengthRule(limit=19, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE003",
            lengthRule=FixedLengthRule(limit=6),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE004",
            lengthRule=FixedLengthRule(limit=12),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE005",
            lengthRule=FixedLengthRule(limit=12),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE006",
            lengthRule=FixedLengthRule(limit=12),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE007",
            lengthRule=FixedLengthRule(limit=10),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE008",
            lengthRule=FixedLengthRule(limit=8),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE009",
            lengthRule=FixedLengthRule(limit=8),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE010",
            lengthRule=FixedLengthRule(limit=8),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE011",
            lengthRule=FixedLengthRule(limit=6),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE012",
            lengthRule=FixedLengthRule(limit=6),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE013",
            lengthRule=FixedLengthRule(limit=4),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE014",
            lengthRule=FixedLengthRule(limit=4),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE015",
            lengthRule=FixedLengthRule(limit=4),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE016",
            lengthRule=FixedLengthRule(limit=4),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE017",
            lengthRule=FixedLengthRule(limit=4),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE018",
            lengthRule=FixedLengthRule(limit=4),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE019",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE020",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE021",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE022",
            lengthRule=FixedLengthRule(limit=4),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE023",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE024",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE025",
            lengthRule=FixedLengthRule(limit=2),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE026",
            lengthRule=FixedLengthRule(limit=2),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE027",
            lengthRule=FixedLengthRule(limit=1),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE028",
            lengthRule=FixedLengthRule(limit=9),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE029",
            lengthRule=FixedLengthRule(limit=9),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE030",
            lengthRule=FixedLengthRule(limit=9),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE031",
            lengthRule=FixedLengthRule(limit=9),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE032",
            lengthRule=VariableLengthRule(limit=11, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE033",
            lengthRule=VariableLengthRule(limit=11, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE034",
            lengthRule=VariableLengthRule(limit=1535, byteLength=2, encoding=Encoding.binary),
            parsingRule=ParseDataset(),
        ),
        Field(
            name="DE035",
            lengthRule=VariableLengthRule(limit=37, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE036",
            lengthRule=VariableLengthRule(limit=104, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE037",
            lengthRule=FixedLengthRule(limit=12),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE038",
            lengthRule=FixedLengthRule(limit=6),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE039",
            lengthRule=FixedLengthRule(limit=2),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE040",
            lengthRule=FixedLengthRule(limit=0),
            parsingRule=ParseUndefined(),
        ),
        Field(
            name="DE041",
            lengthRule=FixedLengthRule(limit=8),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE042",
            lengthRule=FixedLengthRule(limit=15),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE043",
            lengthRule=FixedLengthRule(limit=40),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE044",
            lengthRule=VariableLengthRule(limit=25, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE045",
            lengthRule=VariableLengthRule(limit=76, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE046",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE047",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE048",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE049",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE050",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE051",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE052",
            lengthRule=FixedLengthRule(limit=8),
            parsingRule=ParseBin(),
        ),
        Field(
            name="DE053",
            lengthRule=FixedLengthRule(limit=16),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE054",
            lengthRule=VariableLengthRule(limit=120, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE055",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBin(),
        ),
        Field(
            name="DE056",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE057",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE058",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE059",
            lengthRule=VariableLengthRule(limit=14, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE060",
            lengthRule=VariableLengthRule(limit=12, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseHexadecimal(),
        ),
        Field(
            name="DE061",
            lengthRule=VariableLengthRule(limit=18, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseHexadecimal(),
        ),
        Field(
            name="DE062",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBitmapFormat(subFields=[
                Field(name="SE00", lengthRule=FixedLengthRule(limit=8), parsingRule=ParseBitmap(offset=0)),
                Field(name="SE01", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE02", lengthRule=FixedLengthRule(limit=15), parsingRule=ParseBcdString()),
                Field(name="SE03", lengthRule=FixedLengthRule(limit=4), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE04", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE05", lengthRule=FixedLengthRule(limit=2), parsingRule=ParseBcdString()),
                Field(name="SE06", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE07", lengthRule=FixedLengthRule(limit=26), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE08", lengthRule=FixedLengthRule(limit=6), parsingRule=ParseBcdString()),
                Field(name="SE09", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE10", lengthRule=FixedLengthRule(limit=6), parsingRule=ParseBcdString()),
                Field(name="SE11", lengthRule=FixedLengthRule(limit=2), parsingRule=ParseBcdString()),
                Field(name="SE12", lengthRule=FixedLengthRule(limit=2), parsingRule=ParseBcdString()),
                Field(name="SE13", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE14", lengthRule=FixedLengthRule(limit=12), parsingRule=ParseBcdString()),
                Field(name="SE15", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE16", lengthRule=FixedLengthRule(limit=2), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE17", lengthRule=FixedLengthRule(limit=15), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE18", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE19", lengthRule=FixedLengthRule(limit=2), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE20", lengthRule=FixedLengthRule(limit=10), parsingRule=ParseBcdString()),
                Field(name="SE21", lengthRule=FixedLengthRule(limit=4), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE22", lengthRule=FixedLengthRule(limit=6), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE23", lengthRule=FixedLengthRule(limit=2), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE24", lengthRule=FixedLengthRule(limit=6), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE25", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE26", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
            ]),
        ),
        Field(
            name="DE063",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBitmapFormat(subFields=[
                Field(name="SE00", lengthRule=FixedLengthRule(limit=3), parsingRule=ParseBitmap(offset=0, length=3)),
                Field(name="SE01", lengthRule=FixedLengthRule(limit=4), parsingRule=ParseBcdString()),
                Field(name="SE02", lengthRule=FixedLengthRule(limit=4), parsingRule=ParseBcdString()),
                Field(name="SE03", lengthRule=FixedLengthRule(limit=4), parsingRule=ParseBcdString()),
                Field(name="SE04", lengthRule=FixedLengthRule(limit=4), parsingRule=ParseBcdString()),
                Field(name="SE06", lengthRule=FixedLengthRule(limit=7), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE07", lengthRule=FixedLengthRule(limit=8), parsingRule=ParseBitString()),
                Field(name="SE08", lengthRule=FixedLengthRule(limit=8), parsingRule=ParseBcdString()),
                Field(name="SE09", lengthRule=FixedLengthRule(limit=14), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE10", lengthRule=FixedLengthRule(limit=13), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE11", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE12", lengthRule=FixedLengthRule(limit=30), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE13", lengthRule=FixedLengthRule(limit=6), parsingRule=ParseBcdString()),
                Field(name="SE14", lengthRule=FixedLengthRule(limit=36), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE15", lengthRule=FixedLengthRule(limit=8), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE18", lengthRule=FixedLengthRule(limit=4), parsingRule=ParseBcdString()),
                Field(name="SE19", lengthRule=FixedLengthRule(limit=3), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE21", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
            ]),
        ),
        Field(
            name="DE064",
            lengthRule=FixedLengthRule(limit=0),
            parsingRule=ParseUndefined(),
        ),
        Field(
            name="DE065",
            lengthRule=FixedLengthRule(limit=0),
            parsingRule=ParseUndefined(),
        ),
        Field(
            name="DE066",
            lengthRule=FixedLengthRule(limit=1),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE067",
            lengthRule=FixedLengthRule(limit=2),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE068",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE069",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE070",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE071",
            lengthRule=FixedLengthRule(limit=4),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE072",
            lengthRule=FixedLengthRule(limit=4),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE073",
            lengthRule=FixedLengthRule(limit=6),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE074",
            lengthRule=FixedLengthRule(limit=10),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE075",
            lengthRule=FixedLengthRule(limit=10),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE076",
            lengthRule=FixedLengthRule(limit=10),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE077",
            lengthRule=FixedLengthRule(limit=10),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE078",
            lengthRule=FixedLengthRule(limit=10),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE079",
            lengthRule=FixedLengthRule(limit=10),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE080",
            lengthRule=FixedLengthRule(limit=10),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE081",
            lengthRule=FixedLengthRule(limit=10),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE082",
            lengthRule=FixedLengthRule(limit=12),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE083",
            lengthRule=FixedLengthRule(limit=12),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE084",
            lengthRule=FixedLengthRule(limit=12),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE085",
            lengthRule=FixedLengthRule(limit=12),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE086",
            lengthRule=FixedLengthRule(limit=16),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE087",
            lengthRule=FixedLengthRule(limit=16),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE088",
            lengthRule=FixedLengthRule(limit=16),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE089",
            lengthRule=FixedLengthRule(limit=16),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE090",
            lengthRule=FixedLengthRule(limit=42),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE091",
            lengthRule=FixedLengthRule(limit=1),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE092",
            lengthRule=FixedLengthRule(limit=2),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE093",
            lengthRule=FixedLengthRule(limit=0),
            parsingRule=ParseUndefined(),
        ),
        Field(
            name="DE094",
            lengthRule=FixedLengthRule(limit=7),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE095",
            lengthRule=FixedLengthRule(limit=42),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE096",
            lengthRule=FixedLengthRule(limit=0),
            parsingRule=ParseUndefined(),
        ),
        Field(
            name="DE097",
            lengthRule=FixedLengthRule(limit=17),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE098",
            lengthRule=FixedLengthRule(limit=25),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE099",
            lengthRule=VariableLengthRule(limit=11, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE100",
            lengthRule=VariableLengthRule(limit=11, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE101",
            lengthRule=VariableLengthRule(limit=17, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE102",
            lengthRule=VariableLengthRule(limit=28, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE103",
            lengthRule=VariableLengthRule(limit=28, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE104",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseDataset(),
        ),
        Field(
            name="DE105",
            lengthRule=FixedLengthRule(limit=16),
            parsingRule=ParseBitString(),
        ),
        Field(
            name="DE106",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE107",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE108",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE109",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE110",
            lengthRule=VariableLengthRule(limit=1535, byteLength=2, encoding=Encoding.binary),
            parsingRule=ParseDataset(),
        ),
        Field(
            name="DE111",
            lengthRule=VariableLengthRule(limit=1535, byteLength=2, encoding=Encoding.binary),
            parsingRule=ParseDataset(),
        ),
        Field(
            name="DE112",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE113",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE114",
            lengthRule=VariableLengthRule(limit=1535, byteLength=2, encoding=Encoding.binary),
            parsingRule=ParseDataset(),
        ),
        Field(
            name="DE115",
            lengthRule=VariableLengthRule(limit=24, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE116",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE117",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE118",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE119",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE120",
            lengthRule=VariableLengthRule(limit=1537, byteLength=2, encoding=Encoding.binary),
            parsingRule=ParseDataset(),
        ),
        Field(
            name="DE121",
            lengthRule=VariableLengthRule(limit=11, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE122",
            lengthRule=FixedLengthRule(limit=0),
            parsingRule=ParseUndefined(),
        ),
        Field(
            name="DE123",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBin(),
        ),
        Field(
            name="DE124",
            lengthRule=FixedLengthRule(limit=0),
            parsingRule=ParseUndefined(),
        ),
        Field(
            name="DE125",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE126",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBitmapFormat(subFields=[
                Field(name="SE00", lengthRule=FixedLengthRule(limit=8), parsingRule=ParseBitmap(offset=0, length=8)),
                Field(name="SE01", lengthRule=FixedLengthRule(limit=0), parsingRule=ParseUndefined()),
                Field(name="SE02", lengthRule=FixedLengthRule(limit=0), parsingRule=ParseUndefined()),
                Field(name="SE03", lengthRule=FixedLengthRule(limit=0), parsingRule=ParseUndefined()),
                Field(name="SE04", lengthRule=FixedLengthRule(limit=0), parsingRule=ParseUndefined()),
                Field(name="SE05", lengthRule=FixedLengthRule(limit=8), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE06", lengthRule=FixedLengthRule(limit=17), parsingRule=ParseHexadecimal()),
                Field(name="SE07", lengthRule=FixedLengthRule(limit=17), parsingRule=ParseHexadecimal()),
                Field(name="SE08", lengthRule=FixedLengthRule(limit=20), parsingRule=ParseHexadecimal()),
                Field(name="SE09", lengthRule=FixedLengthRule(limit=20), parsingRule=ParseHexadecimal()),
                Field(name="SE10", lengthRule=FixedLengthRule(limit=6), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE11", lengthRule=FixedLengthRule(limit=0), parsingRule=ParseUndefined()),
                Field(name="SE12", lengthRule=FixedLengthRule(limit=3), parsingRule=ParseBitString()),
                Field(name="SE13", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE14", lengthRule=FixedLengthRule(limit=0), parsingRule=ParseUndefined()),
                Field(name="SE15", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE16", lengthRule=VariableLengthRule(limit=32, byteLength=1, encoding=Encoding.binary), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE17", lengthRule=FixedLengthRule(limit=0), parsingRule=ParseUndefined()),
                Field(name="SE18", lengthRule=FixedLengthRule(limit=12), parsingRule=ParseHexadecimal()),
                Field(name="SE19", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
                Field(name="SE20", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseString(encoding=Encoding.cp500)),
            ]),
        ),
        Field(
            name="DE127",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBin(),
        ),
        Field(
            name="DE128",
            lengthRule=FixedLengthRule(limit=8),
            parsingRule=ParseBitString(),
        ),
        Field(
            name="DE129",
            lengthRule=FixedLengthRule(limit=0),
            parsingRule=ParseUndefined(),
        ),
        Field(
            name="DE130",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBitString(),
        ),
        Field(
            name="DE131",
            lengthRule=FixedLengthRule(limit=5),
            parsingRule=ParseBitString(),
        ),
        Field(
            name="DE132",
            lengthRule=FixedLengthRule(limit=4),
            parsingRule=ParseHexadecimal(),
        ),
        Field(
            name="DE133",
            lengthRule=FixedLengthRule(limit=8),
            parsingRule=ParseString(encoding=Encoding.cp500),
        ),
        Field(
            name="DE134",
            lengthRule=VariableLengthRule(limit=32, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBin(),
        ),
        Field(
            name="DE135",
            lengthRule=VariableLengthRule(limit=15, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseHexadecimal(),
        ),
        Field(
            name="DE136",
            lengthRule=FixedLengthRule(limit=8),
            parsingRule=ParseHexadecimal(),
        ),
        Field(
            name="DE137",
            lengthRule=FixedLengthRule(limit=2),
            parsingRule=ParseHexadecimal(),
        ),
        Field(
            name="DE138",
            lengthRule=FixedLengthRule(limit=2),
            parsingRule=ParseBitString(),
        ),
        Field(
            name="DE139",
            lengthRule=FixedLengthRule(limit=10),
            parsingRule=ParseBin(),
        ),
        Field(
            name="DE140",
            lengthRule=VariableLengthRule(limit=16, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseBin(),
        ),
        Field(
            name="DE141",
            lengthRule=FixedLengthRule(limit=0),
            parsingRule=ParseUndefined(),
        ),
        Field(
            name="DE142",
            lengthRule=VariableLengthRule(limit=255, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseHexadecimal(),
        ),
        Field(
            name="DE143",
            lengthRule=VariableLengthRule(limit=20, byteLength=1, encoding=Encoding.binary),
            parsingRule=ParseHexadecimal(),
        ),
        Field(
            name="DE144",
            lengthRule=FixedLengthRule(limit=2),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE145",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE146",
            lengthRule=FixedLengthRule(limit=6),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE147",
            lengthRule=FixedLengthRule(limit=12),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE148",
            lengthRule=FixedLengthRule(limit=3),
            parsingRule=ParseBcdString(),
        ),
        Field(
            name="DE149",
            lengthRule=FixedLengthRule(limit=12),
            parsingRule=ParseBcdString(),
        ),
    ]),
    IsoVersion._1993: Template(headerRule=VisaHeaderRule(), fields=[]),
}
