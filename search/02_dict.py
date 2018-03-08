# -*- coding:utf-8 -*-
"""
字典为了保证速度，查找速度是采用三列实现的
"""

class HashTalbe(object):

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data

            else:
                nextslot = self.refresh(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.slots[nextslot] = data
                else:
                    self.data[nextslot] = data


    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.size))
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __str__(self):
        l = ['{']

        for index, item in enumerate(self.slots):
            if item != None:
                data = self.data[index]
                l.append('%s: %s, ' % (item, data))

        l.append('}')

        return ''.join(l)


if __name__ == '__main__':
    h = HashTalbe()
    h[54] = 'cat'
    h[26] = 'dog'

    print h
    print h[54]
    h[54] = 'yellow coke'
    print h[54]

    print h.data
    print h.slots





