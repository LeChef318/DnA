class Node:
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges
        self.visited = False
        self.distance = float("Infinity")
        self.prev = None

class Graph():
    def __init__(self) -> None:
        self.nodes = []
    
    def add_node(self, name, edges):
        n = Node(name, edges)
        self.nodes.append(n)

    def get_node(self, name):
        for i in self.nodes:
            if i.name == name:
                return i
        raise RuntimeError("Node not found")
    
    def reset_nodes(self):
        for i in self.nodes:
            i.visited = False
            i.distance = float("Infinity")
            i.prev = None
    
    def find_shortest(self, start, end):
        curNode = self.get_node(start)
        curNode.distance = 0
        while curNode.name != end:
            for i in range(len(curNode.edges)):
                if curNode.edges[i] > 0:
                    nde = self.get_node(i)
                    if nde.distance > (curNode.distance + curNode.edges[i]):
                        nde.distance = curNode.distance + curNode.edges[i]
                        nde.prev = curNode
            curNode.visited = True
            curNode = min(filter(lambda x: x.visited == False ,self.nodes), key=lambda x: x.distance)
            if curNode.distance == float("Infinity"):
                print("No path found")
                return "No path found"
        path = ""
        out_node = curNode
        while True:
            path = path + str(out_node.name) + " -> "
            if out_node.name == start:
                break
            out_node = out_node.prev
        path = path + "Distance: " + str(curNode.distance)
        print(path)
        return curNode.distance



if __name__ == "__main__":
    results = []
    try:
        file = open("./DnA/input.txt", "r")
    except:
        raise FileNotFoundError("File not found")
    else:
        G = Graph()
        nodes = int(file.readline())
        for i in range(nodes):
            line = file.readline()
            l = list(map(int, line.split()))
            G.add_node(i, l)
        tests = int(file.readline())
        for t in range(tests):
            test = list(map(int, file.readline().split()))
            x = G.find_shortest(test[0], test[1])
            G.reset_nodes()
            results.append(x)
        file.close()
        print(results)