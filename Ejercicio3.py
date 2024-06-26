import sys

n = int(input().strip())

sequence = [0] * n

print("Q", " ".join(map(str, sequence)))
sys.stdout.flush()
correct_bits = int(input().strip())

for i in range(n):
    sequence[i] = 1
    
    print("Q", " ".join(map(str, sequence)))
    sys.stdout.flush()
    new_correct_bits = int(input().strip())
    
    if new_correct_bits <= correct_bits:
        sequence[i] = 0
    else:
        correct_bits = new_correct_bits

print("A", " ".join(map(str, sequence)))
sys.stdout.flush()
