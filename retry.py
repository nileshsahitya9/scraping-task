import time

def retry(func, max_attempts=3, delay=5):
  def wrapper(*args, **kwargs):
    attempt = 1
    while attempt <= max_attempts:
      try:
        return func(*args, **kwargs)
      except Exception as e:
        print(f"Attempt {attempt} failed. Retrying in {delay} seconds.", e)
        time.sleep(delay)
      attempt += 1
      print("Max attempts reached. Failed to execute function.")
      return None
  return wrapper