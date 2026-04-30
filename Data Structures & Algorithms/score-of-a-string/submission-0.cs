public class Solution {
    public int ScoreOfString(string s) {
        // If there are no letters or only one letter, return 0 since there is no difference
        if (s.Length <= 1) return 0;

        int sum = 0; // initialize the sum

        // Start from index 1 so we can compare with the previous character
        for (int i = 1; i < s.Length; i++) {
            sum += Math.Abs(s[i] - s[i - 1]); // difference between current and previous char ASCII values
        }

        return sum; // return the total score
    }
}