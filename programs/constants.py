# TODO add comments

#====================================================================
# General New Testament constants
#====================================================================


tosyr = str.maketrans('ABGDHOZKY;CLMNSEI/XRWT','ܐܒܓܕܗܘܙܚܛܝܟܠܡܢܣܥܦܨܩܪܫܬ', ',')

NT_BOOKS = (
    ('Matt',   (25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36,
                39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75, 66, 20)),
    ('Mark',   (45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72,
                47, 20)),
    ('Luke',   (80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35,
                32, 31, 37, 43, 48, 47, 38, 71, 56, 53)),
    ('John',   (51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31,
                27, 33, 26, 40, 42, 31, 25)),
    ('Acts',   (26, 47, 26, 37, 42, 15, 60, 40, 43, 48, 30, 25, 52, 28,
                41, 40, 34, 28, 41, 38, 40, 30, 35, 27, 27, 32, 44, 31)),
    ('Rom',    (32, 29, 31, 25, 21, 23, 25, 39, 33, 21, 36, 21, 14, 23,
                33, 27)),
    ('1Cor',   (31, 16, 23, 21, 13, 20, 40, 13, 27, 33, 34, 31, 13, 40,
                58, 24)),
    ('2Cor',   (24, 17, 18, 18, 21, 18, 16, 24, 15, 18, 33, 21, 14)),
    ('Gal',    (24, 21, 29, 31, 26, 18)),
    ('Eph',    (23, 22, 21, 32, 33, 24)),
    ('Phil',   (30, 30, 21, 23)),
    ('Col',    (29, 23, 25, 18)),
    ('1Thess', (10, 20, 13, 18, 28)),
    ('2Thess', (12, 17, 18)),
    ('1Tim',   (20, 15, 16, 16, 25, 21)),
    ('2Tim',   (18, 26, 17, 22)),
    ('Titus',  (16, 15, 15)),
    ('Phlm',   (25,)),
    ('Heb',    (14, 18, 19, 16, 14, 20, 28, 13, 28, 39, 40, 29, 25)),
    ('James',  (27, 26, 18, 17, 20)),
    ('1Peter', (25, 25, 22, 19, 14)),
    ('2Peter', (21, 22, 18)),
    ('1John',  (10, 29, 24, 21, 21)),
    ('2John',  (13,)),
    ('3John',  (15,)),
    ('Jude',   (25,)),
    ('Rev',    (20, 29, 22, 11, 14, 17, 17, 13, 21, 11, 19, 17, 18, 20,
                8, 21, 18, 24, 21, 15, 27, 20)))
BOOK_EN = tuple('''
    Matthew
    Mark
    Luke
    John
    Acts
    Romans
    1_Corinthians
    2_Corinthians
    Galatians
    Ephesians
    Philippians
    Colossians
    1_Thessalonians
    2_Thessalonians
    1_Timothy
    2_Timothy
    Titus
    Philemon
    Hebrews
    James
    1_Peter
    2_Peter
    1_John
    2_John
    3_John
    Jude
    Revelation
'''.strip().split())

