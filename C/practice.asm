global _start

section .data
	message: db "Hello World", 10

section .text
_start: mov eax, 4
	mov ebx, 1
	mov ecx, message
	mov edx, 12
	int 80h
	mov eax, 1
	mov ebx, 0
	int 80h
