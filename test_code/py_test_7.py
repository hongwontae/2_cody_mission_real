def hello_world (name) :
    print(f"안녕하세요 저는 {name} 입니다.")



def calculation (a, b) :
    plus_result = a+b;
    minus_result = a-b;
    return plus_result, minus_result

a, b = calculation(100, 20)
print(a)
print(b)

hello_world("싸이")