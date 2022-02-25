package bubbleSort;

import java.util.Arrays;

public class BubbleSort {
    
    public int[] sort(int[] array) {
        
        for (int i = 0; i < array.length; i++) {
            
            for (int j = 0; j < array.length - i - 1; j++) {
                
                if (array[j] > array[j + 1]){
                    
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;

                }
            }

        }

        return array;
    }

    public static void main(String[] args) {
        BubbleSort bubbleSort = new BubbleSort();
        int[] array = {3, 5, 1, 8, 5, 4, 7, 6, 9, 0};
        System.out.println(Arrays.toString(bubbleSort.sort(array)));
    }

}
