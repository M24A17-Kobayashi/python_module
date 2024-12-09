# __all__は from ○○ import * をしたときにimportされる対象の定義
# 書いていない場合はすべての関数がimportされる

__all__ = ['hoge1', 'hoge2']

def hoge1():
    print("I'm hoge1 in module03.py")
    
def hoge2():
    print("I'm hoge2 in module03.py")

def hoge3():
    print("I'm hoge3 in module03.py")
    
