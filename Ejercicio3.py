import sys

def interact_with_troll():
    n = int(input()) 
    current_sequence = ['0'] * n 
    
    while True:
        query = 'Q ' + ' '.join(current_sequence)
        print(query) 
        sys.stdout.flush()  
        
        response = int(input().strip())
        
        if response == n:
            answer = 'A ' + ' '.join(current_sequence)
            print(answer)  
            sys.stdout.flush()  
            break
        else:
            for i in range(n):
                current_sequence[i] = '1' if current_sequence[i] == '0' else '0'

interact_with_troll()