class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> strs;
        int left = 0;
        int result = 0;

        for(int i = 0; i<s.size(); i++){
            int right = i;
            while(strs.find(s[i])!=strs.end()){
                strs.erase(s[left]);
                left++;
            }
            strs.insert(s[right]);
            result = max(result, right-left+1);
        }
        return result;
    }
};
