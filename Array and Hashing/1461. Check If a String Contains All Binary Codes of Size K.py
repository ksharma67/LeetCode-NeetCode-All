class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:             
        required_count=1<<k  
        seen=[0] * ((required_count-1)//32+1)
        mask=required_count-1
        hash_code=0
        
        def is_set(code):
            idx = code//32
            bit_pos = code%32            
            return seen[idx] & (1<<bit_pos) != 0
        
        def set_bit(code):
            idx = code//32
            bit_pos = code%32  
            seen[idx] |= (1<<bit_pos)
        
        for i in range(len(s)):
            hash_code = ((hash_code<<1) & mask) | (int(s[i]))
            if i>=k-1 and not is_set(hash_code):
                set_bit(hash_code)
                required_count-=1
                if required_count==0:
                    return True
                                
        return False            
