import pandas as pd

file_name = input("Enter the name of the csv file")
chunk_size = int(input("Enter the number of rows in file"))
batch_no = 1

for chunk in pd.read_csv(file_name + '.csv', chunksize=chunk_size):
    chunk.to_csv('output_data' + str(batch_no) + '.csv', index=False)
    batch_no +=1
    
print('Done')

