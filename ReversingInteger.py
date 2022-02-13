class Solution:
    def reverse(self, x):   
        """
        :type x: int
        :rtype: int
        """           
        value=str(x)
        if value[0]=="-" and value[len(value)-1]=="0":
            answer=-int(value[-2:0:-1])

        elif value[len(value)-1]=='0':
            answer=int(value[::-1])

        elif value[0]=="-":
            answer=-+int(value[:0:-1])

        else:
            answer=int(value[::-1])

        if answer > pow(2,31) - 1 or answer< -1 * pow(2, 31):
            return 0

        return answer

        
