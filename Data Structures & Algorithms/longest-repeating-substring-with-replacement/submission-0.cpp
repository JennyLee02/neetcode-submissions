class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map <char, int> freq;
        int left=0; 
        int right = 0;
        int maxCount = 0;
        int result = 0;

        for(right=0; right<s.size(); right++){
            char c = s[right];
            //add the char c into frequency map 
            freq[c]++;
            //recalculate the maximum count of a char in the window
            maxCount = max(maxCount, freq[c]);

            // while there are more unique char in the window than k
            while((right - left + 1) - maxCount > k){
                //decrement the left most char count of the window
                freq[s[left]]--;
                //move the left pointer to the left 
                left++;
            }
            result = max(result, (right - left + 1));
        }
        return result;
    }
};
