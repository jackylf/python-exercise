import pprint

message = "this is a good day, the weather is great!"
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] += 1

pprint.pprint(count)
