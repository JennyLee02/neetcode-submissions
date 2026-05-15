class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string, vector<string>> map;

        //for each word, sort in alphabetical order
        //if matches the key, store as value in the string vector
        //define a vector and store the map values into the vecvector and return the vector

        for(string &w : strs){
            string temp = w;
            sort(temp.begin(), temp.end());
            map[temp].push_back(w);
        }

        vector<vector<string>> result;
        for(auto &entry : map){
            result.push_back(entry.second);
        }
        return result;
    }
};
