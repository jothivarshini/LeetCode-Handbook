/* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists. */

class target_sum
{
    static int[] targetSum(int []a , int target)
    {
        for(int i = 0 ; i < a.length - 1 ; i++)
            for(int j = i + 1 ; j < a.length ; j++)
            {
                if(a[i] + a[j] == target)
                    return new int[]{i + 1 , j + 1};
            }
        return new int[]{-1 , -1};
    }
    public static void main(String args[])
    {
        int [] a = {1 , 4 , 5 , 11 , 12};
        int target = 9;
        for(int x : targetSum(a , target))
            System.out.print(x + " ");
    }
}