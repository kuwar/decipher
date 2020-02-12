class Reader:
    """
    Read the content of the file. One argument is required - the path to file
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.dict = {}

    def create_dict(self):
        """
        Create dictionary of file character. Key is the character of the file and value is its frequency
        :return:
        """

        # open file to read
        file_contents = open(self.file_path, "r")

        # read the content of file as string
        text_in_file = self.read_file(self.file_path)

        # make a dictionary of character frequency
        self.dict = self.frequency(text_in_file)

        # close the file
        file_contents.close()
        return self.dict

    def frequency(self, text):
        """
        use Counter from collection to count the characters
        Also we can iterate over the text to count frequency of characters
        :param text:
        :return:
        """
        from collections import Counter
        # char_frequency = Counter(text)

        char_frequency = {}

        for char in text:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

        return char_frequency

    def read_file(self, file_path):
        """
        Read the given file as string
        :param file_path:
        :return:
        """
        # open file to read
        file_contents = open(file_path, "r")

        # read the content of file as string
        text_in_file = file_contents.read()

        return text_in_file


if __name__ == "__main__":

    reader = Reader('./text1')
    print(reader.create_dict().keys())
    print(reader.create_dict().values())

    file_contents = reader.create_dict()

    # print(file_contents.items())
    for elem in sorted(file_contents.items(), reverse=True, key=lambda x: x[1]):
        print(elem[0], elem[1])
