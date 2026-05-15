// used fixed size array of size 26
// for each char - a, add and sub ==> if s and t are same, become 0
// check if the elements of count array is zero. 
// if not, return false

class Solution {
public:
    bool isAnagram(string s, string t) {
         int len1=s.size();
         int len2=t.size();

         if(len1 != len2) return false;
         
         int count[26]={0};

         for(int i=0; i<len1; i++){
            count[s[i]-'a']++;
            count[t[i]-'a']--;
         }

         for(int i=0; i<26; i++){
            if(count[i]!=0) return false;
         }

         return true;
    }
};
