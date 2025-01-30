from random import randint
from base64 import b64decode
from datetime import datetime
from unittest import TestCase
from starkbank import iso8583


iso8583.encoding = "ascii"
iso8583.template = iso8583.mastercard


class TestIsoMessage(TestCase):

    def testParseUnparseMastercardAuthorization(self):
        localEncoding = "cp500"
        raw64Messages = [
            "AYnw8fDwdn9GASjhogrx9vXy8PT39PDw8PDw8PHw8fDw8PDw8PDw8PDw8PDw8PH18PDw8PDw8PDw8PH18PDx8vD38vPz8fT59vHw8PDw8PDw8PDw8ffy8/Px9Pnx8vD38vDx8PHy8Pfx8vD39fT5+fD18fDw8PD28PHy8/T18/f18vD09/Tw8PDw8PDx8PHwxPLw8fDx9PHy8vDx8Pj09vnw+PT28Pj18PDw8fDw8PDz8fLz9PX29/jx8vP09fb3+Pnx8vP09fbGydni40DjyMnZxEDCwdXSQEBAQEBAQOLjS0DT1uTJ4kBAQEBA1NZA8PD22fP48PHp+PTw+PTw8Pn3XyoCCECCAlgAhAegAAAABBAQlQUAAAAAAJoDIBIHnAEAnwIGAAAAABUAnxAIAQEDoAAA2sGfGgIIQJ8mCEIhVjSgssSnnycBgJ8zA+Do6J80A0QDAJ82AgIdnzcEE9Ruv/Dy9fDw8PDw8PDw8PD48PD49PD58PLx8PHy8/Tw8PnUw+Lw8fHw9tM=",
            "APXw8fLwfiJkAYLh4Arx9vXy8Pnx+fDw8PDw8Pn3+PHw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw9vHw8vLy+fP18vP48PPy8Pbx8PX48fTw9/bw8fjw9vX2+fDw8PD28vHy9/Ly8PX58vXz+PP2+PL49PDw8PD2+fn19fbz9cnG1tbEQEBAQEBAQEBAQEBAQEBAQEDV1uTEQMPJ4+hAQEBAQEDC2cHw8fDZ9vHw9fHw8PDw+fj2+PTw+fj28PL18UD09fHx+PFA8fbw8Pj08Pnw8vHw8fLz9PDw+dTmwvH59fjy8g==",
            "AQbw9PDw8iMAAY6B4AIAAABCAAAAAPH29fLw+fH58PDw8PDw8fn2+fDw8PDw8PDw8PDw8PDw8fjw8PD48vLx+PPw9fj28vjy8PHw+PLy8Pjy8vD28Pnz9vX48Pbw8/Pz+fj4+Pnw9vL18/H58fbDwYGBmdXx9/P59/bx+Pfx8PPw1/bz8fPU5sLz+fT3+fnw+PLy+Pfw8dT58vDz8PDw+fj2+fj2+fj28PD51ObC8/n09/n58PHw8Pby+PLw8fD48vLx+PPw9fjw8PDw8PD58/b1+PDw8PDw8PPz8/n48PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PDw",
            "AS7w9PLw9msEAQohoRIAAABAAAAAAPH29fP48fDy8PH09/Xw9/jw9vDw8PDw8PDw8PDw8PDw9fL58PDw8PDw8PDx8PPz9/Hy8Pbx9vDy9fj28fn19PDw8PDw8PDx9vHy8Pbx8vD28fLw9vDw8PD2+fn5+fDx8Pjw8PHy9fDw8PDz+PLUiaKDQNmFo4GJk0BAQEBAQEBAQEBAQOWFh4GiQEBAQEBAQEBA1eVA8PLw2fbz8fXU2ebw8fHw1enx8vD2QED49PD5+Pbw8/fw8fPz8PHy+fXw8PHT5sTE1sni1NHT8sL35tfT4sLC5sjWxtPl8PD39PDy8PDw8PDw+dTZ5vDx8fDV6fDx8PDw8PDw8fbw8PDw8Pn5+fnw8fDw8PDw8PDw8PDw8PDw8PDw8PDw8A==",
        ]
        for raw64 in raw64Messages:
            raw = b64decode(raw64)[2:]
            msg = iso8583.parse(raw, encoding=localEncoding)
            self.assertEqual(raw, iso8583.unparse(msg, encoding=localEncoding))

    def testParseUnparseMastercardClearing(self):
        localEncoding = "cp500"
        raw64 = "AYLx8vTw/BABAQRh4AICAAAAAAAAAPH29fLy8/Py8PDz8/Hw8vLw9fDw8PDw8PDw8PDw8PDw8vLw8PDw8PDw8PDw8vLw8PDw8PDw8PDw8vLw8PLz8Pbx9PLx9fT09/Lw8PD19/nx9/XUpuOCmKL38fX5+Pby9/j18Pn18/T0+fn5QOPB58ngwoWZqJNA4qOZhYWj4MSBiJWShUDDiaOo4PHy8/T19vf4QEDC2cHC2cHx9/bw8fT28PP28PDw8PDxwtnT8PDw8PDw8PDw8PTy+fj28PDw8PDw8PDw8PTy8PH1+fD29/Ly8/L2+PX1+Pj08PDw8PDw8PDy8fXy8UBAQEBAQEBAQEBAQEBAQPH19vHy8vjz8/fw1fLz8Pbx+PD28vPw9vH48Pbw8ffz8PD45MHYQOJLwUvw8ff28PH5hImjo5Zh1MPi8PPw8fX18Pbx9PD18PLw8fHJ1eXBw+OEiaOjlvn49vn49vn49vDx89TD4vDz8PH19fD28fTw8PDw8PD19g=="
        raw = b64decode(raw64)[2:]
        msg = iso8583.parse(raw, encoding=localEncoding)
        self.assertEqual(raw, iso8583.unparse(msg, encoding=localEncoding))

    def testParseUnparseVisaAuthorization(self):
        localTemplate = iso8583.visa
        raw64Messages = [
            "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",  # Reject header message
        ]
        for raw64 in raw64Messages:
            raw = b64decode(raw64)[4:]
            msg = iso8583.parse(raw, template=localTemplate)
            self.assertEqual(raw, iso8583.unparse(msg, template=localTemplate))

    def testUnparseParseVisaLogin(self):
        localTemplate = iso8583.visa
        messageType = "login"
        now = datetime.utcnow()
        traceNumber = str(randint(1, 999999)).zfill(6)
        visaLogin = {
            "Header": {
                "H02": "01",
                "H03": "02",
                "H05": "000000",
                "H06": "123456",
                "H07": "00000000",
                "H08": "0000",
                "H09": "000000",
                "H10": "00",
                "H11": "000000",
                "H12": "00",
            },
            "MTI": "0800",
            "DE007": now.strftime("%m%d%H%M%S"),
            "DE011": traceNumber,
            "DE037": "{year}{julianDay}{hours}{traceNumber}".format(
                year=now.year % 10,
                hours=now.strftime("%H"),
                julianDay=now.strftime("%j"),
                traceNumber=traceNumber,
            ),
            "DE063": {
                "SE01": "0002",
            },
            "DE070": {
                "login": "071",
                "logout": "072",
            }[messageType]
        }

        raw = iso8583.unparse(visaLogin, template=localTemplate)

        # Add bitmap and length fields
        visaLogin["DE063"]["SE00"] = [1]
        visaLogin["Header"]["H01"] = "16"
        visaLogin["Header"]["H04"] = "0044"

        parsedMsg = iso8583.parse(raw, template=localTemplate)
        for key, value in visaLogin.items():
            self.assertEqual(value, parsedMsg[key])
