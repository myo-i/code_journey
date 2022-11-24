import re

def increment_string(strng):
    # 末尾の数字にマッチ
    pattern = r"[0-9]+$"
    pcompile = re.compile(pattern)
    result = re.search(pcompile, strng)

    
    if result:
        #末尾の数字にマッチして抽出
        num = result.group()
        numcount = len(num)
        # 先頭の0を除く
        trimzero = int(num)
        
        # 計算
        calc = eval("{} + 1".format(trimzero))
        
        # 0埋め
        fillzero = str(calc).zfill(numcount)
        
        # 結合
        output = re.sub(pcompile, '', strng) + fillzero
        return output
    else:
        return strng + "1"
    
# リファクタ
import re

def increment_string(strng):
    # 末尾の数字にマッチ
    pattern = r"[0-9]+$"
    pcompile = re.compile(pattern)
    result = re.search(pcompile, strng)

    
    if result:
        #末尾の数字にマッチして抽出
        num = result.group()
        
        # 先頭の0を除いて計算
        calc = eval("{} + 1".format(int(num)))
        
        # 0埋め
        fillzero = str(calc).zfill(len(num))
        
        # 結合
        return re.sub(pcompile, '', strng) + fillzero
    else:
        return strng + "1"

