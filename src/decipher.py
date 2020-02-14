import collections
import math

from reader import Reader
import matplotlib.pyplot as plt

"""
In the 5) for the method decipher, replace this line:

"If the key is found in the 2nd file, then it means that its deciphed value is ”e”"

by this line:

"If the key is found in the 2nd file, then it means that its deciphed value is ”z”"
"""


class Decipher(Reader):
    def __init__(self, file1, file2, chosen_str):
        # initialize the super constructor with file 1
        super().__init__(file1)

        self.file2 = file2
        self.chosen_str = chosen_str

        # file, dict, hist, ordered, coded, deciphed, entropy and
        # format

        self.file = ""
        self.dict = {}

        self.hist = []
        self.ordered = []

        # file2 contents
        # it can be changed to opened second file ie file2 given as input.
        # self.coded = open(file2, 'r')
        self.coded = super().read_file(self.file2)

        # empty string
        self.deciphed = ""

        self.entropy = ""

        # str with ”txt” or ”csv” as values
        self.format = "txt"

    # fills hist with the frequency of each letter in the
    # alphabetical order
    def create_hist(self):
        # get the content of file from Reader
        all_symbol = self.create_dict()

        # list of tuple symbol
        # sorted in alphabetical order
        tuple_symbol = all_symbol.items()
        list_of_tuples = sorted(tuple_symbol, key=lambda x: x[0])

        # By iterating assign value to hist
        for character in list_of_tuples:
            self.hist.append(character[1])

    # plots a pie chart of hist with the library of your choice
    def plot_pie(self):
        plt.pie(self.hist)
        plt.show()

    # plots an histogram of hist with the library of your choice
    def plot_hist(self):
        plt.hist(self.hist, bins=10)
        plt.show()

    # fills ordered with every letter in the alphabet, by order
    # of frequency
    def create_ordered(self):
        # get the content of file from Reader
        all_symbol = self.create_dict()

        # list of tuple symbol
        # sorted in order of values
        tuple_symbol = all_symbol.items()
        list_of_tuples = sorted(tuple_symbol, key=lambda x: x[1])

        # By iterating assign value to hist
        for character in list_of_tuples:
            self.ordered.append(character[0])

    def decipher(self):
        all_characters = self.dict

        # sort the content
        sorted_dict = sorted(all_characters, reverse=True, key=lambda x: x[1])

        # get the highest frequency word
        key = sorted_dict[0][0]

    # returns the entropy of the 1st file
    # determines the randomness of the file
    def compute_entropy(self):
        e = 0

        # get the file data
        data = self.create_dict()
        counter = collections.Counter(data)

        # total number of characters
        total_length = sum(data.values())

        for count in counter.values():
            # count is always > 0
            p_x = count / total_length
            e += - p_x * math.log2(p_x)

        return e

    # write the deciphed code in a .txt file or a .csv file,
    # depending of the value of format. If in a csv format, each word should
    # take one column.
    def write_code(self):
        # open file in write mode and
        # if file does not exist then create it
        decipher_content = open('./resources/decoded.csv', 'w+')

        for i in self.deciphed:
            # write to the file line by line
            decipher_content.write(i + "\r\n")

        decipher_content.close()

        return True


if __name__ == "__main__":
    print("Decipher")

    decipher = Decipher('./resources/text1', './resources/text2', "abc")

    decipher.creat_dict()
    decipher.create_hist()
    decipher.plot_hist()
    decipher.plot_pie()