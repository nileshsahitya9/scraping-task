import json

class DatabaseManager:
  def __init__(self, storage_strategy='json'):
    self.storage_strategy = storage_strategy

  def save_data(self, data):
    if self.storage_strategy == 'json':
      with open('scraped_data.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')