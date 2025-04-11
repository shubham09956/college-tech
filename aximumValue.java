import java.util.Scanner;

public class aximumValue {
    public static void main(String[]args){
        Scanner sc=new Scanner(System.in);
        int size=sc.nextInt();
        int max=0;
        int arr[]=new int[size];
        for(int i=0;i<size;i++){
            arr[i]=sc.nextInt();

        }
        for(int i=0;i<arr.length;i++){
            if(arr[i]%2==0){
                int k=2*arr[i];
                if(max<k){
                    max=k;
                }
            }
        }
        System.out.println(max);
        sc.close();
    }
}
