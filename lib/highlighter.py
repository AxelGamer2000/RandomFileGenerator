from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor
from pygments.lexers import PythonLexer
from pygments.token import Token

class PygmentsHighlighter(QSyntaxHighlighter):
    def __init__(self, parent, lexer):
        super().__init__(parent)
        self.lexer = lexer
        self.formats = {
            Token.Keyword: self.create_format("cyan"),
            Token.Name: self.create_format("white"),
            Token.String: self.create_format("green"),
            Token.Comment: self.create_format("grey"),
            Token.Number: self.create_format("red"),
        }

    def create_format(self, color_name):
        fmt = QTextCharFormat()
        fmt.setForeground(QColor(color_name))
        return fmt

    def highlightBlock(self, text):
        cursor = 0
        remaining_text = text
        for token, value in self.lexer.get_tokens(text):
            if not value:
                continue
            start = remaining_text.find(value)
            if start >= 0:
                fmt = QTextCharFormat()
                # recherche hiérarchique
                for parent_token, color_fmt in self.formats.items():
                    if token in parent_token:
                        fmt = color_fmt
                        break
                self.setFormat(cursor + start, len(value), fmt)
                cursor += start + len(value)
                remaining_text = remaining_text[start + len(value):]
