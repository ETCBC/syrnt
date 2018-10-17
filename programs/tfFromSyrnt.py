import os
import collections
import operator
from shutil import rmtree
from glob import glob
from functools import reduce
from tf.fabric import Fabric

from constants import NT_BOOKS, BOOK_EN, SyrNT, tosyr

VERSION = '0.1'

GH_BASE = os.path.expanduser('~/github')
ORG = 'etcbc'
REPO = 'syrnt'
SOURCE_DIR = f'source/{VERSION}'
PLAIN_DIR = f'plain/{VERSION}'
TF_DIR = f'tf/{VERSION}'
SOURCE_PATH = f'{GH_BASE}/{ORG}/{REPO}/{SOURCE_DIR}'
PLAIN_PATH = f'{GH_BASE}/{ORG}/{REPO}/{PLAIN_DIR}'
TF_PATH = f'{GH_BASE}/{ORG}/{REPO}/{TF_DIR}'
TEMP_DIR = f'{GH_BASE}/{ORG}/{REPO}/_temp'

# -1 is unlimited

LIMIT = -1
SHOW = True

NA_VALUE = 'NA'
NA_VALUES = {'n/a'}

for cdir in (TEMP_DIR, TF_PATH):
    os.makedirs(cdir, exist_ok=True)

commonMetaData = collections.OrderedDict(
    dataset=REPO,
    datasetName='Syriac New Testament',
    source='SEDRA',
    sourceUrl='https://sedra.bethmardutho.org/about/contributors',
    encoders=('Ancient Biblical Manuscript Center  (transcription),'
              'George A. Kiraz and James W. Bennett (database)'
              'and Hannes Vlaardingerbroek and Dirk Roorda (TF)'),
    email1='dirk.roorda@dans.knaw.nl',
)
specificMetaData = collections.OrderedDict(
    book='book name',
    chapter='chapter number',
    demcat='demonstrative category',
    fmhdot='feminine he dot',
    gn='gender',
    lexeme='lexeme of the word in syriac script',
    lexeme_ascii='lexeme of the word in sedra transcription',
    nmtyp='numeral type',
    ntyp='noun type',
    nu='number',
    prefix='prefix',
    prefix_ascii='prefix ascii',
    prtyp='pronoun_type',
    ps='person',
    ptctyp='participle type',
    root='root',
    root_ascii='root ascii',
    seyame='seyame',
    sfcontract='suffix contraction',
    sfgn='suffix gender',
    sfnu='suffix number',
    sfps='suffix person',
    sp='part of speech (grammatical category)',
    st='state',
    stem='stem',
    stem_ascii='stem ascii',
    suffix='suffix',
    suffix_ascii='suffix ascii',
    verse='verse number',
    vs='verbal conjugation',
    vt='verbal aspect (tense)',
    word='full form of the word in syriac script',
    word_ascii='full form of the word in sedra transcription',
)
langMetaData = dict(
    en=dict(
        language='English',
        languageCode='en',
        languageEnglish='English',
    ),
)
numFeatures = set('''
    chapter
    verse
    fmhdot
    seyame
'''.strip().split()
)

oText = {
    'sectionFeatures': 'book,chapter,verse',
    'sectionTypes': 'book,chapter,verse',
    'fmt:text-orig-full': '{word} ',
    'fmt:text-trans-full': '{word_ascii} ',
    'fmt:lex-orig-full': '{lexeme} ',
    'fmt:lex-trans-full': '{lexeme_ascii} ',
}


def readCorpus():
    files = glob(f'{SOURCE_PATH}/*.txt')
    nLines = 0
    stop = False
    for f in files:
        (dirF, fileF) = os.path.split(f)
        (corpus, ext) = os.path.splitext(fileF)
        print(f'File "{corpus}" ...')
        with open(f) as fh:
            for (ln, line) in enumerate(fh):
                if nLines == LIMIT:
                    stop = True
                    break
                nLines += 1
                yield (ln + 1, line.rstrip('\n'))
        if stop:
            break


def getVerseLabels():
    verseLabels = []
    for (book, chapters) in NT_BOOKS:
        for (chapter, verseCount) in enumerate(chapters):
            for v in range(1, verseCount + 1):
                verseLabels.append((book, chapter + 1, v))
    bookEn = {NT_BOOKS[i][0]: book for (i, book) in enumerate(BOOK_EN)}
    return (bookEn, verseLabels)


