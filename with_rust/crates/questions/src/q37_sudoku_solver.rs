use std::{cell, collections::binary_heap::Iter};

trait SudokuCellTrait: From<char> + Into<char> {
    // Returns a cell that we don't know the value of. Potentialy, can be either value from 1-9.
    fn new() -> Self;
    // Given a mask of possible values from 1 to 9, 
    // that represents all the possible values the we know the cell can't take, 
    // represented by the sum of powers of two of said values. 
    fn eliminate_mask(self, mask: u16) -> Self;
    fn is_locked(&self) -> bool;
}

struct Solution;

const ALL_FLAGS: u16 = ((1 << 9) - 1) << 1;

/// The possible values of a Sudoku cell.
/// Uses the first 10 bits of the u16.
/// Bit 0 - is the cell locked. i.e. is there just one possible option for the value of this cell.
/// Bit i - (where i is in range 1-9), is it possible for this cell to be the value i. 
/// Assumption - at least one of the bits 1-9 is on. When exactly one bit is on - the zero bit is on.
struct SudokuCell (u16);

impl SudokuCell {
    fn new() -> Self {
        Self(ALL_FLAGS)
    }

    fn is_locked(&self) -> bool {
        self.0 % 2 == 1
    }

    // Reutns true if post elimination, there is just one number.
    fn eliminate_mask(&mut self, mask: u16) {
        if self.is_locked(){
            return;
        }

        self.0 = self.0 & !mask;
        // Is the remaining value have exactly one flag turned on?
        let is_locked = match self.0 {
            2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 => true,
            _ => false
        };
        if is_locked {
            self.0 += 1
        }
    }

    fn set_value(&mut self, value: u8) {
        assert!(!self.is_locked(), "Setting a value of a locked cell.");
        let value_as_mask = 1_u16 << value;
        assert_eq!(value_as_mask, value_as_mask & self.0, "Trying to set the value {value} for a cell where it is not potentially true");

        // Set the new value and set the cell as locked.
        self.0 = value_as_mask + 1;
    }
    
    fn is_potential(&self, i: u8) -> bool {
        (self.0 >> i) % 2 == 1
    }

    fn potential_numbers(&self) -> impl Iterator<Item = u8> + '_ {
        (1u8..=9).filter(|&i| self.is_potential(i))
    }
    

}

impl From<char> for SudokuCell {
    fn from(character: char) -> Self {
        match character {
            '.' => Self::new(),
            _ => {
                let num: u8 = character
                    .to_digit(10)
                    .expect("unexpected character as character of a cell.")
                    .try_into()
                    .unwrap(); 
                Self (1 << num)
            }
        }
    }
}

impl From<SudokuCell> for char {
    fn from(cell: SudokuCell) -> char {
        if !cell.is_locked() {
            return '.';
        }

        char::from_digit((cell.0 - 1).trailing_zeros(), 10).expect("unexpected digits.")
    }
}

impl From<&SudokuCell> for char {
    fn from(cell: &SudokuCell) -> char {
        if !cell.is_locked() {
            return '.';
        }

        char::from_digit((cell.0 - 1).trailing_zeros(), 10).expect("unexpected digits.")
    }
}

enum IterFactory {
    Row(usize),
    Column(usize),
    Square(usize, usize),
}

#[derive(Default)]
enum SudokuCellStatus<'a> {
    #[default]
    None,
    PotentialCell(&'a mut SudokuCell),
    MultiCought,
}


struct SudokuBoard (Vec<Vec<SudokuCell>>);

impl SudokuBoard {
    fn new(board: &Vec<Vec<char>>) -> Self {
        Self (
            board.iter().map(|row | {
                row.iter().map(|cell| SudokuCell::from(*cell)).collect()
            })
            .collect()
        )
    }

    fn assign_to_board(self, board: &mut Vec<Vec<char>>) {
        for i in 0..9 {
            for j in 0..9 {
                board[i][j] = char::from(&self.0[i][j])
            }
        }
    }

    // TODO(Arni): maybe a version that does not collect...
    // TODO(Arni): This should return a list of indexes to the board. Not the cells themselves.
    fn block_iterator(&mut self, iter_factory: &IterFactory) -> Vec<&mut SudokuCell> {
        match iter_factory {
            IterFactory::Row(i) => self.iter_row(*i).collect(),
            IterFactory::Column(j) => self.iter_column(*j).collect(),
            IterFactory::Square(i, j) => self.iter_square(*i, *j).collect(),
        }
    }

    fn iter_row(&mut self, i: usize) -> impl Iterator<Item = &mut SudokuCell> {
        assert!(i < 9);
        self.0[i].iter_mut()
    }

    fn iter_column(&mut self, j: usize) -> impl Iterator<Item = &mut SudokuCell> {
        assert!(j < 9);
        self.0.iter_mut().map(move |row| &mut row[j])
    }

