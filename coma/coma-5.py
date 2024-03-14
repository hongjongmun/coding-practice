# 비밀번호 생성 가능여부
st = input()

if len(st) <= 20:
    if st.isalpha():
        print('P')
    else :
        print('I')
else :
    print('I')