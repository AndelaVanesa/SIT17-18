#http://erz.element.hr/kon/python-1/podatkovne-zbirke/07_zadaci_za_vjezbu.pdf
#http://os-sesvetska-sela-zg.skole.hr/upload/os-sesvetska-sela-zg/images/static3/3254/attachment/08_zadaci_za_vjezbu.pdf
#http://www.znanje.org/knjige/computer/python/095python/095_function_pyt_frames.htm
Def znamenka(s):
    if s in "0123456789":
        return True
    else:
        return False

def brojZnamenaka(s):
    t=0
    for i in range(len(s)):
        if znamenaka(s[]):
            t+=1
        return t

def main():
    s=input("Rijec: ")
    print(brojznamenaka(s))

main()