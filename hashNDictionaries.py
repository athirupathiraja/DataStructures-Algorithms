import math

MAX_HASH_TABLE_SIZE = 4096


def getHashingIndex(dataList, keyString):
    result = 0

    for aCharacter in keyString:
        # converting character to number using ord
        convertedNumber = ord(aCharacter)
        result += convertedNumber

    hashingIndex = result % len(dataList)
    return hashingIndex


def getValidHashingIndex(dataList, keyString):
    index = getHashingIndex(dataList, keyString)

    while True:
        kvPairAtIndex = dataList[index]

        # the return kvAtIndex is to be used to insert funciton the kv pair if the index is none
        if kvPairAtIndex is None:
            return index

        # this returns the index for find funciton if the kv pair is at the index specified
        (k, v) = kvPairAtIndex
        if k == keyString:
            return index

        # KV index is incremented if collision occurs, so the pair can be inserted into the next key in the data array
        index += 1

        # returns to the first inde if the kv pair index has reached the end of the datalist
        if index == len(dataList):
            index = 0


class HashTableWithProbing:
    def __init__(self, maxSize=MAX_HASH_TABLE_SIZE):
        self.dataList = [None] * maxSize

    def insert(self, key, value):
        index = getValidHashingIndex(self.dataList, key)
        self.dataList[index] = (key, value)

    def find(self, key):
        index = getValidHashingIndex(self.dataList, key)
        kv = self.dataList[index]

        if kv is not None:
            key, value = kv
            return value
        else:
            return None

    def update(self, key, value):
        index = getValidHashingIndex(self.dataList, key)
        self.dataList[index] = (key, value)

    def listAll(self):
        return [kv[0] for kv in self.dataList if kv is not None]
