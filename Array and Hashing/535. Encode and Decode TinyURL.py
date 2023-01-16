import string, random
class Codec:
    
    def __init__(self):
        self.hm = {}
        self.count = -1

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.count += 1
        self.hm[self.count] = longUrl
        return "http://tinyurl.com/" + str(self.count)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        n = len("http://tinyurl.com/")
        val = int(shortUrl[n:])
        return self.hm[val]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
