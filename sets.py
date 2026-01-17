# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Perform set operations
union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2
symmetric_diff_set = set1 ^ set2

# Display results
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (set1 - set2):", difference_set)
print("Symmetric Difference:", symmetric_diff_set)