def parseCorpus():
    annotSpecs = SyrNT.ANNOTATIONS
    cur = collections.Counter()
    curSlot = 0
    context = []
    nodeFeatures = collections.defaultdict(dict)
    edgeFeatures = collections.defaultdict(
        lambda: collections.defaultdict(set)
    )
    oSlots = collections.defaultdict(set)
    (bookEn, verseLabels) = getVerseLabels()
    (prevBook, prevChapter) = (None, None)
    lexemes = set()
    for p in readCorpus():
        (book, chapter, verse) = verseLabels[cur['verse']]
        if book != prevBook:
            print(
                f'\t{bookEn[book]:<15} current:'
                f' b={cur["book"]:>2}'
                f' c={cur["chapter"]:>3}'
                f' v={cur["verse"]:>4}'
                f' w={curSlot:>6}'
            )
            if prevChapter is not None:
                context.pop()
                prevChapter = None
            if prevBook is not None:
                context.pop()
            cur['book'] += 1
            prevBook = book
            bookNode = ('book', cur['book'])
            nodeFeatures['book'][bookNode] = book
            nodeFeatures['book@en'][bookNode] = bookEn[book]
            context.append(('book', cur['book']))
        if chapter != prevChapter:
            if prevChapter is not None:
                context.pop()
            cur['chapter'] += 1
            prevChapter = chapter
            nodeFeatures['chapter'][('chapter', cur['chapter'])] = chapter
            nodeFeatures['book'][('chapter', cur['chapter'])] = book
            context.append(('chapter', cur['chapter']))

        cur['verse'] += 1
        nodeFeatures['verse'][('verse', cur['verse'])] = verse
        nodeFeatures['chapter'][('verse', cur['verse'])] = chapter
        nodeFeatures['book'][('verse', cur['verse'])] = book
        (ln, line) = p
        words = line.split()
        context.append(('verse', cur['verse']))
        for word in words:
            curSlot += 1
            (wordTrans, annotationStr) = word.split('|', 1)
            annotations = annotationStr.split('#')
            wordNode = ('word', curSlot)
            nodeFeatures['word_ascii'][wordNode] = wordTrans
            nodeFeatures['word'][wordNode] = wordTrans.translate(tosyr)
            for ((feature, values), data) in zip(annotSpecs, annotations):
                value = data if values is None else values[int(data)]
                featureName = f'{feature}_ascii' if values is None else feature
                if values is None:
                    nodeFeatures[feature][wordNode] = value.translate(tosyr)
                nodeFeatures[featureName][wordNode] = (
                    value
                    if featureName in numFeatures
                    else NA_VALUE if value in NA_VALUES
                    else value
                )
            lexeme = nodeFeatures['lexeme'][wordNode]
            if lexeme not in lexemes:
                lexemes.add(lexeme)
                cur['lexeme'] += 1
                lexNode = ('lexeme', cur['lexeme'])
                nodeFeatures['lexeme'][lexNode] = lexeme
                nodeFeatures['lexeme_ascii'][lexNode] = (
                    nodeFeatures['lexeme_ascii'][wordNode]
                )
            context.append(('lexeme', cur['lexeme']))
            for (nt, curNode) in context:
                oSlots[(nt, curNode)].add(curSlot)
            context.pop()
        context.pop()
    context.pop()
    context.pop()

    print('')

    if SHOW:
        if LIMIT == -1:
            for ft in sorted(nodeFeatures):
                print(ft)
                for n in range(1, 5):
                    for ntp in ('book', 'chapter', 'verse', 'word'):
                        if (ntp, n) in nodeFeatures[ft]:
                            print(f'\t"{nodeFeatures[ft][(ntp, n)]}"')
        else:
            print(nodeFeatures)
            print(oSlots)

    if len(context):
        print('Context:', context)

    print(f'\n{curSlot:>7} x slot')
    for (nodeType, amount) in sorted(cur.items(), key=lambda x: (x[1], x[0])):
        print(f'{amount:>7} x {nodeType}')

    nValues = reduce(
        operator.add, (len(values) for values in nodeFeatures.values()), 0
    )
    print(f'{len(nodeFeatures)} node features with {nValues} values')
    print(f'{len(oSlots)} nodes linked to slots')

    print('Compiling TF data')
    print(f'Building warp feature otype')
    nodeOffset = {'word': 0}
    oType = {}
    n = 1
    for k in range(n, curSlot + 1):
        oType[k] = 'word'
    n = curSlot + 1
    for (nodeType, amount) in sorted(cur.items(), key=lambda x: (x[1], x[0])):
        nodeOffset[nodeType] = n - 1
        for k in range(n, n + amount):
            oType[k] = nodeType
        n = n + amount
    print(f'{len(oType)} nodes')

    print('Filling in the nodes for features')
    newNodeFeatures = collections.defaultdict(dict)
    for (ft, featureData) in nodeFeatures.items():
        newFeatureData = {}
        for ((nodeType, node), value) in featureData.items():
            newFeatureData[nodeOffset[nodeType] + node] = value
        newNodeFeatures[ft] = newFeatureData
    newOslots = {}
    for ((nodeType, node), slots) in oSlots.items():
        newOslots[nodeOffset[nodeType] + node] = slots

    nodeFeatures = newNodeFeatures
    nodeFeatures['otype'] = oType
    edgeFeatures['oslots'] = newOslots

    print(f'Node features: {" ".join(nodeFeatures)}')
    print(f'Edge features: {" ".join(edgeFeatures)}')

    metaData = {
        '': commonMetaData,
        'otext': oText,
        'oslots': dict(valueType='str'),
        'book@en': langMetaData['en'],
    }
    for ft in set(nodeFeatures) | set(edgeFeatures):
        metaData.setdefault(
            ft, {}
        )['valueType'] = 'int' if ft in numFeatures else 'str'
        metaData[ft]['description'] = (
            specificMetaData[ft] if ft in specificMetaData else '?'
        )

    print(f'Remove existing TF directory')
    rmtree(TF_PATH)
    print(f'Save TF dataset')
    TF = Fabric(locations=TF_PATH, silent=True)
    TF.save(
        nodeFeatures=nodeFeatures,
        edgeFeatures=edgeFeatures,
        metaData=metaData
    )


def loadTf():
    print(f'Load TF dataset for the first time')
    TF = Fabric(locations=TF_PATH, modules=[''])
    TF.load('')
    allFeatures = TF.explore(silent=False, show=True)
    loadableFeatures = allFeatures['nodes'] + allFeatures['edges']
    TF.load(loadableFeatures)

    print('All done')


def main():
    parseCorpus()
    loadTf()


main()
