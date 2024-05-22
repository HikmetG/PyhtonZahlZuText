import unittest
import functions

class TestFunctions(unittest.TestCase):
    def test_onesDigit(self):
        self.assertEqual(functions.onesDigit("0",1),"null")
        self.assertEqual(functions.onesDigit("1",1),"eins")
        self.assertEqual(functions.onesDigit("21",2),"ein")
        self.assertEqual(functions.onesDigit("2",1),"zwei")
        self.assertEqual(functions.onesDigit("3",1),"drei")
        self.assertEqual(functions.onesDigit("4",1),"vier")
        self.assertEqual(functions.onesDigit("5",1),"fünf")
        self.assertEqual(functions.onesDigit("6",1),"sechs")
        self.assertEqual(functions.onesDigit("7",1),"sieben")
        self.assertEqual(functions.onesDigit("8",1),"acht")
        self.assertEqual(functions.onesDigit("9",1),"neun")

        self.assertEqual(functions.onesDigit("10",2),"")
        self.assertEqual(functions.onesDigit("20",2),"")
        self.assertEqual(functions.onesDigit("30",2),"")
        self.assertEqual(functions.onesDigit("40",2),"")
        self.assertEqual(functions.onesDigit("50",2),"")
        self.assertEqual(functions.onesDigit("60",2),"")
        self.assertEqual(functions.onesDigit("70",2),"")
        self.assertEqual(functions.onesDigit("80",2),"")
        self.assertEqual(functions.onesDigit("90",2),"")
    
    def test_tensDigit(self):
        self.assertEqual(functions.tensDigit("16",2),"zehn")
        self.assertEqual(functions.tensDigit("22",2),"zwanzig")
        self.assertEqual(functions.tensDigit("35",2),"dreissig")
        self.assertEqual(functions.tensDigit("46",2),"vierzig")
        self.assertEqual(functions.tensDigit("52",2),"fünfzig")
        self.assertEqual(functions.tensDigit("68",2),"sechzig")
        self.assertEqual(functions.tensDigit("75",2),"siebzig")
        self.assertEqual(functions.tensDigit("89",2),"achtzig")
        self.assertEqual(functions.tensDigit("93",2),"neunzig")
    
    def test_turnNumberToText(self):
        self.assertEqual(functions.turnNumberToText("11"),"elf")
        self.assertEqual(functions.turnNumberToText("12"),"zwölf")
        self.assertEqual(functions.turnNumberToText("16"),"sechzehn")
        self.assertEqual(functions.turnNumberToText("17"),"siebzehn")
        self.assertEqual(functions.turnNumberToText("19"),"neunzehn")
        self.assertEqual(functions.turnNumberToText("20"),"zwanzig")
        self.assertEqual(functions.turnNumberToText("26"),"sechsundzwanzig")
        self.assertEqual(functions.turnNumberToText("37"),"siebenunddreissig")

        with self.assertRaises(ValueError):
            functions.turnNumberToText("00")
            functions.turnNumberToText("06")
            functions.turnNumberToText("08")
            functions.turnNumberToText("09")
if __name__ == '__main__':
    unittest.main()