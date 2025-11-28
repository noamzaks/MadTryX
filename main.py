import os
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

import appdirs
import typer
from tyx_schema import (
    Content,
    FunctionDefinition,
    ParameterDescription,
    TyXDocument,
    TyXDocumentSettings,
    TyXSettings,
)


@dataclass
class TemplateInfo:
    filename: str
    preamble: str
    functions: List[Tuple[str, FunctionDefinition]]
    content: Optional[Content] = None
    settings: Optional[TyXDocumentSettings] = None


CONTENT_HEBREW = Content(
    root={
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
                                                    "text": "שם: ישראל ישראלי | ת״ז: 123456789",
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
                                                    "type": "typstcode",
                                                    "version": 1,
                                                    "text": {
                                                        "editorState": {
                                                            "root": {
                                                                "children": [
                                                                    {
                                                                        "children": [
                                                                            {
                                                                                "detail": 0,
                                                                                "format": 0,
                                                                                "mode": "normal",
                                                                                "style": "",
                                                                                "text": "#datetime.today().display()",
                                                                                "type": "text",
                                                                                "version": 1,
                                                                            }
                                                                        ],
                                                                        "format": "",
                                                                        "indent": 0,
                                                                        "type": "paragraph",
                                                                        "version": 1,
                                                                        "textFormat": 0,
                                                                        "textStyle": "",
                                                                    }
                                                                ],
                                                                "format": "",
                                                                "indent": 0,
                                                                "type": "root",
                                                                "version": 1,
                                                            }
                                                        }
                                                    },
                                                }
                                            ],
                                            "format": "",
                                            "type": "paragraph",
                                            "version": 1,
                                            "textFormat": 0,
                                            "textStyle": "",
                                        }
                                    ],
                                    "format": "",
                                    "type": "root",
                                    "version": 1,
                                },
                            },
                        ],
                        "namedParameters": {},
                    }
                ],
                "direction": "rtl",
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
)

