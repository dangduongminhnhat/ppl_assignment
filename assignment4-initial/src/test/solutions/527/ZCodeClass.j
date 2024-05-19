.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public <init>()V
Label0:
.var 0 is this LZCodeClass; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	return
Label1:
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label2:
	ldc 1.0
	ldc 1.0
	fadd
	invokestatic io/writeNumber(F)V
	ldc 1.0
	ldc 1.0
	fsub
	invokestatic io/writeNumber(F)V
	ldc 1.0
	ldc 2.0
	fmul
	invokestatic io/writeNumber(F)V
	ldc 1.0
	ldc 2.0
	fdiv
	invokestatic io/writeNumber(F)V
	ldc 7.5
	ldc 3.5
	frem
	invokestatic io/writeNumber(F)V
	ldc 7.8
	ldc 3.38
	frem
	invokestatic io/writeNumber(F)V
Label3:
	return
Label1:
.limit stack 2
.limit locals 2
.end method
