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
dump:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 64
    mov     QWORD PTR [rbp-56], rdi
    mov     QWORD PTR [rbp-8], 1
    mov     eax, 32
    sub     rax, QWORD PTR [rbp-8]
    mov     BYTE PTR [rbp-48+rax], 10
.L2:
    mov     rcx, QWORD PTR [rbp-56]
    movabs  rdx, -3689348814741910323
    mov     rax, rcx
    mul     rdx
    shr     rdx, 3
    mov     rax, rdx
    sal     rax, 2
    add     rax, rdx
    add     rax, rax
    sub     rcx, rax
    mov     rdx, rcx
    mov     eax, edx
    lea     edx, [rax+48]
    mov     eax, 31
    sub     rax, QWORD PTR [rbp-8]
    mov     BYTE PTR [rbp-48+rax], dl
    add     QWORD PTR [rbp-8], 1
    mov     rax, QWORD PTR [rbp-56]
    movabs  rdx, -3689348814741910323
    mul     rdx
    mov     rax, rdx
    shr     rax, 3
    mov     QWORD PTR [rbp-56], rax
    cmp     QWORD PTR [rbp-56], 0
    jne     .L2
    mov     eax, 32
    sub     rax, QWORD PTR [rbp-8]
    lea     rdx, [rbp-48]
    lea     rcx, [rdx+rax]
    mov     rax, QWORD PTR [rbp-8]
    mov     rdx, rax
    mov     rsi, rcx
    mov     edi, 1
    call    write
    nop
    leave
    retdump:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 64
    mov     QWORD PTR [rbp-56], rdi
    mov     QWORD PTR [rbp-8], 1
    mov     eax, 32
    sub     rax, QWORD PTR [rbp-8]
    mov     BYTE PTR [rbp-48+rax], 10
.L2:
    mov     rcx, QWORD PTR [rbp-56]
    movabs  rdx, -3689348814741910323
    mov     rax, rcx
    mul     rdx
    shr     rdx, 3
    mov     rax, rdx
    sal     rax, 2
    add     rax, rdx
    add     rax, rax
    sub     rcx, rax
    mov     rdx, rcx
    mov     eax, edx
    lea     edx, [rax+48]
    mov     eax, 31
    sub     rax, QWORD PTR [rbp-8]
    mov     BYTE PTR [rbp-48+rax], dl
    add     QWORD PTR [rbp-8], 1
    mov     rax, QWORD PTR [rbp-56]
    movabs  rdx, -3689348814741910323
    mul     rdx
    mov     rax, rdx
    shr     rax, 3
    mov     QWORD PTR [rbp-56], rax
    cmp     QWORD PTR [rbp-56], 0
    jne     .L2
    mov     eax, 32
    sub     rax, QWORD PTR [rbp-8]
    lea     rdx, [rbp-48]
    lea     rcx, [rdx+rax]
    mov     rax, QWORD PTR [rbp-8]
    mov     rdx, rax
    mov     rsi, rcx
    mov     edi, 1
    call    write
    nop
    leave
    ret
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
                    out.write("    ;; -- TODO: not implemented -- \n")
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
