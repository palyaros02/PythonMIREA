class Num:
    def __init__(self, x):
        self.x = x


class BinOp:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Add(BinOp): pass


class Mul(BinOp): pass


class Sub(BinOp): pass


class Visitor:
    def visit(self, tree):
        cls = type(tree).__name__
        method = "visit_" + cls
        return getattr(self, method)(tree)


class PrintVisitor(Visitor):
    def visit_Num(self, tree):
        return str(tree.x)

    def visit_Add(self, tree):
        return "({} + {})".format(self.visit(tree.x), self.visit(tree.y))

    def visit_Mul(self, tree):
        return "({} * {})".format(self.visit(tree.x), self.visit(tree.y))

    def visit_Sub(self, tree):
        return "({} - {})".format(self.visit(tree.x), self.visit(tree.y))


class CalcVisitor(Visitor):
    def visit_Num(self, tree):
        return tree.x

    def visit_Add(self, tree):
        return self.visit(tree.x) + self.visit(tree.y)

    def visit_Mul(self, tree):
        return self.visit(tree.x) * self.visit(tree.y)


    def visit_Sub(self, tree):
        return self.visit(tree.x) - self.visit(tree.y)


class StackVisitor(Visitor):
    def __init__(self):
        self.code = []

    def get_code(self):
        return "\n".join(self.code)

    def visit_Num(self, tree):
        self.code.append(f"PUSH {tree.x}")

    def visitBinOp(op):
        def BinOp(self, tree):
            self.visit(tree.x)
            self.visit(tree.y)
            self.code.append(op)
        return BinOp
    visit_Add = visitBinOp("ADD")
    visit_Mul = visitBinOp("MUL")
    visit_Sub = visitBinOp("SUB")


ast = Add(Num(7), Sub(Mul(Num(3), Num(2)), Num(4)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
print(sv.get_code())
