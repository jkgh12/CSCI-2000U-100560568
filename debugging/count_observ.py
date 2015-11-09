'''Count the number of observations in each group. Each observation
is on a separate line, and groups are separated by blank line.'''

def count_observations(lines):
    counts = []
    current = 0
    for line in lines:
        line = line.strip()
        if line == '':
            counts.append(current)
            current = 0
        else:
            current += 1
    return counts

data = ['a single line\n']
assert count_observations(data) == [1], 'single line failed'

data = ['two\n', 'lines\n']
assert count_observations(data) == [2], 'two lines failed'

data = ['two\n', '\n', 'records\n']
assert count_observations(data) == [1, 1], 'two records failed'
