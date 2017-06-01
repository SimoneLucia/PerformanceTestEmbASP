from languages.asp.ASPInputProgram import ASPInputProgram
from platforms.desktop.DesktopHandler import DesktopHandler
from specializations.dlv.desktop.DLVDesktopService import DLVDesktopService
import os
from languages.Predicate import Predicate
from languages.asp.ASPMapper import ASPMapper


class Node(Predicate):
      
    predicateName="node"
    
    def __init__(self, name=None):
        super(Node, self).__init__([("name", int)])
        self.name = name
          
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Edge(Predicate):
      
    predicateName="edge"
    
    def __init__(self, firstNode=None, secondNode=None):
        super(Edge, self).__init__([("firstNode", int),("secondNode", int)])
        self.firstNode = firstNode
        self.secondNode = secondNode
          
    def getFirstNode(self):
        return self.firstNode
    def getSecondNode(self):
        return self.secondNode
    def setFirstNode(self, firstNode):
        self.firstNode = firstNode
    def setSecondNode(self, secondNode):
        self.secondNode = secondNode

class Col(Predicate):
      
    predicateName="col"
    
    def __init__(self, node=None, color=None):
        super(Col, self).__init__([("node", int),("color")])
        self.node = node
        self.color = color
          
    def getNode(self):
        return self.node
    def getColor(self):
        return self.color
    def setNode(self, node):
        self.node = node
    def setColor(self, color):
        self.color = color



if __name__ == '__main__':

    handler = DesktopHandler(DLVDesktopService(os.path.join("executables", "dlv.mingw.exe")))
 
    inp = ASPInputProgram()

    for i in range(1, 21):
        inp.addObjectInput(Node(i))
        
    inp.addObjectInput(Edge(1,2))
    inp.addObjectInput(Edge(1,5))
    inp.addObjectInput(Edge(1,6))
    inp.addObjectInput(Edge(2,8))
    inp.addObjectInput(Edge(2,3))
    inp.addObjectInput(Edge(3,10))
    inp.addObjectInput(Edge(3,4))
    inp.addObjectInput(Edge(4,5))
    inp.addObjectInput(Edge(4,12))
    inp.addObjectInput(Edge(5,14))
    inp.addObjectInput(Edge(6,7))
    inp.addObjectInput(Edge(6,15))
    inp.addObjectInput(Edge(7,8))
    inp.addObjectInput(Edge(7,17))
    inp.addObjectInput(Edge(8,9))
    inp.addObjectInput(Edge(9,10))
    inp.addObjectInput(Edge(9,18))
    inp.addObjectInput(Edge(10,11))
    inp.addObjectInput(Edge(11,12))
    inp.addObjectInput(Edge(11,19))
    inp.addObjectInput(Edge(12,13))
    inp.addObjectInput(Edge(13,14))
    inp.addObjectInput(Edge(13,20))
    inp.addObjectInput(Edge(14,15))
    inp.addObjectInput(Edge(15,16))
    inp.addObjectInput(Edge(16,17))
    inp.addObjectInput(Edge(16,20))
    inp.addObjectInput(Edge(17,18))
    inp.addObjectInput(Edge(18,19))
    inp.addObjectInput(Edge(19,20))

    
    inp.addFilesPath(os.path.join("ASPprogram", "3col",))
             
    handler.addProgram(inp)

    ASPMapper.getInstance().registerClass(Col)
    
    out = handler.startSync()  

    ASPMapper.getInstance().unregisterClass(Node)
    ASPMapper.getInstance().unregisterClass(Edge)
            
    ans = out.getAnswerSets()[0]

    for obj in ans.getAtoms():
        print("Node: " + str(obj.getNode()) + " Color: " + obj.getColor())
        
