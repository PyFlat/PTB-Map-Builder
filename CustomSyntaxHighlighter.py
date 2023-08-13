from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import RULES, re


class CustomSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.error_format = QTextCharFormat()
        self.error_format.setUnderlineColor(QColor(Qt.red))
        self.error_format.setUnderlineStyle(QTextCharFormat.WaveUnderline)

        self.highlighting_rules = []

        for comm in RULES.COMMANDS:
            self.add_rule(comm, Qt.yellow)

        keywords = [
            {"keywords" : ['on_init', 'on_collect', 'on_step', 'on_explode', "on_destroy", "on_tick"],
            "color": "#dcdcaa"
            },
            {"keywords" : ['@', "end", "win", "loose", "add", "subtract", "multiply", "divide", "set", "reset", "store", "set_item", "drawImage", "drawRect", "clear", "compare", "jump", "setFlag", "tp", "jumpRelative", "createMemory", "loadToMemory", "loadFromMemory", "randomNumber", "loadFromPointer"],
            "color": "#2667ca"
            },
            {"keywords" : ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"],
            "color": "#a7ce9b"
            },
            {"keywords" : ['=>', "="],
            "color": "#9cdcfe"
            },
            {"keywords": ["player.health", "player.bombs", "player.range", "player.dynamite", "player.timed_bombs", "player.damage", "player.nukes",],
            "color": "#c3602d"}
        ]
        self.unique_keywords = []
        for keyword in keywords:
            format = QTextCharFormat()
            format.setForeground(QColor(keyword["color"]))
            self.unique_keywords.append((keyword["keywords"], format))



    def add_rule(self, pattern, color):
        format = QTextCharFormat()
        format.setForeground(QColor(color))
        rule = (QRegularExpression(pattern), format)
        self.highlighting_rules.append(rule)
    def highlightBlock(self, text):
        self.setFormat(0, len(text), QTextCharFormat())  # Clear existing formatting

        if not any(rule.match(text).hasMatch() for rule, _ in self.highlighting_rules):
            # Apply error format to non-matching text
            self.setFormat(0, len(text), self.error_format)

        for keywordlist in self.unique_keywords:
            for keyword in keywordlist[0]:
                index = text.find(keyword)
                while index != -1:
                    self.setFormat(index, len(keyword), keywordlist[1])
                    index = text.find(keyword, index + 1)
                
                
        self.setCurrentBlockState(0)
