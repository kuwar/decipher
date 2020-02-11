from reader import Reader


class Decipher(Reader):
    def __init__(self, file1, file2, chosen_str):
        super().__init__(file1)
        self.file2 = file2
        self.chosen_str = chosen_str

        self.file = ""
        self.dict = {}

        self.hist = []
        self.ordered = []

        # file2 contents
        self.coded = super().read_file(self.file2)

        self.deciphed = ""

        self.entropy = ""

        # str with ”txt” or ”csv” as values
        self.format = "txt"

    def create_dict(self):
        self.hist = list(super().dict)

    def create_hist(self):

    def plot_pie(self):

    def plot_hist(self):

    def create_ordered(self):

    def decipher(self):

    def compute_entropy(self):

    def write_code(self):
