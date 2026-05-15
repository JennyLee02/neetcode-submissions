#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        int diff;

        for(int i=0; i<nums.size(); i++){
            diff=target-nums[i];
            if(map.find(diff)!=map.end()){
                return {map[diff], i};
            }
            else {
                map[nums[i]]=i;
            }
        }

    }
};
