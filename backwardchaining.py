def backward_chaining(rules, goal, facts):
    if goal in facts:
        return True
    for antecedent, consequent in rules:
        if consequent == goal:
            if all(backward_chaining(rules, fact, facts) for fact in antecedent):
                return True
    return False

# Example usage
rules = [
    (('A', 'B'), 'C'),
    (('C',), 'D'),
    (('D',), 'E'),
]

facts = {'A', 'B'}

goal = 'E'
result = backward_chaining(rules, goal, facts)
print(f"Can '{goal}' be inferred?", result)
