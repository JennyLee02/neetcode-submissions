class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map <vector<int>, vector<string>> mp;

        // string vector store words that share the same alphabet count.
        for(string &w : strs){
            vector <int> freq(26, 0);
            for(int i=0; i<w.size(); i++){
                freq[w[i]-'a']++;
            }
            mp[freq].push_back(w);
        }
        
        //store in vector to return in vector
        vector<vector<string>> result;
        for(auto &entry : mp){
            result.push_back(entry.second);
        }
        return result;
    }
};
