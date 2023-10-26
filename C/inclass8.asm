global _start

section .data
	message: db "This is asm", 10	
	message2: db "This is not asm", 10
	message3: db "This is kind of asm", 10

section .text
_start: mov ebx, 10
	mov eax, 7
	inc eax
	inc eax
	inc eax
	cmp eax, ebx
	jz _if
	cmp eax, 9
	jz _else_if
	jne _else


_exit:	mov eax, 1
	mov ebx, 0
	int 80h
	 
_if:	mov eax, 4
	mov ebx, 1
	mov ecx, message
	mov edx, 12
	int 80h
;	jmp _exit 

_else_if:	mov eax, 4
		mov ebx, 1
		mov ecx, message3
		mov edx, 20
		int 80h
;		jmp _exit

_else:  mov eax, 4
	mov ebx, 1
	mov ecx, message2
	mov edx, 16
	int 80h
;	jmp _exit
