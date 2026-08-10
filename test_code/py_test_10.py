f = open("./hello-world.txt", 'a')
f.write("그대는 도대체가 누구시길래\n")
f.close();

f = open("./hello-world.txt", 'r');
kkk = f.read();
print(kkk)