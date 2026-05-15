class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> set(nums.begin(), nums.end());
        int longest = 0;
        

        for(auto &n : set){
            if(set.find(n-1) == set.end()){
                int len = 1;
                int curr = n;

                while(set.find(curr+1) != set.end()){
                    curr++;
                    len++;
                }
                if(len>longest){
                    longest = len;
                }
            }
        }
        return longest;
    }
};
