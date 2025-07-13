import numpy as np

# eventually this will not live in this file
embedding_matrix = {

}

def embed_tokens_to_vectors(inputs = []):
    for i in inputs:
        if i in embedding_matrix.keys():
            continue
        else:
            embedding_matrix[i] = np.random.normal(-0.1, 0.1, size=50)

class Layer:
    def __init__(self, neurons, position):

        pass

a = np.tanh(2)
print(f"{a:.7f}")

embed_tokens_to_vectors([1, 2, 3])

print(embedding_matrix[1][5])
