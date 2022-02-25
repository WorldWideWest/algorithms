package selectionSort;

import java.util.Arrays;

public class SelectionSort {
    public int[] sort(int[] array){

        for (int i = 0; i < array.length; i++) {
            
            int minIndex = i;

            for (int j = i + 1; j < array.length; j++) {
                if(array[minIndex] > array[j]) minIndex = j;
            }
            
            int temp = array[minIndex];
            array[minIndex] = array[i];
            array[i] = temp;

        }

        return array;
    }

    public static void main(String[] args) {
        SelectionSort selectionSort = new SelectionSort();
        int[] array = {3, 5, 1, 8, 5, 4, 7, 6, 9, 0};
        System.out.println(Arrays.toString(selectionSort.sort(array)));
    }
}
