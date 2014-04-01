#import util
#This is a horrible mess of a parser, it does not attempt any tokenization

from dreamer_document import *

class DreamerReader():
    #def __init__(self):

    def getVersion(self,line):
        versionLine = line.split()
        if(len(versionLine) == 2):
            return versionLine[1]
        else:
            return line

    def indentLevel(self, line):
        rawLine = line
        unstrippedLength = len(rawLine)

        line = rawLine.lstrip()
        lineLength = len(line)
        indentationLevel = (unstrippedLength - lineLength)/4

        return indentationLevel

    def parseInstances(self,page):
        InstancesLine =  self.lines[self.lineNumber]

        if InstancesLine.lstrip() == "Instances:":
            currentLineNumber = self.lineNumber + 1
            currentLine = self.lines[currentLineNumber]

            InstancesIndentLevel = self.indentLevel(InstancesLine)

            #if the current indent level hasn't changed then we're still parsing instances
            while self.indentLevel(currentLine) - InstancesIndentLevel > 0:
                instance = Instance()
                #ID
                instance.LayerID = currentLine.lstrip()
                #Position
                positionLines = self.lines[currentLineNumber+1].lstrip().split()
                if len(positionLines)==2:
                    instance.X = int(positionLines[0])
                    instance.Y = int(positionLines[1])

                #Layer Size
                sizeLines = self.lines[currentLineNumber+2].lstrip().split()
                if len(sizeLines)==2:
                    instance.Width = int(sizeLines[0])
                    instance.Height = int(sizeLines[1])

                #Link
                instance.Link = self.lines[currentLineNumber+3].lstrip()
                
                #Comment
                instance.Comment = self.lines[currentLineNumber+4].lstrip()

                page.addInstance(instance)

                #Little bit obfusticated
                currentLineNumber += 5
                currentLine = self.lines[currentLineNumber]

            #set the line number to be the current line number after we've parsed all instances
            self.lineNumber = currentLineNumber

        else:
            print("Expected 'Instances:' in current page")



    def parsePage(self):
        newPage = Page()
        newPage.Name=self.lines[self.lineNumber+1].lstrip()
        newPage.Script=self.lines[self.lineNumber+2].lstrip()
        newPage.BackgroundColor=self.lines[self.lineNumber+3].lstrip()
        newPage.BackgroundImage=self.lines[self.lineNumber+4].lstrip()
        newPage.Audio=self.lines[self.lineNumber+5].lstrip()

        self.lineNumber +=6

        #parse instances
        self.parseInstances(newPage)

        return newPage

    def parseLayer(self):
        newLayer = Layer()
        newLayer.Name = self.lines[self.lineNumber+1].lstrip()
        newLayer.Text = self.lines[self.lineNumber+2].lstrip()
        newLayer.ImageRef = self.lines[self.lineNumber+3].lstrip()
        newLayer.ImageData = self.lines[self.lineNumber+4].lstrip()
        positionLines = self.lines[self.lineNumber+5].lstrip().split()
        if len(positionLines) == 2:
            newLayer.X = positionLines[0]
            newLayer.Y = positionLines[1]

        dimensionLines = self.lines[self.lineNumber+6].lstrip().split()
        if len(dimensionLines) == 2:
            newLayer.Width = dimensionLines[0]
            newLayer.Height = dimensionLines[1]
        
        self.lineNumber +=7

        return newLayer


    def read(self):
        f = open('testfile.dr', 'r')
        fileString = f.read()
        self.lines = fileString.split('\n')
        self.lineNumber = 0

        currentDocument = Document()

        while self.lineNumber < len(self.lines):
            rawLine = self.lines[self.lineNumber]
            unstrippedLength = len(rawLine)

            line = rawLine.lstrip()
            lineLength = len(line)
            indentationLevel = (unstrippedLength - lineLength)/4
            #print(indentationLevel)

            if self.lineNumber==0:
                version = self.getVersion(line)
                currentDocument.Version = version
                #print("Version Number: " + version)

            if self.lineNumber==1:
                storyName = line
                currentDocument.StoryName = storyName;
                #print("Story Name: " + storyName)

            if line == "Page:":
                anotherPage = self.parsePage()
                #print("Page Name: " + anotherPage.Name)
                currentDocument.addPage(anotherPage)

                #skip the rest of the loop and go straight to next iteration
                continue

            if line == "Layer:":
                newLayer = self.parseLayer()
                currentDocument.addLayer(newLayer)

                continue


            self.lineNumber+=1
        f.close()

        #print debugging results
#         for eachPage in currentDocument.Pages:
#             print(eachPage.Name)
#             print(len(eachPage.Instances))
#             for instance in eachPage.Instances:
#                 print(instance.LayerID)
#                 print(str(instance.X) + " " + str(instance.Y))
#                 print(str(instance.Width) + " " + str(instance.Height))
#                 print(instance.Link)
#                 print(instance.Comment)
#         for layer in currentDocument.Layers:
#             print(layer.Name)

        return currentDocument



