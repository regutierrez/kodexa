// Generated from /Users/pdodds/src/kodexa/kodexa/resources/selector.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class selectorLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, NodeType=9, 
		Number=10, AxisName=11, PATHSEP=12, ABRPATH=13, LPAR=14, RPAR=15, LBRAC=16, 
		RBRAC=17, MINUS=18, PLUS=19, DOT=20, MUL=21, DOTDOT=22, AT=23, COMMA=24, 
		PIPE=25, LESS=26, MORE_=27, LE=28, GE=29, COLON=30, CC=31, APOS=32, QUOT=33, 
		Literal=34, Whitespace=35, NCName=36;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "NodeType", 
			"Number", "Digits", "AxisName", "PATHSEP", "ABRPATH", "LPAR", "RPAR", 
			"LBRAC", "RBRAC", "MINUS", "PLUS", "DOT", "MUL", "DOTDOT", "AT", "COMMA", 
			"PIPE", "LESS", "MORE_", "LE", "GE", "COLON", "CC", "APOS", "QUOT", "Literal", 
			"Whitespace", "NCName", "NCNameStartChar", "NCNameChar"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'processing-instruction'", "'or'", "'and'", "'='", "'!='", "'div'", 
			"'mod'", "'$'", null, null, null, "'/'", "'//'", "'('", "')'", "'['", 
			"']'", "'-'", "'+'", "'.'", "'*'", "'..'", "'@'", "','", "'|'", "'<'", 
			"'>'", "'<='", "'>='", "':'", "'::'", "'''", "'\"'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "NodeType", "Number", 
			"AxisName", "PATHSEP", "ABRPATH", "LPAR", "RPAR", "LBRAC", "RBRAC", "MINUS", 
			"PLUS", "DOT", "MUL", "DOTDOT", "AT", "COMMA", "PIPE", "LESS", "MORE_", 
			"LE", "GE", "COLON", "CC", "APOS", "QUOT", "Literal", "Whitespace", "NCName"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public selectorLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "selector.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2&\u0197\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b"+
		"\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a4\n\n\3\13\3\13\3\13\5\13\u00a9\n"+
		"\13\5\13\u00ab\n\13\3\13\3\13\5\13\u00af\n\13\3\f\6\f\u00b2\n\f\r\f\16"+
		"\f\u00b3\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r"+
		"\u013f\n\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23"+
		"\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31"+
		"\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37"+
		"\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\7$\u0174\n$\f$\16$\u0177\13$\3$\3"+
		"$\3$\7$\u017c\n$\f$\16$\u017f\13$\3$\5$\u0182\n$\3%\6%\u0185\n%\r%\16"+
		"%\u0186\3%\3%\3&\3&\7&\u018d\n&\f&\16&\u0190\13&\3\'\3\'\3(\3(\5(\u0196"+
		"\n(\2\2)\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\2\31\r\33\16"+
		"\35\17\37\20!\21#\22%\23\'\24)\25+\26-\27/\30\61\31\63\32\65\33\67\34"+
		"9\35;\36=\37? A!C\"E#G$I%K&M\2O\2\3\2\6\3\2$$\3\2))\5\2\13\f\17\17\"\""+
		"\7\2/\60\62;\u00b9\u00b9\u0302\u0371\u2041\u2042\3\21\2C\2\\\2a\2a\2c"+
		"\2|\2\u00c2\2\u00d8\2\u00da\2\u00f8\2\u00fa\2\u0301\2\u0372\2\u037f\2"+
		"\u0381\2\u2001\2\u200e\2\u200f\2\u2072\2\u2191\2\u2c02\2\u2ff1\2\u3003"+
		"\2\ud801\2\uf902\2\ufdd1\2\ufdf2\2\uffff\2\2\3\1\20\u01ac\2\3\3\2\2\2"+
		"\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2"+
		"\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2"+
		"\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2"+
		"\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2"+
		"\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2"+
		"\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\3"+
		"Q\3\2\2\2\5h\3\2\2\2\7k\3\2\2\2\to\3\2\2\2\13q\3\2\2\2\rt\3\2\2\2\17x"+
		"\3\2\2\2\21|\3\2\2\2\23\u00a3\3\2\2\2\25\u00ae\3\2\2\2\27\u00b1\3\2\2"+
		"\2\31\u013e\3\2\2\2\33\u0140\3\2\2\2\35\u0142\3\2\2\2\37\u0145\3\2\2\2"+
		"!\u0147\3\2\2\2#\u0149\3\2\2\2%\u014b\3\2\2\2\'\u014d\3\2\2\2)\u014f\3"+
		"\2\2\2+\u0151\3\2\2\2-\u0153\3\2\2\2/\u0155\3\2\2\2\61\u0158\3\2\2\2\63"+
		"\u015a\3\2\2\2\65\u015c\3\2\2\2\67\u015e\3\2\2\29\u0160\3\2\2\2;\u0162"+
		"\3\2\2\2=\u0165\3\2\2\2?\u0168\3\2\2\2A\u016a\3\2\2\2C\u016d\3\2\2\2E"+
		"\u016f\3\2\2\2G\u0181\3\2\2\2I\u0184\3\2\2\2K\u018a\3\2\2\2M\u0191\3\2"+
		"\2\2O\u0195\3\2\2\2QR\7r\2\2RS\7t\2\2ST\7q\2\2TU\7e\2\2UV\7g\2\2VW\7u"+
		"\2\2WX\7u\2\2XY\7k\2\2YZ\7p\2\2Z[\7i\2\2[\\\7/\2\2\\]\7k\2\2]^\7p\2\2"+
		"^_\7u\2\2_`\7v\2\2`a\7t\2\2ab\7w\2\2bc\7e\2\2cd\7v\2\2de\7k\2\2ef\7q\2"+
		"\2fg\7p\2\2g\4\3\2\2\2hi\7q\2\2ij\7t\2\2j\6\3\2\2\2kl\7c\2\2lm\7p\2\2"+
		"mn\7f\2\2n\b\3\2\2\2op\7?\2\2p\n\3\2\2\2qr\7#\2\2rs\7?\2\2s\f\3\2\2\2"+
		"tu\7f\2\2uv\7k\2\2vw\7x\2\2w\16\3\2\2\2xy\7o\2\2yz\7q\2\2z{\7f\2\2{\20"+
		"\3\2\2\2|}\7&\2\2}\22\3\2\2\2~\177\7e\2\2\177\u0080\7q\2\2\u0080\u0081"+
		"\7o\2\2\u0081\u0082\7o\2\2\u0082\u0083\7g\2\2\u0083\u0084\7p\2\2\u0084"+
		"\u00a4\7v\2\2\u0085\u0086\7v\2\2\u0086\u0087\7g\2\2\u0087\u0088\7z\2\2"+
		"\u0088\u00a4\7v\2\2\u0089\u008a\7r\2\2\u008a\u008b\7t\2\2\u008b\u008c"+
		"\7q\2\2\u008c\u008d\7e\2\2\u008d\u008e\7g\2\2\u008e\u008f\7u\2\2\u008f"+
		"\u0090\7u\2\2\u0090\u0091\7k\2\2\u0091\u0092\7p\2\2\u0092\u0093\7i\2\2"+
		"\u0093\u0094\7/\2\2\u0094\u0095\7k\2\2\u0095\u0096\7p\2\2\u0096\u0097"+
		"\7u\2\2\u0097\u0098\7v\2\2\u0098\u0099\7t\2\2\u0099\u009a\7w\2\2\u009a"+
		"\u009b\7e\2\2\u009b\u009c\7v\2\2\u009c\u009d\7k\2\2\u009d\u009e\7q\2\2"+
		"\u009e\u00a4\7p\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2"+
		"\7f\2\2\u00a2\u00a4\7g\2\2\u00a3~\3\2\2\2\u00a3\u0085\3\2\2\2\u00a3\u0089"+
		"\3\2\2\2\u00a3\u009f\3\2\2\2\u00a4\24\3\2\2\2\u00a5\u00aa\5\27\f\2\u00a6"+
		"\u00a8\7\60\2\2\u00a7\u00a9\5\27\f\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3"+
		"\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a6\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab"+
		"\u00af\3\2\2\2\u00ac\u00ad\7\60\2\2\u00ad\u00af\5\27\f\2\u00ae\u00a5\3"+
		"\2\2\2\u00ae\u00ac\3\2\2\2\u00af\26\3\2\2\2\u00b0\u00b2\4\62;\2\u00b1"+
		"\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2"+
		"\2\2\u00b4\30\3\2\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8"+
		"\7e\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb\7v\2\2\u00bb"+
		"\u00bc\7q\2\2\u00bc\u013f\7t\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7p\2\2"+
		"\u00bf\u00c0\7e\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7u\2\2\u00c2\u00c3"+
		"\7v\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7/\2\2\u00c6"+
		"\u00c7\7q\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7/\2\2\u00c9\u00ca\7u\2\2"+
		"\u00ca\u00cb\7g\2\2\u00cb\u00cc\7n\2\2\u00cc\u013f\7h\2\2\u00cd\u00ce"+
		"\7c\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7t\2\2\u00d1"+
		"\u00d2\7k\2\2\u00d2\u00d3\7d\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5\7v\2\2"+
		"\u00d5\u013f\7g\2\2\u00d6\u00d7\7e\2\2\u00d7\u00d8\7j\2\2\u00d8\u00d9"+
		"\7k\2\2\u00d9\u00da\7n\2\2\u00da\u013f\7f\2\2\u00db\u00dc\7f\2\2\u00dc"+
		"\u00dd\7g\2\2\u00dd\u00de\7u\2\2\u00de\u00df\7e\2\2\u00df\u00e0\7g\2\2"+
		"\u00e0\u00e1\7p\2\2\u00e1\u00e2\7f\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4"+
		"\7p\2\2\u00e4\u013f\7v\2\2\u00e5\u00e6\7f\2\2\u00e6\u00e7\7g\2\2\u00e7"+
		"\u00e8\7u\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb\7p\2\2"+
		"\u00eb\u00ec\7f\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef"+
		"\7v\2\2\u00ef\u00f0\7/\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7t\2\2\u00f2"+
		"\u00f3\7/\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7n\2\2"+
		"\u00f6\u013f\7h\2\2\u00f7\u00f8\7h\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa"+
		"\7n\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7y\2\2\u00fd"+
		"\u00fe\7k\2\2\u00fe\u00ff\7p\2\2\u00ff\u013f\7i\2\2\u0100\u0101\7h\2\2"+
		"\u0101\u0102\7q\2\2\u0102\u0103\7n\2\2\u0103\u0104\7n\2\2\u0104\u0105"+
		"\7q\2\2\u0105\u0106\7y\2\2\u0106\u0107\7k\2\2\u0107\u0108\7p\2\2\u0108"+
		"\u0109\7i\2\2\u0109\u010a\7/\2\2\u010a\u010b\7u\2\2\u010b\u010c\7k\2\2"+
		"\u010c\u010d\7d\2\2\u010d\u010e\7n\2\2\u010e\u010f\7k\2\2\u010f\u0110"+
		"\7p\2\2\u0110\u013f\7i\2\2\u0111\u0112\7p\2\2\u0112\u0113\7c\2\2\u0113"+
		"\u0114\7o\2\2\u0114\u0115\7g\2\2\u0115\u0116\7u\2\2\u0116\u0117\7r\2\2"+
		"\u0117\u0118\7c\2\2\u0118\u0119\7e\2\2\u0119\u013f\7g\2\2\u011a\u011b"+
		"\7r\2\2\u011b\u011c\7c\2\2\u011c\u011d\7t\2\2\u011d\u011e\7g\2\2\u011e"+
		"\u011f\7p\2\2\u011f\u013f\7v\2\2\u0120\u0121\7r\2\2\u0121\u0122\7t\2\2"+
		"\u0122\u0123\7g\2\2\u0123\u0124\7e\2\2\u0124\u0125\7g\2\2\u0125\u0126"+
		"\7f\2\2\u0126\u0127\7k\2\2\u0127\u0128\7p\2\2\u0128\u013f\7i\2\2\u0129"+
		"\u012a\7r\2\2\u012a\u012b\7t\2\2\u012b\u012c\7g\2\2\u012c\u012d\7e\2\2"+
		"\u012d\u012e\7g\2\2\u012e\u012f\7f\2\2\u012f\u0130\7k\2\2\u0130\u0131"+
		"\7p\2\2\u0131\u0132\7i\2\2\u0132\u0133\7/\2\2\u0133\u0134\7u\2\2\u0134"+
		"\u0135\7k\2\2\u0135\u0136\7d\2\2\u0136\u0137\7n\2\2\u0137\u0138\7k\2\2"+
		"\u0138\u0139\7p\2\2\u0139\u013f\7i\2\2\u013a\u013b\7u\2\2\u013b\u013c"+
		"\7g\2\2\u013c\u013d\7n\2\2\u013d\u013f\7h\2\2\u013e\u00b5\3\2\2\2\u013e"+
		"\u00bd\3\2\2\2\u013e\u00cd\3\2\2\2\u013e\u00d6\3\2\2\2\u013e\u00db\3\2"+
		"\2\2\u013e\u00e5\3\2\2\2\u013e\u00f7\3\2\2\2\u013e\u0100\3\2\2\2\u013e"+
		"\u0111\3\2\2\2\u013e\u011a\3\2\2\2\u013e\u0120\3\2\2\2\u013e\u0129\3\2"+
		"\2\2\u013e\u013a\3\2\2\2\u013f\32\3\2\2\2\u0140\u0141\7\61\2\2\u0141\34"+
		"\3\2\2\2\u0142\u0143\7\61\2\2\u0143\u0144\7\61\2\2\u0144\36\3\2\2\2\u0145"+
		"\u0146\7*\2\2\u0146 \3\2\2\2\u0147\u0148\7+\2\2\u0148\"\3\2\2\2\u0149"+
		"\u014a\7]\2\2\u014a$\3\2\2\2\u014b\u014c\7_\2\2\u014c&\3\2\2\2\u014d\u014e"+
		"\7/\2\2\u014e(\3\2\2\2\u014f\u0150\7-\2\2\u0150*\3\2\2\2\u0151\u0152\7"+
		"\60\2\2\u0152,\3\2\2\2\u0153\u0154\7,\2\2\u0154.\3\2\2\2\u0155\u0156\7"+
		"\60\2\2\u0156\u0157\7\60\2\2\u0157\60\3\2\2\2\u0158\u0159\7B\2\2\u0159"+
		"\62\3\2\2\2\u015a\u015b\7.\2\2\u015b\64\3\2\2\2\u015c\u015d\7~\2\2\u015d"+
		"\66\3\2\2\2\u015e\u015f\7>\2\2\u015f8\3\2\2\2\u0160\u0161\7@\2\2\u0161"+
		":\3\2\2\2\u0162\u0163\7>\2\2\u0163\u0164\7?\2\2\u0164<\3\2\2\2\u0165\u0166"+
		"\7@\2\2\u0166\u0167\7?\2\2\u0167>\3\2\2\2\u0168\u0169\7<\2\2\u0169@\3"+
		"\2\2\2\u016a\u016b\7<\2\2\u016b\u016c\7<\2\2\u016cB\3\2\2\2\u016d\u016e"+
		"\7)\2\2\u016eD\3\2\2\2\u016f\u0170\7$\2\2\u0170F\3\2\2\2\u0171\u0175\7"+
		"$\2\2\u0172\u0174\n\2\2\2\u0173\u0172\3\2\2\2\u0174\u0177\3\2\2\2\u0175"+
		"\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178\3\2\2\2\u0177\u0175\3\2"+
		"\2\2\u0178\u0182\7$\2\2\u0179\u017d\7)\2\2\u017a\u017c\n\3\2\2\u017b\u017a"+
		"\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e"+
		"\u0180\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0182\7)\2\2\u0181\u0171\3\2"+
		"\2\2\u0181\u0179\3\2\2\2\u0182H\3\2\2\2\u0183\u0185\t\4\2\2\u0184\u0183"+
		"\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187"+
		"\u0188\3\2\2\2\u0188\u0189\b%\2\2\u0189J\3\2\2\2\u018a\u018e\5M\'\2\u018b"+
		"\u018d\5O(\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018c\3\2\2"+
		"\2\u018e\u018f\3\2\2\2\u018fL\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192"+
		"\t\6\2\2\u0192N\3\2\2\2\u0193\u0196\5M\'\2\u0194\u0196\t\5\2\2\u0195\u0193"+
		"\3\2\2\2\u0195\u0194\3\2\2\2\u0196P\3\2\2\2\17\2\u00a3\u00a8\u00aa\u00ae"+
		"\u00b3\u013e\u0175\u017d\u0181\u0186\u018e\u0195\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}