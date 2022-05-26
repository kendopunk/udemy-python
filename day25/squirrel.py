# 2018 Squirrel Data w/ pandas
import pandas as p

# shorter CSV file name
FILE = "squirrel_data.csv"
PFC = "Primary Fur Color"
ACCEPTABLE_COLORS = ['Gray', 'Cinnamon', 'Black']


def normalize_fur_color(color):
    if color == 'Gray':
        return 'grey'
    elif color == 'Cinnamon':
        return 'red'
    else:
        return color.lower()


# read the csv
df = p.read_csv(FILE)

# drop missing / null / NaN, etc from "Primary Fur Color" column
df.dropna(subset=[PFC], inplace=True)

# filter on acceptable colors
color_filter = df[PFC].isin(ACCEPTABLE_COLORS)
df = df[color_filter]

# apply the converter(s)
converters = {
    PFC: lambda x: normalize_fur_color(x)
}
df[PFC] = df[PFC].apply(converters[PFC])

# aggregate by color, change column names, convert to CSV
PFC = "Primary Fur Color"
agg_by_color = df.groupby(PFC).size().reset_index(name='Count')
agg_by_color.columns = ['Fur Color', 'Count']
agg_by_color.to_csv("squirrel_count_by_color.csv", index=False)
