public class Solution {
    public int[] ReplaceElements(int[] arr) {
        int maxSoFar = -1; // last element will be -1
        for (int i = arr.Length - 1; i >= 0; i--) {
            int temp = arr[i];
            arr[i] = maxSoFar;
            if (temp > maxSoFar) {
                maxSoFar = temp;
            }
        }
        return arr; // return the array
    }
}