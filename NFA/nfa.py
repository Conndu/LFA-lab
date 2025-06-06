def compute_epsilon_closure(state_set):
    # Placeholder for future epsilon closure logic
    return state_set

def evaluate_nfa(automaton, input_string):
    active_states = {automaton["initial"]}
    for char in input_string:
        temp_states = set()
        for st in active_states:
            transition_key = (st, char)
            if transition_key in automaton["moves"]:
                temp_states.update(automaton["moves"][transition_key])
        active_states = temp_states
        if not active_states:
            return False
    return bool(active_states & automaton["accepting"])

def load_nfa_from_file(filepath):
    with open(filepath, 'r') as file:
        raw_lines = [line.strip() for line in file if line.strip()]

    sigma = set()
    all_states = set()
    start = None
    finals = set()
    move_table = dict()
    test_inputs = []

    section = None

    for entry in raw_lines:
        if entry.startswith("Sigma:"):
            section = "sigma"
        elif entry.startswith("States:"):
            section = "states"
        elif entry.startswith("Start:"):
            start = entry.split(":")[1].strip()
        elif entry.startswith("Final:"):
            finals = set(entry.split(":")[1].strip().split())
        elif entry.startswith("Transitions:"):
            section = "transitions"
        elif entry.startswith("Words:"):
            section = "words"
        else:
            if section == "sigma":
                sigma.update(entry.split())
            elif section == "states":
                all_states.update(entry.split())
            elif section == "transitions":
                from_state, input_symbol, to_state = entry.split()
                pair = (from_state, input_symbol)
                if pair not in move_table:
                    move_table[pair] = set()
                move_table[pair].add(to_state)
            elif section == "words":
                test_inputs.append(entry)

    automaton_data = {
        "states": all_states,
        "alphabet": sigma,
        "initial": start,
        "accepting": finals,
        "moves": move_table
    }

    return automaton_data, test_inputs

if __name__ == "__main__":
    nfa_model, input_words = load_nfa_from_file("nfa_input.txt")

    for test_word in input_words:
        verdict = "ACCEPTED" if evaluate_nfa(nfa_model, test_word) else "REJECTED"
        print(f"Word '{test_word}': {verdict}")
