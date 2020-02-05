print("======= if..else =========")
a = True
b = True

if a:
	if b:
		print("if a and b")
	else:
		print("else a and b")
else:
	if b:
		print("else if b")
	else:
		print("else else b")

color = "abc"

if color == "red":
	print("red color")
elif color == "green":
	print("green color")
elif color == "blue":
	print("blue color")
else:
	print("Not heard of the color", color)

arr = []

if arr:
	print("something here")
else:
    print("empty array")

letter = 'o'

if letter == 'a' or letter == 'e' or letter == 'i' \
   or letter == 'o' or letter == 'u':
   print(letter, "is a vowel")
else:
   print(letter, "is not a vowel")

vowels = 'aeiou'
letter = 'c'

if letter in vowels:
	print(letter, "is a vowel")
else:
    print(letter, "is not a vowel")

print("======= while loop =========")
count = 1
while count <= 5:
	print(count)
	count += 1

print("====== for loop ==========")
x = 1
for x in range(1, 5):
	print(x)

print("======= hash =========")
hsh = {"a": "abc", "b": "xyz", True: "boolean"}
print(hsh)

print("======= function =========")
def do_nothing():
	print("do_nothing function called", x-3, "times")

do_nothing()

print("======= range =========")
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

for x in my_range(1, 10, 0.5):
    print(x)

print("======= for with range =========")
a = [1,2,3,4,5]
for x in a:
	print(x)
