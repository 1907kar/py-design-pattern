class HtmlElement:
    def __init__(self, element, text="", intend=0):
        self.element = element
        self.text = text
        self.intend = intend

    def __str__(self):
        if self.text != "":   
            return f"{self.intend*" "}<{self.element}>{self.text}</{self.element}>"
        return f"{self.intend*" "}<{self.element}>{self.text}"

# ul = HtmlElement('ul')
# li = HtmlElement('li', 'cat', 2)
# ul_ = HtmlElement('/ul')
# print(ul)
# print(li)
# print(ul_)

    
class HtmlBuilder:
    def __init__(self):
        self.html_list = []
    
    def add_element(self, element, text="", intend=0):
        self.html_list.append(HtmlElement(element, text, intend))
        return self
    
    def export_html(self):
        for element in self.html_list:
            print(element)


animals = HtmlBuilder()\
    .add_element('ul')\
    .add_element('li', 'dog', 2)\
    .add_element('li', 'cat', 2)\
    .add_element('li', 'lion', 2)\
    .add_element('li', 'tiger', 2)\
    .add_element('/ul')\
    .export_html()

vehicles = HtmlBuilder()\
    .add_element('ul')\
    .add_element('ul','Petrol',2)\
    .add_element('li', 'dzire', 4)\
    .add_element('li', 'ritz', 4)\
    .add_element('li', 'city', 4)\
    .add_element('li', 'polo', 4)\
    .add_element('/ul', intend=2)\
    .add_element('ul','Electric',2)\
    .add_element('li', 'kona', 4)\
    .add_element('li', 'i20', 4)\
    .add_element('li', 'hector', 4)\
    .add_element('/ul', intend=2)\
    .add_element('/ul')\
    .export_html()
    