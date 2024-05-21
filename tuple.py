#e.g coordinates

coordinates = (4,5)

#immutable!!!! cannot be changed/modified

print(coordinates[0]) #accessed by index

#practical for data that's never going to change

#lists of tuples

coordinates2 = [(4,5), (6,7)]
coordinates2[0] = (6,7)
print(coordinates2)
coordinates2[0][0] = 4