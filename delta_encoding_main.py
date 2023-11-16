import utils.DatasetsConstants as constants
from lossless_data_compression import delta_encoding
import lossless_data_compression.delta_encoding_string as delta_encoding_str
import os
import utils.file_operations as file_operations
from datetime import datetime
import time
import csv

file_path = os.getcwd() + constants.TIMESERIES_IOT_TEMP_PATH

columns = [[] for _ in range(len(next(csv.reader(open(file_path)))))]
new_columns = [[] for _ in range(len(next(csv.reader(open(file_path)))))]

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for i, value in enumerate(row):
            if i == 2:
                columns[i].append(int(time.mktime(datetime.strptime(value, "%d-%m-%Y %H:%M").timetuple())))
            else:
                if isinstance(value, (int, float)):
                    columns[i].append(float(value))
                else:
                    columns[i].append(str(value))
              
start_time = time.time()

for i, column in enumerate(columns):
    if isinstance(column[0], (int, float)):
        new_columns[i] = delta_encoding.delta_encode(column)
    else:
        new_columns[i] = delta_encoding_str.delta_encode_strings(column)
    

end_time = time.time()
elapsed_time = (end_time - start_time) * 1000

output_path = os.getcwd() + "/output/output.csv"
with open(output_path, 'w', newline='') as file:
    writer = csv.writer(file, escapechar='\\')
    writer.writerows(new_columns)

size_diff, percentage_diff = file_operations.compare_file_sizes(file_path, output_path)
print("The algorythms took", elapsed_time, "to obtain", size_diff, "corresponding to ", (100 - percentage_diff), "%")
