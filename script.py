import subprocess
import time
import csv


class Test:
    def __init__(self, nome, repetition):
        self.repetition = repetition
        self.nome = nome
        self.timesJava = list()
        self.timesPython = list()
        self.timesSolver = list()
        
        lisJava = ["java", "-jar", self.nome + ".jar"]

        for i in range(self.repetition):
            start = int(time.time()*1e+9)
            proc = subprocess.Popen(lisJava, universal_newlines=True, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, )
            out, err = proc.communicate()
            end = int(time.time()*1e+9)
            print(err + out)
            self.timesJava.append(str(end - start))
        print("---JAVA---")
        print("-Processo Completo Tempi-")
        print(self.timesJava)


        lisPy = ["python3", self.nome + ".py"]

        for i in range(self.repetition):
            start = int(time.time()*1e+9)
            proc = subprocess.Popen(lisPy, universal_newlines=True, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, )
            out, err = proc.communicate()
            end = int(time.time()*1e+9)
            print(out)
            self.timesPython.append(str(end - start))
        print("---PYTHON---")
        print("-Processo Completo Tempi-")
        print(self.timesPython)

        lis = ["dlv.mingw.exe", "ASPprogram/" + self.nome + "-withFact", "--"]

        for i in range(self.repetition):
            start = int(time.time()*1e+9)
            proc = subprocess.Popen(lis, universal_newlines=True, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, )
            out, err = proc.communicate()
            end = int(time.time()*1e+9)
            self.timesSolver.append(str(end - start))
        print("---SOLVER---")
        print("-Solo SOlver Tempi-")
        print(self.timesSolver)

    def getRepetition(self):
        return self.repetition

    def getName(self):
        return self.nome

    def getTimesSolver(self):
        return self.timesSolver

    def getMediaSolver(self):
        som = 0
        for i in self.timesSolver:
            som += int(i)
        print(som/self.repetition)
        return som/self.repetition
    
    def getTimesJava(self):
        return self.timesJava

    def getTimesMenusSolverJava(self):
        return self.getMediaJava() - self.getMediaSolver()

    def getMediaJava(self):
        som = 0
        for i in self.timesJava:
            som += int(i)
        print(som/self.repetition)
        return som/self.repetition

    def getTimesPython(self):
        return self.timesPython
    
    def getTimesMenusSolverPython(self):
        return self.getMediaPython() - self.getMediaSolver()

    def getMediaPython(self):
        som = 0
        for i in self.timesPython:
            som += int(i)
        print(som/self.repetition)
        return som/self.repetition

if __name__ == '__main__':
    test1 = Test("sudoku-DLV", 50)
    test2 = Test("3col-DLV", 50)
    test3 = Test("3col-CLINGO", 50)
    test4 = Test("sudoku-CLINGO", 50)
    allTests = [test1, test2, test3, test4]
    with open('tempi.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        for i in allTests:
            spamwriter.writerow([i.getName()])
            spamwriter.writerow(["Java", "Python", "solver"])
            for j in range(i.getRepetition()):
                spamwriter.writerow([i.getTimesJava()[j], i.getTimesPython()[j], i.getTimesSolver()[j]])
            spamwriter.writerow(["Media","Media","Media"])
            spamwriter.writerow([str(i.getMediaJava()).replace(".", ","),str(i.getMediaPython()).replace(".", ","), str(i.getMediaSolver()).replace(".", ",")])
            spamwriter.writerow(["Differenza","Differenza"])
            spamwriter.writerow([str(i.getTimesMenusSolverJava()).replace(".", ","), str(i.getTimesMenusSolverPython()).replace(".", ",")])
            spamwriter.writerow(["--------------------------------------------------------------------------------------------"])







