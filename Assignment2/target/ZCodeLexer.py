# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0198\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\7\2z\n\2\f\2\16\2}\13\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\5\24\u00e1")
        buf.write("\n\24\3\24\5\24\u00e4\n\24\3\25\6\25\u00e7\n\25\r\25\16")
        buf.write("\25\u00e8\3\26\3\26\7\26\u00ed\n\26\f\26\16\26\u00f0\13")
        buf.write("\26\3\27\3\27\5\27\u00f4\n\27\3\27\6\27\u00f7\n\27\r\27")
        buf.write("\16\27\u00f8\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3")
        buf.write("\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0111\n\36\3\37\3\37\3\37\3\37\3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3")
        buf.write("*\7*\u0139\n*\f*\16*\u013c\13*\3*\3*\3*\3*\3*\5*\u0143")
        buf.write("\n*\3*\3*\5*\u0147\n*\3*\3*\3+\3+\3+\3+\3+\5+\u0150\n")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u0161")
        buf.write("\n/\3\60\3\60\3\60\5\60\u0166\n\60\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\7\66")
        buf.write("\u0176\n\66\f\66\16\66\u0179\13\66\3\67\3\67\3\67\3\67")
        buf.write("\38\38\78\u0181\n8\f8\168\u0184\138\38\38\38\38\39\39")
        buf.write("\79\u018c\n9\f9\169\u018f\139\39\59\u0192\n9\39\39\3:")
        buf.write("\3:\3:\2\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\2+\2")
        buf.write("-\2/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C ")
        buf.write("E!G\"I#K$M%O&Q\'S(U\2W\2Y\2[\2]\2_)a*c+e,g-i.k/m\60o\61")
        buf.write("q\62s\63\3\2\17\4\2\f\f\17\17\3\2\62;\4\2GGgg\4\2--//")
        buf.write("\5\2$$))^^\6\2\f\f\17\17$$^^\3\2))\3\2$$\7\2ddhhppttv")
        buf.write("v\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\13\16\16\"\"\4\3\f\f")
        buf.write("\17\17\2\u01a3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3")
        buf.write("u\3\2\2\2\5\u0080\3\2\2\2\7\u0087\3\2\2\2\t\u008b\3\2")
        buf.write("\2\2\13\u0093\3\2\2\2\r\u0098\3\2\2\2\17\u009c\3\2\2\2")
        buf.write("\21\u00a2\3\2\2\2\23\u00a5\3\2\2\2\25\u00ab\3\2\2\2\27")
        buf.write("\u00b4\3\2\2\2\31\u00b7\3\2\2\2\33\u00bc\3\2\2\2\35\u00c1")
        buf.write("\3\2\2\2\37\u00c7\3\2\2\2!\u00cb\3\2\2\2#\u00d2\3\2\2")
        buf.write("\2%\u00d9\3\2\2\2\'\u00de\3\2\2\2)\u00e6\3\2\2\2+\u00ea")
        buf.write("\3\2\2\2-\u00f1\3\2\2\2/\u00fa\3\2\2\2\61\u00fd\3\2\2")
        buf.write("\2\63\u00ff\3\2\2\2\65\u0101\3\2\2\2\67\u0103\3\2\2\2")
        buf.write("9\u0105\3\2\2\2;\u0110\3\2\2\2=\u0112\3\2\2\2?\u0116\3")
        buf.write("\2\2\2A\u011a\3\2\2\2C\u011d\3\2\2\2E\u0121\3\2\2\2G\u0123")
        buf.write("\3\2\2\2I\u0126\3\2\2\2K\u0128\3\2\2\2M\u012a\3\2\2\2")
        buf.write("O\u012d\3\2\2\2Q\u0130\3\2\2\2S\u0146\3\2\2\2U\u014f\3")
        buf.write("\2\2\2W\u0151\3\2\2\2Y\u0153\3\2\2\2[\u0155\3\2\2\2]\u0160")
        buf.write("\3\2\2\2_\u0165\3\2\2\2a\u0169\3\2\2\2c\u016b\3\2\2\2")
        buf.write("e\u016d\3\2\2\2g\u016f\3\2\2\2i\u0171\3\2\2\2k\u0173\3")
        buf.write("\2\2\2m\u017a\3\2\2\2o\u017e\3\2\2\2q\u0189\3\2\2\2s\u0195")
        buf.write("\3\2\2\2uv\7%\2\2vw\7%\2\2w{\3\2\2\2xz\n\2\2\2yx\3\2\2")
        buf.write("\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~")
        buf.write("\177\b\2\2\2\177\4\3\2\2\2\u0080\u0081\7t\2\2\u0081\u0082")
        buf.write("\7g\2\2\u0082\u0083\7v\2\2\u0083\u0084\7w\2\2\u0084\u0085")
        buf.write("\7t\2\2\u0085\u0086\7p\2\2\u0086\6\3\2\2\2\u0087\u0088")
        buf.write("\7x\2\2\u0088\u0089\7c\2\2\u0089\u008a\7t\2\2\u008a\b")
        buf.write("\3\2\2\2\u008b\u008c\7f\2\2\u008c\u008d\7{\2\2\u008d\u008e")
        buf.write("\7p\2\2\u008e\u008f\7c\2\2\u008f\u0090\7o\2\2\u0090\u0091")
        buf.write("\7k\2\2\u0091\u0092\7e\2\2\u0092\n\3\2\2\2\u0093\u0094")
        buf.write("\7h\2\2\u0094\u0095\7w\2\2\u0095\u0096\7p\2\2\u0096\u0097")
        buf.write("\7e\2\2\u0097\f\3\2\2\2\u0098\u0099\7h\2\2\u0099\u009a")
        buf.write("\7q\2\2\u009a\u009b\7t\2\2\u009b\16\3\2\2\2\u009c\u009d")
        buf.write("\7w\2\2\u009d\u009e\7p\2\2\u009e\u009f\7v\2\2\u009f\u00a0")
        buf.write("\7k\2\2\u00a0\u00a1\7n\2\2\u00a1\20\3\2\2\2\u00a2\u00a3")
        buf.write("\7d\2\2\u00a3\u00a4\7{\2\2\u00a4\22\3\2\2\2\u00a5\u00a6")
        buf.write("\7d\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7m\2\2\u00aa\24\3\2\2\2\u00ab\u00ac")
        buf.write("\7e\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af")
        buf.write("\7v\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7g\2\2\u00b3\26\3\2\2\2\u00b4\u00b5")
        buf.write("\7k\2\2\u00b5\u00b6\7h\2\2\u00b6\30\3\2\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\32\3\2\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be")
        buf.write("\7n\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7h\2\2\u00c0\34")
        buf.write("\3\2\2\2\u00c1\u00c2\7d\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4")
        buf.write("\7i\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\36")
        buf.write("\3\2\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca")
        buf.write("\7f\2\2\u00ca \3\2\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd")
        buf.write("\7w\2\2\u00cd\u00ce\7o\2\2\u00ce\u00cf\7d\2\2\u00cf\u00d0")
        buf.write("\7g\2\2\u00d0\u00d1\7t\2\2\u00d1\"\3\2\2\2\u00d2\u00d3")
        buf.write("\7u\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7i\2\2\u00d8$\3")
        buf.write("\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7q\2\2\u00dc\u00dd\7n\2\2\u00dd&\3\2\2\2\u00de\u00e0")
        buf.write("\5)\25\2\u00df\u00e1\5+\26\2\u00e0\u00df\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00e4\5-\27\2")
        buf.write("\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4(\3\2\2")
        buf.write("\2\u00e5\u00e7\t\3\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8")
        buf.write("\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write("*\3\2\2\2\u00ea\u00ee\7\60\2\2\u00eb\u00ed\t\3\2\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2")
        buf.write("\u00ee\u00ef\3\2\2\2\u00ef,\3\2\2\2\u00f0\u00ee\3\2\2")
        buf.write("\2\u00f1\u00f3\t\4\2\2\u00f2\u00f4\t\5\2\2\u00f3\u00f2")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f6\3\2\2\2\u00f5")
        buf.write("\u00f7\t\3\2\2\u00f6\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9.\3\2\2")
        buf.write("\2\u00fa\u00fb\7>\2\2\u00fb\u00fc\7/\2\2\u00fc\60\3\2")
        buf.write("\2\2\u00fd\u00fe\7/\2\2\u00fe\62\3\2\2\2\u00ff\u0100\7")
        buf.write("-\2\2\u0100\64\3\2\2\2\u0101\u0102\7,\2\2\u0102\66\3\2")
        buf.write("\2\2\u0103\u0104\7\61\2\2\u01048\3\2\2\2\u0105\u0106\7")
        buf.write("\'\2\2\u0106:\3\2\2\2\u0107\u0108\7v\2\2\u0108\u0109\7")
        buf.write("t\2\2\u0109\u010a\7w\2\2\u010a\u0111\7g\2\2\u010b\u010c")
        buf.write("\7h\2\2\u010c\u010d\7c\2\2\u010d\u010e\7n\2\2\u010e\u010f")
        buf.write("\7u\2\2\u010f\u0111\7g\2\2\u0110\u0107\3\2\2\2\u0110\u010b")
        buf.write("\3\2\2\2\u0111<\3\2\2\2\u0112\u0113\7p\2\2\u0113\u0114")
        buf.write("\7q\2\2\u0114\u0115\7v\2\2\u0115>\3\2\2\2\u0116\u0117")
        buf.write("\7c\2\2\u0117\u0118\7p\2\2\u0118\u0119\7f\2\2\u0119@\3")
        buf.write("\2\2\2\u011a\u011b\7q\2\2\u011b\u011c\7t\2\2\u011cB\3")
        buf.write("\2\2\2\u011d\u011e\7\60\2\2\u011e\u011f\7\60\2\2\u011f")
        buf.write("\u0120\7\60\2\2\u0120D\3\2\2\2\u0121\u0122\7?\2\2\u0122")
        buf.write("F\3\2\2\2\u0123\u0124\7#\2\2\u0124\u0125\7?\2\2\u0125")
        buf.write("H\3\2\2\2\u0126\u0127\7>\2\2\u0127J\3\2\2\2\u0128\u0129")
        buf.write("\7@\2\2\u0129L\3\2\2\2\u012a\u012b\7>\2\2\u012b\u012c")
        buf.write("\7?\2\2\u012cN\3\2\2\2\u012d\u012e\7@\2\2\u012e\u012f")
        buf.write("\7?\2\2\u012fP\3\2\2\2\u0130\u0131\7?\2\2\u0131\u0132")
        buf.write("\7?\2\2\u0132R\3\2\2\2\u0133\u0134\5Y-\2\u0134\u0135\5")
        buf.write("Y-\2\u0135\u0147\3\2\2\2\u0136\u013a\5Y-\2\u0137\u0139")
        buf.write("\5U+\2\u0138\u0137\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0142\3\2\2\2\u013c")
        buf.write("\u013a\3\2\2\2\u013d\u013e\5W,\2\u013e\u013f\5Y-\2\u013f")
        buf.write("\u0143\3\2\2\2\u0140\u0143\n\6\2\2\u0141\u0143\5]/\2\u0142")
        buf.write("\u013d\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144\u0145\5Y-\2\u0145\u0147\3\2")
        buf.write("\2\2\u0146\u0133\3\2\2\2\u0146\u0136\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0149\b*\3\2\u0149T\3\2\2\2\u014a\u014b")
        buf.write("\5W,\2\u014b\u014c\5Y-\2\u014c\u0150\3\2\2\2\u014d\u0150")
        buf.write("\n\7\2\2\u014e\u0150\5]/\2\u014f\u014a\3\2\2\2\u014f\u014d")
        buf.write("\3\2\2\2\u014f\u014e\3\2\2\2\u0150V\3\2\2\2\u0151\u0152")
        buf.write("\t\b\2\2\u0152X\3\2\2\2\u0153\u0154\t\t\2\2\u0154Z\3\2")
        buf.write("\2\2\u0155\u0156\7^\2\2\u0156\\\3\2\2\2\u0157\u0158\5")
        buf.write("[.\2\u0158\u0159\t\n\2\2\u0159\u0161\3\2\2\2\u015a\u015b")
        buf.write("\5[.\2\u015b\u015c\5W,\2\u015c\u0161\3\2\2\2\u015d\u015e")
        buf.write("\5[.\2\u015e\u015f\5[.\2\u015f\u0161\3\2\2\2\u0160\u0157")
        buf.write("\3\2\2\2\u0160\u015a\3\2\2\2\u0160\u015d\3\2\2\2\u0161")
        buf.write("^\3\2\2\2\u0162\u0163\7\17\2\2\u0163\u0166\7\f\2\2\u0164")
        buf.write("\u0166\7\f\2\2\u0165\u0162\3\2\2\2\u0165\u0164\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167\u0168\b\60\4\2\u0168`\3\2\2")
        buf.write("\2\u0169\u016a\7]\2\2\u016ab\3\2\2\2\u016b\u016c\7_\2")
        buf.write("\2\u016cd\3\2\2\2\u016d\u016e\7.\2\2\u016ef\3\2\2\2\u016f")
        buf.write("\u0170\7*\2\2\u0170h\3\2\2\2\u0171\u0172\7+\2\2\u0172")
        buf.write("j\3\2\2\2\u0173\u0177\t\13\2\2\u0174\u0176\t\f\2\2\u0175")
        buf.write("\u0174\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2")
        buf.write("\u0177\u0178\3\2\2\2\u0178l\3\2\2\2\u0179\u0177\3\2\2")
        buf.write("\2\u017a\u017b\t\r\2\2\u017b\u017c\3\2\2\2\u017c\u017d")
        buf.write("\b\67\2\2\u017dn\3\2\2\2\u017e\u0182\5Y-\2\u017f\u0181")
        buf.write("\5U+\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0185\u0186\5[.\2\u0186\u0187\n\n\2\2\u0187")
        buf.write("\u0188\b8\5\2\u0188p\3\2\2\2\u0189\u018d\5Y-\2\u018a\u018c")
        buf.write("\5U+\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0191\3\2\2\2\u018f")
        buf.write("\u018d\3\2\2\2\u0190\u0192\t\16\2\2\u0191\u0190\3\2\2")
        buf.write("\2\u0192\u0193\3\2\2\2\u0193\u0194\b9\6\2\u0194r\3\2\2")
        buf.write("\2\u0195\u0196\13\2\2\2\u0196\u0197\b:\7\2\u0197t\3\2")
        buf.write("\2\2\25\2{\u00e0\u00e3\u00e8\u00ee\u00f3\u00f8\u0110\u013a")
        buf.write("\u0142\u0146\u014f\u0160\u0165\u0177\u0182\u018d\u0191")
        buf.write("\b\b\2\2\3*\2\3\60\3\38\4\39\5\3:\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    RETURN = 2
    VAR = 3
    DYNAMIC = 4
    FUNC = 5
    FOR = 6
    UNTIL = 7
    BY = 8
    BREAK = 9
    CONTINUE = 10
    IF = 11
    ELSE = 12
    ELIF = 13
    BEGIN = 14
    END = 15
    NUMBER = 16
    STRING = 17
    BOOL = 18
    NUMBERLIT = 19
    ASSIGNMENTSIGN = 20
    SUB = 21
    ADD = 22
    MUL = 23
    DIV = 24
    REMAIN = 25
    BOOLEANLIT = 26
    NEG = 27
    CON = 28
    DIS = 29
    STRCON = 30
    EQ = 31
    NOTEQ = 32
    LESS = 33
    GREATER = 34
    LESSSOREQ = 35
    GREATEROREQ = 36
    COMPARESTR = 37
    STRINGLIT = 38
    NEWLINE = 39
    LEFTSQUARE = 40
    RIGHTSQUARE = 41
    COMMA = 42
    OPENPARENTHESIS = 43
    CLOSEPARENTHESIS = 44
    IDENTIFIER = 45
    WHITESPACE = 46
    ILLEGAL_ESCAPE = 47
    UNCLOSE_STRING = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'number'", "'string'", "'bool'", "'<-'", 
            "'-'", "'+'", "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", 
            "'...'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=='", 
            "'['", "']'", "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
            "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
            "NUMBER", "STRING", "BOOL", "NUMBERLIT", "ASSIGNMENTSIGN", "SUB", 
            "ADD", "MUL", "DIV", "REMAIN", "BOOLEANLIT", "NEG", "CON", "DIS", 
            "STRCON", "EQ", "NOTEQ", "LESS", "GREATER", "LESSSOREQ", "GREATEROREQ", 
            "COMPARESTR", "STRINGLIT", "NEWLINE", "LEFTSQUARE", "RIGHTSQUARE", 
            "COMMA", "OPENPARENTHESIS", "CLOSEPARENTHESIS", "IDENTIFIER", 
            "WHITESPACE", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
                  "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", 
                  "BEGIN", "END", "NUMBER", "STRING", "BOOL", "NUMBERLIT", 
                  "INTPART", "DECPART", "EXPPART", "ASSIGNMENTSIGN", "SUB", 
                  "ADD", "MUL", "DIV", "REMAIN", "BOOLEANLIT", "NEG", "CON", 
                  "DIS", "STRCON", "EQ", "NOTEQ", "LESS", "GREATER", "LESSSOREQ", 
                  "GREATEROREQ", "COMPARESTR", "STRINGLIT", "INSIDE_STRING", 
                  "SINGLE_QUOTE", "DOUBLE_QUOTE", "BACKSLASH", "ESCAPE_SEQUENCES", 
                  "NEWLINE", "LEFTSQUARE", "RIGHTSQUARE", "COMMA", "OPENPARENTHESIS", 
                  "CLOSEPARENTHESIS", "IDENTIFIER", "WHITESPACE", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[40] = self.STRINGLIT_action 
            actions[46] = self.NEWLINE_action 
            actions[54] = self.ILLEGAL_ESCAPE_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = '\n'
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:].replace("\r", "").replace("\n", ""))
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


