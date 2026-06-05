def print_twice3(bruce5):
    print(bruce5)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice3(cat)
    print_twice3(cat)

line1 = "Bing tiddle"
line2 = " Tiddle bang."
cat_twice(line1,line2)

# O resultado desse exemplo eh:
# Bing tiddle Tiddle bang.
# Bing tiddle Tiddle bang.