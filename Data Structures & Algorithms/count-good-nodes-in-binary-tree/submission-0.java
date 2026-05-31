class Solution {
    public int goodNodes(TreeNode root) {
        return dfs(root, root.val);
    }

    private int dfs(TreeNode node, int maxSoFar) {
        if (node == null) return 0;

        int good = node.val >= maxSoFar ? 1 : 0;

        maxSoFar = Math.max(maxSoFar, node.val);

        good += dfs(node.left, maxSoFar);
        good += dfs(node.right, maxSoFar);

        return good;
    }
}
