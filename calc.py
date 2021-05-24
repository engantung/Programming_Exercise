import sys

class Calculator:

    def __init__(self):
        setattr(self, "add", self.add)
        setattr(self, "multiply", self.mul)

    def add(self, args):
        x = int(bool(len(args)))
        for a in args:
            x += int(a)
        return x-1

    def mul(self, args):
        x = int(bool(len(args)))
        for a in args:
            x *= int(a)
        return x

    def eval(self, expr):
        l = [self.eval(l) if isinstance(l, list) else l for l in expr]
        return getattr(self, l[0])(l[1:])

    def parse(self, expr):
        return self.__parse(expr[1:-1])

    def __parse(self, expr):
        e = expr.strip(" ")
        if len(e) < 1:
            return "nil"
        t = []
        if e[0] == "(":
            d = 0
            r = ""
            for c in e:
                if c == "(":
                    d += 1
                elif c == ")":
                    d -= 1
                r += c
                if d == 0:
                    t.append(self.__parse(r[1:-1]))
                    if len(e[len(r):]):
                        t.extend(self.__parse(e[len(r):]))
                    break
            
        else:
            if " " in e:
                t.append(e[:e.index(" ")])
                t.extend(self.__parse(e[e.index(" ") + 1:]))
            else:
                return [e]
        if t:
                return t
        else:
            return "nil"

def check_argument():
    input_argument = sys.argv[-1]
    if input_argument[0] == "(":
        #example input argument -> "(add 1 2 3 4)"
        calc = Calculator()
        for arg in sys.argv[1:]:
            print(calc.eval(calc.parse(arg)))
    else:
        #example input argument -> "123"
        print(input_argument)

if __name__ == "__main__":    
    check_argument()