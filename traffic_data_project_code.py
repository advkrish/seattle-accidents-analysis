import csv
import matplotlib.pyplot as plt

def sort(lists):
        for i in range(len(lists) - 1, 0, -1):
            for j in range(i):
                if lists[j][1] < lists[j + 1][1]: 
                    lists[j], lists[j + 1] = lists[j + 1], lists[j]
        return lists

def plot_data(y):
    data_file_path ="/Users/advikk/Documents/sea_accidents.csv"
    values = []
    
    with open(data_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            values.append(row['LOCATION'])
    
    count_values = {}
    for value in values:
        count_values[value] = count_values.get(value, 0) + 1
    
    items = list(count_values.items())
    sorted_items = sort(items)
    
    if y > len(sorted_items):
        loop_count = len(sorted_items)
    else:
        loop_count = y
    
    
    locations = []
    counts = []
    for i in range(loop_count):
        value, count = sorted_items[i]
        if value != '':  
            locations.append(value)
            counts.append(count)
    
    plt.figure(figsize=(12, 8))
    plt.bar(locations, counts)
    plt.title(f'Top {loop_count} Accident Locations')
    plt.xlabel('Location')
    plt.ylabel('Number of Accidents')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.subplots_adjust(bottom=0.710)
    plt.show()

plot_data(10)


# def top_y_column_values(column_name, y):
#     data_file_path = "/Users/advikk/Documents/sea_accidents.csv"
#     values = []

#     with open(data_file_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             values.append(row[column_name])

#     count_values = {}
#     for value in values:
#         count_values[value] = count_values.get(value, 0) + 1

#     items = list(count_values.items())
#     sorted_items = sort(items)

#     if y > len(sorted_items):
#         loop_count = len(sorted_items)
#     else:
#         loop_count = y

#     for i in range(loop_count+1):
#         value, count = sorted_items[i]
#         if value != '':
#             print(value, ":", count, "times found")

# def count_exact_matches(column1, value1, column2, value2, column3, value3):
#     data_file_path = "/Users/advikk/Documents/sea_accidents.csv"
#     count = 0

#     with open(data_file_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if (row[column1] == value1 and 
#                 row[column2] == value2 and 
#                 row[column3] == value3):
#                 count = count+1

#     print("Found", count, "occurrences where:")
#     print(column1 , ":", value1)
#     print(column2 , ":", value2)
#     print(column3 , ":", value3)

# if __name__ == "__main__":
#     data_file_path = "/Users/advikk/Documents/sea_accidents.csv"

#     with open(data_file_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         print("columns:")
#         for column in reader.fieldnames:
#             print(column)
#         print("\nEnter three column names to search in that are comma seperated:")
#         print("Example: WEATHER,ROADCOND,LIGHTCOND")
        
#     columns = input().split(',')
#     if len(columns) == 3:
#         print("Now enter the values for each :")
#         print("Example: Rain,Wet,Day")
#         values = input().split(',')
#         if len(values) == 3:
#             count_exact_matches(columns[0], values[0], columns[1], values[1], columns[2], values[2])

