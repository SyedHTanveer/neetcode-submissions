public class Solution {
    public bool IsSubsequence(string s, string t) {
        int i = 0;
        int j = 0;

        while (i < t.Length && j < s.Length) {
            if (t[i] == s[j]) {
                j++;
            }

            i++;
        }

        if (s.Length == j) {
            return true;
        }
    
    return false;
    }
}