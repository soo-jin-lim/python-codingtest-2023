#프랙탈 원 그리기
from turtle import *  #그림그려주는 거북이

setup(width=600, height=600) # 거북이 만들기
color('red', 'yellow')

begin_fill()
while True:
    forward(200)
    left(170)
    if abs (pos()) < 1:
        break
end_fill()
done()

mainloop()