/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int recurse(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int i = recurse(root.left);
        int j = recurse(root.right);
        return 1 + Math.max(i,j);
    }
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        int i = recurse(root.right);
        int j = recurse(root.left);
        if (Math.abs(i - j) > 1) return false;

        return isBalanced(root.left) && isBalanced(root.right);
    }
}
