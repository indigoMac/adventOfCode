from collections import defaultdict, deque

def extract_data():
    rules = []
    updates = []
    
    with open('day_5/input.txt', 'r') as file:
        for lines in file:
            if '|' in lines:
                nums = lines.strip('\n').split('|')
                rules.append([int(num) for num in nums])
            elif ',' in lines:
                nums = lines.strip('\n').split(',')
                updates.append([int(num) for num in nums])
    return rules, updates


def build_graph(rules):
    """
    Build an adjacency list representation of the rules.
    """
    graph = defaultdict(list)
    for x, y in rules:
        graph[x].append(y)
    return graph


def is_valid_topological_order(graph, update):
    """
    Check if the given update follows a valid topological order
    for the subgraph induced by the pages in the update.
    """
    relevant_nodes = set(update)
    filtered_graph = {node: [neighbor for neighbor in neighbors if neighbor in relevant_nodes]
                      for node, neighbors in graph.items() if node in relevant_nodes}

    in_degree = defaultdict(int)
    for neighbors in filtered_graph.values():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    queue = deque([node for node in update if in_degree[node] == 0])
    for page in update:
        if not queue or queue[0] != page:
            return False
        current = queue.popleft()
        for neighbor in filtered_graph.get(current, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return True


def reorder_update(graph, update):
    """
    Reorder an incorrect update based on topological sorting of the graph.
    """
    relevant_nodes = set(update)
    filtered_graph = {node: [neighbor for neighbor in neighbors if neighbor in relevant_nodes]
                      for node, neighbors in graph.items() if node in relevant_nodes}

    in_degree = defaultdict(int)
    for neighbors in filtered_graph.values():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    # Perform topological sorting
    queue = deque([node for node in relevant_nodes if in_degree[node] == 0])
    sorted_update = []

    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in filtered_graph.get(current, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


def find_middle_pages(updates):
    """
    Find the middle pages of the updates.
    """
    return [update[len(update) // 2] for update in updates if update]


if __name__ == "__main__":
    rules, updates = extract_data()
    graph = build_graph(rules)

    valid_updates = []
    invalid_updates = []

    for update in updates:
        if is_valid_topological_order(graph, update):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    # Reorder the invalid updates
    reordered_updates = [reorder_update(graph, update) for update in invalid_updates]

    # Find middle pages and compute their sum
    middle_pages = find_middle_pages(reordered_updates)
    result = sum(middle_pages)

    print(f"Reordered Updates: {reordered_updates}")
    print(f"Middle Pages: {middle_pages}")
    print(f"Result: {result}")
