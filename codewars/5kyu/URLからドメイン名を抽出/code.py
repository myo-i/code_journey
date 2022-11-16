import re

def domain_name(url):
    print(url)
    patternWWW = r"htt(p|ps)://www\.([^\.]*)\.(\S*)"
    pattern = r"htt(p|ps)://([^\.]*)\.(\S*)"
    www = r"www.([^\.]*)\.(\S*)"
    elsepattern = r"([^\.]*)\.(\S*)"
    
    repatternWWW = re.compile(patternWWW)
    repattern = re.compile(pattern)
    rewww = re.compile(www)
    reelsepattern = re.compile(elsepattern)
    
    if "://www" in url:
        result1 = repatternWWW.match(url)
        return result1.group(2)
    elif (url.startswith("www.")):
        result2 = rewww.match(url)
        return result2.group(1)
    elif (url.startswith("http://") or url.startswith("https://")):
        result3 = repattern.match(url)
        return result3.group(2)
    else:
        result4 = reelsepattern.match(url)
        return result4.group(1)
        

