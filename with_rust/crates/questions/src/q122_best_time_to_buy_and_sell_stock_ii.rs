struct Solution; 

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.len() <= 1 {
            return 0;
        }

        let mut i = 0;
        let mut acc = 0;

        while i < prices.len() - 1 {
            acc += 0.max(prices[i+1] - prices[i]);
            i += 1
        }

        acc
    }
}