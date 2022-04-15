# main.py
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

# table = PrettyTable()
table = ColorTable(theme=Themes.DEFAULT)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'c'
# table.sortby = "Pokemon Name"
# table.border = False
print(table)
