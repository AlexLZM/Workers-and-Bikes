
def find_min_sum(workers, bikes):
    # use bitmask to represent a selection of bikes, in each digit,  0 is not used, 1 is used
    n = len(workers)
    m = len(bikes)

    # memo[mask] is the min sum we can get with those bikes used, indicated by mask
    memo = [float('inf')] * (1 << m) # indexed from 0 to 11111111...111 (m of ones)


    min_dis = float('inf') # final answer, we will update it

    def distance(worker, bike):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])


    def count_1_in_mask(mask):
        count = 0
        while mask > 0:
            mask &= (mask - 1)
            count += 1
        return count

    memo[0] = 0 # we get 0 sum using 0 bikes
    for mask in range(1 << m):

        worker_i = count_1_in_mask(mask) # we are doing sequantial assgnment for workers
        if worker_i >= n:
            min_dis = min(memo[mask], min_dis) # all workers has a bike now, update min_dis
            continue
        # try all unused bikes
        for bike_i in range(m):
            if mask & (1 << bike_i) == 0: # find a unused bike
                new_mask = mask | (1 << bike_i) # find new mask with the bike used
                memo[new_mask] = min(memo[new_mask], memo[mask] + distance(tuple(workers[worker_i]), tuple(bikes[bike_i])))
    return min_dis
        
    
