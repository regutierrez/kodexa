# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion = "3.10"
_lextokens = set(
    (
        "ABBREV_AXIS_AT",
        "ABBREV_PATH_SEP",
        "ABBREV_STEP_PARENT",
        "ABBREV_STEP_SELF",
        "AND_OP",
        "AXISNAME",
        "AXIS_SEP",
        "CLOSE_BRACKET",
        "CLOSE_PAREN",
        "COLON",
        "COMMA",
        "DIV_OP",
        "DOLLAR",
        "EQUAL_OP",
        "FLOAT",
        "FUNCNAME",
        "INTEGER",
        "INTERSECT_OP",
        "LITERAL",
        "MINUS_OP",
        "MOD_OP",
        "MULT_OP",
        "NCNAME",
        "NODETYPE",
        "OPEN_BRACKET",
        "OPEN_PAREN",
        "OR_OP",
        "PATH_SEP",
        "PIPELINE_OP",
        "PLUS_OP",
        "REL_OP",
        "STAR_OP",
        "UNION_OP",
    )
)
_lexreflags = 32
_lexliterals = ""
_lexstateinfo = {"INITIAL": "inclusive"}
_lexstatere = {
    "INITIAL": [
        (
            "(?P<t_LITERAL>\"[^\"]*\"|'[^']*')|(?P<t_FLOAT>\\d+\\.\\d*|\\.\\d+)|(?P<t_INTEGER>\\d+)|(?P<t_NCNAME>(([A-Z]|_|[a-z]|\\xc0-\\xd6]|[\\xd8-\\xf6]|[\\xf8-\\u02ff]|[\\u0370-\\u037d]|[\\u037f-\\u1fff]|[\\u200c-\\u200d]|[\\u2070-\\u218f]|[\\u2c00-\\u2fef]|[\\u3001-\\uD7FF]|[\\uF900-\\uFDCF]|[\\uFDF0-\\uFFFD]|[\\U00010000-\\U000EFFFF]))(([A-Z]|_|[a-z]|\\xc0-\\xd6]|[\\xd8-\\xf6]|[\\xf8-\\u02ff]|[\\u0370-\\u037d]|[\\u037f-\\u1fff]|[\\u200c-\\u200d]|[\\u2070-\\u218f]|[\\u2c00-\\u2fef]|[\\u3001-\\uD7FF]|[\\uF900-\\uFDCF]|[\\uFDF0-\\uFFFD]|[\\U00010000-\\U000EFFFF])|[-.0-9\\xb7\\u0300-\\u036f\\u203f-\\u2040])*)|(?P<t_REL_OP>[<>]=?)|(?P<t_ABBREV_STEP_PARENT>\\.\\.)|(?P<t_EQUAL_OP>!?=)|(?P<t_ABBREV_PATH_SEP>//)|(?P<t_ABBREV_STEP_SELF>\\.)|(?P<t_AXIS_SEP>::)|(?P<t_CLOSE_BRACKET>\\])|(?P<t_CLOSE_PAREN>\\))|(?P<t_DOLLAR>\\$)|(?P<t_OPEN_BRACKET>\\[)|(?P<t_OPEN_PAREN>\\()|(?P<t_PIPELINE_OP>::)|(?P<t_PLUS_OP>\\+)|(?P<t_STAR_OP>\\*)|(?P<t_UNION_OP>\\|)|(?P<t_ABBREV_AXIS_AT>@)|(?P<t_COLON>:)|(?P<t_COMMA>,)|(?P<t_MINUS_OP>-)|(?P<t_PATH_SEP>/)",
            [
                None,
                ("t_LITERAL", "LITERAL"),
                ("t_FLOAT", "FLOAT"),
                ("t_INTEGER", "INTEGER"),
                (None, "NCNAME"),
                None,
                None,
                None,
                None,
                (None, "REL_OP"),
                (None, "ABBREV_STEP_PARENT"),
                (None, "EQUAL_OP"),
                (None, "ABBREV_PATH_SEP"),
                (None, "ABBREV_STEP_SELF"),
                (None, "AXIS_SEP"),
                (None, "CLOSE_BRACKET"),
                (None, "CLOSE_PAREN"),
                (None, "DOLLAR"),
                (None, "OPEN_BRACKET"),
                (None, "OPEN_PAREN"),
                (None, "PIPELINE_OP"),
                (None, "PLUS_OP"),
                (None, "STAR_OP"),
                (None, "UNION_OP"),
                (None, "ABBREV_AXIS_AT"),
                (None, "COLON"),
                (None, "COMMA"),
                (None, "MINUS_OP"),
                (None, "PATH_SEP"),
            ],
        )
    ]
}
_lexstateignore = {"INITIAL": " \t\r\n"}
_lexstateerrorf = {"INITIAL": "t_error"}
_lexstateeoff = {}
