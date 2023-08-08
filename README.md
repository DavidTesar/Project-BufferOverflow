# Project-BufferOverflow

# # Compiling C code in linux

```    
    // (for 32 bit architecture) gcc -o hello -m32 hello.c
    $ gcc -o hello hello.c
    $ ./hello 
    Hello, world!
```


# Fuzzing input (Finding Offset)

```
    python3 -c 'print("A" * 200)' | ./program

    Crashes if # of bytes read > size of the buffer
```

# Checking security mechanisms

```
    checksec <exeutable>
```


# Steps done when looking at possible buffer overflow vulnerability

1. Attempt to crash the program with user-defined input
2. Inspect assembly code in debugger - inspect how/where the input is read
3. Find the offset using a fuzzer/offset explorer

    # Using pattern functionality in gdb debugger with a [module peda](https://github.com/longld/peda)
    ```
    pattern create <byte size> <outputFile>
    ```

4. Create a shellcode to exploit the program --> change the EIP value of the return



Topic learned on an amazing YouTube video present bellow
[Buffer Overflow by Cr0w](https://www.youtube.com/watch?v=6sUd3AA7Q50&t=322s&ab_channel=crow)
