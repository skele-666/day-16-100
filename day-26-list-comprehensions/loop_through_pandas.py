import pandas

# Pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Key gives titles of columns values gives column data in order
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

    print(index)
    print(row)

# {new_key:new_value for (key, value) in dict.items)}
# For pandas:
# {new_key:new_value for (key, value) in data_frame.iterrows()}