CONTENT_ENGLISH = Content(
    root={
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
                                                    "format": 0,
                                                    "text": "(12345) Course Name | Exercise",
                                                    "type": "text",
                                                    "version": 1,
                                                }
                                            ],
                                            "format": "",
                                            "type": "paragraph",
                                            "version": 1,
                                            "textFormat": 0,
                                        }
                                    ],
                                    "format": "",
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
                                                    "format": 0,
                                                    "text": "Name: John Doe",
                                                    "type": "text",
                                                    "version": 1,
                                                }
                                            ],
                                            "format": "",
                                            "type": "paragraph",
                                            "version": 1,
                                            "textFormat": 0,
                                        }
                                    ],
                                    "format": "",
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
                                                    "type": "typstcode",
                                                    "version": 1,
                                                    "text": {
                                                        "editorState": {
                                                            "root": {
                                                                "children": [
                                                                    {
                                                                        "children": [
                                                                            {
                                                                                "detail": 0,
                                                                                "format": 0,
                                                                                "mode": "normal",
                                                                                "style": "",
                                                                                "text": "#datetime.today().display()",
                                                                                "type": "text",
                                                                                "version": 1,
                                                                            }
                                                                        ],
                                                                        "format": "",
                                                                        "indent": 0,
                                                                        "type": "paragraph",
                                                                        "version": 1,
                                                                        "textFormat": 0,
                                                                        "textStyle": "",
                                                                    }
                                                                ],
                                                                "format": "",
                                                                "indent": 0,
                                                                "type": "root",
                                                                "version": 1,
                                                            }
                                                        }
                                                    },
                                                }
                                            ],
                                            "format": "",
                                            "type": "paragraph",
                                            "version": 1,
                                            "textFormat": 0,
                                            "textStyle": "",
                                        }
                                    ],
                                    "format": "",
                                    "type": "root",
                                    "version": 1,
                                },
                            },
                        ],
                        "namedParameters": {},
                    }
                ],
                "format": "",
                "type": "paragraph",
                "version": 1,
                "textFormat": 0,
                "textStyle": "",
            },
            {
                "children": [
                    {"format": 0, "text": "Question 1", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h1",
            },
            {
                "children": [
                    {"format": 0, "text": "(a)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(b)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(c)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "Question 2", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h1",
            },
            {
                "children": [
                    {"format": 0, "text": "(a)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(b)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(c)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "Question 3", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h1",
            },
            {
                "children": [
                    {"format": 0, "text": "(a)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(b)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(c)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "Question 4", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h1",
            },
            {
                "children": [
                    {"format": 0, "text": "(a)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(b)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(c)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "Question 5", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h1",
            },
            {
                "children": [
                    {"format": 0, "text": "(a)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(b)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(c)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "Question 6", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h1",
            },
            {
                "children": [
                    {"format": 0, "text": "(a)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(b)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
            {
                "children": [
                    {"format": 0, "text": "(c)", "type": "text", "version": 1}
                ],
                "format": "",
                "type": "heading",
                "version": 1,
                "tag": "h2",
            },
        ],
        "format": "",
        "type": "root",
        "version": 1,
    }
)

CONTENT_EMPTY = Content(
    root={
        "children": [
            {
                "children": [],
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
    }
)

SETTINGS_HEBREW = TyXDocumentSettings(language="he")

PREAMBLE_HEBREW_BASE = (
    """
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
    + "\n"
)
PREAMBLE_ENGLISH_BASE = (
    """
#import "@preview/ctheorems:1.1.3": *

#let theorem = thmbox("1", "Theorem", base_level: 0, inset: 0pt)
#let u-theorem = theorem.with(numbering: none)
#let corollary = thmbox("2", "Corollary", base: "1", inset: 0pt)
#let u-corollary = corollary.with(numbering: none)
#let lemma = thmbox("1", "Lemma", base_level: 0, inset: 0pt)
#let u-lemma = lemma.with(numbering: none)
#let proposition = thmbox("1", "Proposition", base_level: 0, inset: 0pt)
#let u-proposition = proposition.with(numbering: none)
#let conjecture = thmbox("1", "Conjecture", base_level: 0, inset: 0pt)
#let u-conjecture = conjecture.with(numbering: none)
#let definition = thmbox("1", "Definition", base_level: 0, inset: 0pt)
#let u-definition = definition.with(numbering: none)
#let example = thmbox("1", "Example", base_level: 0, inset: 0pt)
#let u-example = example.with(numbering: none)
#let problem = thmbox("1", "Problem", base_level: 0, inset: 0pt)
#let u-problem = problem.with(numbering: none)
#let exercise = thmbox("1", "Exercise", base_level: 0, inset: 0pt)
#let u-exercise = exercise.with(numbering: none)
#let solution = thmbox("1", "Solution", base_level: 0, inset: 0pt)
#let u-solution = solution.with(numbering: none)
#let remark = thmbox("1", "Remark", base_level: 0, inset: 0pt)
#let u-remark = remark.with(numbering: none)
#let claim = thmbox("1", "Claim", base_level: 0, inset: 0pt)
#let u-claim = claim.with(numbering: none)
#let fact = thmbox("1", "Fact", base_level: 0, inset: 0pt)
#let u-fact = fact.with(numbering: none)
#let case = thmbox("1", "Case", base_level: 0, inset: 0pt)
#let proof = thmproof("proof", "Proof", base_level: 0, inset: 0pt)

#show: thmrules
""".strip()
    + "\n"
)

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

PREAMBLE_BASIC = """
#let title(title, author, date) = {
  box(width: 100%, align(center)[
    #v(0.5em)
    #text(weight: "bold", size: 24pt, title)

    #v(-0.5em)
    #author

    #date

    #v(0.5em)
  ])
}
""".strip()

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
    TemplateInfo(
        "hebrew-basic.tyx", preamble=PREAMBLE_HEBREW_BASE + PREAMBLE_BASIC, functions=[]
    ),
    TemplateInfo(
        "hebrew-fancy.tyx", preamble=PREAMBLE_HEBREW_BASE + PREAMBLE_FANCY, functions=[]
    ),
    TemplateInfo(
        "hebrew-empty.tyx",
        functions=[],
        preamble=PREAMBLE_HEBREW_BASE,
        content=CONTENT_EMPTY,
    ),
    TemplateInfo(
        "english-basic.tyx",
        preamble=PREAMBLE_ENGLISH_BASE + PREAMBLE_BASIC,
        functions=[],
        settings=TyXDocumentSettings(),
        content=CONTENT_ENGLISH,
    ),
    TemplateInfo(
        "english-fancy.tyx",
        preamble=PREAMBLE_ENGLISH_BASE + PREAMBLE_FANCY,
        functions=[],
        settings=TyXDocumentSettings(),
        content=CONTENT_ENGLISH,
    ),
    TemplateInfo(
        "english-empty.tyx",
        functions=[],
        preamble=PREAMBLE_ENGLISH_BASE,
        content=CONTENT_EMPTY,
    ),
]


def write_templates():
    templates_directory = Path("templates")

    for template in TEMPLATES:
        result = TyXDocument(
            version="0.2.12",
            content=template.content or CONTENT_HEBREW,
            settings=template.settings or SETTINGS_HEBREW,
            preamble=template.preamble,
        )
        result.field_schema = "https://tyx-editor.com/schemas/tyx-document.schema.json"

        result.settings.functions = {
            name: f for (name, f) in FUNCTIONS_BASE + template.functions
        }

        (templates_directory / (template.filename)).write_text(
            result.model_dump_json(indent=2, exclude_none=True), encoding="utf-8"
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
            [f"alt+o {shortcut}", f'math applyStyle {{"color": "{color}"}}']
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
        shortcuts.append([f"alt+w {shortcut}", f"math insert \\{letter}"])

    # Functions
    for shortcut, function in [
        ("c", "cos"),
        ("s", "sin"),
        ("t", "tan"),
        ("alt+h c", "cosh"),
        ("alt+h s", "sinh"),
        ("alt+h t", "tanh"),
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
        shortcuts.append([f"alt+q {shortcut}", f"math insert \\{function}"])

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
        shortcuts.append([f"alt+e {shortcut}", f"setFunctionCall {environment}"])

        if environment != "proof":
            shortcuts.append(
                [f"alt+e shift+{shortcut}", f"setFunctionCall u-{environment}"]
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
        shortcuts.append([f"alt+i {shortcut}", f"math insert \\{command}"])

    settings = TyXSettings(
        language="he",
        keyboardMap="Hebrew",
        keyboardShortcuts=shortcuts,
    )

    Path("settings.json").write_text(
        settings.model_dump_json(indent=2, exclude_none=True), encoding="utf-8"
    )


def main(deploy: bool = False):
    write_templates()
    write_settings()

    if deploy:
        tyx_config_path = Path(
            appdirs.user_config_dir("com.tyx-editor.tyx", False, roaming=True)
        )
        for d in ("fonts", "templates"):
            if os.path.exists(tyx_config_path / d):
                shutil.rmtree(tyx_config_path / d)
            shutil.copytree(d, tyx_config_path / d)
        for f in ("settings.json",):
            if os.path.exists(tyx_config_path / f):
                os.remove(tyx_config_path / f)
            shutil.copyfile(f, tyx_config_path / f)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    typer.run(main)
