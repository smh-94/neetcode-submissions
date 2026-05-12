class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res,i = [],0
    #we use i to iterate through the string S
        while i < len(s):
            #set j to be equal to i so we don't have to 
            j = i
            #while j is not at the delimiter
            while s[j] != "#":
                #continue incrementing until we reach the delimiter
                j += 1
                #set the length of the string as the difference between i and j;
                #where j is exclusive
            length = int(s[i:j])
            #append from the original string s, spliced from the first character after the delimiter to the end of the length acquired.
            res.append(s[j + 1 : j + 1 + length])
            #reset i to the next position after the next delimiter.
            i = j + 1 + length
        #return the result
        return res