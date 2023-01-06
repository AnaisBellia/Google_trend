import matplotlib as plt
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
import time
from collections import Counter
import numpy as np

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

#count_words("shakespear.txt")


@log_time
def counter_function(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        Counter(content.split())
    print(Counter(content.split()).most_common(10))

#counter_function("shakespear.txt")


# experiment 100 times

def experiment(file_path):
    for i in range(2):
        dictionary = []
        counter = []

        dict = count_words(file_path)
        count =counter_function(file_path)

        dictionary.append(float(dict))
        counter.append(float(count))

        i = i+1

    print("dictionnary mean", np.mean(dict))
    print("counter mean ",np.mean(count))


    fig,axs = plt.subplots(2)
    axs[0].plot(dict)
    axs[1].plot(count)
    plt.show()

if __name__ == "__main__":

    experiment('shakespear.txt')