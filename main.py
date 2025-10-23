import os
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

from tyx_schema import (
    FunctionDefinition,
    ParameterDescription,
    TyXDocument,
    TyXDocumentSettings,
    TyXSettings,
)


@dataclass
class TemplateInfo:
    preamble: str
    functions: List[Tuple[str, FunctionDefinition]]
    filename: str


DOCUMENT_BASE = TyXDocument(
    version="0.2.11",
    content={
        "root": {
            "children": [
                {
                    "children": [
                        {
                            "type": "functioncall",
                            "version": 1,
                            "name": "title",
                            "inline": False,
                            "positionParameters": [
                                {
                                    "type": "content",
                                    "value": {
                                        "children": [
                                            {
                                                "children": [
                                                    {
                                                        "detail": 0,
                                                        "format": 0,
                                                        "mode": "normal",
                                                        "style": "",
                                                        "text": "(12345) שם קורס | תרגיל",
                                                        "type": "text",
                                                        "version": 1,
                                                    }
                                                ],
                                                "direction": "rtl",
                                                "format": "",
                                                "indent": 0,
                                                "type": "paragraph",
                                                "version": 1,
                                                "textFormat": 0,
                                                "textStyle": "",
                                            }
                                        ],
                                        "direction": "rtl",
                                        "format": "",
                                        "indent": 0,
                                        "type": "root",
                                        "version": 1,
                                    },
                                },
                                {
                                    "type": "content",
                                    "value": {
                                        "children": [
                                            {
                                                "children": [
                                                    {
                                                        "detail": 0,
                                                        "format": 0,
                                                        "mode": "normal",
                                                        "style": "",
                                                        "text": "שם: גלעד טל | ת״ז: 123456789",
                                                        "type": "text",
                                                        "version": 1,
                                                    }
                                                ],
                                                "direction": "rtl",
                                                "format": "",
                                                "indent": 0,
                                                "type": "paragraph",
                                                "version": 1,
                                                "textFormat": 0,
                                                "textStyle": "",
                                            }
                                        ],
                                        "direction": "rtl",
                                        "format": "",
                                        "indent": 0,
                                        "type": "root",
                                        "version": 1,
                                    },
                                },
                                {
                                    "type": "content",
                                    "value": {
                                        "children": [
                                            {
                                                "children": [
                                                    {
                                                        "detail": 0,
                                                        "format": 0,
                                                        "mode": "normal",
                                                        "style": "",
                                                        "text": "היום",
                                                        "type": "text",
                                                        "version": 1,
                                                    }
                                                ],
                                                "direction": "rtl",
                                                "format": "",
                                                "indent": 0,
                                                "type": "paragraph",
                                                "version": 1,
                                                "textFormat": 0,
                                                "textStyle": "",
                                            }
                                        ],
                                        "direction": "rtl",
                                        "format": "",
                                        "indent": 0,
                                        "type": "root",
                                        "version": 1,
                                    },
                                },
                            ],
                            "namedParameters": {},
                        }
                    ],
                    "direction": None,
                    "format": "",
                    "indent": 0,
                    "type": "paragraph",
                    "version": 1,
                    "textFormat": 0,
                    "textStyle": "",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "שאלה 1",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h1",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(א)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ב)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ג)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "שאלה 2",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h1",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(א)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ב)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ג)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "שאלה 3",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h1",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(א)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ב)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ג)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "שאלה 4",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h1",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(א)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ב)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ג)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "שאלה 5",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h1",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(א)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ב)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ג)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "שאלה 6",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h1",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(א)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ב)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "(ג)",
                            "type": "text",
                            "version": 1,
                        }
                    ],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "heading",
                    "version": 1,
                    "tag": "h2",
                },
                {
                    "children": [],
                    "direction": "rtl",
                    "format": "",
                    "indent": 0,
                    "type": "paragraph",
                    "version": 1,
                    "textFormat": 0,
                    "textStyle": "",
                },
            ],
            "direction": "rtl",
            "format": "",
            "indent": 0,
            "type": "root",
            "version": 1,
        }
    },
    settings=TyXDocumentSettings(
        language="he",
    ),
    **{
        "$schema": "https://tyx-editor.com/schemas/tyx-document.schema.json",
    },
)

