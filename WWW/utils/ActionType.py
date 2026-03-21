from enum import Enum
class ActionType(str, Enum):
    CLICK = "CLICK"
    SELECT = "SELECT"
    TYPE = "TYPE"
    #more types depending on what the data has