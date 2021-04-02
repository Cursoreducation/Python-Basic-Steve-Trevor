# input as flat text
a = {"Type": "A", "field1": "value1", "field2": "value2", "field3": "value3"}
# the same input can also be read from a file
a = open('file.txt', 'r')
# returns a printable representation of the input;
# the output can be written to a file as well
print(repr(a))
# write content to files using repr
with open('file.txt', 'w') as f:
    f.write(repr(a))
