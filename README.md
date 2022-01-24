# LeetcodeProblems

* [JumpGame](#JumpGame)
* [RotateImage](#RotateImage)


## 1.JumpGame

* We can use the Greedy Method to this solve this

### what is Greedy method (RealWorld Example)?

* Like everyone knows the Relay Game in the Olympics ,what is the motive of the game is there will be four people for each team, and there will be placed with the gap of 100m a each . First person just need to pass the cone in his hand to the next person of his team , and it will be continued until the cone reaches the last person(i.e Fourth Person).He/She is the one who reaches the end point or finish line . Same concept is for greedy method also .Like think the first person's finsih line is the second person,if the first person reaches the second person then the job of first person will be finished .same applies in the greedy method 
* So in the Above solution i just initalized two pointer one at the end of the array . Another one is at before the end point . So im checking if the before point can reach the end point , then iam just making the before point as a end point ,I'm continuning this until i reach a first index or point in the array and checking whether the first index value can reach the last index or not if not we are returning False , else we are returning True.

### Back to relay race example

* This is same like realy race.Like if the fourth person can reach the finsih line , then we are considering a fourth person as a finish point , we are repeating this until we reaching the first person ,in that point the second person will be the finsih line , so if first person can reach the second person then the team can reach the endpoint this is like a True Statement in our program . Take a scenario where one of the four person is injuried , then no person can run a 200m .Now the team cannot reach the endline this is like a else statement in our solution


## 2.RotateImage
 * Whenever you get a problem based on matrix or multi-indexed array, try to think solving in a way of outer and inner  matrix.solution for this problem ,we can solve this prblm by handling the value for 
 one topleft in temp and changing the value of other position inplace 
 always think if there is matrix kind of problem do it in the way of
 allocating    ****"top" , "bottom","left","right"**** and then think to solve 
 the problem and we need to make sure also we are changing the inner squares
 also so only we are using the range(r-l) to make sure to take care of the 
 inner matrix to be solved.First Solve outer matrix and come to inner matrix.Most of the times this kind of approach will work
