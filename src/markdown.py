

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes,  text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.TEXT:
            
            new_nodes = append_text_node(old_node.text,  text_type, new_nodes)
        else:
            new_nodes.append(old_node)
    return new_nodes
            
def append_text_node(old_node_text, text_type, new_nodes):
    delimiters = text_type.value[1]
    text_node_and_rest = old_node_text.split(delimiters[0], 1)
    print(text_node_and_rest, 1)
    if len(text_node_and_rest[0]) > 0:
        new_nodes.append(TextNode(text_node_and_rest[0], TextType.TEXT))
    print(text_node_and_rest, 43434)
    if len(text_node_and_rest) < 2 or len(text_node_and_rest[1]) < 1:
        return new_nodes
    else:
        return append_type_node(text_node_and_rest[1],  text_type, new_nodes)
    
def append_type_node(old_node_text,  text_type, new_nodes):
    delimiters = text_type.value[1]
    if text_type == TextType.LINK or text_type == TextType.IMAGE:
        return append_link_node(old_node_text,  text_type, new_nodes)
           
    typed_text_and_rest = old_node_text.split(delimiters[0], 1)
    
    if len(typed_text_and_rest) < 2:
        raise Exception("Invalid syntax, unclosed delimiters")
        
    if len(typed_text_and_rest[0]) > 0:    
        new_nodes.append(TextNode(text=typed_text_and_rest[0], text_type=text_type))
    
    if len(typed_text_and_rest[1]) > 0:
        return append_text_node(typed_text_and_rest[1],  text_type, new_nodes)

    return new_nodes
    
def append_link_node(old_node_text,  text_type, new_nodes):
    delimiters = text_type.value[1]
    text_link_and_rest = old_node_text.split(delimiters[1], 1)
    
    if len(text_link_and_rest) < 2 or len(text_link_and_rest[0]) < 1 or len(text_link_and_rest[1]) < 1:
        raise Exception("Invalid syntax, unclosed delimiters")
        
    text = text_link_and_rest[0]
    link_and_rest = text_link_and_rest[1].split(delimiters[2], 1)

    if len(link_and_rest) < 2 or len(link_and_rest[0]) < 1:
        raise Exception("Invalid link, unclosed delimiters")
       
    url = link_and_rest[0]
            
    new_nodes.append(TextNode(text=text, text_type=text_type, url=url))
    
    if len(link_and_rest[1]) > 0:
        return append_text_node(link_and_rest[1],  text_type, new_nodes)
     
    return new_nodes
    
    