class Pilas(object):
    def __init__(self):
        self.items=[]
    def push(self, dato):
        self.items.append(dato)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return (len(self.items))
    def consultar(self):
        print(self.items)
    def consultar1(self,dato):
        return self.items[dato]
    def tam(self):
        return (len(self.items))