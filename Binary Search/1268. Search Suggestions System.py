class trie:
    def __init__(self, val):
        self.val = val
        self.children = {}# val -> node
        self.order = []
        
class Solution:
    
    def helper(self, sub_ans, cur_word, head):
        if len(sub_ans) == 3:
            return
        for e in head.order:
            if e == chr(ord("a")-1):
                sub_ans.append(cur_word)
            else:
                self.helper(sub_ans, cur_word+e, head.children[e])
        
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #create a trie to store the product name
        #for each input, return the corresponding words
        head = trie("")
        for name in products:
            cur = head
            for e in name:
                if e not in cur.children:
                    cur.children[e] = trie(e)
                    cur.order.append(e)
                    index = len(cur.order)-1
                    while index>0 and ord(cur.order[index-1]) > ord(cur.order[index]):
                        cur.order[index-1], cur.order[index] = cur.order[index], cur.order[index-1]
                        index -= 1
                cur = cur.children[e]
            cur.order = [chr(ord("a")-1)] + cur.order
        ans = []

        for i, e in enumerate(searchWord):
            if e in head.children:
                cur_word = searchWord[:i+1]
                sub_ans = []
                self.helper(sub_ans, cur_word, head.children[e])
                ans.append(sub_ans)
                head = head.children[e]
            else:
                for _ in range(i, len(searchWord)):
                    ans.append([])
                break
        return ans
