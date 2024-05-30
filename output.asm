segment .text
global _start
_start:
    ;; -- push 33 --
    push 33
    ;; -- push 36 --
    push 36
    ;; -- plus --
    pop rax
    pop rbx
    add rax, rbx
    push rax
    ;; -- dump --
    ;; dump
    ;; -- push 500 --
    push 500
    ;; -- push 80 --
    push 80
    ;; -- minus --
    pop rax
    pop rbx
    sub rax, rbx
    push rax
    ;; -- dump --
    ;; dump
    mov rax, 60
    mov rdi, 0
    syscall
    ret