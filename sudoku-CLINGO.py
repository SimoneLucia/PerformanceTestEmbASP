from languages.asp.ASPInputProgram import ASPInputProgram
from platforms.desktop.DesktopHandler import DesktopHandler
from specializations.clingo.desktop.ClingoDesktopService import ClingoDesktopService
from base.Output import Output
import os
from languages.Predicate import Predicate
from languages.asp.AnswerSets import AnswerSets



class Cell(Predicate):
      
    predicateName="cell"
    
    def __init__(self, row=None, column=None, value=None):
        super(Cell, self).__init__([("row", int), ("column", int), ("value", int)])
        self.row = row
        self.value = value
        self.column = column
          
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def getValue(self):
        return self.value
    def setRow(self, row):
        self.row = row
    def setColumn(self, column):
        self.column = column
    def setValue(self, value):
        self.value = value



if __name__ == '__main__':
    n = 9
    inputMatrix = [ [ 1, 0, 0, 0, 0, 7, 0, 9, 0 ],
                    [ 0, 3, 0, 0, 2, 0, 0, 0, 8 ],
                    [ 0, 0, 9, 6, 0, 0, 5, 0, 0 ],
                    [ 0, 0, 5, 3, 0, 0, 9, 0, 0 ],
                    [ 0, 1, 0, 0, 8, 0, 0, 0, 2 ],
                    [ 6, 0, 0, 0, 0, 4, 0, 0, 0 ],
                    [ 3, 0, 0, 0, 0, 0, 0, 1, 0 ],
                    [ 0, 4, 1, 0, 0, 0, 0, 0, 7 ],
                    [ 0, 0, 7, 0, 0, 0, 3, 0, 0 ] ]

    handler = DesktopHandler(ClingoDesktopService(os.path.join("executables", "clingo64.exe")))
 
    inp = ASPInputProgram()
            
    for i in range(n):
        for j in range(n):
            if (inputMatrix[i][j] != 0):
                inp.addObjectInput(Cell(i,j,inputMatrix[i][j]))
                      
    inp.addFilesPath(os.path.join("ASPprogram", "sudoku",))
             
    handler.addProgram(inp)
            
    out = handler.startSync()  
            
    ans = out.getAnswerSets()[0]
             
    for obj in ans.getAtoms():
        inputMatrix[obj.getRow()][obj.getColumn()] = obj.getValue()
            
    tmp=""
    for i in range(9):
        for j in range(9):
            tmp += str(inputMatrix[i][j]) + " "
        print(tmp)
        tmp=""
