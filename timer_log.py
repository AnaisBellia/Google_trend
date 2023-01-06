import matplotlib as plt
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
import time
from collections import Counter

# TIMER LOG

# decorator
# Implement a decorator that logs execution time
def log_time(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        #return result
        print("time :" , end-start)
    return wrapper


@log_time
def count_words(file_path):
    # Load text file
    with open(file_path, 'r') as f:
        text = f.read()
        # Count the number of appearances of each word in the text and store it in a dictionary
        words = text.split()
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    # Convert the dictionary to a pandas dataframe
        df = pd.DataFrame.from_dict(word_counts, orient='index', columns=['count'])
        df = df.sort_values(by='count', ascending=False)
        print(df.head(10))

count_words("shakespear.txt")


@log_time
def counter_function(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        Counter(content.split())
    print(Counter(content.split()))

counter_function("shakespear.txt")