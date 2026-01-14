import pandas as pd
import math


data = {
    'Furniture': ['No', 'Yes', 'No', 'No', 'Yes'],
    'Rooms': [3, 3, 4, 3, 4],
    'NewKitchen': ['Yes', 'No', 'No', 'No', 'No'],
    'Acceptable': ['Yes', 'No', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)
TARGET = 'Acceptable'

# -------------------------
# Entropy
# -------------------------
def entropy(data):
    ent = 0
    for count in data[TARGET].value_counts():
        p = count / len(data)
        ent -= p * math.log2(p)
    return ent

# -------------------------
# Information Gain
# -------------------------
def information_gain(data, attr):
    parent_entropy = entropy(data)
    weighted_entropy = 0

    for value in data[attr].unique():
        subset = data[data[attr] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)

    return parent_entropy - weighted_entropy

# -------------------------
# Build ID3 Tree
# -------------------------
def build_tree(data, attributes):
    if len(data[TARGET].unique()) == 1:
        return data[TARGET].iloc[0]

    if not attributes:
        return data[TARGET].mode()[0]

    best_attr = max(attributes, key=lambda a: information_gain(data, a))
    tree = {best_attr: {}}

    remaining_attrs = [a for a in attributes if a != best_attr]

    for value in data[best_attr].unique():
        subset = data[data[best_attr] == value]
        tree[best_attr][value] = build_tree(subset, remaining_attrs)

    return tree

# -------------------------
# Print Single-Line Rules
# -------------------------
def print_rules(tree, rule=""):
    if not isinstance(tree, dict):
        print(f"IF {rule} THEN Acceptable = {tree}")
        return

    for attr, branches in tree.items():
        for value, subtree in branches.items():
            new_rule = f"{rule}{attr} = {value} AND "
            print_rules(subtree, new_rule)

# -------------------------
# Run
# -------------------------
attributes = ['Furniture', 'Rooms', 'NewKitchen']
tree = build_tree(df, attributes)


print_rules(tree)
