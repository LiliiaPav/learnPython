text = 'Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked if Peter Piper picked a peck of pickled peppers Where is the peck of pickled peppers Peter Piper picked'
text = text.lower().split()
result = {}
for w in text:
    if w in result:
        result[w] += 1
    else:
        result[w] = 1
print(result)
