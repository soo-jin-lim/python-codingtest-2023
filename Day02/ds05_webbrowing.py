#스택 활용
import ds04_stack as st
import webbrowser # 웹 브라우저 모듈
import time

st.SIZE = 100
st.stack = [None for _ in range(st.SIZE)]
st.top = -1

if __name__ == '__main__':
    urls = ['www.naver.com', 'ww.daum.net','www.nate.com','www.google.com']

for url in urls:
    st.push(url)
    webbrowser.open(f'http://{url}')
    print(url,end='-->')
    time.sleep(1)


    print('방문종료')

    time.sleep(5)

    while True:
        url = st.pop()
        if url == None:
            break
        webbrowser.open(f'http://{url}')
        print(url, end='-->')
        time.sleep

        print('재방문 종료')
        print(st.stack)

        input('꺼지지말고 기다려')


