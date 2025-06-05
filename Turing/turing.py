from collections import defaultdict, deque


class TuringMachine:
    def __init__(self, tape_string: str):
        self.tape = list(tape_string)  # konwertujemy wejściowy ciąg znaków na listę (taśma)
        self.head = 0
        self.state = 'init'
        self.transitions = defaultdict(lambda: defaultdict(list)) # umozliwia powtorki, stad uzycie

    def load_transitions(self, filename: str):
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                current_state, current_symbol, new_symbol, direction, new_state = line.split()
                self.transitions[current_state][current_symbol].append((new_symbol, direction, new_state))

    def run(self):
        # Używam BFS do eksploracji stanów (niedeterministycznie)
        queue = deque()     # double ended queue
        initial_config = (self.tape[:], self.head, self.state, [])  # kopia taśmy, pozycja głowicy, stan początkowy, pusta historia
        queue.append(initial_config)

        while queue:
            tape, head, state, path = queue.popleft()  # pobieramy najstarszą konfigurację (BFS - eksplorujemy najpierw najkrótsze ścieżki)

            if state.startswith("halt"):
                for config in path:
                    self.display_tape(*config)  # * oznacza ze rozpakowuje tą krotke
                self.display_tape(tape, head, state)
                return

            current_symbol = tape[head] if 0 <= head < len(tape) else '_'
            transitions = self.transitions[state].get(current_symbol, [])   # zwróc pustą liste jeśli nie ma mozliwych przejsc

            for new_symbol, direction, new_state in transitions:    # przechodzimy przez wszystkie możliwe przejścia z aktualnego stanu i symbolu
                new_tape = tape[:]
                if head < 0:
                    new_tape = ['_'] * abs(head) + new_tape
                    head = 0
                if head >= len(new_tape):
                    new_tape += ['_'] * (head - len(new_tape) + 1)

                new_tape[head] = new_symbol
                new_head = head + (1 if direction == 'R' else -1 if direction == 'L' else 0)

                queue.append((new_tape, new_head, new_state, path + [(tape[:], head, state)]))  # dodajemy nową konfigurację do kolejki wraz z aktualizowaną historią
        print("Brak sciezki do halt")

    def display_tape(self, tape: list, head: int, state: str):
        display = ('_' if head < 0 else '') + ''.join(tape).rstrip('_') + ('_' if head >= len(tape) else '')
        print(display, state)
        print(' ' * head + '^')
