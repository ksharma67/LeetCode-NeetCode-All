class RandomizedSet:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.val_to_index = {}  # Hash table to store values and their indices in the array
    self.vals = []          # Array to store the actual values

  def insert(self, val: int) -> bool:
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    """
    if val in self.val_to_index:    # If the value already exists in the hash table, return false
        return False
    self.val_to_index[val] = len(self.vals)    # Add the value to the hash table with its index in the array
    self.vals.append(val)           # Append the value to the end of the array
    return True                     # Return true to indicate success

  def remove(self, val: int) -> bool:
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    """
    if val not in self.val_to_index:    # If the value does not exist in the hash table, return false
        return False
    index = self.val_to_index[val]      # Get the index of the value in the array
    last_val = self.vals[-1]            # Get the last value in the array
    self.vals[index] = last_val         # Swap the value at the index with the last value in the array
    self.val_to_index[last_val] = index # Update the index of the last value in the hash table
    self.vals.pop()                     # Remove the last value from the array
    del self.val_to_index[val]           # Remove the removed value from the hash table
    return True                          # Return true to indicate success

  def getRandom(self) -> int:
    """
    Get a random element from the set.
    """
    return random.choice(self.vals)     # Return a random value from the array      

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
