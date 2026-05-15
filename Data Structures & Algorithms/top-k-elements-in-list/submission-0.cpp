class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int, int> map;

        for(int &num : nums){
            map[num]++;
        }

        priority_queue <pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> min_heap;

        for(auto &entry : map){
            min_heap.push({entry.second, entry.first});
            if(min_heap.size()>k){
                min_heap.pop();
            }
        }

        vector<int> result;
        for(int i=0; i<k; i++){
            result.push_back(min_heap.top().second);
            min_heap.pop();
        }

        return result;

    }
};
