<img src="images/etcbc.png" align="right"/>
<img src="images/tf.png" align="right"/>

Feature documentation
=====================

Here you find a description of the transcriptions of the Syriac New Testament (SyrNT) corpus, the
Text-Fabric model in general, and the node types, features and edges for the
SyrNT corpus in particular.

See also [about](about.md) [text-fabric](textfabric.md)

Conversion from SEDRA 3.0 to TF
---------------------------------

Below is an account how we transform SEDRA database into
[Text-Fabric](https://github.com/annotation/text-fabric) format by means of
[tfFromSyrnt.py](../programs/tfFromSyrnt.py).

The Text-Fabric model views the text as a series of atomic units, called
*slots*. In this corpus *words* are the slots.

On top of that, more complex textual objects can be represented as *nodes*. In
this corpus we have node types for: *word*, *verse*,
*chapter*, and *book*.

The type of every node is given by the feature
[**otype**](https://annotation.github.io/text-fabric/tf/cheatsheet.html#special-node-feature-otype).
Every node is linked to a subset of slots by
[**oslots**](https://annotation.github.io/text-fabric/tf/cheatsheet.html#special-edge-feature-oslots).

Nodes can be related by means of edges.

Nodes and edges can be annotated with features. See the table below.

Text-Fabric supports three customizable section levels. In this corpus they are
*book*, *chapter*, *verse*.

Other docs
----------

[Text-Fabric API](https://annotation.github.io/text-fabric/tf/cheatsheet.html)

Reference table of features
===========================

*(Keep this under your pillow)*

Node type *word*
-------------------------

Basic unit of text. They are separated by spaces and/or punctuation.

feature | values |  type | description
------- | ------ | ------ | ----
**word** | `ܟܬܒܐ` | string | the text of a word as UNICODE string
**lexeme** | `ܟܬܒܐ` | string | the lexeme of a word as UNICODE string
**root** | `ܟܬܒ` | string | the root of a word as UNICODE string
**stem** | `ܟܬܒܐ` | string | the stem of a word as UNICODE string
**prefix** | `ܕ` `ܘܠ` | string | the prefix in a word as UNICODE string
**suffix** | `ܗ` `ܘܗܝ` | string | the suffix in a word as UNICODE string
**demcat** | `far` `near` `NA` | string | demonstrative category
**fmhdot** | `0` `1` | number | presence of feminine he dot
**gn** | `f` `m` `c` `NA` | string | gender
**nmtyp** | `cardinal` `NA` | string | numeral type
**ntyp** | `common` `proper` `NA` | string | noun type
**nu** | `s` `p` `NA` | string | number
**prtyp** | `personal` `interrogative` `personal` | string | pronoun type
**ps** | `1` `2` `3` `NA` | string | person
**ptctyp** | `active` `passive` `NA` | string | participle type
**seyame** | `0` `1` | number | presence of seyame
**sfcontract** | `suffix` `contraction` `NA` | string | suffix contraction
**sfgn** | `f` `m` `NA`| string | suffix gender; **NB** `NA` denotes `c` of not applicable
**sfnu** | `p` `NA` | string | suffix number; **NB** `NA` denotes `s` or not applicable
**sfps** | `1` `2` `3` `NA` | string | suffix person
**sp** | `noun` `verb` `particle` `pronoun` `adjective` `numeral` `adverb` `idiom` | string | part of speech (grammatical category)
**st** | `absolute` `construct` `emphatic` `NA` | string | state
**vs** | `peal` `pael` `paiel` `ethpael` ... `NA` | string | verbal conjugation (stem)
**vt** | `perfect` `participle` `imperfect` `imperative` `infinitive` `NA` | string | verbal aspect (tense)

The features `word`, `lexeme`, `root`, `stem`, `prefix`, `suffix` are also available in transcriptions:

*feature*`_sedra` for the SEDRA transcription

*feature*`_etcbc` for the ETCBC/WIT transcription

Node type *lexeme*
-------------------------

Class of word occurrences that share the same basic traits and that differ
in morphology.

feature | values |  type | description
------- | ------ | ------ | ----
**lexeme** | `ܟܬܒܐ` | string | the text of a lexeme as UNICODE string
**lexeme sedra** | `CTBA` | string | the text of a lexeme in SEDRA transliteration
Node type *verse*
-------------------------

Subdivision of a containing *chapter*. 

feature | values | description
------- | ------ | ------
**verse** | `1` | number of the *verse*
**chapter** | `1` | see under node type *chapter*
**book** | `Matt` | see under node type *book*

Node type *chapter*
-----------------------------

Subdivision of a containing *book*.

feature | values | description
------- | ------ | ------
**chapter** | `1` | number of the *chapter*
**book** | `Matt` | see under node type *book*

Node type *book*
-----------------------------

The main entity of which the corpus is composed, representing the transcription
of a complete book.

Some books come in several witnesses, marked as `A`, `B`. 
We treat them as separate books, and augment their names and acronyms with `_A`, `_B`, etc.

feature | values | description
------- | ------ | ------
**book@en** | `Matthew` | English name of the book
**book** | `Matt` | acronym of the book name

