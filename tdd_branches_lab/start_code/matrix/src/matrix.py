class Matrix:
    def __init__(self, matrix_string):
        if "\n" in matrix_string:
            self.matrix_list = [[int(char) for char in row.split()] for row in matrix_string.split("\n")]
        else:
            self.matrix_list = [int(item) for item in matrix_string.split()]
        
    def row(self, index):
        if len(self.matrix_list) > 1:
            return self.matrix_list[index -1]
        return self.matrix_list
    
    def column(self, index):
        output = []
        if len(self.matrix_list) > 1:
            for row in self.matrix_list:
                output.append(row[index-1])
        else:
            output.append(self.matrix_list[index-1])
        return output

