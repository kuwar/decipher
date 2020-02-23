import collections
import math

from reader import Reader
import matplotlib.pyplot as plt

MAX_SYMBOL_SIZE = 26


class Decipher(Reader):
    def __init__(self, file1, file2, file_extension):
        # initialize the super constructor with file 1
        super().__init__(file1)

        # call super function to make dict
        super().create_dict()

        # file location to decode the message
        self.file2 = file2

        self.hist = []
        self.hist_symbols = []
        self.ordered = []

        # file2 contents
        # it can be changed to opened second file ie file2 given as input.
        # self.coded = open(file2, 'r')
        self.coded = super().read_file(self.file2)

        # empty string
        self.deciphed = ""

        self.entropy = 0

        # str with ”txt” or ”csv” as values
        self.format = file_extension

    # fills hist with the frequency of each letter in the
    # alphabetical order
    def create_hist(self):
        # list of tuple symbol
        # sorted in alphabetical order
        tuple_symbol = self.dict.items()
        list_of_tuples = sorted(tuple_symbol, key=lambda x: x[0])

        # By iterating assign value to hist
        for character in list_of_tuples:
            self.hist.append(character[1])
            self.hist_symbols.append(character[0])
        return self.hist

    # plots a pie chart of hist with the library of your choice
    def plot_pie(self):
        plt.title("Frequency of each characters")
        labels = self.hist_symbols
        sizes = self.hist
        # fig, ax = plt.subplots()
        plt.pie(sizes, startangle=90, labels=labels, autopct='%1.1f%%')
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    # plots an histogram of hist with the library of your choice
    def plot_hist(self):
        plt.hist(self.hist, bins=10, label=self.hist_symbols)

        plt.title("Frequency of each characters")
        plt.ylabel("Frequency")
        plt.xlabel("Characters")
        plt.xticks(self.hist, self.hist_symbols)

        plt.show()

    # fills ordered with every letter in the alphabet, by order
    # of frequency
    def create_ordered(self):
        # list of tuple symbol
        tuple_symbol = self.dict.items()
        # sorted in order of values
        list_of_tuples = sorted(tuple_symbol, key=lambda x: x[1])

        # By iterating assign value to hist
        for character in list_of_tuples:
            self.ordered.append(character[0])

        return self.ordered

    def decipher(self):
        # sort the content
        sorted_dict = sorted(
            self.dict.items(), reverse=True, key=lambda x: x[1])

        # get the highest frequency word
        key_char, freq = sorted_dict[0]

        # -ve value here shows that it is decipher
        key = -(ord('z') - ord(key_char))

        for symbol in self.coded:
            if symbol.isalnum():
                num = ord(symbol)
                num += key

                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                self.deciphed += chr(num)
            else:
                self.deciphed += symbol
        return self.deciphed

    # returns the entropy of the 1st file
    # determines the randomness of the file
    def compute_entropy(self):
        counter = collections.Counter(self.dict)

        # total number of characters
        total_length = sum(self.dict.values())

        for count in counter.values():
            # count is always > 0
            p_x = count / total_length
            self.entropy += - p_x * math.log2(p_x)

        return self.entropy

    # write the deciphed code in a .txt file or a .csv file,
    # depending of the value of format. If in a csv format, each word should
    # take one column.
    def write_code(self):
        # open file in write mode and
        # if file does not exist then create it
        decipher_content = open('./decoded.csv', 'w+')

        for i in self.deciphed:
            # write to the file line by line
            decipher_content.write(i + "\r\n")

        decipher_content.close()

        return True


def output_formater(message):
    """
    Display message formater
    """
    print("###############################################################")
    print("#############", message, "############")
    print("###############################################################")


if __name__ == "__main__":
    output_formater("Decipher")

    # decipher instantiation
    decipher = Decipher('./text1', './text2', "txt")

    output_formater("Dictionary for character frequency")
    print(decipher.dict)

    decipher.create_hist()
    output_formater("Frequency of character alphabetically")
    print(decipher.hist)

    # display histogram
    decipher.plot_hist()
    # display piechart
    decipher.plot_pie()

    # ordered character ordered based on its frequency
    decipher.create_ordered()
    output_formater("Characters ordered on basis of frequency")
    print(decipher.ordered)

    # display entropy of file
    output_formater("Entropy")
    decipher.compute_entropy()
    print(decipher.entropy)

    # encrypt the cipher text
    output_formater("Decipher value")
    decipher.decipher()
    print(decipher.deciphed)

    # Write to file the decipher contents
    decipher.write_code()