#====================================================================
# SyrNT constants
#====================================================================
class SyrNT:

    # SyroMorph Data format
    #
    # See also morph.app.SyriacDatum.java,
    # edu.byu.nlp.ccash.syriacmorphtag.gwt.SyrTagValues and the data files themselves.
    #
    # e.g., CTBA|CTBA#CTBA#CTB###0#0#0#3#1#0#2#0#0#2#0#0#2#0#0#0#0#0 ...
    #
    # On the left of the bar is the full token. On the right of the bar are the
    # annotations for that token.  All of the tokens in a verse are on the same line
    # separated by a space.
    #
    # The annotations are as follows:
    ANNOTATIONS = (             # <index> <name>
        ('stem', None),         #  0 stem
        ('lexeme', None),       #  1 lexeme (baseform)
        ('root', None),         #  2 root
        ('prefix', None),       #  3 prefix
        ('suffix', None),       #  4 suffix
        ('seyame', (0, 1)),       #  5 seyame
        ('vs',  #  6 verb conjugation
            ('n/a',                 #  0 n/a
             'peal',                #  1 peal
             'ethpeal',             #  2 ethpeal
             'pael',                #  3 pael
             'ethpael',             #  4 ethpael
             'aphel',               #  5 aphel
             'ettaphal',            #  6 ettaphal
             'shaphel',             #  7 shaphel
             'eshtaphal',           #  8 eshtaphal
             'saphel',              #  9 saphel
             'estaphal',            # 10 estaphal
             'pauel',               # 11 pauel
             'ethpaual',            # 12 ethpaual
             'paiel',               # 13 paiel
             'ethpaial',            # 14 ethpaial
             'palpal',              # 15 palpal
             'ethpalpal',           # 16 ethpalpal
             'palpel',              # 17 palpel
             'ethpalpal2',          # 18 ethpalpal2
             'pamel',               # 19 pamel
             'ethpamel',            # 20 ethpamel
             'parel',               # 21 parel
             'ethparal',            # 22 ethparal
             'pali',                # 23 pali
             'ethpali',             # 24 ethpali
             'pahli',               # 25 pahli
             'ethpahli',            # 26 ethpahli
             'taphel',              # 27 taphel
             'ethaphal')            # 28 ethaphal
        ),
        ('vt',              #  7 aspect
            ('n/a',                 # 0 n/a
             'perfect',             # 1 perfect
             'imperfect',           # 2 imperfect
             'imperative',          # 3 imperative
             'infinitive',          # 4 infinitive
             'participle')          # 5 participle
        ),
        ('st',               #  8 state
            ('n/a',                 # 0 n/a
             'absolute',            # 1 absolute
             'construct',           # 2 construct
             'emphatic')            # 3 emphatic
        ),
        ('nu',              #  9 number
            ('n/a',                 # 0 n/a
             's',            # 1 singular
             'p')              # 2 plural
        ),
        ('ps',              # 10 person
            ('n/a',                 # 0 n/a
             '1',               # 1 first
             '2',              # 2 second
             '3')               # 3 third
        ),
        ('gn',              # 11 gender
            ('n/a',                 # 0 n/a
             'c',              # 1 common
             'm',           # 2 masculine
             'f')            # 3 feminine
        ),
        ('prtyp',        # 12 pronoun type
            ('n/a',                 # 0 n/a
             'personal',            # 1 personal
             'demonstrative',       # 2 demonstrative
             'interrogative')       # 3 interrogative
        ),
        ('demcat',
                                # 13 demonstrative category
            ('n/a',                 # 0 n/a
             'near',                # 1 near
             'far')                 # 2 far
        ),
        ('ntyp',           # 14 noun type
            ('n/a',                 # 0 n/a
             'proper',             # 1 propper
             'common')              # 2 common
        ),
        ('nmtyp',        # 15 numeral type
            ('n/a',                 # 0 n/a
             'cardinal',            # 1 cardinal
             'ordinal',             # 2 ordinal
             'cipher')              # 3 cipher
        ),
        ('ptctyp',     # 16 participle type
            ('n/a',                 # 0 n/a
             'active',              # 1 active
             'passive')             # 2 passive
        ),
        ('sp',# 17 grammatical category
            ('verb',                # 0 verb
             'participle',          # 1 participle
             'noun',                # 2 noun
             'pronoun',             # 3 pronoun
             'numeral',             # 4 numeral
             'adjective',           # 5 adjective
             'particle',            # 6 particle
             'adverb',              # 7 adverb
             'idiom')               # 8 idiom
        ),
        ('sfcontract',  # 18 suffix contraction
            ('n/a',                 # 0 n/a
             'suffix',              # 1 suffix
             'contraction')         # 2 contraction
        ),
        ('sfgn',       # 19 suffix gender
            ('n/a',       # 0 common OR n/a
             'm',           # 1 masculine
             'f')            # 2 feminine
        ),
        ('sfps',       # 20 suffix person
            ('n/a',                 # 0 n/a
             '1',               # 1 first
             '2',              # 2 second
             '3')               # 3 third
        ),
        ('sfnu',       # 21 suffix number
            ('n/a',     # 0 singular OR n/a
             'p')              # 1 plural
        ),
        ('fmhdot', (0, 1)),  # 22 feminine he dot
                                    # 0 does not have the feminine he dot
                                    # 1 has the feminine he dot
    )


