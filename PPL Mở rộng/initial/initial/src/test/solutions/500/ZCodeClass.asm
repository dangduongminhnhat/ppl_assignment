main:
	li $t0, 0x3f800000
	mtc1 $t0, $f0
	li $t0, 0x3f800000
	mtc1 $t0, $f1
	add.s $f0, $f0, $f1
	mov.s $f12, $f0
	jal writeNumber
	jal exit
writeNumber:
        li $v0, 2
        syscall
        jr $ra
exit:
        li $v0, 10
        syscall
