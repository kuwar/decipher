import re


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

        # read the content of file as string
        text_in_file = self.read_file(self.file_path)

        # remove sepcial characters
        text_in_file = self.get_alpha_only(text_in_file)

        # convert all text to lower case
        text_in_file = text_in_file.lower()

        # make a dictionary of character's frequency
        self.dict = self.frequency(text_in_file)

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

        # close the file
        file_contents.close()

        # remove the special characters and return content of file
        return text_in_file

    def get_alpha_only(self, mixed_string):
        """
        Get only characters ie abcd and numbers
        """
        return re.sub('[^A-Za-z0-9]+', '', mixed_string)


if __name__ == "__main__":

    reader = Reader('./text1')
    print(reader.create_dict().keys())
    print(reader.create_dict().values())

    file_contents = reader.create_dict()

    sorted_dict = sorted(file_contents.items(), reverse=True, key=lambda x: x[1])

    print(sorted_dict[0][0])

    # print(file_contents.items())
    for elem in sorted_dict:
        print(elem[0], elem[1])
