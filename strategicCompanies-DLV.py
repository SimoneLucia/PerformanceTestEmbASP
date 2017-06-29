from languages.asp.ASPInputProgram import ASPInputProgram
from platforms.desktop.DesktopHandler import DesktopHandler
from specializations.dlv.desktop.DLVDesktopService import DLVDesktopService
from specializations.clingo.desktop.ClingoDesktopService import ClingoDesktopService
from base.Output import Output
import os
from languages.Predicate import Predicate
from languages.asp.AnswerSets import AnswerSets
from languages.asp.ASPMapper import ASPMapper



class ProducedBy(Predicate):
      
    predicateName="produced_by"
    
    def __init__(self, p=None, c1=None, c2=None, c3=None, c4=None):
        super(ProducedBy, self).__init__([("p"), ("c1"), ("c2"), ("c3"), ("c4")])
        self.p = p
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
          
    def getP(self):
        return self.p
    def getC1(self):
        return self.c1
    def getC2(self):
        return self.c2
    def getC3(self):
        return self.c3
    def getC4(self):
        return self.c4
    def setP(self, p):
        self.p = p
    def setC1(self, c1):
        self.c1 = c1
    def setC2(self, c2):
        self.c2 = c2
    def setC3(self, c3):
        self.c3 = c3
    def setC4(self, c4):
        self.c4 = c4



class ControlledBy(Predicate):
      
    predicateName="controlled_by"
    
    def __init__(self, c=None, c1=None, c2=None, c3=None, c4=None):
        super(ControlledBy, self).__init__([("c"), ("c1"), ("c2"), ("c3"), ("c4")])
        self.c = c
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
          
    def getC(self):
        return self.c
    def getC1(self):
        return self.c1
    def getC2(self):
        return self.c2
    def getC3(self):
        return self.c3
    def getC4(self):
        return self.c4
    def setC(self, c):
        self.c = c
    def setC1(self, c1):
        self.c1 = c1
    def setC2(self, c2):
        self.c2 = c2
    def setC3(self, c3):
        self.c3 = c3
    def setC4(self, c4):
        self.c4 = c4



class StrategicPair(Predicate):
      
    predicateName="strategic_pair"
    
    def __init__(self, c1=None, c2=None):
        super(StrategicPair, self).__init__([("c1"), ("c2")])
        self.c1 = c1
        self.c2 = c2

    def getC1(self):
        return self.c1
    def getC2(self):
        return self.c2    
    def setC1(self, c1):
        self.c1 = c1
    def setC2(self, c2):
        self.c2 = c2


class Strategic(Predicate):
      
    predicateName="strategic"
    
    def __init__(self, c=None):
        super(Strategic, self).__init__([("c")])
        self.c = c

    def getC(self):
        return self.c  
    def setC(self, c):
        self.c = c



if __name__ == '__main__':

    handler = DesktopHandler(DLVDesktopService(os.path.join("executables", "dlv.mingw.exe")))
 
    inp = ASPInputProgram()
    
    inp.addObjectInput(ProducedBy("pasta", "barilla", "amato", "dececco", "divella"))
    inp.addObjectInput(ProducedBy("tonno", "callipo", "star", "almera", "asdomar"))

    inp.addObjectInput(ControlledBy("callipo", "star", "almera", "asdomar", "barilla"))
    inp.addObjectInput(ControlledBy("barilla", "callipo", "almera", "dececco", "star"))

    inp.addObjectInput(StrategicPair("callipo", "barilla"))
                      
    inp.addFilesPath(os.path.join("ASPprogram", "strategicCompanies",))
             
    handler.addProgram(inp)

    ASPMapper.getInstance().registerClass(Strategic)
    ASPMapper.getInstance().unregisterClass(StrategicPair)
    ASPMapper.getInstance().unregisterClass(ControlledBy)
    ASPMapper.getInstance().unregisterClass(ProducedBy)

    out = handler.startSync()  
            
    ans = out.getAnswerSets()[0]
             
    for obj in ans.getAtoms():
        print(obj.getC())
            
    
