
with open("hello.txt","r",encoding="utf-8") as f:
    for sor in f:
        print(sor.strip())


with open("valami.txt","a",encoding="utf-8") as w:
    w.write("\nHamburger")