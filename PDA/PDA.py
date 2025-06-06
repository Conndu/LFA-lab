def pda_nested_comments(input_string, debug=False):
    stack = []
    i = 0
    
    while i < len(input_string):
        if debug:
            print(f"i={i}, stack depth={len(stack)}, next chars: '{input_string[i:i+2]}'")

        if i < len(input_string) - 1 and input_string[i:i+2] == '/*':
            stack.append('/*')
            if debug:
                print(f"  Found comment start, stack depth now: {len(stack)}")
            i += 2

        elif i < len(input_string) - 1 and input_string[i:i+2] == '*/':
            if not stack:
                if debug:
                    print("  Error: Found */ without matching /*")
                return False
            stack.pop()
            if debug:
                print(f"  Found comment end, stack depth now: {len(stack)}")
            i += 2
            
        else:
            i += 1

    is_valid = len(stack) == 0
    if debug and not is_valid:
        print(f"Error: {len(stack)} unclosed comments")
    
    return is_valid

def read_lines_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print(f"File {filename} not found. Using default test cases.")
        return [
            "/* simple comment */",
            "/* outer /* inner */ outer */", 
            "/* unclosed comment",
            "closed without open */",
            "/* first */ /* second */",
            "code /* comment */ more code"
        ]

lines = read_lines_from_file("input.txt")

print("PDA Nested Comments Validator Results:")
print("=" * 50)

for line in lines:
    if not line.strip():
        print("Empty line -> VALID")
        continue
    result = pda_nested_comments(line, debug=False)
    print(f"'{line:30}' -> {'VALID' if result else 'INVALID'}")

print("\nDebug example for '/* outer /* inner */ outer */':")
print("-" * 50)
pda_nested_comments("/* outer /* inner */ outer */", debug=True)