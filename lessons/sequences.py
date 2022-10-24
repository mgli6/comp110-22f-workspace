"""Notes and examples of tuple and range rsequence types."""

# Declaring a type alias that "invents" the Point2D type

Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10.0)
start_position = (start_position[0] + 5.0, start_position[1] + 10.0)

print(start_position)

# Examples of ranges
a_range: range = range(0, 10, 1)
# Access its items
print(a_range[0])
print(len(a_range))
for i in a_range:
    print(i)

# An example of using the default parameter step
# where the default step is 1
another_range: range = range(0, 10)

# If only 1 argument is passed to a range, it specifies
# the stop marker, and start is 0 by default
zero_start: range = range(10)
for x in zero_start:
    print(x)


names: list[str] = ["Dogger", "Bengal", "Max", "Ya boi"]

for name in names:
    print(name)

# Range is often used to write for loops where
# your iteration pattern is not consecutive
for i in range(0, len(names), 2):
    print(names[i])