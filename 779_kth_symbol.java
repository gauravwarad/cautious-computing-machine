class Solution {
    public int kthGrammar(int n, double k) {

        if (n == 1){
            return 0;
        }

        int row = kthGrammar(n-1, Math.ceil(k/2));

        if (row == 0){
            if (k%2==0){
                return 1;
            }
            else{
                return 0;
            }
        }
        else{
            if (k%2==0){
                return 0;
            }
            else{
                return 1;
            }
        }

    }
    public static void main(String args []){
        int n = 2;
        double k = 2;
        Solution obj = new Solution();
        System.out.println(obj.kthGrammar(n, k));
    }
}