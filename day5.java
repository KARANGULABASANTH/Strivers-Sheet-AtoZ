// Floor and Ceil in Sorted Array

// class Solution {
//     public int[] getFloorAndCeil(int[] nums, int x) {
//        int a[]=new int[2];
//        int small=-1;
//        int big=-1;
//        for (int i=0;i<nums.length;i++)
//        {
//          if (nums[i]<=x)
//          {
//             small=nums[i];
//          }
//          if (nums[i]>=x)
//          {
//             big=nums[i];
//             break;
//          }
//        }
//        a[0]=small;
//        a[1]=big;
//        return a;
//     }
// }