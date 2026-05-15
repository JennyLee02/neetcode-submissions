class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 0);
        
        for(int i=0; i<nums.size(); i++){
            int left = 1;
            int right =1;
            for(int j=0; j<i; j++){
                left *= nums[j];
            }
            for(int k=nums.size()-1; k>i; k--){
                right *= nums[k];
            }
            result[i] = left * right;
        }
        return result;
    }
};
