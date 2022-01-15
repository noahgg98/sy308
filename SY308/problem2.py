import sys


def file_read(fn):
    
    #open file and read from file
    with open(fn, 'r') as f:
        for lines in f.readlines():
            try:
                int(lines[2:5]) 
                if lines[0:2] == 'SY':
                    print(lines)

            except:
                None



if __name__=='__main__':
    file_read(sys.argv[1])