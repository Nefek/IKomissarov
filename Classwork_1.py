text = "Hello, Python!"
print (text[0])
print (text[0:5])
print (text[4:10])
print (text[0:14])
print (text[7:])
print (text[:5])
print (text[:])
print (text[-1])
print (text[-1:-14])
print (text[::2])
print (text[::-1])
print (text + "Nice to code you")
print (text[-1] * 10)

my_list = [True, 768, 3.14, "text", 70.2]
second_list = [123, "text"]
print (my_list)
print (my_list[0])
print (my_list[1:3])
print (my_list[2:])
print (second_list *2)
print (my_list + second_list)

my_tuple = (True, 768, 3.14, "text", 70.2)
second_tuple = (123, "text")
print (my_tuple)
print (my_tuple[0])
print (my_tuple *2)
print (my_tuple + second_tuple)

my_dict = {}
my_dict["country"] = "Mexico"
print (my_dict["country"])
another_dict = {"number":23, 2: True, "my_list":[1, 2, 3]}
print (another_dict.keys())
print (another_dict.values())

s = set()
print(s)
set()
s = {"hi", "bye"}
print (s)
{"hi", "bye"}
a = set()
a.add(1)
a.add(2)
print (a)
{1, 2}
a.add(2)
print (a)
{1, 2}
b = {2, 3}
a.difference(b)
{1}
b.difference(a)
{3}
a.intersection(b)
{2}



