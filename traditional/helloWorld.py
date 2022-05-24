import time

traditional="hello world!!!!"

print("*"*30+ "\n")

for i in range( len(traditional) ):
    print(traditional[i], end="")
    time.sleep(0.3)
print("\U0001F60D")
print("\n\n" + "*"*30 + "\n")