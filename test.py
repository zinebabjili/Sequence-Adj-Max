import pandas as pd


# struct node of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

    def getSize(self, value):
        relR, relD, rel = 0, 0, 0

        if self.right is not None:
            relR = self.right.getSize(value + 1)
        if self.down is not None:
            relD = self.down.getSize(value + 1)
        rel = max(relR, relD)

        return max(value, rel)

    def getPath(self, path):
        longestR, longestD = "", ""
        if path == "":
            path = "" + str(self.data)

        if self.right is not None:
            longestR = self.right.getPath(path + "-" + str(self.right.data))
        if self.down is not None:
            longestD = self.down.getPath(path + "-" + str(self.down.data))
        if len(longestD) > len(longestR):
            longestR = longestD
        else:
            longestR = longestR
        if len(longestR) > len(path):
            return longestR
        else:
            return path


# Driver Code
if __name__ == '__main__':
    url = 'https://drive.google.com/file/d/1DlcPgs7Vdl3zN8cUyeztky7wr0RnlWpF/view'
    file_id = url.split('/')[-2]
    dwn_url = 'https://drive.google.com/uc?id=' + file_id
    df = pd.read_csv(dwn_url, header=None)
    size = len(df.axes[0])

    # matrix of type nodes initialized by 0
    matrix_nodes = [[Node(0) for i in range(size)] for j in range(size)]

    # Fill the nodes's matrix from csv file
    for i in range(size):
        for j in range(size):
            matrix_nodes[i][j] = Node(df[i][j])

    for i in range(size):
        for j in range(size):
            if j + 1 < size and abs(matrix_nodes[i][j].data - matrix_nodes[i][j + 1].data) == 1:
                matrix_nodes[i][j].right = matrix_nodes[i][j + 1]
            else:
                matrix_nodes[i][j].right = None

            if i + 1 < size and abs(matrix_nodes[i][j].data - matrix_nodes[i + 1][j].data) == 1:
                matrix_nodes[i][j].down = matrix_nodes[i + 1][j]
            else:
                matrix_nodes[i][j].down = None

    # Get the node with the longest sequence
    maxNode = Node(matrix_nodes[0][0].data)
    maxLength = matrix_nodes[0][0].getSize(0)
    for i in range(size):
        for j in range(size):
            if matrix_nodes[i][j].getSize(0) > maxLength:
                maxNode = matrix_nodes[i][j]

    print(maxNode.getSize(0))
    print(maxNode.getPath(""))
