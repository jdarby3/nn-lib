# This import allows us to check the type of a file

from pathlib import Path


# 

class token():
    def __init__(self, token_str, token_id):
        self.token_str = token_str
        self.token_id = token_id


# Instructions on how to use the program

print("Upload .txt files. More files gives a more generalizable tokenization.")


# User defines the tokenizers vocab size, must be larger than 256 so we can cover all the ascii characters

while True:
    vocab_size = input("Vocab size: ")
    if type(vocab_size) == int and vocab_size > 256:
        break
    else:
        print("INVALID INPUT - Vocab size must be an integer larger than 256")



# This will store all of our data to be processed

samples = []


#

while True:
    print("When all files are uploaded type DONE")
    file_name = input("File path: ")

    if file_name == "DONE":
        break

    elif Path(file_name).suffix.lower() == ".txt":  
        print("FILE ACCEPTED")   
        with open(file_name, 'r') as f:
            samples.append(f.read())
    
    else: 
        print("INVALID INPUT - Files must .txt files")


num_files = len(samples)
num_chars = sum(len(i) for i in samples)


print(f'Number of input files: {num_files}')
print(f'Total number of characters given: {num_chars}')

# actual tokenization loop
# we need to iterate over the entire sample, as tokens, updated with the previous mint, every time we mint a token?


for sample in samples:
    for char in sample:
        
for i in range(vocab_size):
    