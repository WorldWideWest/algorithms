package insertionSort;
import java.util.Arrays;

public class InsertionSort{
    
    public int[] sort(int[] array){

        for(int i = 1; i < array.length; i++){
            int j = i;
            while(j > 0 && array[j - 1] > array[j]){
                int temp = array[j];
                array[j] = array[j - 1];
                array[j - 1] = temp;
                j -= 1;
            }
        }

        return array;
    }

    public static void main(String[] args) {
        InsertionSort insertionSort = new InsertionSort();
        int[] array = {4, 3, 7, 0, 9};
        System.out.println(Arrays.toString(insertionSort.sort(array)));
    }

}