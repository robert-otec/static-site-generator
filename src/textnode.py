from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
    # First check if 'other' is also a TextNode
        if not isinstance(other, TextNode):
            return False
    
    # Now compare all the properties
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
    # Use .value to get the string representation of the enum
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"