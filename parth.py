#!/usr/bin/env python3

import sys
import subprocess
import shlex
from os import path

iota_counter = 0
def iota(reset = False):
    global iota_counter
    if reset:
        iota_counter = 0
    result = iota_counter
    iota_counter += 1
    return result

OP_PUSH=iota(True)
OP_PLUS=iota()
OP_MINUS=iota()
OP_EQUAL=iota()
OP_DUMP=iota()
OP_IF=iota()
OP_END=iota()
OP_ELSE=iota()
OP_DUP=iota()
OP_GT=iota()
COUNT_OPS=iota()

def push(x):
    return (OP_PUSH, x)

def plus():
    return (OP_PLUS, )

def minus():
    return (OP_MINUS, )

def equal():
    return (OP_EQUAL, )

def dump():
    return (OP_DUMP, )

def iff():
    return (OP_IF, )

def end():
    return (OP_END, )

def elss():
    return (OP_ELSE, )

def dup():
    return (OP_DUP, )

def gt():
    return (OP_GT, )\

def simulate_program(program):
    stack = []
    ip = 0
    while ip < len(program):
        assert COUNT_OPS == 10, "Exhaustive handling of operations in simualation"
        op = program[ip]
        if op[0] == OP_PUSH:
            stack.append(op[1])
            ip += 1
        elif op[0] == OP_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
            ip += 1
        elif op[0] == OP_MINUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
            ip += 1    
        elif op[0] == OP_EQUAL:
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a == b))
            ip += 1
        elif op[0] == OP_DUMP:
            a = stack.pop()
            print(a)
            ip += 1
        elif op[0] == OP_IF:
            a = stack.pop()
            if a == 0:
                assert len(op) >= 2, "'if' instruction does not have reference to the end of its block, please call cross_reference_blocks() on the program before trying to simulate it"
                ip = op[1]
            else:
                ip += 1
        elif op[0] == OP_ELSE:
            assert len(op) >= 2, "'else' instruction does not have reference to the end of its block, please call cross_reference_blocks() on the program before trying to simulate it"
            ip = op[1]
        elif op[0] == OP_END:
            ip += 1
        elif op[0] == OP_DUP:
            a = stack.pop()
            stack.append(a)
            stack.append(a)
            ip += 1
        elif op[0] == OP_GT:
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b > a))
            ip += 1
        else:
            assert False, "Unreachable"

def compile_program(program, out_file_path):
    with open(out_file_path, "w") as out:
            out.write("segment .text\n")
            out.write("dump:\n")
            out.write("    mov    r9, -3689348814741910323\n")
            out.write("    sub    rsp, 40\n")
            out.write("    mov    BYTE [rsp+31], 10\n")
            out.write("    lea    rcx, [rsp+30]\n")
            out.write(".L2:\n")
            out.write("    mov    rax, rdi\n")
            out.write("    lea    r8, [rsp+32]\n")
            out.write("    mul    r9\n")
            out.write("    mov    rax, rdi\n")
            out.write("    sub    r8, rcx\n")
            out.write("    shr    rdx, 3\n")
            out.write("    lea    rsi, [rdx+rdx*4]\n")
            out.write("    add    rsi, rsi\n")
            out.write("    sub    rax, rsi\n")
            out.write("    add    eax, 48\n")
            out.write("    mov    BYTE [rcx], al\n")
            out.write("    mov    rax, rdi\n")
            out.write("    mov    rdi, rdx\n")
            out.write("    mov    rdx, rcx\n")
            out.write("    sub    rcx, 1\n")
            out.write("    cmp    rax, 9\n")
            out.write("    ja     .L2\n")
            out.write("    lea    rax, [rsp+32]\n")
            out.write("    mov    edi, 1\n")
            out.write("    sub    rdx, rax\n")
            out.write("    xor    eax, eax\n")
            out.write("    lea    rsi, [rsp+32+rdx]\n")
            out.write("    mov    rdx, r8\n")
            out.write("    mov    rax, 1\n")
            out.write("    syscall\n")
            out.write("    add    rsp, 40\n")
            out.write("    ret\n")
            out.write("global _start\n")
            out.write("_start:\n")
            for ip in range(len(program)):
                assert COUNT_OPS == 10, "Exhausitve handling of operations in compilation"
                op = program[ip]
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
                    out.write("    sub rbx, rax\n")
                    out.write("    push rbx\n")
                elif op[0] == OP_DUMP:
                    out.write("    ;; -- dump --\n")
                    out.write("    pop rdi\n")
                    out.write("    call dump\n")
                elif op[0] == OP_EQUAL:
                    out.write("    ;; -- equal --\n")
                    out.write("    mov rcx, 0\n")
                    out.write("    mov rdx, 1\n")
                    out.write("    pop rax\n")
                    out.write("    pop rbx\n")
                    out.write("    cmp rax, rbx\n")
                    out.write("    cmove rcx, rdx\n")
                    out.write("    push rcx\n")
                elif op[0] == OP_IF:
                    out.write("    ;; -- if --\n")
                    out.write("    pop rax\n")
                    out.write("    test rax, rax\n")
                    assert len(op) >= 2, "'if' instruction does not have reference to the end of its block, please call cross_reference_blocks() on the program before trying to compile it"
                    out.write("    jz addr_%d\n" % op[1])
                elif op[0] == OP_ELSE:
                    out.write("    ;; -- else --\n")
                    assert len(op) >= 2, "'else' instruction does not have reference to the end of its block, please call cross_reference_blocks() on the program before trying to compile it"
                    out.write("    jmp addr_%d\n" % op[1])
                    out.write("addr_%d:\n" % (ip + 1))
                elif op[0] == OP_END:
                    out.write("addr_%d:\n" % ip)
                elif op[0] == OP_DUP:
                    out.write("    ;; -- dup --\n")
                    out.write("    pop rax\n")
                    out.write("    push rax\n")
                    out.write("    push rax\n")
                elif op[0] == OP_GT:
                    out.write("    ;; -- gt --\n")
                    out.write("    mov rcx, 0\n")
                    out.write("    mov rdx, 1\n")
                    out.write("    pop rbx\n")
                    out.write("    pop rax\n")
                    out.write("    cmp rax, rbx\n")
                    out.write("    cmovg rcx, rdx\n")
                    out.write("    push rcx\n")   
                else:
                    assert False, "Unreachable"
            out.write("    mov rax, 60\n")
            out.write("    mov rdi, 0\n")
            out.write("    syscall\n")
            out.write("    ret")

