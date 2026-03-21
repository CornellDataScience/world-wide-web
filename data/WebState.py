from typing import Any
from xml.dom.minidom import Document, Element, Node
from dataclasses import dataclass, field
class WebState:
    # A single state of the website at a point in time.

    #DOM Tree representing the current state.
    dom_tree: Document

    #Processes the dict form of the attribute and returns an Element. 
    def build_element(raw_element, doc):
        tag = raw_element.get("tag", "none")
        elem : Element = doc.createElement(tag)

        attrs = raw_element.get("attributes", "{}")
        node_id = raw_element.get("backend_node_id", "")

        attrs["backend_node_id"] = str(node_id)

        for key,value in attrs.items():
            elem.setAttribute(key,value)
        
        return elem
    
    doc: Document = minidom.Document()

    #Builds a full Document given the dict form of the tree
    def document_from_raw_tree(tree: dict[str, Any]) -> Document:
        doc: Document = minidom.Document()
 
        def _build(node_dict: dict[str, Any], owner: Document) -> Element:
            tag = node_dict.get("tag", "unknown")
            elem: Element = owner.createElement(tag)
 
            attrs = node_dict.get("attributes", {})
            node_id = node_dict.get("backend_node_id", "")
            if node_id and "backend_node_id" not in attrs:
                attrs["backend_node_id"] = str(node_id)
            for k, v in attrs.items():
                elem.setAttribute(k, v)
 
            text = node_dict.get("text", "").strip()
            if text:
                elem.appendChild(owner.createTextNode(text))
 
            for child_dict in node_dict.get("children", []):
                elem.appendChild(_build(child_dict, owner))
 
            return elem
 
        root_elem = _build(tree, doc)
        doc.appendChild(root_elem)
        return doc
 

    def dom_to_string(self) -> str :
        return self.dom_tree.toxml()