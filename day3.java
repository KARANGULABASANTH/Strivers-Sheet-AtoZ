// import java.util.*;
// class day3{
//     public static void main(String args[])
//     {
//         Scanner sc=new Scanner(System.in);
//         System.out.println("Enter a number");
//         int n=sc.nextInt();
//         int t=n;
//         int ocount=0;
//         while (t!=0)
//         {
//             int ans=t%10;
//             if (ans%2!=0)
//             {
//                 ocount+=1;
//             }
//             t=t/10;
//         }
//         System.out.println(ocount);
//         sc.close();
//     }
// }


//    Armstrong Number

// import java.util.*;
// class day3{
//     public static void main(String args[])
//     {
//         Scanner sc=new Scanner(System.in);
//         System.out.println("Enter a number");
//         int n=sc.nextInt();
//         int t;
//         t=n;
//         int s=0;
//         int ans;
//         while (n!=0)
//         {
//             ans=n%10;
//             s+=(ans*ans*ans);
//             n=n/10;
//         }
//         if (t==s)
//         {
//             System.out.println("It is armstrong number");
//         }
//         else 
//         {
//             System.out.println("No it  is not armstrong number");
//         }
//         sc.close();
//     }
// }


//      Prime Number 

// class Solution {
//     static boolean isPrime(int n) {
//         int count=0;
//         for (int i=1;i<=n;i++)
//         {
//             if (n%i==0)
//             {
//                 count+=1;
//             }
//         }
//         if (count==2)
//         {
//             return true;
//         }
//         else 
//         {
//             return false;
//         }
//     }
// }




//   Divisoprs of a number 

// class Solution {
//     public ArrayList<Integer> getDivisors(int n) {
//         // int a[]=new int[n];
//         ArrayList<Integer>a=new ArrayList<Integer>();
//         // int t=0;
//         for (int i=1;i<=n;i++)
//         {
//             if (n%i==0)
//             {
//                 a.add(i);
//                 // t+=1;
//             }
//         }
//         return a;
//     }
// }