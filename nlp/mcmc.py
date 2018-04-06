"""
This is a Markov Chain class. 
Given a list of numbers (encoded text) calculates the invariant using bigram frequencies
"""
import numpy as np
import nltk
from tqdm import tqdm

class MCMC:

    def __init__(self, text):
        self.text = text
        # assumes text is a list of numbers 1, ..., length of vocab
        self.vocab = np.unique(text)
        self.bigrams = list(nltk.bigrams(text)) 
        
    def propose_state(self):
            return np.random.choice(self.vocab)
    
    def acceptance_probability(self, current_state, proposed_state):
        numer = len(list(filter(lambda x: x[0]==current_state and x[1]==proposed_state, self.bigrams)))
        denom = len(list(filter(lambda x: x[0]==current_state, self.bigrams)))
        return numer/denom
    
    
    def estimate_invariant(self, num_iters =  10000):
        current_state = self.propose_state()
        freq_dict = {current_state:1}
        
        for _ in tqdm(range(num_iters)):
            proposed_state = self.propose_state()
            p = self.acceptance_probability(current_state, proposed_state)
            
            if np.random.uniform() < p:
                current_state = proposed_state
              
            if current_state not in freq_dict.keys():
                freq_dict[current_state] = 1
            else:
                freq_dict[current_state] += 1
          
        total_count = sum(freq_dict.values())
        for i in freq_dict.keys():
            freq_dict[i] = freq_dict[i]/total_count
        
                
        return freq_dict 



