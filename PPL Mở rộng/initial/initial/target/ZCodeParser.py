# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("\u01d0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\177\n\3\3\4\3\4")
        buf.write("\5\4\u0083\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5\u0094\n\5\3\6\3\6\5\6\u0098\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\5\7\u009f\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\5\b\u00a7\n\b\3\t\3\t\5\t\u00ab\n\t\3\n\3\n\5\n")
        buf.write("\u00af\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00b9")
        buf.write("\n\f\3\r\3\r\5\r\u00bd\n\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u00da\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\23\5\23\u00e6\n\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00f4\n\25\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\5\32\u010c\n\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\5\35\u0119\n\35\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u011f\n\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write("\3 \3 \5 \u012c\n \3!\3!\3!\3!\3!\3!\3!\3!\5!\u0136\n")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0140\n\"\3#\3#")
        buf.write("\3$\3$\3$\3$\3$\3%\3%\5%\u014b\n%\3&\3&\3&\3&\3&\5&\u0152")
        buf.write("\n&\3\'\3\'\5\'\u0156\n\'\3(\3(\3(\3(\3(\5(\u015d\n(\3")
        buf.write(")\3)\3)\3)\3)\5)\u0164\n)\3*\3*\3*\3*\3*\3*\3*\7*\u016d")
        buf.write("\n*\f*\16*\u0170\13*\3+\3+\3+\3+\3+\3+\3+\7+\u0179\n+")
        buf.write("\f+\16+\u017c\13+\3,\3,\3,\3,\3,\3,\3,\7,\u0185\n,\f,")
        buf.write("\16,\u0188\13,\3-\3-\3-\5-\u018d\n-\3.\3.\3.\5.\u0192")
        buf.write("\n.\3/\3/\3/\3/\3/\3/\3/\3/\5/\u019c\n/\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\5\62\u01ac\n\62\3\63\3\63\5\63\u01b0\n\63\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\65\3\65\3\65\3\65\5\65\u01bb\n\65\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67\u01c6\n")
        buf.write("\67\38\38\39\39\3:\3:\3;\3;\3;\2\5RTV<\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprt\2\7\3\2\22\24\3\2\31\33\3\2\27")
        buf.write("\30\3\2\36\37\3\2!\'\2\u01c6\2v\3\2\2\2\4~\3\2\2\2\6\u0082")
        buf.write("\3\2\2\2\b\u0093\3\2\2\2\n\u0097\3\2\2\2\f\u009e\3\2\2")
        buf.write("\2\16\u00a6\3\2\2\2\20\u00aa\3\2\2\2\22\u00ae\3\2\2\2")
        buf.write("\24\u00b0\3\2\2\2\26\u00b8\3\2\2\2\30\u00bc\3\2\2\2\32")
        buf.write("\u00be\3\2\2\2\34\u00c5\3\2\2\2\36\u00cc\3\2\2\2 \u00d9")
        buf.write("\3\2\2\2\"\u00db\3\2\2\2$\u00e5\3\2\2\2&\u00e7\3\2\2\2")
        buf.write("(\u00f3\3\2\2\2*\u00f5\3\2\2\2,\u00f8\3\2\2\2.\u00fb\3")
        buf.write("\2\2\2\60\u0104\3\2\2\2\62\u010b\3\2\2\2\64\u010d\3\2")
        buf.write("\2\2\66\u0112\3\2\2\28\u0118\3\2\2\2:\u011e\3\2\2\2<\u0120")
        buf.write("\3\2\2\2>\u012b\3\2\2\2@\u0135\3\2\2\2B\u013f\3\2\2\2")
        buf.write("D\u0141\3\2\2\2F\u0143\3\2\2\2H\u014a\3\2\2\2J\u0151\3")
        buf.write("\2\2\2L\u0155\3\2\2\2N\u015c\3\2\2\2P\u0163\3\2\2\2R\u0165")
        buf.write("\3\2\2\2T\u0171\3\2\2\2V\u017d\3\2\2\2X\u018c\3\2\2\2")
        buf.write("Z\u0191\3\2\2\2\\\u019b\3\2\2\2^\u019d\3\2\2\2`\u01a1")
        buf.write("\3\2\2\2b\u01ab\3\2\2\2d\u01af\3\2\2\2f\u01b1\3\2\2\2")
        buf.write("h\u01ba\3\2\2\2j\u01bc\3\2\2\2l\u01c5\3\2\2\2n\u01c7\3")
        buf.write("\2\2\2p\u01c9\3\2\2\2r\u01cb\3\2\2\2t\u01cd\3\2\2\2vw")
        buf.write("\5\20\t\2wx\5\4\3\2xy\7\2\2\3y\3\3\2\2\2z{\5\6\4\2{|\5")
        buf.write("\4\3\2|\177\3\2\2\2}\177\5\6\4\2~z\3\2\2\2~}\3\2\2\2\177")
        buf.write("\5\3\2\2\2\u0080\u0083\5\b\5\2\u0081\u0083\5\66\34\2\u0082")
        buf.write("\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083\7\3\2\2\2\u0084")
        buf.write("\u0085\7\7\2\2\u0085\u0086\7/\2\2\u0086\u0087\7-\2\2\u0087")
        buf.write("\u0088\5\n\6\2\u0088\u0089\7.\2\2\u0089\u008a\5\20\t\2")
        buf.write("\u008a\u008b\5\22\n\2\u008b\u0094\3\2\2\2\u008c\u008d")
        buf.write("\7\7\2\2\u008d\u008e\7/\2\2\u008e\u008f\7-\2\2\u008f\u0090")
        buf.write("\5\n\6\2\u0090\u0091\7.\2\2\u0091\u0092\58\35\2\u0092")
        buf.write("\u0094\3\2\2\2\u0093\u0084\3\2\2\2\u0093\u008c\3\2\2\2")
        buf.write("\u0094\t\3\2\2\2\u0095\u0098\5\f\7\2\u0096\u0098\3\2\2")
        buf.write("\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098\13\3")
        buf.write("\2\2\2\u0099\u009a\5\16\b\2\u009a\u009b\7,\2\2\u009b\u009c")
        buf.write("\5\f\7\2\u009c\u009f\3\2\2\2\u009d\u009f\5\16\b\2\u009e")
        buf.write("\u0099\3\2\2\2\u009e\u009d\3\2\2\2\u009f\r\3\2\2\2\u00a0")
        buf.write("\u00a1\5D#\2\u00a1\u00a2\7/\2\2\u00a2\u00a7\3\2\2\2\u00a3")
        buf.write("\u00a4\5D#\2\u00a4\u00a5\5f\64\2\u00a5\u00a7\3\2\2\2\u00a6")
        buf.write("\u00a0\3\2\2\2\u00a6\u00a3\3\2\2\2\u00a7\17\3\2\2\2\u00a8")
        buf.write("\u00ab\58\35\2\u00a9\u00ab\3\2\2\2\u00aa\u00a8\3\2\2\2")
        buf.write("\u00aa\u00a9\3\2\2\2\u00ab\21\3\2\2\2\u00ac\u00af\5(\25")
        buf.write("\2\u00ad\u00af\5\"\22\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad")
        buf.write("\3\2\2\2\u00af\23\3\2\2\2\u00b0\u00b1\5\32\16\2\u00b1")
        buf.write("\u00b2\5\26\f\2\u00b2\u00b3\5\30\r\2\u00b3\25\3\2\2\2")
        buf.write("\u00b4\u00b5\5\34\17\2\u00b5\u00b6\5\26\f\2\u00b6\u00b9")
        buf.write("\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b4\3\2\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\27\3\2\2\2\u00ba\u00bd\5\36\20\2")
        buf.write("\u00bb\u00bd\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3")
        buf.write("\2\2\2\u00bd\31\3\2\2\2\u00be\u00bf\7\r\2\2\u00bf\u00c0")
        buf.write("\7-\2\2\u00c0\u00c1\5N(\2\u00c1\u00c2\7.\2\2\u00c2\u00c3")
        buf.write("\5\20\t\2\u00c3\u00c4\5 \21\2\u00c4\33\3\2\2\2\u00c5\u00c6")
        buf.write("\7\17\2\2\u00c6\u00c7\7-\2\2\u00c7\u00c8\5N(\2\u00c8\u00c9")
        buf.write("\7.\2\2\u00c9\u00ca\5\20\t\2\u00ca\u00cb\5 \21\2\u00cb")
        buf.write("\35\3\2\2\2\u00cc\u00cd\7\16\2\2\u00cd\u00ce\5\20\t\2")
        buf.write("\u00ce\u00cf\5 \21\2\u00cf\37\3\2\2\2\u00d0\u00da\5\66")
        buf.write("\34\2\u00d1\u00da\5\60\31\2\u00d2\u00da\5.\30\2\u00d3")
        buf.write("\u00da\5,\27\2\u00d4\u00da\5*\26\2\u00d5\u00da\5(\25\2")
        buf.write("\u00d6\u00da\5&\24\2\u00d7\u00da\5\"\22\2\u00d8\u00da")
        buf.write("\5\24\13\2\u00d9\u00d0\3\2\2\2\u00d9\u00d1\3\2\2\2\u00d9")
        buf.write("\u00d2\3\2\2\2\u00d9\u00d3\3\2\2\2\u00d9\u00d4\3\2\2\2")
        buf.write("\u00d9\u00d5\3\2\2\2\u00d9\u00d6\3\2\2\2\u00d9\u00d7\3")
        buf.write("\2\2\2\u00d9\u00d8\3\2\2\2\u00da!\3\2\2\2\u00db\u00dc")
        buf.write("\7\20\2\2\u00dc\u00dd\58\35\2\u00dd\u00de\5$\23\2\u00de")
        buf.write("\u00df\7\21\2\2\u00df\u00e0\58\35\2\u00e0#\3\2\2\2\u00e1")
        buf.write("\u00e2\5 \21\2\u00e2\u00e3\5$\23\2\u00e3\u00e6\3\2\2\2")
        buf.write("\u00e4\u00e6\3\2\2\2\u00e5\u00e1\3\2\2\2\u00e5\u00e4\3")
        buf.write("\2\2\2\u00e6%\3\2\2\2\u00e7\u00e8\7/\2\2\u00e8\u00e9\7")
        buf.write("-\2\2\u00e9\u00ea\5H%\2\u00ea\u00eb\7.\2\2\u00eb\u00ec")
        buf.write("\58\35\2\u00ec\'\3\2\2\2\u00ed\u00ee\7\4\2\2\u00ee\u00ef")
        buf.write("\5N(\2\u00ef\u00f0\58\35\2\u00f0\u00f4\3\2\2\2\u00f1\u00f2")
        buf.write("\7\4\2\2\u00f2\u00f4\58\35\2\u00f3\u00ed\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f4)\3\2\2\2\u00f5\u00f6\7\f\2\2\u00f6")
        buf.write("\u00f7\58\35\2\u00f7+\3\2\2\2\u00f8\u00f9\7\13\2\2\u00f9")
        buf.write("\u00fa\58\35\2\u00fa-\3\2\2\2\u00fb\u00fc\7\b\2\2\u00fc")
        buf.write("\u00fd\7/\2\2\u00fd\u00fe\7\t\2\2\u00fe\u00ff\5N(\2\u00ff")
        buf.write("\u0100\7\n\2\2\u0100\u0101\5N(\2\u0101\u0102\5\20\t\2")
        buf.write("\u0102\u0103\5 \21\2\u0103/\3\2\2\2\u0104\u0105\5\62\32")
        buf.write("\2\u0105\u0106\7\26\2\2\u0106\u0107\5N(\2\u0107\u0108")
        buf.write("\58\35\2\u0108\61\3\2\2\2\u0109\u010c\7/\2\2\u010a\u010c")
        buf.write("\5\64\33\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c")
        buf.write("\63\3\2\2\2\u010d\u010e\7/\2\2\u010e\u010f\7*\2\2\u010f")
        buf.write("\u0110\5b\62\2\u0110\u0111\7+\2\2\u0111\65\3\2\2\2\u0112")
        buf.write("\u0113\5:\36\2\u0113\u0114\58\35\2\u0114\67\3\2\2\2\u0115")
        buf.write("\u0119\7)\2\2\u0116\u0117\7)\2\2\u0117\u0119\58\35\2\u0118")
        buf.write("\u0115\3\2\2\2\u0118\u0116\3\2\2\2\u01199\3\2\2\2\u011a")
        buf.write("\u011f\5<\37\2\u011b\u011f\5> \2\u011c\u011f\5@!\2\u011d")
        buf.write("\u011f\5B\"\2\u011e\u011a\3\2\2\2\u011e\u011b\3\2\2\2")
        buf.write("\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f;\3\2\2")
        buf.write("\2\u0120\u0121\7\5\2\2\u0121\u0122\7/\2\2\u0122\u0123")
        buf.write("\7\26\2\2\u0123\u0124\5N(\2\u0124=\3\2\2\2\u0125\u0126")
        buf.write("\7\6\2\2\u0126\u0127\7/\2\2\u0127\u0128\7\26\2\2\u0128")
        buf.write("\u012c\5N(\2\u0129\u012a\7\6\2\2\u012a\u012c\7/\2\2\u012b")
        buf.write("\u0125\3\2\2\2\u012b\u0129\3\2\2\2\u012c?\3\2\2\2\u012d")
        buf.write("\u012e\5D#\2\u012e\u012f\7/\2\2\u012f\u0130\7\26\2\2\u0130")
        buf.write("\u0131\5N(\2\u0131\u0136\3\2\2\2\u0132\u0133\5D#\2\u0133")
        buf.write("\u0134\7/\2\2\u0134\u0136\3\2\2\2\u0135\u012d\3\2\2\2")
        buf.write("\u0135\u0132\3\2\2\2\u0136A\3\2\2\2\u0137\u0138\5D#\2")
        buf.write("\u0138\u0139\5f\64\2\u0139\u013a\7\26\2\2\u013a\u013b")
        buf.write("\5N(\2\u013b\u0140\3\2\2\2\u013c\u013d\5D#\2\u013d\u013e")
        buf.write("\5f\64\2\u013e\u0140\3\2\2\2\u013f\u0137\3\2\2\2\u013f")
        buf.write("\u013c\3\2\2\2\u0140C\3\2\2\2\u0141\u0142\t\2\2\2\u0142")
        buf.write("E\3\2\2\2\u0143\u0144\7/\2\2\u0144\u0145\7-\2\2\u0145")
        buf.write("\u0146\5H%\2\u0146\u0147\7.\2\2\u0147G\3\2\2\2\u0148\u014b")
        buf.write("\5J&\2\u0149\u014b\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u0149")
        buf.write("\3\2\2\2\u014bI\3\2\2\2\u014c\u014d\5L\'\2\u014d\u014e")
        buf.write("\7,\2\2\u014e\u014f\5J&\2\u014f\u0152\3\2\2\2\u0150\u0152")
        buf.write("\5L\'\2\u0151\u014c\3\2\2\2\u0151\u0150\3\2\2\2\u0152")
        buf.write("K\3\2\2\2\u0153\u0156\5N(\2\u0154\u0156\5F$\2\u0155\u0153")
        buf.write("\3\2\2\2\u0155\u0154\3\2\2\2\u0156M\3\2\2\2\u0157\u0158")
        buf.write("\5P)\2\u0158\u0159\7 \2\2\u0159\u015a\5P)\2\u015a\u015d")
        buf.write("\3\2\2\2\u015b\u015d\5P)\2\u015c\u0157\3\2\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015dO\3\2\2\2\u015e\u015f\5R*\2\u015f\u0160")
        buf.write("\5t;\2\u0160\u0161\5R*\2\u0161\u0164\3\2\2\2\u0162\u0164")
        buf.write("\5R*\2\u0163\u015e\3\2\2\2\u0163\u0162\3\2\2\2\u0164Q")
        buf.write("\3\2\2\2\u0165\u0166\b*\1\2\u0166\u0167\5T+\2\u0167\u016e")
        buf.write("\3\2\2\2\u0168\u0169\f\4\2\2\u0169\u016a\5r:\2\u016a\u016b")
        buf.write("\5T+\2\u016b\u016d\3\2\2\2\u016c\u0168\3\2\2\2\u016d\u0170")
        buf.write("\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f")
        buf.write("S\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0172\b+\1\2\u0172")
        buf.write("\u0173\5V,\2\u0173\u017a\3\2\2\2\u0174\u0175\f\4\2\2\u0175")
        buf.write("\u0176\5p9\2\u0176\u0177\5V,\2\u0177\u0179\3\2\2\2\u0178")
        buf.write("\u0174\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017bU\3\2\2\2\u017c\u017a\3\2\2")
        buf.write("\2\u017d\u017e\b,\1\2\u017e\u017f\5X-\2\u017f\u0186\3")
        buf.write("\2\2\2\u0180\u0181\f\4\2\2\u0181\u0182\5n8\2\u0182\u0183")
        buf.write("\5X-\2\u0183\u0185\3\2\2\2\u0184\u0180\3\2\2\2\u0185\u0188")
        buf.write("\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("W\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\7\35\2\2\u018a")
        buf.write("\u018d\5X-\2\u018b\u018d\5Z.\2\u018c\u0189\3\2\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018dY\3\2\2\2\u018e\u018f\7\27\2\2\u018f")
        buf.write("\u0192\5Z.\2\u0190\u0192\5\\/\2\u0191\u018e\3\2\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192[\3\2\2\2\u0193\u019c\7\25\2\2\u0194")
        buf.write("\u019c\7(\2\2\u0195\u019c\7\34\2\2\u0196\u019c\7/\2\2")
        buf.write("\u0197\u019c\5F$\2\u0198\u019c\5`\61\2\u0199\u019c\5^")
        buf.write("\60\2\u019a\u019c\5j\66\2\u019b\u0193\3\2\2\2\u019b\u0194")
        buf.write("\3\2\2\2\u019b\u0195\3\2\2\2\u019b\u0196\3\2\2\2\u019b")
        buf.write("\u0197\3\2\2\2\u019b\u0198\3\2\2\2\u019b\u0199\3\2\2\2")
        buf.write("\u019b\u019a\3\2\2\2\u019c]\3\2\2\2\u019d\u019e\7-\2\2")
        buf.write("\u019e\u019f\5N(\2\u019f\u01a0\7.\2\2\u01a0_\3\2\2\2\u01a1")
        buf.write("\u01a2\5d\63\2\u01a2\u01a3\7*\2\2\u01a3\u01a4\5b\62\2")
        buf.write("\u01a4\u01a5\7+\2\2\u01a5a\3\2\2\2\u01a6\u01a7\5N(\2\u01a7")
        buf.write("\u01a8\7,\2\2\u01a8\u01a9\5b\62\2\u01a9\u01ac\3\2\2\2")
        buf.write("\u01aa\u01ac\5N(\2\u01ab\u01a6\3\2\2\2\u01ab\u01aa\3\2")
        buf.write("\2\2\u01acc\3\2\2\2\u01ad\u01b0\7/\2\2\u01ae\u01b0\5F")
        buf.write("$\2\u01af\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0e\3\2")
        buf.write("\2\2\u01b1\u01b2\7/\2\2\u01b2\u01b3\7*\2\2\u01b3\u01b4")
        buf.write("\5h\65\2\u01b4\u01b5\7+\2\2\u01b5g\3\2\2\2\u01b6\u01b7")
        buf.write("\7\25\2\2\u01b7\u01b8\7,\2\2\u01b8\u01bb\5h\65\2\u01b9")
        buf.write("\u01bb\7\25\2\2\u01ba\u01b6\3\2\2\2\u01ba\u01b9\3\2\2")
        buf.write("\2\u01bbi\3\2\2\2\u01bc\u01bd\7*\2\2\u01bd\u01be\5l\67")
        buf.write("\2\u01be\u01bf\7+\2\2\u01bfk\3\2\2\2\u01c0\u01c1\5N(\2")
        buf.write("\u01c1\u01c2\7,\2\2\u01c2\u01c3\5l\67\2\u01c3\u01c6\3")
        buf.write("\2\2\2\u01c4\u01c6\5N(\2\u01c5\u01c0\3\2\2\2\u01c5\u01c4")
        buf.write("\3\2\2\2\u01c6m\3\2\2\2\u01c7\u01c8\t\3\2\2\u01c8o\3\2")
        buf.write("\2\2\u01c9\u01ca\t\4\2\2\u01caq\3\2\2\2\u01cb\u01cc\t")
        buf.write("\5\2\2\u01ccs\3\2\2\2\u01cd\u01ce\t\6\2\2\u01ceu\3\2\2")
        buf.write("\2$~\u0082\u0093\u0097\u009e\u00a6\u00aa\u00ae\u00b8\u00bc")
        buf.write("\u00d9\u00e5\u00f3\u010b\u0118\u011e\u012b\u0135\u013f")
        buf.write("\u014a\u0151\u0155\u015c\u0163\u016e\u017a\u0186\u018c")
        buf.write("\u0191\u019b\u01ab\u01af\u01ba\u01c5")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'number'", 
                     "'string'", "'bool'", "<INVALID>", "'<-'", "'-'", "'+'", 
                     "'*'", "'/'", "'%'", "<INVALID>", "'not'", "'and'", 
                     "'or'", "'...'", "'='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'=='", "<INVALID>", "<INVALID>", "'['", "']'", 
                     "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "RETURN", "VAR", "DYNAMIC", 
                      "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "ELIF", "BEGIN", "END", "NUMBER", "STRING", 
                      "BOOL", "NUMBERLIT", "ASSIGNMENTSIGN", "SUB", "ADD", 
                      "MUL", "DIV", "REMAIN", "BOOLEANLIT", "NEG", "CON", 
                      "DIS", "STRCON", "EQ", "NOTEQ", "LESS", "GREATER", 
                      "LESSSOREQ", "GREATEROREQ", "COMPARESTR", "STRINGLIT", 
                      "NEWLINE", "LEFTSQUARE", "RIGHTSQUARE", "COMMA", "OPENPARENTHESIS", 
                      "CLOSEPARENTHESIS", "IDENTIFIER", "WHITESPACE", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_runlist = 1
    RULE_run = 2
    RULE_funcdecl = 3
    RULE_parameterlist = 4
    RULE_parameterprime = 5
    RULE_param = 6
    RULE_newlinesep = 7
    RULE_endfuncdecl = 8
    RULE_ifstmt = 9
    RULE_eliflist = 10
    RULE_elselist = 11
    RULE_onlyifstmt = 12
    RULE_elifstmt = 13
    RULE_elsestmt = 14
    RULE_statement = 15
    RULE_blockstmt = 16
    RULE_statementlist = 17
    RULE_funcstmt = 18
    RULE_returnstmt = 19
    RULE_continuestmt = 20
    RULE_breakstmt = 21
    RULE_forstmt = 22
    RULE_assignstmt = 23
    RULE_lhs = 24
    RULE_elementarray = 25
    RULE_vardeclstmt = 26
    RULE_newlinelist = 27
    RULE_vardecl = 28
    RULE_varstartdecl = 29
    RULE_dynamicstartdecl = 30
    RULE_normaldecl = 31
    RULE_arraydecl = 32
    RULE_typ = 33
    RULE_funccall = 34
    RULE_argumentlist = 35
    RULE_argueprime = 36
    RULE_arguelement = 37
    RULE_expression = 38
    RULE_expression1 = 39
    RULE_expression2 = 40
    RULE_expression3 = 41
    RULE_expression4 = 42
    RULE_expression5 = 43
    RULE_expression6 = 44
    RULE_operand = 45
    RULE_subexpression = 46
    RULE_element_expression = 47
    RULE_index_operator = 48
    RULE_arrayexpression = 49
    RULE_arraylit = 50
    RULE_sizelist = 51
    RULE_arraytype = 52
    RULE_eleprime = 53
    RULE_multiplyingoperator = 54
    RULE_addingoperator = 55
    RULE_logicaloperator = 56
    RULE_relateoperator = 57

    ruleNames =  [ "program", "runlist", "run", "funcdecl", "parameterlist", 
                   "parameterprime", "param", "newlinesep", "endfuncdecl", 
                   "ifstmt", "eliflist", "elselist", "onlyifstmt", "elifstmt", 
                   "elsestmt", "statement", "blockstmt", "statementlist", 
                   "funcstmt", "returnstmt", "continuestmt", "breakstmt", 
                   "forstmt", "assignstmt", "lhs", "elementarray", "vardeclstmt", 
                   "newlinelist", "vardecl", "varstartdecl", "dynamicstartdecl", 
                   "normaldecl", "arraydecl", "typ", "funccall", "argumentlist", 
                   "argueprime", "arguelement", "expression", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "operand", "subexpression", "element_expression", 
                   "index_operator", "arrayexpression", "arraylit", "sizelist", 
                   "arraytype", "eleprime", "multiplyingoperator", "addingoperator", 
                   "logicaloperator", "relateoperator" ]

    EOF = Token.EOF
    COMMENT=1
    RETURN=2
    VAR=3
    DYNAMIC=4
    FUNC=5
    FOR=6
    UNTIL=7
    BY=8
    BREAK=9
    CONTINUE=10
    IF=11
    ELSE=12
    ELIF=13
    BEGIN=14
    END=15
    NUMBER=16
    STRING=17
    BOOL=18
    NUMBERLIT=19
    ASSIGNMENTSIGN=20
    SUB=21
    ADD=22
    MUL=23
    DIV=24
    REMAIN=25
    BOOLEANLIT=26
    NEG=27
    CON=28
    DIS=29
    STRCON=30
    EQ=31
    NOTEQ=32
    LESS=33
    GREATER=34
    LESSSOREQ=35
    GREATEROREQ=36
    COMPARESTR=37
    STRINGLIT=38
    NEWLINE=39
    LEFTSQUARE=40
    RIGHTSQUARE=41
    COMMA=42
    OPENPARENTHESIS=43
    CLOSEPARENTHESIS=44
    IDENTIFIER=45
    WHITESPACE=46
    ILLEGAL_ESCAPE=47
    UNCLOSE_STRING=48
    ERROR_CHAR=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlinesep(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesepContext,0)


        def runlist(self):
            return self.getTypedRuleContext(ZCodeParser.RunlistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.newlinesep()
            self.state = 117
            self.runlist()
            self.state = 118
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RunlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def run(self):
            return self.getTypedRuleContext(ZCodeParser.RunContext,0)


        def runlist(self):
            return self.getTypedRuleContext(ZCodeParser.RunlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_runlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRunlist" ):
                return visitor.visitRunlist(self)
            else:
                return visitor.visitChildren(self)




    def runlist(self):

        localctx = ZCodeParser.RunlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_runlist)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.run()
                self.state = 121
                self.runlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.run()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def vardeclstmt(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_run

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRun" ):
                return visitor.visitRun(self)
            else:
                return visitor.visitChildren(self)




    def run(self):

        localctx = ZCodeParser.RunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_run)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.funcdecl()
                pass
            elif token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.BOOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.vardeclstmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPENPARENTHESIS(self):
            return self.getToken(ZCodeParser.OPENPARENTHESIS, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterlistContext,0)


        def CLOSEPARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSEPARENTHESIS, 0)

        def newlinesep(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesepContext,0)


        def endfuncdecl(self):
            return self.getTypedRuleContext(ZCodeParser.EndfuncdeclContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(ZCodeParser.FUNC)
                self.state = 131
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 132
                self.match(ZCodeParser.OPENPARENTHESIS)
                self.state = 133
                self.parameterlist()
                self.state = 134
                self.match(ZCodeParser.CLOSEPARENTHESIS)
                self.state = 135
                self.newlinesep()
                self.state = 136
                self.endfuncdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(ZCodeParser.FUNC)
                self.state = 139
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 140
                self.match(ZCodeParser.OPENPARENTHESIS)
                self.state = 141
                self.parameterlist()
                self.state = 142
                self.match(ZCodeParser.CLOSEPARENTHESIS)
                self.state = 143
                self.newlinelist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameterlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterlist" ):
                return visitor.visitParameterlist(self)
            else:
                return visitor.visitChildren(self)




    def parameterlist(self):

        localctx = ZCodeParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameterlist)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.BOOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.parameterprime()
                pass
            elif token in [ZCodeParser.CLOSEPARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameterprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameterprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterprime" ):
                return visitor.visitParameterprime(self)
            else:
                return visitor.visitChildren(self)




    def parameterprime(self):

        localctx = ZCodeParser.ParameterprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameterprime)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.param()
                self.state = 152
                self.match(ZCodeParser.COMMA)
                self.state = 153
                self.parameterprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arraylit(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylitContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.typ()
                self.state = 159
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.typ()
                self.state = 162
                self.arraylit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinesepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlinesep

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlinesep" ):
                return visitor.visitNewlinesep(self)
            else:
                return visitor.visitChildren(self)




    def newlinesep(self):

        localctx = ZCodeParser.NewlinesepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_newlinesep)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.newlinelist()
                pass
            elif token in [ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.BOOL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndfuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_endfuncdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndfuncdecl" ):
                return visitor.visitEndfuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def endfuncdecl(self):

        localctx = ZCodeParser.EndfuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_endfuncdecl)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.blockstmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def onlyifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.OnlyifstmtContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def elselist(self):
            return self.getTypedRuleContext(ZCodeParser.ElselistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.onlyifstmt()
            self.state = 175
            self.eliflist()
            self.state = 176
            self.elselist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliflistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstmtContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_eliflist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliflist" ):
                return visitor.visitEliflist(self)
            else:
                return visitor.visitChildren(self)




    def eliflist(self):

        localctx = ZCodeParser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_eliflist)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.elifstmt()
                self.state = 179
                self.eliflist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElselistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elsestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElsestmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elselist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElselist" ):
                return visitor.visitElselist(self)
            else:
                return visitor.visitChildren(self)




    def elselist(self):

        localctx = ZCodeParser.ElselistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elselist)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.elsestmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OnlyifstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def OPENPARENTHESIS(self):
            return self.getToken(ZCodeParser.OPENPARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSEPARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSEPARENTHESIS, 0)

        def newlinesep(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesepContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_onlyifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOnlyifstmt" ):
                return visitor.visitOnlyifstmt(self)
            else:
                return visitor.visitChildren(self)




    def onlyifstmt(self):

        localctx = ZCodeParser.OnlyifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_onlyifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(ZCodeParser.IF)
            self.state = 189
            self.match(ZCodeParser.OPENPARENTHESIS)
            self.state = 190
            self.expression()
            self.state = 191
            self.match(ZCodeParser.CLOSEPARENTHESIS)
            self.state = 192
            self.newlinesep()
            self.state = 193
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def OPENPARENTHESIS(self):
            return self.getToken(ZCodeParser.OPENPARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSEPARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSEPARENTHESIS, 0)

        def newlinesep(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesepContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstmt" ):
                return visitor.visitElifstmt(self)
            else:
                return visitor.visitChildren(self)




    def elifstmt(self):

        localctx = ZCodeParser.ElifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(ZCodeParser.ELIF)
            self.state = 196
            self.match(ZCodeParser.OPENPARENTHESIS)
            self.state = 197
            self.expression()
            self.state = 198
            self.match(ZCodeParser.CLOSEPARENTHESIS)
            self.state = 199
            self.newlinesep()
            self.state = 200
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def newlinesep(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesepContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elsestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




    def elsestmt(self):

        localctx = ZCodeParser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_elsestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(ZCodeParser.ELSE)
            self.state = 203
            self.newlinesep()
            self.state = 204
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardeclstmt(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclstmtContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def funcstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FuncstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.vardeclstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.breakstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.continuestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 211
                self.returnstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 212
                self.funcstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 213
                self.blockstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 214
                self.ifstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newlinelist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinelistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,i)


        def statementlist(self):
            return self.getTypedRuleContext(ZCodeParser.StatementlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ZCodeParser.BEGIN)
            self.state = 218
            self.newlinelist()
            self.state = 219
            self.statementlist()
            self.state = 220
            self.match(ZCodeParser.END)
            self.state = 221
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statementlist(self):
            return self.getTypedRuleContext(ZCodeParser.StatementlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statementlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementlist" ):
                return visitor.visitStatementlist(self)
            else:
                return visitor.visitChildren(self)




    def statementlist(self):

        localctx = ZCodeParser.StatementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statementlist)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.BOOL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.statement()
                self.state = 224
                self.statementlist()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPENPARENTHESIS(self):
            return self.getToken(ZCodeParser.OPENPARENTHESIS, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def CLOSEPARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSEPARENTHESIS, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncstmt" ):
                return visitor.visitFuncstmt(self)
            else:
                return visitor.visitChildren(self)




    def funcstmt(self):

        localctx = ZCodeParser.FuncstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funcstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 230
            self.match(ZCodeParser.OPENPARENTHESIS)
            self.state = 231
            self.argumentlist()
            self.state = 232
            self.match(ZCodeParser.CLOSEPARENTHESIS)
            self.state = 233
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returnstmt)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(ZCodeParser.RETURN)
                self.state = 236
                self.expression()
                self.state = 237
                self.newlinelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(ZCodeParser.RETURN)
                self.state = 240
                self.newlinelist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ZCodeParser.CONTINUE)
            self.state = 244
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(ZCodeParser.BREAK)
            self.state = 247
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def newlinesep(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesepContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(ZCodeParser.FOR)
            self.state = 250
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 251
            self.match(ZCodeParser.UNTIL)
            self.state = 252
            self.expression()
            self.state = 253
            self.match(ZCodeParser.BY)
            self.state = 254
            self.expression()
            self.state = 255
            self.newlinesep()
            self.state = 256
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGNMENTSIGN(self):
            return self.getToken(ZCodeParser.ASSIGNMENTSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.lhs()
            self.state = 259
            self.match(ZCodeParser.ASSIGNMENTSIGN)
            self.state = 260
            self.expression()
            self.state = 261
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def elementarray(self):
            return self.getTypedRuleContext(ZCodeParser.ElementarrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_lhs)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.elementarray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementarrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTSQUARE(self):
            return self.getToken(ZCodeParser.LEFTSQUARE, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elementarray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementarray" ):
                return visitor.visitElementarray(self)
            else:
                return visitor.visitChildren(self)




    def elementarray(self):

        localctx = ZCodeParser.ElementarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elementarray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 268
            self.match(ZCodeParser.LEFTSQUARE)
            self.state = 269
            self.index_operator()
            self.state = 270
            self.match(ZCodeParser.RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardeclstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardeclstmt" ):
                return visitor.visitVardeclstmt(self)
            else:
                return visitor.visitChildren(self)




    def vardeclstmt(self):

        localctx = ZCodeParser.VardeclstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_vardeclstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.vardecl()
            self.state = 273
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlinelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlinelist" ):
                return visitor.visitNewlinelist(self)
            else:
                return visitor.visitChildren(self)




    def newlinelist(self):

        localctx = ZCodeParser.NewlinelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_newlinelist)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(ZCodeParser.NEWLINE)
                self.state = 277
                self.newlinelist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varstartdecl(self):
            return self.getTypedRuleContext(ZCodeParser.VarstartdeclContext,0)


        def dynamicstartdecl(self):
            return self.getTypedRuleContext(ZCodeParser.DynamicstartdeclContext,0)


        def normaldecl(self):
            return self.getTypedRuleContext(ZCodeParser.NormaldeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_vardecl)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.varstartdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.dynamicstartdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.normaldecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 283
                self.arraydecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarstartdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGNMENTSIGN(self):
            return self.getToken(ZCodeParser.ASSIGNMENTSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varstartdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarstartdecl" ):
                return visitor.visitVarstartdecl(self)
            else:
                return visitor.visitChildren(self)




    def varstartdecl(self):

        localctx = ZCodeParser.VarstartdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_varstartdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(ZCodeParser.VAR)
            self.state = 287
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 288
            self.match(ZCodeParser.ASSIGNMENTSIGN)
            self.state = 289
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DynamicstartdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGNMENTSIGN(self):
            return self.getToken(ZCodeParser.ASSIGNMENTSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamicstartdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamicstartdecl" ):
                return visitor.visitDynamicstartdecl(self)
            else:
                return visitor.visitChildren(self)




    def dynamicstartdecl(self):

        localctx = ZCodeParser.DynamicstartdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_dynamicstartdecl)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(ZCodeParser.DYNAMIC)
                self.state = 292
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 293
                self.match(ZCodeParser.ASSIGNMENTSIGN)
                self.state = 294
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(ZCodeParser.DYNAMIC)
                self.state = 296
                self.match(ZCodeParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormaldeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGNMENTSIGN(self):
            return self.getToken(ZCodeParser.ASSIGNMENTSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_normaldecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormaldecl" ):
                return visitor.visitNormaldecl(self)
            else:
                return visitor.visitChildren(self)




    def normaldecl(self):

        localctx = ZCodeParser.NormaldeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_normaldecl)
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.typ()
                self.state = 300
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 301
                self.match(ZCodeParser.ASSIGNMENTSIGN)
                self.state = 302
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.typ()
                self.state = 305
                self.match(ZCodeParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def arraylit(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylitContext,0)


        def ASSIGNMENTSIGN(self):
            return self.getToken(ZCodeParser.ASSIGNMENTSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_arraydecl)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.typ()
                self.state = 310
                self.arraylit()
                self.state = 311
                self.match(ZCodeParser.ASSIGNMENTSIGN)
                self.state = 312
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.typ()
                self.state = 315
                self.arraylit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.BOOL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPENPARENTHESIS(self):
            return self.getToken(ZCodeParser.OPENPARENTHESIS, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def CLOSEPARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSEPARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = ZCodeParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_funccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 322
            self.match(ZCodeParser.OPENPARENTHESIS)
            self.state = 323
            self.argumentlist()
            self.state = 324
            self.match(ZCodeParser.CLOSEPARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argueprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgueprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argumentlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentlist" ):
                return visitor.visitArgumentlist(self)
            else:
                return visitor.visitChildren(self)




    def argumentlist(self):

        localctx = ZCodeParser.ArgumentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_argumentlist)
        try:
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBERLIT, ZCodeParser.SUB, ZCodeParser.BOOLEANLIT, ZCodeParser.NEG, ZCodeParser.STRINGLIT, ZCodeParser.LEFTSQUARE, ZCodeParser.OPENPARENTHESIS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.argueprime()
                pass
            elif token in [ZCodeParser.CLOSEPARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgueprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arguelement(self):
            return self.getTypedRuleContext(ZCodeParser.ArguelementContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def argueprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgueprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argueprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgueprime" ):
                return visitor.visitArgueprime(self)
            else:
                return visitor.visitChildren(self)




    def argueprime(self):

        localctx = ZCodeParser.ArgueprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_argueprime)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.arguelement()
                self.state = 331
                self.match(ZCodeParser.COMMA)
                self.state = 332
                self.argueprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.arguelement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArguelementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def funccall(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arguelement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguelement" ):
                return visitor.visitArguelement(self)
            else:
                return visitor.visitChildren(self)




    def arguelement(self):

        localctx = ZCodeParser.ArguelementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_arguelement)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.funccall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def STRCON(self):
            return self.getToken(ZCodeParser.STRCON, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expression)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.expression1()
                self.state = 342
                self.match(ZCodeParser.STRCON)
                self.state = 343
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def relateoperator(self):
            return self.getTypedRuleContext(ZCodeParser.RelateoperatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = ZCodeParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expression1)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.expression2(0)
                self.state = 349
                self.relateoperator()
                self.state = 350
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression2Context,0)


        def logicaloperator(self):
            return self.getTypedRuleContext(ZCodeParser.LogicaloperatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 364
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 358
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 359
                    self.logicaloperator()
                    self.state = 360
                    self.expression3(0) 
                self.state = 366
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def addingoperator(self):
            return self.getTypedRuleContext(ZCodeParser.AddingoperatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expression3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 370
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 371
                    self.addingoperator()
                    self.state = 372
                    self.expression4(0) 
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def multiplyingoperator(self):
            return self.getTypedRuleContext(ZCodeParser.MultiplyingoperatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expression4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 382
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 383
                    self.multiplyingoperator()
                    self.state = 384
                    self.expression5() 
                self.state = 390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEG(self):
            return self.getToken(ZCodeParser.NEG, 0)

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expression5)
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.match(ZCodeParser.NEG)
                self.state = 392
                self.expression5()
                pass
            elif token in [ZCodeParser.NUMBERLIT, ZCodeParser.SUB, ZCodeParser.BOOLEANLIT, ZCodeParser.STRINGLIT, ZCodeParser.LEFTSQUARE, ZCodeParser.OPENPARENTHESIS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.expression6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expression6)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(ZCodeParser.SUB)
                self.state = 397
                self.expression6()
                pass
            elif token in [ZCodeParser.NUMBERLIT, ZCodeParser.BOOLEANLIT, ZCodeParser.STRINGLIT, ZCodeParser.LEFTSQUARE, ZCodeParser.OPENPARENTHESIS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(ZCodeParser.BOOLEANLIT, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def funccall(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallContext,0)


        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


        def subexpression(self):
            return self.getTypedRuleContext(ZCodeParser.SubexpressionContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(ZCodeParser.ArraytypeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_operand)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(ZCodeParser.NUMBERLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 403
                self.match(ZCodeParser.BOOLEANLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 404
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 405
                self.funccall()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 406
                self.element_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 407
                self.subexpression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 408
                self.arraytype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPARENTHESIS(self):
            return self.getToken(ZCodeParser.OPENPARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSEPARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSEPARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_subexpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpression" ):
                return visitor.visitSubexpression(self)
            else:
                return visitor.visitChildren(self)




    def subexpression(self):

        localctx = ZCodeParser.SubexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_subexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(ZCodeParser.OPENPARENTHESIS)
            self.state = 412
            self.expression()
            self.state = 413
            self.match(ZCodeParser.CLOSEPARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayexpression(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayexpressionContext,0)


        def LEFTSQUARE(self):
            return self.getToken(ZCodeParser.LEFTSQUARE, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expression" ):
                return visitor.visitElement_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_expression(self):

        localctx = ZCodeParser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.arrayexpression()
            self.state = 416
            self.match(ZCodeParser.LEFTSQUARE)
            self.state = 417
            self.index_operator()
            self.state = 418
            self.match(ZCodeParser.RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = ZCodeParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_index_operator)
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.expression()
                self.state = 421
                self.match(ZCodeParser.COMMA)
                self.state = 422
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def funccall(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayexpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayexpression" ):
                return visitor.visitArrayexpression(self)
            else:
                return visitor.visitChildren(self)




    def arrayexpression(self):

        localctx = ZCodeParser.ArrayexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arrayexpression)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.funccall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTSQUARE(self):
            return self.getToken(ZCodeParser.LEFTSQUARE, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = ZCodeParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 432
            self.match(ZCodeParser.LEFTSQUARE)
            self.state = 433
            self.sizelist()
            self.state = 434
            self.match(ZCodeParser.RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sizelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizelist" ):
                return visitor.visitSizelist(self)
            else:
                return visitor.visitChildren(self)




    def sizelist(self):

        localctx = ZCodeParser.SizelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_sizelist)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(ZCodeParser.NUMBERLIT)
                self.state = 437
                self.match(ZCodeParser.COMMA)
                self.state = 438
                self.sizelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.match(ZCodeParser.NUMBERLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTSQUARE(self):
            return self.getToken(ZCodeParser.LEFTSQUARE, 0)

        def eleprime(self):
            return self.getTypedRuleContext(ZCodeParser.EleprimeContext,0)


        def RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = ZCodeParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(ZCodeParser.LEFTSQUARE)
            self.state = 443
            self.eleprime()
            self.state = 444
            self.match(ZCodeParser.RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EleprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def eleprime(self):
            return self.getTypedRuleContext(ZCodeParser.EleprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_eleprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEleprime" ):
                return visitor.visitEleprime(self)
            else:
                return visitor.visitChildren(self)




    def eleprime(self):

        localctx = ZCodeParser.EleprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_eleprime)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.expression()
                self.state = 447
                self.match(ZCodeParser.COMMA)
                self.state = 448
                self.eleprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def REMAIN(self):
            return self.getToken(ZCodeParser.REMAIN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_multiplyingoperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplyingoperator" ):
                return visitor.visitMultiplyingoperator(self)
            else:
                return visitor.visitChildren(self)




    def multiplyingoperator(self):

        localctx = ZCodeParser.MultiplyingoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_multiplyingoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.REMAIN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddingoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_addingoperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddingoperator" ):
                return visitor.visitAddingoperator(self)
            else:
                return visitor.visitChildren(self)




    def addingoperator(self):

        localctx = ZCodeParser.AddingoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_addingoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.SUB or _la==ZCodeParser.ADD):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicaloperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CON(self):
            return self.getToken(ZCodeParser.CON, 0)

        def DIS(self):
            return self.getToken(ZCodeParser.DIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logicaloperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicaloperator" ):
                return visitor.visitLogicaloperator(self)
            else:
                return visitor.visitChildren(self)




    def logicaloperator(self):

        localctx = ZCodeParser.LogicaloperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_logicaloperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.CON or _la==ZCodeParser.DIS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelateoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def COMPARESTR(self):
            return self.getToken(ZCodeParser.COMPARESTR, 0)

        def NOTEQ(self):
            return self.getToken(ZCodeParser.NOTEQ, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def LESSSOREQ(self):
            return self.getToken(ZCodeParser.LESSSOREQ, 0)

        def GREATEROREQ(self):
            return self.getToken(ZCodeParser.GREATEROREQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relateoperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelateoperator" ):
                return visitor.visitRelateoperator(self)
            else:
                return visitor.visitChildren(self)




    def relateoperator(self):

        localctx = ZCodeParser.RelateoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_relateoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NOTEQ) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.LESSSOREQ) | (1 << ZCodeParser.GREATEROREQ) | (1 << ZCodeParser.COMPARESTR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[40] = self.expression2_sempred
        self._predicates[41] = self.expression3_sempred
        self._predicates[42] = self.expression4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




