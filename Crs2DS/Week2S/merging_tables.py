# python3
# import sys
# import threading

class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        #my fixes
        #self.ranks=row_counts
        # if 0 in row_counts:
        self.ranks = [1] * n_tables
        
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)
        # slide 27
        # merge two components
        # use union by rank heuristic

        # if its a root
        if src_parent == dst_parent:
            return False

        # #rank heuristic   
        # if self.ranks[src_parent] != self.ranks[dst_parent]:
        #     self.parents[dst_parent] = src_parent

        #     self.row_counts[src_parent]+=self.row_counts[dst_parent]
        # else:
        #     self.ranks[dst_parent]+=1    
       
        if self.ranks[src_parent] > self.ranks[dst_parent]:

            self.parents[dst_parent] = src_parent

            self.row_counts[src_parent]+=self.row_counts[dst_parent]
           
        else:
            self.parents[src_parent] = dst_parent

            self.row_counts[dst_parent]+=self.row_counts[src_parent]
            
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[dst_parent]+=1
                
        # update max_row_count with the new maximum table size
        self.max_row_count=max(self.max_row_count,max(self.row_counts))
        #self.max_row_count=max(self.row_counts)

        return True

    def get_parent(self, table):
        # find parent and compress path

        if table!=self.parents[table]:
            self.parents[table]=self.get_parent(self.parents[table])

        return self.parents[table]

        # if table!=self.parents[table]:
        #     table=self.parents[table]
  

        # return table


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()

if __name__ == "__main__":

    main()
