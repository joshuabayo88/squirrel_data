import pandas

data = pandas.read_csv("Squirrel_Data.csv")

gray_squirrels_count = len(data[data.PrimaryFurColor == "Gray"])
cinnamon_squirrels_count = len(data[data.PrimaryFurColor == "Cinnamon"])
black_squirrels_count = len(data[data.PrimaryFurColor == "Black"])

print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

all_squirrels_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count],
}

squirrels_dataframe = pandas.DataFrame(all_squirrels_dict)
print(squirrels_dataframe)
squirrels_dataframe.to_csv("FurCount.csv")