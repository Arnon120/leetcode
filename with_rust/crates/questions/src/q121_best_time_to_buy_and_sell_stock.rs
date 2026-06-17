#[allow(dead_code)]
struct Solution;

impl Solution {
    #[allow(dead_code)]
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut best_profit = 0;
        let mut current_min_price = i32::MAX;
        
        for price in prices {
            current_min_price = current_min_price.min(price);
            best_profit = best_profit.max(price - current_min_price);
        }

        best_profit
    }
}