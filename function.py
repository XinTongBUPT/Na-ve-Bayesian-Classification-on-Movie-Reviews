import math
import re

class Bayes_Classifier:

    def __init__(self):
        self.numDocs = 0
        self.numPosDict = 0
        self.numNegDict = 0
        self.sumPosDict = 0
        self.sumNegDict = 0
        self.posDict = {}
        self.negDict = {}
        self.numPosDoc = 0
        self.numNegDoc = 0

    def train(self, lines):
        data = self.dealwithData(lines)
        self.posDict, self.negDict, self.numPosDoc, self.numNegDoc = self.bagofWords(data)
        self.numDocs = len(lines)
        self.numPosDict = len(self.posDict)
        self.numNegDict = len(self.negDict)
        pos = self.posDict
        neg = self.negDict
        self.sumPosDict = sum(self.posDict.values())
        self.sumNegDict = sum(self.negDict.values())
        print(self.posDict)

    def classify(self, lines):
        predictions = []
        data = self.dealwithData(lines)
        for row in data:
            posProb = math.log(self.numPosDoc / self.numDocs)
            negProb = math.log(self.numNegDoc / self.numDocs)
            for word in row[2:]:
                if word in self.posDict.keys():
                    posProb = posProb + math.log((self.posDict[word] + 1) / (self.numPosDict+self.sumPosDict))
                else:
                    posProb = posProb + math.log(1 / (self.numPosDict + self.sumPosDict+ self.sumNegDict))

                if word in self.negDict.keys():
                    negProb = negProb + math.log((self.negDict[word] + 1) / (self.numNegDict + self.sumNegDict))
                else:
                    negProb = negProb + math.log(1 / (self.numNegDict + self.sumNegDict+ self.sumPosDict))
            if posProb >= negProb:
                predictions.append('5')
            else:
                predictions.append('1')
        return predictions

    def dealwithData(self,lines):
        data = []
        for row in lines:
            data.append(row.split('|'))
        for row in data:
            row[2] = self.removeCaracters(row[2])
            row[2:] = row[2].split(' ')
        return data

    def bagofWords(self,data):
        negDict = {}
        posDict = {}
        numNegDoc = 0
        numPosDoc = 0
        for row in data:
            if row[0] == '1':
                numNegDoc = numNegDoc+1
                for word in row[2:]:
                    if word in negDict.keys():
                        negDict[word] = negDict[word] + 1
                    else:
                        negDict[word] = 1
            if row[0] == '5':
                numPosDoc = numPosDoc+1
                for word in row[2:]:
                    if word in posDict.keys():
                        posDict[word] = posDict[word] + 1
                    else:
                        posDict[word] = 1
        return posDict,negDict,numPosDoc,numNegDoc

    def removeCaracters(self,text):
        # Remover pontuacoes
        text = text.lower()
        text = text.replace(".", " ")
        text = text.replace(",", " ")
        text = text.replace(":", " ")
        text = text.replace(";", " ")
        text = text.replace("?", " ")
        text = text.replace("-", " ")
        text = text.replace("!", " ")
        text = text.replace(")", " ")
        text = text.replace("(", " ")
        text = text.replace("*", " ")
        text = text.replace("<", " ")
        text = text.replace(">", " ")
        text = text.replace("/", " ")
        text = text.replace("#", " ")
        text = text.replace("'", " ")
        text = text.replace("$", " ")
        text = text.replace("%", " ")
        text = text.replace("@", " ")
        text = text.replace(r'\r', ' ')
        text = text.replace(r'\r', ' ')
        text = text.replace("\n", ' ')
        text = text.replace(r"\\", ' ')


        # Remover artigos e pronomes
        text = text.replace("to ", " ")
        text = text.replace("a ", " ")
        text = text.replace("as ", " ")
        text = text.replace("the ", " ")
        text = text.replace("of ", " ")
        text = text.replace("on ", " ")
        text = text.replace("in ", " ")
        text = text.replace("an ", " ")
        text = text.replace("its ", " ")
        text = text.replace("for ", " ")
        text = text.replace("i ", " ")
        text = text.replace("and ", " ")
        text = text.replace("this ", " ")
        text = text.replace("that ", " ")
        text = text.replace("these ", " ")
        text = text.replace("it ", " ")
        text = text.replace("he ", " ")
        text = text.replace("she ", " ")
        text = text.replace("his ", " ")
        text = text.replace("there ", " ")
        text = text.replace("with ", " ")
        text = text.replace("me ", " ")
        text = text.replace("is ", " ")
        text = text.replace("are ", " ")
        text = text.replace("it's ", " ")
        text = text.replace("make ", " ")
        text = text.replace("him ", " ")

        '''
        f = open('stopwords.txt', "r")
        data = f.readlines()
        f.close()
        for x in data:
            text = text.replace(x, "")
        '''
        s = "!#$%&()*+,-./:;<=>?@[\]^_`{'~}"
        s += '"1234567890'
        for x in s:
            text = text.replace(x, ' ')

        return text