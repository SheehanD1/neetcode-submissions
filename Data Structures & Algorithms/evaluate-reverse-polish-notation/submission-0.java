class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> store = new Stack<>();
        for (String token : tokens) {
            if (token.equals("+")) {
                int b = store.pop();
                int a = store.pop();
                store.push(a + b);
            } else if (token.equals("-")) {
                int b = store.pop();
                int a = store.pop();
                store.push(a - b);
            } else if (token.equals("*")) {
                int b = store.pop();
                int a = store.pop();
                store.push(a * b);
            } else if (token.equals("/")) {
                int b = store.pop();
                int a = store.pop();
                store.push(a / b);
            } else {
                store.push(Integer.parseInt(token));
            }
        }
        return store.pop();
    }
}
