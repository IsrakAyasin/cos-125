section .data
	j dd 4
	i dd 0

section .text
_start:
    mov eax, counter
    
    
    mov eax, 1
	mov ebx, 0
	int 80h