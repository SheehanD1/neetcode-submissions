class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> temp = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (temp.get(s.charAt(i)) != null) {
                temp.put(s.charAt(i), temp.get(s.charAt(i)) + 1);
            } else{
                temp.put(s.charAt(i), 1);
            }
        }
        for (int i = 0; i < t.length(); i++) {
            if (temp.get(t.charAt(i)) == null || temp.get(t.charAt(i)) <= 0) {
                return false;
            } else { 
                temp.put(t.charAt(i), temp.get(t.charAt(i)) - 1);
            }
        }
        return true;
    }
}
