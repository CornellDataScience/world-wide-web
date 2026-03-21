from typing import Any
from xml.dom.minidom import Document, Element, Node
from dataclasses import dataclass, field
class WebState:
    # A single state of the website at a point in time.

    #DOM Tree representing the current state.
    dom_tree: Document

    def dom_to_string(self) -> str :
        return self.dom_tree.toxml()