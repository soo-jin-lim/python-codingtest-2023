count =3

def openBox():
    print('종이 상자 엽니다')
    global count
    print('종이 상자를 엽니다')
    count -= 1
    if count == 0:
        print('반지름 넣고 반환****')
        return
    
    openBox()
    print('종이 상자를 닫습니다')

if __name__ == '__main__':
    openBox()