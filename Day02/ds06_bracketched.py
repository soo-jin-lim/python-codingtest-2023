#수식 괄호 유효성 여부 확인

import ds04_stack as st

def checkBtacket(expr):
    for ch in expr:
        if ch in '({{<':
            st.push(ch)
        elif ch in')}]>':
            out = st.pop()
            if ch == ')' and out == '(':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass
    if st.isStackEmpty():
        return True
    else:
        return False

st.SIZE = 10
st.stack = [None for _ in range(st.SIZE)]

if __name__ == '__main__':
    exprArry = ['(a+b)', ')a+b(','(a*b)+(c/d)', '(a+b]', '(<a+{b-c}/[c**d]>)' ]
    
    for expr in exprArry:
        top = -1
        print(expr, '==>', checkBtacket(expr))

