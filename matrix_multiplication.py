
class memoized_lookup_chain:

    def __init__(self, dim_list):

        n = len(dim_list)
        self._memoized_m = [[float("inf") for j in range(n - i)] for i in range(n)]
        self._dim_list = dim_list

    def __call__(self, start, end):

        if(start > end):
            raise ValueError("'start' cannot be greater than 'end': ({0}, {1})".format(start, end))
        
        if(self._memoized_m[start][end] < float("inf")):
            return self._memoized_m[start][end]

        if(start == end):
            self._memoized_m[start][end] = 0
        else:
            for k in range(start, end - 1):
                q = self.__call__(start, k)
                + self.__call__(k+1, end)
                + (self._dim_list[start-1] * self._dim_list[k] * self._dim_list[j])
                if(q < self._memoized_m[start][end]):
                    self._memoized_m[start][end] = q
        
        return self._memoized_m[start][end]
        

def matrix_chain_order(dim_list):

    return memoized_lookup_chain(dim_list)(0, len(dim_list) - 1)


print str(matrix_chain_order([10, 5, 20, 10, 40, 100]))