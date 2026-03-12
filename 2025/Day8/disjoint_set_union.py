class DSU:
    def __init__(self, size:int):
        self.parent = list(range(size))
        self.rank = [0] * size 
        self.numComponents = size 
        self.history_stack = [] # [parent, child, rank_increased_flag]

    def find(self, node:int) -> int:
        while node != self.parent[node]:
            node = self.parent[node]
        return node 
    
    def union(self, u:int, v:int) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            self.history_stack.append(None)
            return False 
        rank_increased = False 
        if self.rank[root_u] < self.rank[root_v]:
            root_u, root_v = root_v, root_u 
        if self.rank[root_u] == self.rank[root_v]:
            self.rank[root_u] += 1 
            rank_increased = True 
        self.parent[root_v] = root_u 
        self.numComponents -= 1
        self.history_stack.append([root_u, root_v, rank_increased])
        return True 
    
    def rollback(self, u:int, v:int) -> bool:
        if not self.history_stack:
            return False 
        last_change = self.history_stack.pop()
        if last_change is None:
            return False 
        root_u, root_v, rank_increased = last_change 
        self.parent[root_v] = root_v 
        if rank_increased:
            self.rank[root_u] -= 1 
        self.numComponents += 1
        return True 