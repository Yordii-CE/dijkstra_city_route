class Dijkstra:
    def __init__(self, graph):        
        self.tb = self.setDefaultValues(graph)
 
    def setDefaultValues(self, graph):
        tb = []
        for node in graph:
            tb.append({            
                'node': node,
                'visited' : False,
                'distance' : None,
                'father' : None
            })
        return tb

    def setInitialNode(self, initialNode):
        self.initialNode = initialNode
        node = None
        for item in self.tb:
            if item['node'] == initialNode:
                item['distance'] = 0
                item['father'] = initialNode
                node = item['node']
        return node
        
    def updateVisited(self, node):
        for item in self.tb:
            if item['node'] == node:
                item['visited'] = True

    def updateDistance(self, node, newDistance):
        for item in self.tb:
            if item['node'] == node:
                item['distance'] = newDistance   

    def updateFather(self, node, father):
        for item in self.tb:
            if item['node'] == node:
                item['father'] = father

    def getOtherNode(self):
        tbNotDistance0 = list(filter(lambda x : x['distance'] != None and x['visited'] == False, self.tb)) 
        if len(tbNotDistance0) == 0: return None

        item = min(tbNotDistance0, key=lambda item: item['distance'])
        return item['node']
    
    def createRoutes(self, initialNode):
        work = self.setInitialNode(initialNode)
        while(work != None):
            self.updateVisited(work)
            for i in work.connections:
                node, distance = i['node'], i['distance']
                newDistance = self.getDistance(work) + distance

                if(self.getDistance(node) == None):
                    self.updateDistance(node, newDistance)
                    self.updateFather(node, work)            
                else:
                    if(newDistance <= self.getDistance(node)):
                        self.updateDistance(node, newDistance)
                        self.updateFather(node, work)
            work = self.getOtherNode()                      

    def getDistance(self, node):
        distance = 0
        for item in self.tb:
            if item['node'] == node:
                distance = item['distance']
                break

        return distance
    
    def getTbItem(self, node):
        tbItem = None
        for item in self.tb:            
            if item['node'] == node:
                tbItem = item
                break
        return tbItem
    
    def getBestRoute(self, destination):
        try:
            itemDestination = self.getTbItem(destination)  
            nodes = [itemDestination]

            while(itemDestination != None):            
                fatherItem = self.getTbItem(itemDestination['father'])           
                nodes.append(fatherItem)
                
                if(fatherItem['node'] == self.initialNode): break
                itemDestination = fatherItem
                
            nodes.reverse()
            return nodes
        except:
            return []    


class Route:
    pass