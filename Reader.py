class Reader:
    def __init__(self, filename):
        self.libraries = []
        with open(filename, 'r') as f:
            first_line = f.readline().split()
            self.B = int(first_line[0])
            self.L = int(first_line[1])
            self.D = int(first_line[2])
            second_line = f.readline().split()
            self.scores = map(lambda x: int(x), second_line)
            for _ in range(self.B):
                try:
                    library = {}
                    tmp = f.readline().split()
                    first_line_l = map(lambda x: int(x), tmp)
                    library['signup'] = first_line_l[1]
                    library['canShip'] = first_line_l[2]
                    tmp = f.readline().split()
                    library['books'] = sorted(map(lambda x: int(x), tmp))
                    self.libraries.append(library)
                except:
                    pass

if __name__ == "__main__":
    Reader('testcases/example.txt')
