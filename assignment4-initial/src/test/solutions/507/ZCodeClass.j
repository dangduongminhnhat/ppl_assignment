.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a Z

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
.var 2 is b Z from Label2 to Label3
	iconst_1
	istore_2
Label4:
	iload_2
	putstatic ZCodeClass/a Z
Label5:
	getstatic ZCodeClass/a Z
	invokestatic io/writeBool(Z)V
Label3:
	return
Label1:
.limit stack 1
.limit locals 3
.end method
