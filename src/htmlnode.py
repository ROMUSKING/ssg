class HTMLNode:
    def __init__(self,
                 tag = None,
                 value = None,
                 children = None,
                 props = None):
        self.tag = tag
        self.value = value
        self.children  = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_str = ""
        if self.props != None:
            for prop, value in self.props.items():
                props_str += f' {prop}="{value}"'
        return props_str
    
    def __eq__(self, other):
        return (self.tag == other.tag and 
            self.value == other.value and
            self.props == other.props and
            self.children == other.children)
        
    def __repr__(self):
        return f"{self.tag} = tag, {self.value} = value, {self.children}  = children, {self.props} = props"
    
class LeafNode(HTMLNode):
    def __init__(self,
                 tag,
                 value,
                 props = None):  
        
        super().__init__(tag=tag,
                    value=value,
                    props=props)
        
    def to_html(self):
        if self.value == "" or self.value == None:
            raise ValueError("No value in leaf node")
        if self.tag == "" or self.tag == None:
            return f"{self.value}"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __eq__(self, other):
        return (self.tag == other.tag and 
            self.value == other.value and
            self.props == other.props )
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

   
class ParentNode(HTMLNode):
    def __init__(self,
                 tag,
                 children,
                 props = None):  
        
        super().__init__(tag=tag,
                    children=children,
                    props=props)
        
        
    def to_html(self):
        if self.children == "" or self.children == None or self.children == ():
            raise ValueError("parent has no children")
        if self.tag == "" or self.tag == None:
            raise ValueError("parent has no tag")
        
        html = f"<{self.tag}{self.props_to_html()}>"
         
        for child in self.children:
            html += child.to_html()
    
        html += f"</{self.tag}>"
        
        return html

    def __eq__(self, other):
        return (self.tag == other.tag and 
            self.props == other.props and
            self.children == other.children)
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
