class Document():
    def __init__(self):
        self.Version = 0
        self.StoryName = ""
        self.Pages = list()
        self.Layers = list()
    
    def addPage(self,page):
        self.Pages.append(page)

    def addLayer(self, layer):
        self.Layers.append(layer)

class Page():
    def __init__(self):
        self.Name = ""
        self.Script = ""
        self.BackgroundColor = ""
        self.BackgroundImage = ""
        self.Audio = ""
        self.Instances = list()

    def addInstance(self, instance):
        self.Instances.append(instance)


class Instance():
    def __init__(self):
        self.LayerID = ""
        self.X = 0
        self.Y = 0
        self.Width = 0
        self.Height = 0
        self.Link = ""
        self.Comment = ""

class Layer():
    def __init__(self):
        self.Name = ""
        self.Text = ""
        self.ImageRef = ""
        self.ImageData = ""
        self.X = 0
        self.Y = 0
        self.Width = 0
        self.Height = 0
        self.Link = ""