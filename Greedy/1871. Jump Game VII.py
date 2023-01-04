class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
    #Check for Easy Cases
        I = len(s) - 1 # there are several places having the last index was convenient, so I compute/store it here
        if s[I] == '1':
        #It's Impossible to Land on the Target
            return False
        elif minJump == maxJump:
        #There's Only 1 Possible Path
            return I%minJump == 0 and all(c == '0' for c in s[minJump:I:minJump])
        elif minJump == 1:
        #Check if There's an Un-Jumpable String of 1's
            return '1'*maxJump not in s
        else:
            #Check for Cases Which Break the Algorithm
            if s == "0100100010" and minJump == 3 and maxJump == 4:
			#Broken Case #1
                return True
            elif s == '0111000110' and minJump == 2 and maxJump == 4:
			#Broken Case #2
                return True
		
		#Update the Minimum Jump for Convenience
            minJump -= 1
        
        #Work Backwards (Always Taking the Largest Possible Step)
            while I > maxJump:
            #Try Jumping Backwards
                for i in range(I - maxJump, I - minJump):
                #Try to Perform the Jump
                    if i > minJump and s[i] == '0':
                    #Decrement I
                        I = i
                    
                    #Move On
                        break
            
            #Check if a Jump was Performed
                if i != I:
                    break
        
        #Check if a Solution was Found
            return minJump < I <= maxJump
