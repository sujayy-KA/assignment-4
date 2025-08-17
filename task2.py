file_1=open('sample.txt','w')
file_writing=input('enter text to write in file: ')
file_1.write(file_writing + '\n')
print('data written to file successfully to sample.txt')
file_1.close()

file_1=open('sample.txt', 'a')
file_appending=input('enter text to append in file: ')
file_1.write(file_appending)
print('data appended to file successfully to sample.txt')
file_1.close()

file_1=open('sample.txt', 'r')
reading=file_1.read()    
print('Reading file content: \n', reading)
file_1.close()

