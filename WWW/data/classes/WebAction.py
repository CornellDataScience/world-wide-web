from data import ActionType
from typing import Any
from xml.dom.minidom import Document, Element, Node
class WebAction:
    #A single action by the agent

    #type of action
    action_type: ActionType 
    #the minidom.Element that is being targeted by the action
    target: Element
    #string value for typing
    value: str = ""

    #Need methods to parse an action from the data

