import sys

iota_counter = 0
def iota(reset = False):
    global iota_counter
    if reset:
        iota_counter = 0
    result = iota_counter
    iota_counter += 1
    return result

OP_PUSH = iota(True)
OP_PLUS = iota()
OP_MINUS = iota()
OP_DUMP = iota()
COUNT_OPS = iota()

def push(x):
    return (OP_PUSH, x)

def plus():
    return (OP_PLUS, )

def minus():
    return (OP_MINUS, )

def dump():
    return (OP_DUMP, )

def simulate_program(program):
    stack = []
    for op in program:
        assert COUNT_OPS == 4, "Exhaustive handling of operations in simualation"
        if op[0] == OP_PUSH:
            stack.append(op[1])
        elif op[0] == OP_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif op[0] == OP_MINUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif op[0] == OP_DUMP:
            a = stack.pop()
            print(a)
        else:
            assert False, "Unreachable"

def compile_program(program):
    assert False, "Not implemented"

# TODO un-hardcode simulation
program = [
    push(33),
    push(36),
    plus(),
    dump(),
    push(500),
    push(80),
    minus(),
    dump()
]

def usage():
    print("Usage: porth <SUBCOMMAND> [ARGS]")
    print("SUBCOMMANDS:")
    print("    sim    Simulate the program")
    print("    com    Compile the program")
    print()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        print("ERROR: no subcommand is provided")
        exit(1)

    subcommand = sys.argv[1]

    if subcommand == "sim":
        simulate_program(program)
    elif subcommand == "com":
        compile_program(program)
    else:
        usage()
        print('ERROR: unknown subcommand "%s"' % (subcommand))
        exit(1)
