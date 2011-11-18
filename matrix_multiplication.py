
class memoized_lookup_chain:

    def __init__(self, dim_list):

        n = len(dim_list)
        self._memoized_m = [[float("inf") for j in range(n)] for i in range(n)]
        self._optimum_indices = [[-1 for j in range(n)] for i in range(n)]
        self._dim_list = dim_list

    def __call__(self, start, end):

        if(start > end):
            raise ValueError("'start' cannot be greater than 'end': ({0}, {1})".format(start, end))
        
        if(self._memoized_m[start][end] < float("inf")):
            return self._memoized_m[start][end]

        if(start == end):
            self._memoized_m[start][end] = 0
        else:
            for k in range(start, end):
                q = self(start, k) + self(k+1, end) + (self._dim_list[start-1] * self._dim_list[k] * self._dim_list[end])
                if(q < self._memoized_m[start][end]):
                    self._memoized_m[start][end] = q
                    self._optimum_indices[start][end] = k
        
        return self._memoized_m[start][end]
        

def matrix_chain_order(dim_list):

    lc = memoized_lookup_chain(dim_list)
    result = lc(1, len(dim_list)-1)

    print str(lc._optimum_indices)
    return result


print str(matrix_chain_order([41, 69, 12, 30, 88, 38, 51, 66]))
