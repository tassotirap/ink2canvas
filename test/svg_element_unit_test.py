import sys
import unittest
from inkex import Effect
sys.path.append('..')

from ink2canvas.svg.Element import Element


class TestSvgElement(unittest.TestCase):
    def setUp(self):
        self.element = Element()
        self.effect = Effect()
        self.document = self.effect.parse("arquivos_test/circulo.svg")
        self.node = self.effect.document.getroot()
        
    def testAttrWithNs(self):
        self.element.node = self.node
        retorno = self.element.attr("width", "ns")
        self.assertEqual(retorno, "210mm")
        
        
    def testAttrWithoutNs(self):
        self.element.node = self.node
        retorno = self.element.attr("width")
        self.assertEqual(retorno, "210mm")
   
if __name__ == '__main__':
    unittest.main()
    
