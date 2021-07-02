'''
Grid implimentation.
'''
import numpy

class map:
    
    def __init__(self, height=5, width=5):
        self.grid = numpy.array([[empty_space() for _ in range(width)] for _ in range(height)])

    def __str__(self):
        output = ''
        for line in self.grid:
            for space in line:
                output += f'{space}'
            output += '\n'
        return output

class empty_space:

    def __init__(self):
        pass

    def __str__(self):
        return ' 0 '

def main():
    n = map()
    print(n)

if __name__ == '__main__':
    main()