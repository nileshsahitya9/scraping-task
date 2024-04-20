class Cache:
  def __init__(self):
    self.cache = {}
    
  def check_cache(self, key, value):
    if key in self.cache and self.cache[key] == value:
      return True
    else:
      self.cache[key] = value
      return False