#====================================================================
# SEDRA-III constants
#====================================================================
class SedraIII:

    # ROOTS.TXT
    ROOTS_ATTR = ((             # Attributes: 16-bit intiger as follows
        'seyame', 1, (     # 0  SEYAME FLAG:
            0,        #     0 NO SEYAME
            1            #     1 SEYAME
        )), (
        'root_type', 2, (       # 1-2 ROOT TYPE:
            'normal',           #     00 NORMAL
            'parethesied',      #     01 PARETHESIED
            'bracketed',        #     10 BRACKETED
            'high_frequency'
                                #     11 HIGH FREQUENCY ROOT, e.g. propositons
        )), (
        '<RESERVED>', 13, None  # 3-15 <RESERVED>
    ))
    # LEXEMES.TXT
    LEXEMES_ATTR = ((           # Attributes: 16-bit intiger as follows
        'seyame', 1, (     # 0 SEYAME FLAG:
            0,        #     0 NO SEYAME
            1            #     1 SEYAME
        )), (
        'word_type', 1, (       # 1 WORD TYPE:
            'normal',           #     0 NORMAL
            'parenthesised'     #     1 PARENTHESISED
        )), (
        'sp', 4, (
                                # 2-5 GRAMMATICAL CATEGORY:
            'verb',             #     0000 VERB
            'participle_adjective',
                                #     0001 PARTICIPLE ADJECTIVE
            'denominative',     #     0010 DENOMINATIVE
            'substantive',      #     0011 SUBSTANTIVE
            'noun',             #     0100 NOUN
            'pronoun',          #     0101 PRONOUN
            'proper_noun',      #     0110 PROPER_NOUN
            'numeral',          #     0111 NUMERAL
            'adjective',        #     1000 ADJECTIVE
            'particle',         #     1001 PARTICLE
            'idiom',            #     1010 IDIOM
            'adverb_AiYT',
                                #     1011 ADVERB (ending with AiYT)
            'adjective_of_place',
                                #     1100 ADJECTIVE OF PLACE
            'adverb'            #     1101 ADVERB
        )), (
        'rest', 10, None        ##              /add -HV
        )
    )
    LEXEMES_FEAT = ((           # Morphological Type: 32-bit intiger as follows
        'first_suffix', 4, (    # 0-3 First SUFFIX:
            'n/a',           #     0000 <NONE>
            'ToA',              #     0001 ToA
            'YoA',              #     0010 YoA
            'NoA',              #     0011 NoA
            'oNoA',             #     0100 oNoA
            'iYNoA',            #     0101 iYNoA
            'uONoA',            #     0110 uONoA
            'ToNoA',            #     0111 ToNoA
            'TuONoA',           #     1000 TuONoA
            'uOSoA',            #     1001 uOSoA
            'oRoA',             #     1010 oRoA
            'QoNoA',            #     1011 QoNoA
            'i;N'               #     1100 i;N
        )), (
        'second_suffix', 2, (   # 4-5 SECOND SUFFIX:
            'n/a',           #     00 <NONE>
            'oYoA',             #     01 oYoA
            'iYToA'             #     10 iYToA
        )), (
        'third_suffix', 2, (    # 6-7 THIRD SUFFIX:
            'n/a',           #     00 <NONE>
            'uOToA',            #     01 uOToA
            'oAiYT'             #     10 oAiYT
        )), (
        'prefix', 2, (          # 8-9 PREFIX:
            'n/a',           #     00 <NONE>
            'M',                #     01 M
            'T',                #     10 T
            '?????????',        ##              /add -HV
        )), (
        'first_vowel', 3, (     # 10-12 FIRST VOWEL:
            'n/a',           #     000 <NONE>
            'a',                #     001 a
            'o',                #     010 o
            'e',                #     011 e
            'i',                #     100 i
            'u'                 #     101 u
        )), (
        'second_vowel', 3, (    # 13-15 SECOND VOWEL: as above
            'n/a',           ##    000 <NONE>
            'a',                ##    001 a
            'o',                ##    010 o
            'e',                ##    011 e
            'i',                ##    100 i
            'u'                 ##    101 u
        )), (
        'third_vowel', 3, (     # 16-18 THIRD VOWEL: as above
            'n/a',           ##    000 <NONE>
            'a',                ##    001 a
            'o',                ##    010 o
            'e',                ##    011 e
            'i',                ##    100 i
            'u'                 ##    101 u
        )), (
        'fourth_vowel', 3, (    # 19-21 FOURTH VOWEL: as above
            'n/a',           ##    000 <NONE>
            'a',                ##    001 a
            'o',                ##    010 o
            'e',                ##    011 e
            'i',                ##    100 i
            'u'                 ##    101 u
        )), (
        'num_vowels', 3, None   # 22-24 Total no of vowels in lexeme: 0-7
        ), (
        'radical_type', 3, (    # 25-27 RADICAL TYPE:
            'n/a',           #     000 <NONE>
            'bi',               #     001 BI
            'tri',              #     010 TRI
            'four_radical',     #     011 FOUR_RADICAL
            'five_radical',     #     100 FIVE_RADICAL
            'six_radical',      #     101 SIX_RADICAL
            'compound'          #     110 COMPOUND
        )), (
        'verbal_conjugation', 4, (            # 28-31 FORM:
            'n/a',           #     0000 <NONE>
            'peal',             #     0001 PEAL
            'ethpeal',          #     0010 ETHPEAL
            'pael',             #     0011 PAEL
            'ethpael',          #     0100 ETHPAEL
            'aphel',            #     0101 APHEL
            'ettaphal',         #     0110 ETTAPHAL
            'shaphel',          #     0111 SHAPHEL
            'eshtaphal',        #     1000 ESHTAPHAL
            'saphel',           #     1001 SAPHEL
            'estaphal',         #     1010 ESTAPHAL
            'p',                #     1011 P
            'ethp',             #     1100 ETHP
            'palpel',           #     1101 PALPEL
            'ethpalpal',        #     1110 ETHPALPAL
            '?????????',        ##              /add -HV
        ))
    )
    # WORDS.TXT
    WORDS_ATTR = ((             # Attributes: 16-bit intiger as follows
        'seyame', 1, (     # 0 SEYAME FLAG:
            0,        #     0 NO SEYAME
            1            #     1 SEYAME
        )), (
        'ignore', 4, None       # 1-4 ignore
        ), (
        'enclitic', 1, (   # 5 ENCLITIC FLAG:
            0,     #     0 NOT ENCLITIC
            1          #     1 ENCLITIC
        )), (
        'isLexeme', 1, (     # 6 LEXEME FLAG:
            0,               #     0 NO
            1
                                #     1 YES, i.e. = word represents lexeme
        )), (
        'rest', 9, None         ##              /add -HV
        )
    )
    WORDS_FEAT = ((             # Morphological Features: 32-bit intiger as follows
        '<RESERVED>', 2, None   # 0-1 <RESERVED>
        ), (
        'suffix_gender', 2, (   # 2-3 SUFFIX GENDER:
            'c/n/a', #     00 COMMON or <NONE>
            'm',        #     01 MASCULINE
            'f'       #     10 SUFFEMININE
        )), (
        'suffix_person', 2, (   # 4-5 SUFFIX PERSON:
            'n/a',           #     00 <NONE>
            '3',            #     01 THIRD
            '2',           #     10 SECOND
            '1'             #     11 FIRST
        )), (
        'suffix_number', 1, (   # 6 SUFFIX NUMBER:
            's/n/a',
                                #     0 SINGULAR or <NONE>
            'p'            #     1 PLURAL
        )), (
        'suffix_contraction', 2, (
                                # 7-8 SUFFIX/CONTRACTION:
            'n/a',           #     00 <NONE>
            'suffix',           #     01 SUFFIX
            'contraction'       #     10 CONTRACTION
        )), (
        'prefix_code', 6, None  # 9-14 PREFIX CODE: 0-63
        ), (
        'gender', 2, (          # 15-16 GENDER:
            'n/a',           #     00 <NONE>
            'c',           #     01 COMMON
            'm',        #     10 MASCULINE
            'f'          #     11 FEMININE
        )), (
        'person', 2, (          # 17-18 PERSON:
            'n/a',           #     00 <NONE>
            '3',            #     01 THIRD
            '2',           #     10 SECOND
            '1'             #     11 FIRST
        )), (
        'number', 2, (          # 19-20 NUMBER:
            'n/a',           #     00 <NONE>
            's',         #     01 SINGULAR
            'p'            #     10 PLURAL
        )), (
        'state', 2, (           # 21-22 STATE:
            'n/a',           #     00 <NONE>
            'absolute',         #     01 ABSOLUTE
            'construct',        #     10 CONSTRUCT
            'emphatic'          #     11 EMPHATIC
        )), (
        'aspect', 3, (           # 23-25 TENSE:
            'n/a',           #     000 <NONE>
            'perfect',          #     001 PERFECT
            'imperfect',        #     010 IMPERFECT
            'imperative',       #     011 IMPERATIVE
            'infinitive',       #     100 INFINITIVE
            'active_participle',#     101 ACTIVE_PARTICIPLE
            'passive_participle',
                                #     110 PASSIVE_PARTICIPLE
            'participles'       #     111 PARTICIPLES
        )), (
        'verbal_conjugation', 6, (            # 26-31 FORM:
            'n/a',           #     000000 <NONE>
            'peal',             #     000001 PEAL
            'ethpeal',          #     000010 ETHPEAL
            'pael',             #     000011 PAEL
            'ethpael',          #     000100 ETHPAEL
            'aphel',            #     000101 APHEL
            'ettaphal',         #     000110 ETTAPHAL
            'shaphel',          #     000111 SHAPHEL
            'eshtaphal',        #     001000 ESHTAPHAL
            'saphel',           #     001001 SAPHEL
            'estaphal',         #     001010 ESTAPHAL
            'pauel',            #     001011 PAUEL
            'ethpaual',         #     001100 ETHPAUAL
            'paiel',            #     001101 PAIEL
            'ethpaial',         #     001110 ETHPAIAL
            'palpal',           #     001111 PALPAL
            'ethpalpal',        #     010000 ETHPALPAL
            'palpel',           #     010001 PALPEL
            'ethpalpal',        #     010010 ETHPALPAL
            'pamel',            #     010011 PAMEL
            'ethpamal',         #     010100 ETHPAMAL
            'parel',            #     010101 PAREL
            'ethparal',         #     010110 ETHPARAL
            'pali',             #     010111 PALI
            'ethpali',          #     011000 ETHPALI
            'pahli',            #     011001 PAHLI
            'ethpahli',         #     011010 ETHPAHLI
            'taphel',           #     011011 TAPHEL
            'ethaphal'          #     011100 ETHAPHAL
        ))
    )
    # ENGLISH.TXT
    ENGLISH_ATTR = ((           # Attributes: 15-bit intiger as follows:
        '<RESERVED>', 1, None   # 0 <RESERVED>
        ), (
        'comment_position', 1, (# 1 COMMENT POSITION:
            'before_meaning',
                                #     0 COMMENT BEFORE MEANING
            'after_meaning'
                                #     1 COMMENT AFTER MEANING
        )), (
        'comment_font', 1, (    # 2 COMMENT FONT:
            'normal',           #     0 NORMAL
            'italic'            #     1 ITALIC
        )), (
        'string_before_font', 1, (
                                # 3 STRING BEFORE FONT: as above
            'normal',           ##    0 NORMAL
            'italic'            ##    1 ITALIC
        )), (
        'string_after_font', 1, (
                                # 4 STRING AFTER FONT: as above
            'normal',           ##    0 NORMAL
            'italic'            ##    1 ITALIC
        )), (
        'verb_type', 2, (       # 5-6 VERB TYPE:
            'n/a',           #     00 <NONE>
            'transitive',       #     01 TRANSITIVE
            'intransitive'      #     10 INTRANSITIVE
        )), (
        'number', 2, (          # 7-8 NUMBER: as above
            'n/a',           ##    00 <NONE>
            's',         ##    01 SINGULAR
            'p'            ##    10 PLURAL
        )), (
        'gender', 2, (          # 9-10 GENDER: as above
            'n/a',           ##    00 <NONE>
            'c',           ##    01 COMMON
            'm',        ##    10 MASCULINE
            'f'          ##    11 FEMININE
        )), (
        'form', 5, None         # 11-15 FORM: as above
                                ## TODO: what forms are these?
                                ## Below the attested values:
                                ## (5 bits; the sixth bit is always 0)
                                ## 000001  1
                                ## 000010  2
                                ## 000011  3
                                ## 000100  4
                                ## 000101  5
                                ## 000110  6
                                ## 000111  7
                                ## 001000  8
                                ## 001001  9
                                ## 001101 13
                                ## 001110 14
                                ## 010000 16
                                ## 010010 18
                                ## 010110 22
        )
    )
    # ETIMOLGY.TXT
    ETYMOLOGY_ATTR = ((         # Attributes: 16-bit intigier as follows:
        'language', 4, (        # 0-3 LANGUAGE:
            'syriac',           #     0000  SYRIAC
            'akkadian',         #     0001  AKKADIAN
            'aramaic',          #     0010  ARAMAIC
            'arabic',           #     0011  ARABIC
            'armenian',         #     0100  ARMENIAN
            'greek',            #     0101  GREEK
            'hebrew',           #     0110  HEBREW
            'latin',            #     0111  LATIN
            'persian',          #     1000  PERSIAN
            'sanskrit'          #     1001  SANSKRIT
        )), (
        'type', 1, (            # 4 TYPE:
            'normal',           #     0 NORMAL
            'parenthesied'      #     1 PARENTHESIED
        )), (
        'rest', 11, None        ##              /add -HV
        )
    )
