class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        answer = False 
        matrix = nums
        
    
        right = len(matrix)-2 
        goal_post = len(matrix)-1 
        
        if len(matrix) <= 1 :
            return True 
    
        while right >=0 :
            if matrix[right] >= goal_post-right :
                if right == 0 :
                    answer = True
                    right -= 1
                else:
                    goal_post = right 
                    right -= 1 
                
            else : 
                right -= 1 
        return answer
    
    
