import java.util.Scanner;

class EchoOdd{
    public static void main(String[]args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the array Size");
        int n=sc.nextInt();
        int arr[]=new int [n];
        // int arr[]={1,2,4,5,6,8,9};
        for(int i=0;i<arr.length;i++){
            arr[i]=sc.nextInt();
        }
        for(int i=1;i<arr.length; i=i+2){
           
            System.out.println(arr[i]);
           
        
        }
        sc.close();


    }
}
