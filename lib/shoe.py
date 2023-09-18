#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size):
        self.brand = brand

        if not isinstance(size, int):
            print("size must be an integer")
            self.size = None
        else:
            self.size = size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

