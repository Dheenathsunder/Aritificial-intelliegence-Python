def forward_chaining(rules, facts):
    inferred = set(facts)
    while True:
        new_inferred = set()
        for antecedent, consequent in rules:
            if all(fact in inferred for fact in antecedent):
                new_inferred.add(consequent)
        if not new_inferred.difference(inferred):
            break
        inferred.update(new_inferred)
    return inferred

# Example usage
rules = [
    (('A', 'B'), 'C'),
    (('C',), 'D'),
    (('D',), 'E'),
]

facts = {'A', 'B'}

result = forward_chaining(rules, facts)
print("Inferred facts:", result)
