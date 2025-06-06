def count_ones_turing(binary_string, debug=False):
    tape = list(binary_string) + ['_', '_', '_', '_', '_']
    head = 0
    state = 'SCAN'
    counter_start = len(binary_string) + 1
    
    while True:
        if debug:
            print(f"[{state}] HEAD={head}, TAPE={''.join(tape)}")
        
        if state == 'SCAN':
            if head < len(binary_string):
                if tape[head] == '1':
                    tape[head] = 'X'
                    state = 'ADD_COUNT'
                    head = counter_start
                elif tape[head] == '0' or tape[head] == 'X':
                    head += 1
                else:
                    head += 1
            else:
                state = 'DONE'
                break
                
        elif state == 'ADD_COUNT':
            while head < len(tape) and tape[head] == '1':
                head += 1
            if head >= len(tape):
                tape.extend(['_'] * 5)
            tape[head] = '1'
            state = 'RETURN'
            head = 0
            
        elif state == 'RETURN':
            state = 'SCAN'

    count = 0
    for i in range(counter_start, len(tape)):
        if tape[i] == '1':
            count += 1
    
    return count, ''.join(tape)

test_strings = [
    "101",
    "1111", 
    "0000",
    "1010101",
    "110011",
    "1",
    "0",
    "11100111"
]

print("Binary Counter Turing Machine Results:")
print("=" * 45)

for test_str in test_strings:
    count, final_tape = count_ones_turing(test_str, debug=False)
    print(f"'{test_str:8}' -> Count: {count}, Final tape: {final_tape}")

print("\nDebug example for '101':")
print("-" * 30)
count_ones_turing("101", debug=True)