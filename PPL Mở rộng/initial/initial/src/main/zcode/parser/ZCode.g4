// Student's id: 2110416
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: newlinesep runlist EOF;

runlist: run runlist | run;
run: funcdecl | vardeclstmt;

funcdecl: FUNC IDENTIFIER OPENPARENTHESIS parameterlist CLOSEPARENTHESIS newlinesep endfuncdecl
		| FUNC IDENTIFIER OPENPARENTHESIS parameterlist CLOSEPARENTHESIS newlinelist
		;
parameterlist: parameterprime | ;
parameterprime: param COMMA parameterprime | param;
param: typ IDENTIFIER | typ arraylit;

newlinesep: newlinelist | ;

endfuncdecl: returnstmt | blockstmt;

ifstmt: onlyifstmt eliflist elselist;
eliflist: elifstmt eliflist | ;
elselist: elsestmt | ;

onlyifstmt: IF OPENPARENTHESIS expression CLOSEPARENTHESIS newlinesep statement;
elifstmt: ELIF OPENPARENTHESIS expression CLOSEPARENTHESIS newlinesep statement;
elsestmt: ELSE newlinesep statement;

statement: vardeclstmt
			| assignstmt
			| forstmt
			| breakstmt
			| continuestmt
			| returnstmt
			| funcstmt
			| blockstmt
			| ifstmt
			;

blockstmt: BEGIN newlinelist statementlist END newlinelist;
statementlist: statement statementlist| ;

funcstmt: IDENTIFIER OPENPARENTHESIS argumentlist CLOSEPARENTHESIS newlinelist;

returnstmt: RETURN expression newlinelist | RETURN newlinelist;

continuestmt: CONTINUE newlinelist;

breakstmt: BREAK newlinelist;

forstmt: FOR IDENTIFIER UNTIL expression BY expression newlinesep statement;

assignstmt: lhs ASSIGNMENTSIGN expression newlinelist;
lhs: IDENTIFIER | elementarray;
elementarray: IDENTIFIER LEFTSQUARE index_operator RIGHTSQUARE;

vardeclstmt: vardecl newlinelist;

newlinelist: NEWLINE | NEWLINE newlinelist;

vardecl: varstartdecl
		| dynamicstartdecl
		| normaldecl
		| arraydecl
		;
varstartdecl: VAR IDENTIFIER ASSIGNMENTSIGN expression;
dynamicstartdecl: DYNAMIC IDENTIFIER ASSIGNMENTSIGN expression | DYNAMIC IDENTIFIER;
normaldecl: typ IDENTIFIER ASSIGNMENTSIGN expression | typ IDENTIFIER;
arraydecl: typ arraylit ASSIGNMENTSIGN expression | typ arraylit;

// arrayvalue: arraytype | multidimarray;

typ: NUMBER | BOOL | STRING;

funccall: IDENTIFIER OPENPARENTHESIS argumentlist CLOSEPARENTHESIS;
argumentlist: argueprime | ;
argueprime: arguelement COMMA argueprime | arguelement;
arguelement: expression | funccall;

expression: expression1 STRCON expression1 | expression1;
expression1: expression2 relateoperator expression2 | expression2;
expression2: expression2 logicaloperator expression3 | expression3;
expression3: expression3 addingoperator expression4 | expression4;
expression4: expression4 multiplyingoperator expression5 | expression5;
expression5: NEG expression5 | expression6;
expression6: SUB expression6 | operand;
operand: NUMBERLIT 
		| STRINGLIT
		| BOOLEANLIT
		| IDENTIFIER
		| funccall
		| element_expression
		| subexpression
		| arraytype
		;

subexpression: OPENPARENTHESIS expression CLOSEPARENTHESIS;

element_expression: arrayexpression LEFTSQUARE index_operator RIGHTSQUARE;
index_operator: expression COMMA index_operator | expression;
arrayexpression: IDENTIFIER | funccall;

arraylit: IDENTIFIER LEFTSQUARE sizelist RIGHTSQUARE;
sizelist: NUMBERLIT COMMA sizelist | NUMBERLIT;

// multidimarray: LEFTSQUARE dimarraylist RIGHTSQUARE;
// dimarraylist: dimarrayprime | ;
// dimarrayprime: dimarrayelement COMMA dimarrayprime | dimarrayelement;
// dimarrayelement: LEFTSQUARE dimarrayelement RIGHTSQUARE | arraytype;

arraytype: LEFTSQUARE eleprime RIGHTSQUARE;
eleprime: expression COMMA eleprime | expression;

multiplyingoperator: MUL | DIV | REMAIN;
addingoperator: ADD | SUB;

logicaloperator: CON | DIS;

relateoperator: EQ
				| COMPARESTR
				| NOTEQ
				| LESS
				| GREATER
				| LESSSOREQ
				| GREATEROREQ
				;

COMMENT: '##' (~[\r\n])* -> skip;

RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NUMBER: 'number';
STRING: 'string';
BOOL: 'bool';

NUMBERLIT: INTPART DECPART? EXPPART?;
fragment INTPART: [0-9]+;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [Ee] [+-]? [0-9]+;

ASSIGNMENTSIGN: '<-';

SUB: '-';
ADD: '+';
MUL: '*';
DIV: '/';
REMAIN: '%';

BOOLEANLIT: 'true' | 'false';

NEG: 'not';
CON: 'and';
DIS: 'or';

STRCON: '...';

EQ: '=';
NOTEQ: '!=';
LESS: '<';
GREATER: '>';
LESSSOREQ: '<=';
GREATEROREQ: '>=';
COMPARESTR: '==';

STRINGLIT: (DOUBLE_QUOTE DOUBLE_QUOTE | DOUBLE_QUOTE INSIDE_STRING* ((SINGLE_QUOTE DOUBLE_QUOTE) | ~['"\\] | ESCAPE_SEQUENCES) DOUBLE_QUOTE) {self.text = self.text[1:-1]};
fragment INSIDE_STRING: (SINGLE_QUOTE DOUBLE_QUOTE) | ~[\n\r"\\] | ESCAPE_SEQUENCES;
fragment SINGLE_QUOTE: ['];
fragment DOUBLE_QUOTE: ["];
fragment BACKSLASH: '\\';
fragment ESCAPE_SEQUENCES: (BACKSLASH [bfrnt]) | (BACKSLASH SINGLE_QUOTE) | (BACKSLASH BACKSLASH);

NEWLINE: ('\r\n' | '\n') {self.text = '\n'};
LEFTSQUARE: '[';
RIGHTSQUARE: ']';
COMMA: ',';
OPENPARENTHESIS: '(';
CLOSEPARENTHESIS: ')';

IDENTIFIER: [A-Za-z_] [A-Za-z_0-9]*;

WHITESPACE: [ \t\b\f] -> skip;

ILLEGAL_ESCAPE: DOUBLE_QUOTE INSIDE_STRING* BACKSLASH ~[bfrnt] {raise IllegalEscape(self.text[1:])}; 
UNCLOSE_STRING: DOUBLE_QUOTE INSIDE_STRING* ([\n\r] | EOF) {raise UncloseString(self.text[1:].replace("\r", "").replace("\n", ""))};
ERROR_CHAR: . {raise ErrorToken(self.text)};