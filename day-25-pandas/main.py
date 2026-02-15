import csv, pandas


def main():
    # with open("./weather_data.csv", "r") as f:
    #     data = [line.strip() for line in f]
    # print(data)

    # Using csv library
    with open("./weather_data.csv", "r") as f:
        data = csv.reader(f)  # Creates csv reader obj
        temperatures = []
        for row in data:
            if row[1] != "temp":
                temperatures.append(int(row[1]))
    # print(data)
    # print(temperatures)

    # Using pandas library
    data = pandas.read_csv("./weather_data.csv")
    # print(data) # So much nicer!
    # print("\n")
    # print(data["temp"])
    # print(type(data)) # DataFrame
    # print(type(data["temp"])) # Series
    #
    # data_dict = data.to_dict()
    # print(data_dict)
    #
    # temp_list = data["temp"].to_list()
    # print(temp_list)
    #
    #
    # # Calculate avg temperature
    # avg_temp = sum(temp_list)/len(temp_list)
    # print(avg_temp)
    #
    # # OR
    # print(data["temp"].mean())
    #
    # # Get max value
    # print(data["temp"].max())
    #
    # # Get data in columns
    # print(data["condition"])
    # print(data.condition)

    # Get data in rows
    # print(data[data.day == "Monday"])
    # print(data[data.temp == data.temp.max()])

    monday = data[data.day == "Monday"]
    print(monday.condition)

    # Get Monday's temperature and convert Fahrenheit
    print(monday.temp)
    print((monday.temp[0] * 9 / 5) + 32)

    # Create dataframe from scratch
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }

    data = pandas.DataFrame(data_dict)

    # Convert to csv
    data.to_csv("new_data.csv")


if __name__ == "__main__":
    main()
