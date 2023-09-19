class Node:    
    def __init__(self, value):
        self.value = value
        self.connections = []

    def connect(self, connections):
        self.connections = connections
