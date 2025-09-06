# Vocabulary Builder
import json
import os
from collections import defaultdict

# Class for the vocabulary Builder
class VacabularyBuilder:
    def __init__(self):
        self.words_file = 'vocabulary.json'
        self.stats_file = 'vacabulary_stats.json'
        self.words = self.load_words()
        self.stats = self.load_stats()
        
    def load_words(self):
        if os.path.exists(self.words_file):
            with open(self.words_file, 'r') as f:
                return json.load(f)        
        return {}
    
    def load_stats(self):
        if os.path.exists(self.stats_file):
            with open(self.stats_file, 'r') as f:
                return json.load(f)
        return defaultdict(lambda: {"correct": 0, "attempt": 0})
    
    def save_words(self):
        with open(self.words_file, 'w') as f:
            json.dump(self.words, f, indent=2)
            
    def save_stats(self):
        with open(self.stats_file, 'w') as f:
            json.dump(dict(self.stats), f, indent=2)
    
    def add_word(self):
        pass