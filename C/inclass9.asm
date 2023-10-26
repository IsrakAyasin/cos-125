
global _start

section .data
	counter dd 10

section .text
_start:
;	mov eax, 4
;	mov ebx, 1
;	mov ecx, counter
;	mov edx, 2
;	int 80h
	mov ebx, [counter]
	cmp ebx, 3
	jz _exit
	dec ebx
	mov [counter], ebx
	jmp _start
_exit:
	mov eax, 1
	mov ebx, [counter]
	int 80h
