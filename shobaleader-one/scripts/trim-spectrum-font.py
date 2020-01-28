import pickle


def squash(sublist):
    return list(filter(lambda x: x != 0, sublist))


def slim(data):
    # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    slimmed = []
    rotated = list(zip(*data[::-1]))
    for row in rotated:
        if not list(row) == [0] * 8:
            slimmed.append(list(row))
    return list(map(list, list(zip(*slimmed[::-1]))))


full_font = pickle.load(open("fonts/spectrum/full-font.pickle", "rb"))
slim_font = {}

for key, data in full_font.items():
    if key == " ":
        continue
    print(f"Squashing {key}")
    slim_font[key] = slim(data)

# FIND AVERAGE WIDTH AND MAKE SPACE THAT WIDTH
top_rows = list(map(lambda x: x[0], slim_font.values()))
flattened = sum(top_rows, [])
count = len(flattened)
mean = round(count / len(slim_font.keys()))

slim_font[" "] = [[0] * mean] * 8

with open("fonts/spectrum/slim-font.pickle", "wb") as f:
    pickle.dump(slim_font, f)
