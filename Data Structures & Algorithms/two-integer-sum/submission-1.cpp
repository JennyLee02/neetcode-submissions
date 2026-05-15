class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int diff;
        unordered_map <int, int> seen;

        for(int i=0; i<nums.size(); i++){
            diff=target-nums[i];
            if(seen.count(diff)){
                return {seen[diff], i};
            }
            else seen[nums[i]] = i;
        }
    }
};
