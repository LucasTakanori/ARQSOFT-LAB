from Spreadsheet.Content.TextContent import TextContent
from Spreadsheet.Content.NumberContent import NumberContent
from Spreadsheet.Content.FormulaContent import FormulaContent
class Cell:
    def __init__(self, coordinate, value):
        self.coordinate = coordinate
        self.set_content(value)
        print(self.content)
        self.dependent_cells = set()

    def set_content(self, text_input: str):
        print(text_input)
        try:
            # Try converting the string to a float
            # If successful, add Numbercontent
            self.content = NumberContent(float(text_input))
            print("buenas")
        except ValueError:
            # If conversion fails, it's not a numeric string
            if text_input.startswith('='): # Check if it starts with '='
                self.content = FormulaContent(text_input)
                print("tetas")
            else:# Otherwise, it's a regular string
                self.content = TextContent(text_input)
                print("culo") 

    def get_content(self):
        return self.content
    
    def __str__(self) -> str:
        return str(self.content.get_value())