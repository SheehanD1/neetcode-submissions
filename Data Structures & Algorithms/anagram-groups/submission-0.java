class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> check = new HashMap<>();
        for (char c : s.toCharArray()) {
            check.put(c, check.getOrDefault(c, 0) + 1);
        }
        for (char c : t.toCharArray()) {
            if (!check.containsKey(c)) {
                return false;
            }
            check.put(c, check.get(c) - 1);
            if (check.get(c) < 0) {
                return false;
            }
        }
        return true;
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        List<String> list = new ArrayList<>(Arrays.asList(strs));
        List<List<String>> result = new ArrayList<>();
        boolean[] used = new boolean[list.size()];
        int listSize = list.size();

        for (int i = 0; i < listSize; i++) {
            if (used[i]) continue;

            List<String> cur = new ArrayList<>();
            cur.add(list.get(i));
            used[i] = true;

            for (int j = i + 1; j < listSize; j++) {
                if (!used[j] && isAnagram(list.get(i), list.get(j))) {
                    cur.add(list.get(j));
                    used[j] = true;
                }
            }

            result.add(cur);
        }

        return result;
    }
}
