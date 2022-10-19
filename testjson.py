import json

data={
    "name":["pp","panpan"],
    "age":27,
    "gender":"female"
}
print(type(data))
data1 = json.dumps(data)
print(data1,type(data1))
data2 = json.loads(data1)
print(data2,type(data2))
