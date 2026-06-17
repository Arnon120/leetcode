struct Solution;

// pub fn max_profit_at_one_sell_if_get_out_of_market_at(prices: &Vec<i32>) -> Vec<i32> {
//     let mut best_profit = 0;
//     let mut current_min_price = i32::MAX;
//     let mut best_profits = vec![0; prices.len()];

//     for i in 0..prices.len(){
//         current_min_price = current_min_price.min(prices[i]);
//         best_profit = best_profit.max(prices[i] - current_min_price);
//         best_profits[i] = best_profit
        
//     }

//     best_profits
// }

pub fn max_profit_at_one_sell_if_get_out_of_market_at(prices: &[i32]) -> Vec<i32> {
    let mut best_profit = 0;
    let mut current_min_price = i32::MAX;

    prices
        .iter()
        .map(|&price| {
            current_min_price = current_min_price.min(price);
            best_profit = best_profit.max(price - current_min_price);
            best_profit
        })
        .collect()
}

// pub fn max_profit_at_one_sell_if_get_into_market_at(prices: &Vec<i32>) -> Vec<i32> {
//     let mut best_profit = 0;
//     let mut current_max_price = i32::MIN;
//     let mut best_profits = vec![0; prices.len()];

//     for i in (0..prices.len()).into_iter().rev() {
//         current_max_price = current_max_price.max(prices[i]);
//         best_profit = best_profit.max(current_max_price - prices[i]);
//         best_profits[i] = best_profit
//     }

//     best_profits
// }

pub fn max_profit_at_one_sell_if_get_into_market_at(prices: &[i32]) -> Vec<i32> {
    let mut best_profit = 0;
    let mut current_max_price = i32::MIN;

    let mut result: Vec<i32> = prices
        .iter()
        .rev()
        .map(|&price| {
            current_max_price = current_max_price.max(price);
            best_profit = best_profit.max(current_max_price - price);
            best_profit
        })
        .collect(); // Note we want to collect. The map is lazy up untill this point. We want to side effects to happen in this order.

    result.reverse();
    result
}

// The actual best solution. Run 4 simulations in paralel, while traversing the prices list - left to right.
// What four simulations? Should you or should you not do this action (buy1, sell1, buy2, sell2) on today's stock.
// Return the best option for the fourth simulation.
impl Solution {
    // You can complete at most two transactions.
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.len() < 2 {
            return 0;
        }
        // The length prices is more than 2.
        
        // Dynamic programing:
        // TODO(Arni): Both lists always hold some unnecessary stuff at their end. 
        //      The other end of one list is never used with anything from the other list - but it might be useful in it of itself.
        let best_sell_from_start_to_day = max_profit_at_one_sell_if_get_out_of_market_at(&prices);
        let best_sell_from_day_to_end = max_profit_at_one_sell_if_get_into_market_at(&prices);

        let mut best_option_at_two_sells = best_sell_from_day_to_end[0];
        for i in 0..(prices.len() - 1) {
            best_option_at_two_sells = best_option_at_two_sells.max(best_sell_from_start_to_day[i] + best_sell_from_day_to_end[i+1])
        }

        best_option_at_two_sells
    }
}

#[cfg(test)]
mod test {
    use super::*;
    use rstest::rstest;


    #[rstest]
    #[case(vec![1,2,3,4,5], 4)]
    #[case(vec![3,3,5,0,0,3,1,4], 6)]
    #[case(vec![1,9,2,10,3,11], 17)]

    fn test_max_profit(#[case] prices: Vec<i32>, #[case] expected: i32) {
        assert_eq!(Solution::max_profit(prices), expected)
    }
}



struct Solution2;

impl Solution2 {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        prices
            .into_iter()
            .fold([-100000_i32; 4], |mut balances, price| {
                balances[0] = balances[0].max(-price);
                balances[1] = balances[1].max(balances[0] + price);
                balances[2] = balances[2].max(balances[1] - price);
                balances[3] = balances[3].max(balances[2] + price);
                balances
            })[3]
    }
}