try:
    file_1 = open('sample.txt', 'r')   
    reading = file_1.read()
    print('Reading file content: \n', reading)
    file_1.close()
except FileNotFoundError:
    print("error : the file 'sample.txt' was not found.")
