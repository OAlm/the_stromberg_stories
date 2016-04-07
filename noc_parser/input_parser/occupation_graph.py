__author__ = 'alm'

from datasets_pattern_code import noc
import networkx as nx


class Occupation:

    NOC_LIST_OCCUPATION_FILE = "../Veale's NOC List/Veale's category hierarchy.xlsx"

    def __init__(self):
        self.g = nx.Graph()

    def generate_occupation_graph(self):
        for row in noc.parse_rows(self.NOC_LIST_OCCUPATION_FILE):
            for key in row.keys():
                print key





if __name__ == "__main__":

    o = Occupation()
    o.generate_occupation_graph()