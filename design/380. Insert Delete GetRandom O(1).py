# Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        if val in self.pos:
            idx = self.pos[val]  # get val index in list
            last = self.nums[-1]  # get the last addition
            self.nums[idx] = last  # overwrite val index with last addition
            self.pos[last] = idx  # update the last addition's index to it's new spot
            self.nums.pop()  # get rid of the last addition from it's original spot...it now has a new home elsewhere
            del self.pos[
                val]  # original line was "self.pos.pop(val, 0)". we don't need pop-or-default semantics here, del will work
            return True
        return False

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]
