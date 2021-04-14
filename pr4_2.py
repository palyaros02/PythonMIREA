class HTML:
    def __init__(self):
        self.stack = []
        self.code = []
        self.tag = None
    def __enter__(self):
        self.code.append(f"<{self.tag}>")
        self.stack.append(f"</{self.tag}>")
        return self
    def __exit__(self, *args):
        self.code.append(self.stack.pop())
    def body(self):
        self.tag = "body"
        return self
    def div(self):
        self.tag = "div"
        return self
    def p(self, text):
        self.code.append(f"<p>{text}</p>")
    def get_code(self):
        return "\n".join(self.code)



html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')
print(html.get_code())