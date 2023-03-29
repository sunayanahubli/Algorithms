import networkx as nx
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
# import karateclub


def print_intro():
    print(
        '''These latent representations are used to represent the social representation b/w two graphs. It uses a randomized path traversing technique to provide insights into localized structures within networks. It does so by utilizing these random paths as sequences, that are then used to train a Skip-Gram Language Model.

Skip-Gram Model is used to predict the next word in the sentence by maximizing the co-occurrence probability among the words that appear within a window, w, in a sentence. For our implementation, we will use the Word2Vec implementation which uses the cosine distance to calculate the probability.
''')


def input_values():
    pass

def print_results():
    pass

def run_algorithm():
    pass
def execute():
    print_intro()
    input_values()
    run_algorithm()
    print_results()

