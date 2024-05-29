
#!/bin/sh

set -xe

nasm -felf64 hello.asm
ld -o hello hello.o
