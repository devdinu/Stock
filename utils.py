def as_list(response):
    return "".join(["<li>" + item + "</li>" for item in response])

def list(items):
    return "<ul>" + items + "</ul>"

def wrap_with(tag, text):
    return tag + text + end_tag(tag)

def end_tag(tag):
    return tag[:1] + "/" + tag[1:]

def ordered_list(items):
    return wrap_with(tag("ol"), as_list(items))

def tag(what):
    return "<" + what + ">"

def script(jsfile):
    return "<script type=\"text/javascript\" src=\"" +jsfile+ "\"></script>"

def include_jsfiles(jsfiles):
    return wrap_with(tag("head")    , "".join([script(js) for js in jsfiles]))

def options(items):
    return "".join(map(lambda t: wrap_with(tag("option"), t), items))

def dropdowns(items):
    return wrap_with(tag("select"), options(items))

def main_html(text, jsfiles=[]):
    return "<html>" + include_jsfiles(jsfiles) + text + "</html>"
