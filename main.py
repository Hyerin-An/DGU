import in2post

class stack:
    def __init__(self):  # 스택 객체 생성
        self.items = []
    def push(self, item):  # 스택 요소 추가 push(.append())
        self.items.append(item)
    def pop(self):   # 스택 요소 삭제 pop()
        return self.items.pop()

acc = stack()
# str = input("Postfix 형식의 사칙연산식을 입력하세요: ").split()
# 사용자 입력 받기
infix_expression = input("Infix 형식의 사칙연산식을 입력하세요: ").split()

postfix_expression = in2post.infix_to_postfix(infix_expression)
print("Postfix 형식으로 변환된 식:", postfix_expression)
str = postfix_expression.split()
# print("Postfix 형식으로 변환된 식:", str)

x = 0

for c in str:
    x = 0
    if c == '+':
        x = acc.pop() + acc.pop()
    elif c == '*':
        x = acc.pop() * acc.pop()
    elif c == '-':
        x = acc.pop() - acc.pop()
    elif c == '/':
        x = acc.pop() / acc.pop()
    elif c >= '0' and c <= '9':
        x = 10 * c + c
    acc.push(c)

x = acc.pop()
print(x)