PREAMBLE_BASE = """
#import "@preview/ctheorems:1.1.3": *

#let theorem = thmbox("1", "משפט", base_level: 0, inset: 0pt)
#let u-theorem = theorem.with(numbering: none)
#let corollary = thmbox("2", "מסקנה", base: "1", inset: 0pt)
#let u-corollary = corollary.with(numbering: none)
#let lemma = thmbox("1", "למה", base_level: 0, inset: 0pt)
#let u-lemma = lemma.with(numbering: none)
#let proposition = thmbox("1", "הצעה", base_level: 0, inset: 0pt)
#let u-proposition = proposition.with(numbering: none)
#let conjecture = thmbox("1", "השערה", base_level: 0, inset: 0pt)
#let u-conjecture = conjecture.with(numbering: none)
#let definition = thmbox("1", "הגדרה", base_level: 0, inset: 0pt)
#let u-definition = definition.with(numbering: none)
#let example = thmbox("1", "דוגמה", base_level: 0, inset: 0pt)
#let u-example = example.with(numbering: none)
#let problem = thmbox("1", "בעייה", base_level: 0, inset: 0pt)
#let u-problem = problem.with(numbering: none)
#let exercise = thmbox("1", "תרגיל", base_level: 0, inset: 0pt)
#let u-exercise = exercise.with(numbering: none)
#let solution = thmbox("1", "פתרון", base_level: 0, inset: 0pt)
#let u-solution = solution.with(numbering: none)
#let remark = thmbox("1", "הערה", base_level: 0, inset: 0pt)
#let u-remark = remark.with(numbering: none)
#let claim = thmbox("1", "טענה", base_level: 0, inset: 0pt)
#let u-claim = claim.with(numbering: none)
#let fact = thmbox("1", "עובדה", base_level: 0, inset: 0pt)
#let u-fact = fact.with(numbering: none)
#let case = thmbox("1", "מקרה", base_level: 0, inset: 0pt)
#let proof = thmproof("proof", "הוכחה", base_level: 0, inset: 0pt)

#set text(font: "David CLM")

#show: thmrules
""".strip()

FUNCTIONS_BASE = [
    (
        "title",
        FunctionDefinition(
            positional=[
                ParameterDescription(label="title", type="content"),
                ParameterDescription(label="author", type="content"),
                ParameterDescription(label="date", type="content"),
            ],
        ),
    ),
    *[
        (
            theorem,
            FunctionDefinition(
                positional=[
                    ParameterDescription(label="body", type="content"),
                ],
            ),
        )
        for theorem in [
            "theorem",
            "u-theorem",
            "corollary",
            "u-corollary",
            "lemma",
            "u-lemma",
            "proposition",
            "u-proposition",
            "conjecture",
            "u-conjecture",
            "definition",
            "u-definition",
            "example",
            "u-example",
            "problem",
            "u-problem",
            "exercise",
            "u-exercise",
            "solution",
            "u-solution",
            "remark",
            "u-remark",
            "claim",
            "u-claim",
            "fact",
            "u-fact",
            "case",
            "proof",
        ]
    ],
]

PREAMBLE_FANCY = """
#let title(title, author, date) = {
  box(width: 100%, stroke: 1pt, inset: 3pt, box(width: 100%, stroke: 0.5pt, inset: 5pt, align(center)[
    #v(0.5em)
    #text(weight: "bold", size: 24pt, title)

    #v(-0.5em)
    #author

    #date

    #v(0.5em)
  ]))
}
""".strip()

TEMPLATES = [
    TemplateInfo("", [], "hebrew-basic.tyx"),
    TemplateInfo(PREAMBLE_FANCY, [], "hebrew-fancy.tyx"),
]


def write_templates():
    templates_directory = Path("templates")

    for template in TEMPLATES:
        result = DOCUMENT_BASE.model_copy(deep=True)
        result.preamble = PREAMBLE_BASE + "\n" + template.preamble
        result.settings.functions = {
            name: f for (name, f) in FUNCTIONS_BASE + template.functions
        }

        (templates_directory / (template.filename)).write_text(
            result.model_dump_json(indent=2, exclude_none=True)
        )


