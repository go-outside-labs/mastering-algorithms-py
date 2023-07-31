#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

import random

class RandomizedSet:

    def __init__(self):
        self.set = []
        self.dict = {}
        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.set.append(val)
        self.dict[val] = len(self.set)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element, idx = self.set[-1], self.dict[val]
            self.set[idx], self.dict[last_element] = last_element, idx
            self.set.pop()
            del self.dict[val]
            return True
        return False
        
    def get_random(self) -> int:
        return random.choice(self.set)
  
