class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int len1 = s1.size();
        int len2 = s2.size();
        unordered_map<char, int> map1;
        unordered_map<char, int> map2;
        int left = 0;
        int right = len1-1;

        if(len1 > len2){
            return false;
        }

        for(int i=0; i<len1; i++){
            map1[s1[i]]++;
            map2[s2[i]]++;
        }

        while(right < len2){
            if(map1 == map2) return true;
            map2[s2[left]]--;
            if(map2[s2[left]]==0) map2.erase(s2[left]);
            left++;

            if(right<len2){
                right++;
                map2[s2[right]]++;
            }
        }
        return false;

        
        

        


    }
};
