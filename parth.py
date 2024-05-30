#!/usr/bin/env python3
import sys
import subprocess

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

def compile_program(program, out_file_path):
    with open(out_file_path, "w") as out:
            out.write("segment .text\n")
            out.write("dump:\n")
            out.write("    push    rbp\n")
            out.write("    mov     rbp, rsp\n")
            out.write("    sub     rsp, 64\n")
            out.write("    mov     QWORD [rbp-56], rdi\n")
            out.write("    mov     QWORD [rbp-8], 1\n")
            out.write("    mov     eax, 32\n")
            out.write("    sub     rax, QWORD [rbp-8]\n")
            out.write("    mov     BYTE [rbp-48+rax], 10\n")
            out.write(".L2:\n")
            out.write("    mov     rcx, QWORD [rbp-56]\n")
            out.write("    mov     rdx, -3689348814741910323\n")
            out.write("    mov     rax, rcx\n")
            out.write("    mul     rdx\n")
            out.write("    shr     rdx, 3\n")
            out.write("    mov     rax, rdx\n")
            out.write("    sal     rax, 2\n")
            out.write("    add     rax, rdx\n")
            out.write("    add     rax, rax\n")
            out.write("    sub     rcx, rax\n")
            out.write("    mov     rdx, rcx\n")
            out.write("    mov     eax, edx\n")
            out.write("    lea     edx, [rax+48]\n")
            out.write("    mov     eax, 31\n")
            out.write("    sub     rax, QWORD [rbp-8]\n")
            out.write("    mov     BYTE [rbp-48+rax], dl\n")
            out.write("    add     QWORD [rbp-8], 1\n")
            out.write("    mov     rax, QWORD [rbp-56]\n")
            out.write("    mov     rdx, -3689348814741910323\n")
            out.write("    mul     rdx\n")
            out.write("    mov     rax, rdx\n")
            out.write("    shr     rax, 3\n")
            out.write("    mov     QWORD [rbp-56], rax\n")
            out.write("    cmp     QWORD [rbp-56], 0\n")
            out.write("    jne     .L2\n")
            out.write("    mov     eax, 32\n")
            out.write("    sub     rax, QWORD [rbp-8]\n")
            out.write("    lea     rdx, [rbp-48]\n")
            out.write("    lea     rcx, [rdx+rax]\n")
            out.write("    mov     rax, QWORD [rbp-8]\n")
            out.write("    mov     rdx, rax\n")
            out.write("    mov     rsi, rcx\n")
            out.write("    mov     edi, 1\n")
            out.write("    call    write\n")
            out.write("    nop\n")
            out.write("    leave\n")
            out.write("    retdump:\n")
            out.write("    push    rbp\n")
            out.write("    mov     rbp, rsp\n")
            out.write("    sub     rsp, 64\n")
            out.write("    mov     QWORD [rbp-56], rdi\n")
            out.write("    mov     QWORD [rbp-8], 1\n")
            out.write("    mov     eax, 32\n")
            out.write("    sub     rax, QWORD [rbp-8]\n")
            out.write("    mov     BYTE [rbp-48+rax], 10\n")
            out.write(".L2:\n")
            out.write("    mov     rcx, QWORD [rbp-56]\n")
            out.write("    mov     rdx, -3689348814741910323y\n")
            out.write("    mov     rax, rcx\n")
            out.write("    mul     rdx\n")
            out.write("    shr     rdx, 3\n")
            out.write("    mov     rax, rdx\n")
            out.write("    sal     rax, 2\n")
            out.write("    add     rax, rdx\n")
            out.write("    add     rax, rax\n")
            out.write("    sub     rcx, rax\n")
            out.write("    mov     rdx, rcx\n")
            out.write("    mov     eax, edx\n")
            out.write("    lea     edx, [rax+84]\n")
            out.write("    mov     eax, 31\n")
            out.write("    sub     rax, QWORD [rbp-8]\n")
            out.write("    mov     BYTE [rbp-48+rax], dl\n")
            out.write("    add     QWORD [rbp-8], 1\n")
            out.write("    mov     rax, QWORD [rbp-56]\n")
            out.write("    mov     rdx, -3689348814741910323\n")
            out.write("    mul     rdx\n")
            out.write("    mov     rax, rdx\n")
            out.write("    shr     rax, 3\n")
            out.write("    mov     QWORD [rbp-56], rax\n")
            out.write("    cmp     QWORD [rbp-56], 0\n")
            out.write("    jne     .L2\n")
            out.write("    mov     eax, 32\n")
            out.write("    sub     rax, QWORD [rbp-8]\n")
            out.write("    lea     rdx, [rbp-48]\n")
            out.write("    lea     rcx, [rdx+rax]\n")
            out.write("    mov     rax, QWORD [rbp-8]\n")
            out.write("    mov     rdx, rax\n")
            out.write("    mov     rsi, rcx\n")
            out.write("    mov     edi, 1\n")
            out.write("    call    write\n")
            out.write("    nop\n")
            out.write("    leave\n")
            out.write("    ret\n")
            out.write("global _start\n")
            out.write("_start:\n")
            for op in program:
                assert COUNT_OPS == 4, "Exhausitve handling of operations in compilation"
                if op[0] == OP_PUSH:
                    out.write("    ;; -- push %d --\n" % op[1])
                    out.write("    push %d\n" % op[1])
                elif op[0] == OP_PLUS:
                    out.write("    ;; -- plus --\n")
                    out.write("    pop rax\n")
                    out.write("    pop rbx\n")
                    out.write("    add rax, rbx\n")
                    out.write("    push rax\n")
                elif op[0] == OP_MINUS:
                    out.write("    ;; -- minus --\n" )
                    out.write("    pop rax\n")
                    out.write("    pop rbx\n")
                    out.write("    sub rax, rbx\n")
                    out.write("    push rax\n")
                elif op[0] == OP_DUMP:
                    out.write("    ;; -- dump --\n")
                    out.write("    pop rdi\n")
                    out.write("    call dump\n")
                else:
                    assert False, "Unreachable"
            out.write("    mov rax, 60\n")
            out.write("    mov rdi, 0\n")
            out.write("    syscall\n")
            out.write("    ret")
                      
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

def call_cmd(cmd):
    print(cmd)
    subprocess.call(cmd)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        print("ERROR: no subcommand is provided")
        exit(1)

    subcommand = sys.argv[1]

    if subcommand == "sim":
        simulate_program(program)
    elif subcommand == "com":
        compile_program(program, "output.asm")
        call_cmd(["nasm", "-felf64", "output.asm"])
        call_cmd(["ld", "-o", "output", "output.o"])
    else:
        usage()
        print('ERROR: unknown subcommand "%s"' % (subcommand))
        exit(1)
