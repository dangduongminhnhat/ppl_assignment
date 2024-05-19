writeNumber:
        li $v0, 2
        syscall
        jr $ra
exit:
        li $v0, 10
        syscall
