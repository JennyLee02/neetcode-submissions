class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        s.erase(remove_if(s.begin(), s.end(), [](char c){return !isalnum(c);}), s.end());
        int right = s.size()-1;

        while(left<right){
            if(s[left]!= s[right]){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
