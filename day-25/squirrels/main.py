import pandas


def main():
    data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260215.csv")
    squirrel_primary_colors = data["Primary Fur Color"]

    color_dict = {
        "Primary Fur Color": [],
        "Count": []
    }

    for color in squirrel_primary_colors:
        if pandas.isna(color):
            continue

        if color not in color_dict["Primary Fur Color"]:
            color_dict["Primary Fur Color"].append(color)
            color_dict["Count"].append(0)

        i = color_dict["Primary Fur Color"].index(color)
        color_dict["Count"][i] += 1

    print(color_dict)

    df = pandas.DataFrame(color_dict)
    print(df)

    df.to_csv("squirrel_count.csv")

if __name__ == "__main__":
    main()
