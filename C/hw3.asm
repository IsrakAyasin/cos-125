global _start

section .data
count: dd 0

section .text
_start: 
  mov eax, count ; Load count into the eax register
  add dword [count], 1 ; Increment count
  cmp eax, 8 ; Compare count to 8
  jz _start ; If count is equal to 8, jump to the beginning of the loop
  
_exit:
  mov eax, 1 ; Set the system call number to 1 (exit)
  mov ebx, 0 ; Set the exit status to 0
  int 80h ; Make the system call