    fn iter_square(&mut self, i: usize, j: usize) -> impl Iterator<Item = &mut SudokuCell> {
        assert!(i < 3 && j < 3);
        self
            .0
            .iter_mut()
            .enumerate()
            .filter(move |(index, _row)| {*index / 3 == i})
            .map(move |(_index, row)| {
                row
                    .iter_mut()
                    .enumerate()
                    .filter(move |(jndex, _cell)| {*jndex / 3 == j} )
                    .map(move |(_jndex, cell)| cell)
                }
            ).flatten()
    }

    // Replace with eliminate_block
    fn eliminate_column(&mut self, j: usize) -> bool{
        self.eliminate_block(&IterFactory::Column(j)) 
    }

    // Replace with eliminate_block
    fn eliminate_row(&mut self, i: usize) -> bool {
        self.eliminate_block(&IterFactory::Row(i))
    }

    fn eliminate_square(&mut self, i: usize, j: usize) -> bool {
        self.eliminate_block(&IterFactory::Square(i, j))
    }

    // Returns true if all the block is already fixed.
    fn eliminate_block(&mut self, iter_factory: &IterFactory) -> bool {
        let mut mask = 0;
        for cell in self.block_iterator(iter_factory){
            if cell.is_locked() {
                mask += cell.0 -1
            }
        }
        if mask == ALL_FLAGS{
            return true;
        }

        // If for a give cell, all options for the value of a cell are exusted - mark it.
        for cell in self.block_iterator(iter_factory) {
            cell.eliminate_mask(mask);
        }

        // // Make sure that in the block - each number appears at least once.
        // let mut potential_cells: [SudokuCellStatus<'_>; 9] = Default::default();
        // for cell in self.block_iterator(iter_factory) {
        //     for i in cell.potential_numbers() {
        //         let index = usize::from(i) - 1;
        //         match potential_cells[index] {
        //             SudokuCellStatus::None => {
        //                 potential_cells[index] = SudokuCellStatus::PotentialCell(cell);
        //             },
        //             SudokuCellStatus::PotentialCell(_) => {
        //                 potential_cells[index] = SudokuCellStatus::MultiCought;
        //             },
        //             SudokuCellStatus::MultiCought => {}
        //         }
        //     }
        // }

        // potential_cells.into_iter().enumerate().for_each(|(i, cellstaus)| {
        //     if let SudokuCellStatus::PotentialCell(cell) = cellstaus {
        //         cell.set_value(u8::try_from(i).unwrap() + 1);
        //     }
        // });


        false
    }

    // Returns true if all the Soduko is solved.
    fn iterate_over_all(&mut self) -> bool {
        let mut was_all_fixed = true;
        for i in 0..9 {
            was_all_fixed = was_all_fixed & self.eliminate_row(i);
        }
        for j in 0..9 {
            was_all_fixed = was_all_fixed & self.eliminate_column(j)
        }
        for i in 0..3 {
            for j in 0..3 {
                was_all_fixed = was_all_fixed & self.eliminate_square(i, j)
            }
        }
        
        was_all_fixed
    }
    
}


impl Solution {

    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        let mut sudoku_board = SudokuBoard::new(board);
        for _i in 0..82 {
            if sudoku_board.iterate_over_all() {
                break;
            }
        }

        sudoku_board.assign_to_board(board);

    }
}



#[cfg(test)]
mod tests{
    use super::*;
    use rstest::rstest;

    fn str_board_to_chars_board(board: [[&str; 9]; 9]) -> Vec<Vec<char>>{
        board
            .into_iter()
            .map(|row| {
                    row
                        .into_iter()
                        .map(|cell| cell.chars().next().unwrap())
                        .collect()
                }
            ).collect()
    }

    #[test]
    fn possible_nums_init(){
        let possibles = SudokuCell::new();
        println!("possibles = {:b}", possibles.0);
        assert_eq!(possibles.0 , 1022);
    }



    #[rstest]
    #[case(
        [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
        [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    )]
    #[case(
        [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]],
        [["5","1","9","7","4","8","6","3","2"],["7","8","3","6","5","2","4","1","9"],["4","2","6","1","3","9","8","7","5"],["3","5","7","9","8","6","2","4","1"],["2","6","4","3","1","7","5","9","8"],["1","9","8","5","2","4","3","6","7"],["9","7","5","8","6","3","1","2","4"],["8","3","2","4","9","1","7","5","6"],["6","4","1","2","7","5","9","8","3"]]
    )]
    fn test_solve_sudoku(#[case] board: [[&str;9];9], #[case] expected_board: [[&str;9];9] ) {
        let mut board= str_board_to_chars_board(board);
        Solution::solve_sudoku(&mut board);

        let expected_board = str_board_to_chars_board(expected_board);

        assert_eq!(board, expected_board)
    }
    
    
}