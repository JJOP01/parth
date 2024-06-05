# parth
stack-based programming language

## Example

Simple program that prints numbers from 10 to 1 in descending order

```parth
10 while dup 0 > do
    dup .
    1 -
end
```

## Quick Start

### Simulation

```console
$ cat program.parth
34 35 .
$ ./parth.py sim program.parth
69
```

### Compilation

Compilation generates assembly code, compiles it with [nasm](https://www.nasm.us/), and then links it with [GNU ld](https://www.gnu.org/software/binutils/). Both of these should be in `$PATH` to run parth.

```console
$ cat program.parth
34 35 .
$ ./parth.py com program.parth
[INFO] Generating ./program.asm
[CMD] nasm -felf64 ./program.asm
[CMD] ld -o ./program ./program.o
$ ./program
69
```

## Language Reference

This is what the language supports so far

### Stack Manipulation

- `<integer>` - push the integer onto the stack. Right now the integer is anything that is parasable by [int](https://docs.python.org/3/library/functions.html#int).
```
push(<integer>)
```
- `dup` - duplicates an element on top of the stack.
```
a = pop()
push(a)
push(a)
```
- `.` - prints the element on top of the stack to stdout and remove it from the stack.
```
a = pop()
print(a)
```

### Comparison

- `=` - checks if two elements on top of the stack are equal. Removes the elements from the stack and pushes `1` if they are equal and `0` if they are not.
```
a = pop()
b = pop()
push(int(a == b))
```
- `>` - checks if the element below the top of the stack is greater than the top element.
```
b = pop()
a = pop()
push(int(a > b))
```

### Arithmetics

- `+` - sums up two elements on top of the stack.
```
a = pop()
b = pop()
push(int(a + b))
```
- `-` - subtracts the top of the stack from the element below.
```
a = pop()
b = pop()
push(b - a)
```

### Control Flow

- `<cond> if <then-branch> else <else-branch> end` - pops the element on top of the stack and if the element is not `0` executes the `<then-branch>`, otherwise `<else-branch>`
```
34 35 + 69 = if 69 . else 420 . end    // prints 69  <cond> = 1 (IF BLOCK)
420 1 + 420 = if 69 . else 420 . end   // prints 420 <cond> = 0 (ELSE BLOCK)
```
- `while <condtion> do <body> end` - keeps executing both `<condition>` and `<body>` until `<condition>` produces `0` at the top of the stack. Checking the result of `<condition>` removes it from the stack.
```
10 while dup 0 > do
    dup .
    1 -
end
```