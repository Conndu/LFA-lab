def load_dfa(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    dfa = {}
    current_section = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if '/' in line:
            sep = line.find('/')
            if '[' in line:
                key = line[1:sep-1]
                dfa[key] = []
                current_section = key
            else:
                dfa[current_section].append(line[:sep])
        else:
            if '[' in line:
                key = line[1:-1]
                dfa[key] = []
                current_section = key
            else:
                dfa[current_section].append(line)


    for rule in dfa['Rules']:
        if not any(symbol in rule for symbol in dfa['Symbols']):
            return "Error"


    for rule in dfa['Rules']:
        parts = rule.split(', ')
        if not all(part in dfa['States'] for part in [parts[0], parts[-1]]):
            return "Error"

    return dfa


def simulate_dfa(input_file, config_file):
    dfa = load_dfa(config_file)
    if dfa == "Error":
        return "Invalid DFA description."

    current_state = dfa['First state'][0]
    print(current_state)

    with open(input_file, "r") as file:
        for line in file:
            symbol = line.strip()
            for rule in dfa['Rules']:
                parts = rule.split(', ') if ', ' in rule else rule.split()
                if current_state == parts[0] and symbol == parts[1]:
                    current_state = parts[2]
                    print(current_state)
                    break

    return 1 if current_state in dfa['Final state'] else 0



print(load_dfa("dfa.txt"))
print(simulate_dfa("test.txt", "dfa.txt"))
