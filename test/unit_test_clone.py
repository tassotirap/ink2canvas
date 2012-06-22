'''
Created on 23/05/2012

@author: thiago
'''
import unittest
import sys
sys.path.append('..')

from ink2canvas.svg import Use, G
from ink2canvas.main import Ink2Canvas

#TODO: ver se eh para fazermos as transformacoes baseados nos paramentros do pai ou do filho(use)
#      ver o x e y de quem eu uso(os do use estao todos 0 , 0) 
class Test(unittest.TestCase):
    
    def setUp(self):
        self.ink2canvas = Ink2Canvas()
        svg_input = "arquivos_test/unit_test_clone_quadrados.svg"
        self.ink2canvas.parse(svg_input)
        self.ink2canvas.effect()
        self.root = self.ink2canvas.core.root 
        self.ListofUses = []
        
        
        #get the html code
        
        
    def criaListaDeUse(self,nosQueDevemSerDesenhados):
       
        for noEmQuestao in nosQueDevemSerDesenhados:
            if(isinstance(noEmQuestao, Use)):
                self.ListofUses.append(noEmQuestao)
            if(isinstance(noEmQuestao, G)):
                self.criaListaDeUse(noEmQuestao.children)
                    
    def procuraPelaTagUSE(self,nosQueDevemSerDesenhados):
        retorno = False
        for noEmQuestao in nosQueDevemSerDesenhados:
            if(isinstance(noEmQuestao, Use)):
                return True
            if(isinstance(noEmQuestao, G)):
                retorno = self.procuraPelaTagUSE(noEmQuestao.children)
                if(retorno):
                    break
        return retorno
        
    def testCloneCreate(self):
        raizDaArvore = self.root
        boolean = self.procuraPelaTagUSE(raizDaArvore.getDrawable())
        self.assertEqual(boolean,True) 
    
    def testProcuraIdDoClone(self):
        self.criaListaDeUse(self.root.getDrawable())
        for cadaUse in self.ListofUses:
            idQueTenhoQueAchar = cadaUse.getCloneId()
            self.assertIsNotNone(idQueTenhoQueAchar)
            elementoDoId = self.ink2canvas.core.root.buscaElementoPorId(idQueTenhoQueAchar,self.root.getDrawable())
            self.assertIsNotNone(elementoDoId)
    
    def testCLoneBuffer(self):
        svg_input = "arquivos_test/unit_test_clone_identico.svg"
        self.ink2canvas.parse(svg_input)
        self.ink2canvas.effect()
        self.root = self.ink2canvas.core.root 
        self.ListofUses = []
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCLoneCreate']
    unittest.main()