def parse_token_as_op(token):
    file_path, row, col, word = token
    assert COUNT_OPS == 10, "Exhaustive op handling in parse_token_as_op"
    if word == '+':
        return plus()
    elif word == "-":
        return minus()
    elif word == ".":
        return dump()
    elif word == "=":
        return equal()
    elif word == "if":
        return iff()
    elif word == "end":
        return end()
    elif word == "else":
        return elss()
    elif word == "dup":
        return dup()
    elif word == ">":
        return gt()
    else:
        try:
            return push(int(word))
        except ValueError as e:
            print("%s:%d:%d: %s" % (file_path, row, col, e))
            exit(1)

def cross_reference_blocks(program):
    stack = []
    for ip in range(len(program)):
        op = program[ip]
        assert COUNT_OPS == 10, "Exhaustive handling of ops in cross_reference_blocks. Keep in mind only operations that form blocks need to be handled here. "
        if op[0] == OP_IF:
            stack.append(ip)
        elif op[0] == OP_ELSE:
            if_ip = stack.pop()
            assert program[if_ip][0] == OP_IF, "'else' can only be used in 'if' blocks"
            program[if_ip] = (OP_IF, ip + 1) # reference else address in if-else block as jumping point 
            stack.append(ip)
        elif op[0] == OP_END:
            block_ip = stack.pop()
            if program[block_ip][0] == OP_IF or program[block_ip][0] == OP_ELSE:
                program[block_ip] = (program[block_ip][0], ip)
            else:
                assert False, "'end' can only close 'if-else' blocks for now"
    return program
            
def find_col(line, start, predicate):
    while start < len(line) and not predicate(line[start]):
        start += 1
    return start

def lex_line(line):
    col = find_col(line, 0, lambda x: not x.isspace())
    while col < len(line):
        col_end = find_col(line, col, lambda x: x.isspace())
        yield (col, line[col:col_end])
        col = find_col(line, col_end, lambda x: not x.isspace())

def lex_file(file_path):
    with open(file_path, "r") as f:
        return [(file_path, row, col, token)
            for (row, line) in enumerate(f.readlines())
            for (col, token) in lex_line(line)]

def load_program_from_file(file_path):
    return cross_reference_blocks([parse_token_as_op(token) for token in lex_file(file_path)])        

def usage(program):
    print("Usage: %s <SUBCOMMAND> [ARGS]" % program)
    print("SUBCOMMANDS:")
    print("    sim <file>    Simulate the program")
    print("    com <file>    Compile the program")
    print()

def call_cmd(cmd):
    print(cmd)
    subprocess.call(cmd)

def uncons(xs):
    return (xs[0], xs[1:])

if __name__ == '__main__':
    program_name, argv = uncons(sys.argv)
    assert len(argv) >= 1
    if len(argv) < 1:
        usage(program_name)
        print("ERROR: no subcommand is provided")
        exit(1)
    subcommand, argv = uncons(argv)

    if subcommand == "sim":
        if len(argv) < 1:
            usage(program_name)
            print("ERROR: no input file is provided for the simulation")
            exit(1)
        input_file_path, argv = uncons(argv)
        program = load_program_from_file(input_file_path)
        simulate_program(program)
    elif subcommand == "com":
        # TODO: -r flag for com that runs the application upon successful compilation
        if len(argv) < 1:
            usage(program_name)
            print("ERROR: no input file is provided for the compilation")
            exit(1)
        input_file_path, argv = uncons(argv)
        program = load_program_from_file(input_file_path)
        compile_program(program, "output.asm")
        print("[INFO] Generating Assembly") 
        call_cmd(["nasm", "-felf64", "output.asm"])
        call_cmd(["ld", "-o", "output", "output.o"])
    else:
        usage(program_name)
        print('ERROR: unknown subcommand "%s"' % (subcommand))
        exit(1)
