.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a F

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
	ldc 1.0
	putstatic ZCodeClass/a F
	return
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label2:
Label4:
.var 2 is a F from Label4 to Label5
	ldc 2.0
	fstore_2
	fload_2
	invokestatic io/writeNumber(F)V
Label5:
	getstatic ZCodeClass/a F
	invokestatic io/writeNumber(F)V
Label3:
	return
Label1:
.limit stack 1
.limit locals 3
.end method
