import sys
from turing import TuringMachine


def main():
    if len(sys.argv) != 3:
        print("Użycie: python main.py <taśma> <plik_funkcji_przejścia>")
        sys.exit(1)

    input_tape = sys.argv[1]
    transitions_file = sys.argv[2]

    machine = TuringMachine(input_tape)
    machine.load_transitions(transitions_file)
    machine.run()


if __name__ == "__main__":
    main()
