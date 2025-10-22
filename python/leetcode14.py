def longest_common_prefix(str):
    
    if not str:
        return ""
    
    short_str = min(str, key=len)
    
    for i, char in enumerate(short_str):
        for other in str:
            if other[i] != char:
                return short_str[:i]
            
    
    return short_str


print(longest_common_prefix(["interview", "internet", "internal", "include"]))