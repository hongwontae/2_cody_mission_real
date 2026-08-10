import json


# 파일 객체를 인자로 받아서 Python 객체로 변환
with open("./student.json", "r", encoding="utf-8") as f :
    data = json.load(f)
    print(data)
    print(type(data))


person = {
    "name" : "Hong",
    "age" : 29
}

# Python 객체를 받고 JSON 문자열로 변환
# type -> str
data2 = json.dumps(person)
print(data2)
print(type(data2))


# JSON 문자열을 받고 Python 객체로 변환
# type -> dict
data3 = json.loads(data2)
print(data3)
print(type(data3))


with open("./student.json", "r", encoding="utf-8") as f2 :
    f_data = json.load(f2)

print(f_data)

student = {
    "name": "홍길동",
    "age": 20
}

with open("./student.json", "w", encoding="utf-8") as f3 :
    f_data2 = json.dump(student, f3, indent=4, ensure_ascii=False)
