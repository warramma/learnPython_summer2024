#5-29-24

#2d lists and nested loops

#---print all numbers in 2d grid with nested loop

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in number_grid:
    for index in row:
        print(index)