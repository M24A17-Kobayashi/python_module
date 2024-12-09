from module03 import *

def main():
    hoge1()
    hoge2()
    hoge3() # hoge3は__all__に含んでいないのでここでエラーが出る

if __name__=="__main__":
    main()