class Solution {
public:

    string encode(vector<string>& strs) {
        string result;
        for (string &w :strs){
            w.insert(0, to_string(w.size())+"#");
            result+=w;
        }
        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        while (i<s.size()){
            int j = i;
            while(s[j] != '#'){
                j++;
            }

            //convert the string number to int
            int len = stoi(s.substr(i, j-i));
            //extract the word from string
            string word = s.substr(j+1, len);
            result.push_back(word);
            i = 1+j+len;
        }
        return result;
    }
};
