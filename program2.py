def decode_message( s: str, p: str) -> bool:

# write your code here
        if len(s)!=len(p) :
                if (p =='*'):
                    return True
                else:
                      return False
        
        else:
                for i in range(len(s)):
                    if (p[i]== s[i] or p[i]=='?'):
                          return True
  
        return False