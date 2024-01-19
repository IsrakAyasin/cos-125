global _start

section .data
    j dd 4       ; Define j as a double-word variable with initial value 4
    i dd 0        ; Define i as a double-word variable with initial value 0

section .text
_start:
    mov ebx, [j]  ; Load the value of j into ebx
    mov eax, [i]  ; Load the value of i into eax
    jmp _loop     ; Jump to the loop

_loop:
    add ebx, eax  ; ebx (j) = ebx(j) + eax(i)
    cmp ebx, 40   ; Compare j to 40
    jg _if        ; If j is greater than 40, go to _if label
    cmp eax, 3    ; Compare i to 4
    jz _exit      ; If i equals 4, exit the loop
    inc eax       ; Increment the value of eax (i)
    jmp _loop     ; Otherwise, jump back to the beginning of the loop

_if:
    sub ebx, 40   ; Subtract 40 from ebx (j)
    jmp _loop     ; Jump back to the loop

_exit: 
    mov eax, 1    ; Set eax to 1 (syscall number for exit)
    int 80h       ; Make the system call to exit the program
