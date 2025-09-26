S = input().strip()
pos = [-1]*26
for i,ch in enumerate(S):
    idx = ord(ch)-97
    if pos[idx]==-1:
        pos[idx]=i
print(*pos)
