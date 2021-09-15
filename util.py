def graph_from_csv(filename):
    """Turn a CSV of child, parent, relation entries into a graph represented
    by a dictionary, for example:

    {'A': [('B', 'ab'), ('C', 'ac')],
     'B': [('C','bc'), ('D','bd')],
     'C': [('D','cd')],
     'D': [('C','dc')]}
"""
    rows = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)

        # Skip header row
        next(reader, None)

        for row in reader:
            rows.append(row)


    graph = dict()
    for row in rows:
        child, parent, relation = row
        if not parent in graph:
            graph[parent] = []
        graph[parent].append((child, relation))

    return graph