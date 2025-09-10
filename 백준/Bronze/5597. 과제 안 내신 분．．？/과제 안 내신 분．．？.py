students = set(range(1, 31))
submitted = {int(input()) for _ in range(28)}
not_submitted = sorted(students - submitted)

print(not_submitted[0])
print(not_submitted[1])
