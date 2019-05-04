class graph :
    def __init__(self,the_graph=None):
        if the_graph is None:
            the_graph = {}
        self.the_graph = the_graph
    def AddEdge(self, edge):
        edge = set(edge)
        (start,end) = tuple(edge)
        if start in self.the_graph:
            self.the_graph[start].append(end)
        else:
            self.the_graph[start] = [end]        
    def GetEdges(self):
        listedge = []
        for start in self.the_graph :
            for end in self.the_graph[start]:
                if {start,end} not in listedge:
                    listedge.append({start,end})
        return listedge
    def GetNode(self):
        nodes = []
        for node in self.the_graph.keys():
            nodes.append(node)
        return node
