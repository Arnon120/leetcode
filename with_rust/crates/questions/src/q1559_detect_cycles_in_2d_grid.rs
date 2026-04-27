
// Sized union fined.
struct UnionFind {
    par: Vec<usize>,
    sizes: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self {
            par: (0..n).collect(),
            sizes: vec![1; n],
        }
    }

    fn find(&mut self, i: usize) -> usize {
        if i==self.par[i] {
            return i;
        }
        self.par[i] = self.find(self.par[i]);
        self.par[i]
    }

    fn union(&mut self, i:usize, j:usize) -> bool {
        let (pi, pj) = (self.find(i), self.find(j));
        if pi==pj {
            return false
        }

        if self.sizes[pi]<self.sizes[pj] {
            self.par[pi]=pj;
            self.sizes[pj]+=self.sizes[pi];
        } else {
            self.par[pj]=pi;
            self.sizes[pi]+=self.sizes[pj];
        }
        true
    }

}


struct Solution;

struct TravelGrid {
    travel_grid: Vec<Vec<bool>>,
    // Number of rows (the length of the outer vector).
    n: usize,
    // Number of columns (the length of the inner vector).
    m: usize,
}

impl TravelGrid {
    fn new(grid: &Vec<Vec<char>>) -> Self {
        let n = grid.len();
        let travel_grid = Vec::with_capacity(grid.len()); 
        let m = if n > 0 {
            grid[0].len()
        } else {
            0
        };
        Self { travel_grid, n, m}
    }

    fn get(&mut self, i: usize, j: usize) -> bool {
        self.get_set(i, j, None).expect("i or j were out of bounds")
    }

    fn set(&mut self, i: usize, j: usize, new_val: bool) {
        let _ = self.get_set(i, j, Some(new_val));
    }

    // Returns an error if i or j are out of bounds.
    fn get_set(&mut self, i: usize, j: usize, new_val: Option<bool>) -> Result<bool,()> {
        if i >=self.n || j >= self.m {
            return Err(());
        }

        if i >= self.travel_grid.len() {
            assert_eq!(i, self.travel_grid.len(), "access to travel grid was out of order.");
            self.travel_grid.push(Vec::with_capacity(self.m));
        };

        if j >= self.travel_grid[i].len() {
            let mut extension = (self.travel_grid[i].len()..=j).map(|_| false).collect();
            (self.travel_grid[i]).append(&mut extension);
        }

        if let Some(new_val) = new_val {
            self.travel_grid[i][j] = new_val;
        }

        Ok(self.travel_grid[i][j])
    }
}


#[derive(PartialEq, Eq, Debug)]
enum TravelDirection {
    // This round is the starting point.
    Start,
    Up,
    Right,
    Down,
    Left
}

impl Solution {
    fn travel_from(came_from: TravelDirection,i: usize, j: usize, grid: &Vec<Vec<char>>, travel_grid: &mut TravelGrid) -> bool{
        // println!("traveled to {i},{j}");
        if travel_grid.get(i, j){
            // if came_from == TravelDirection::Start{
            //     println!("This tile was already covered.")
            // }

            return false;
        }
        travel_grid.set(i, j, true);
        let character = grid[i][j];
        // if came_from == TravelDirection::Start {
        //     println!("Starting the search for a cycle for the letter: {character}");
        // }
 
        let mut next_pairs = vec![];
        if came_from != TravelDirection::Down && i > 0 {
            next_pairs.push((TravelDirection::Up, i-1, j));

        }
        if came_from != TravelDirection::Right && j > 0 {
            next_pairs.push((TravelDirection::Left, i, j-1));
        }
        if came_from != TravelDirection::Up && i + 1 < grid.len() {
            next_pairs.push((TravelDirection::Down, i + 1, j));
        }
        if came_from != TravelDirection::Left && j + 1 < grid[i].len() {
            next_pairs.push((TravelDirection::Right, i, j + 1));
        }
        // println!("Next pairs are: {next_pairs:?}");

        for (going_to, next_i, next_j) in next_pairs {
            if grid[next_i][next_j] == character {
                // The next cell is of this cycle.
                let next_was_traveled = travel_grid.get(next_i, next_j);
                if next_was_traveled {
                    return true;
                }
                else {
                    let found_cycle = Self::travel_from(going_to, next_i, next_j, grid, travel_grid);
                    if found_cycle {
                        return true;
                    }
                };

            }
            else {
                // The next cell is not of this cycle.
                continue;
            }
        }

        return false;
    }

    pub fn contains_cycle(grid: Vec<Vec<char>>) -> bool {      
        if grid.is_empty() {
            return false;
        }
        let mut travel_grid = TravelGrid::new(&grid);
        
        for i in 0..grid.len() {
            for j in 0..grid[i].len() {
                let travel_result = Self::travel_from(TravelDirection::Start, i,j,&grid, &mut travel_grid);
                if travel_result {
                    return true;
                }
            }
        }

        return false;
    }
}


#[cfg(test)]
mod tests {
    // use rstest::rstest;
    use super::*;

    #[test]
    fn run_test(){
        let test_cases = [
            (
                vec![vec!['a','a','b']], 
                false
            ),
            (
                vec![
                    vec!['d','b','b'],
                    vec!['c','a','a'],
                    vec!['b','a','c'],
                    vec!['c','c','c'],
                    vec!['d','d','a']
                ],
                false
            )
        ];
        for (grid, expected) in test_cases {
            test_contains_cycle(grid, expected);
        }
    }

    fn test_contains_cycle(grid: Vec<Vec<char>>, expected: bool) {
        let result = Solution::contains_cycle(grid);
        assert_eq!(result, expected);
    }
}