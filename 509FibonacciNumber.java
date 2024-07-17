class FibonacciNumber{
    public int fib(int n) {
        if (n==1){
            return 1;
        }
        else if (n == 0){
            return 0;
        }
        return fib(n-1) + fib(n-2);
    }

    public static void main(String args []){
        int n = 8;
        FibonacciNumber obj = new FibonacciNumber();
        System.out.println(obj.fib(n));
    }
}