def write_settings():
    shortcuts = [
        ["ctrl+space", "toggleKeyboardMap Hebrew"],
        ["alt+f", "math insert \\frac"],
        ["alt+.", "math insert \\dot"],
        # ["alt+p", "math insert ^2"],
    ]

    # Coloring
    for shortcut, color in [
        ("r", "red"),
        ("g", "green"),
        ("o", "orange"),
        ("t", "teal"),
    ]:
        shortcuts.append(
            [f"ctrl+o {shortcut}", f'math applyStyle {{"color": "{color}"}}']
        )

    # Greek
    for shortcut, letter in [
        ("a", "alpha"),
        ("c", "chi"),
        ("d", "delta"),
        ("shift+d", "Delta"),
        ("e", "varepsilon"),
        ("shift+e", "epsilon"),
        ("h", "eta"),
        ("g", "gamma"),
        ("shift+g", "Gamma"),
        ("i", "iota"),
        ("shift+i", "iota"),
        ("k", "kappa"),
        ("l", "lambda"),
        ("shift+l", "Lambda"),
        ("m", "mu"),
        ("n", "nu"),
        ("o", "omega"),
        ("w", "omega"),
        ("shift+o", "Omega"),
        ("shift+w", "Omega"),
        ("j", "varphi"),
        ("f", "phi"),
        ("shift+f", "Phi"),
        ("p", "pi"),
        ("shift+p", "Pi"),
        ("y", "psi"),
        ("shift+y", "Psi"),
        ("s", "sigma"),
        ("shift+s", "Sigma"),
        ("t", "tau"),
        ("q", "vartheta"),
        ("v", "theta"),
        ("shift+v", "Theta"),
        ("u", "upsilon"),
        ("shift+u", "Upsilon"),
        ("shift+r", "varrho"),
        ("x", "xi"),
        ("shift+x", "Xi"),
        ("z", "zeta"),
    ]:
        shortcuts.append([f"ctrl+w {shortcut}", f"math insert \\{letter}"])

    # Functions
    for shortcut, function in [
        ("c", "cos"),
        ("s", "sin"),
        ("t", "tan"),
        ("ctrl+h c", "cosh"),
        ("ctrl+h s", "sinh"),
        ("ctrl+h t", "tanh"),
        ("v", "circ"),
        ("o", "cot"),
        ("y", "det"),
        ("i", "inf"),
        ("u", "sup"),
        ("k", "ker"),
        ("n", "ln"),
        ("=", "equiv"),
        ("8", "infty"),
        ("shift+n", "min"),
        ("shift+x", "max"),
        ("shift+s", "Im"),
        ("shift+a", "Re"),
    ]:
        shortcuts.append([f"ctrl+q {shortcut}", f"math insert \\{function}"])

    # Environments
    for shortcut, environment in [
        ("v", "proof"),
        ("l", "lemma"),
        ("c", "claim"),
        ("d", "definition"),
        ("x", "corollary"),
        ("k", "lemma"),
        ("t", "theorem"),
        (",", "exercise"),
        ("p", "solution"),
        ("e", "example"),
        ("g", "remark"),
    ]:
        shortcuts.append([f"ctrl+e {shortcut}", f"insertFunctionCall {environment}"])

        if environment != "proof":
            shortcuts.append(
                [f"ctrl+e shift+{shortcut}", f"insertFunctionCall u-{environment}"]
            )

    # Set Theory
    for shortcut, command in [
        ("i", "in"),
        ("j", "cap"),
        ("u", "cup"),
        ("m", "setminus"),
        ("v", "circ"),
        ("c", "mathbb{C}"),
        ("f", "mathbb{F}"),
        ("r", "mathbb{R}"),
        ("z", "mathbb{Z}"),
        ("n", "mathbb{N}"),
        ("q", "mathbb{Q}"),
        # ("shift+p", "perp"),
        ("shift+i", "notin"),
        ("e", "emptyset"),
        ("t", "aleph"),
        ("o", "lor"),
        ("b", "subseteq"),
        ("shift+b", "subset"),
        # ("ctrl+shift+b", "subsetneq"),
        ("p", "supseteq"),
        ("shift+p", "supset"),
        # ("ctrl+shift+p", "supsetneq"),
        ("shift+a", "bigwedge"),
        ("shift+o", "bigvee"),
    ]:
        shortcuts.append([f"ctrl+i {shortcut}", f"math insert \\{command}"])

    settings = TyXSettings(
        language="he",
        keyboardMap="Hebrew",
        keyboardShortcuts=shortcuts,
        **{
            "$schema": "https://tyx-editor.com/schemas/tyx-settings.schema.json",
        },
    )

    Path("settings.json").write_text(
        settings.model_dump_json(indent=2, exclude_none=True)
    )


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    write_templates()
    write_settings()
