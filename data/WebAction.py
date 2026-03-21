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

    #Takes raw dict data and converts target of the action to a DOM Tree
    def from_raw(cls, raw: dict[str, Any]) -> "WebAction":
        doc: Document = minidom.Document()
        elem = element_from_raw(raw.get("target_element", {}), doc)
        doc.appendChild(elem)
        return cls(
            action_type=ActionType(raw["action_type"]),
            target=elem,
            value=raw.get("value", ""),
        )

