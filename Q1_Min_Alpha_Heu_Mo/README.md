# Game Search Algorithms for Tic-Tac-Toe

## Overview

This project implements four game search algorithms for the Tic-Tac-Toe game:

* Minimax Search
* Alpha-Beta Search
* Heuristic Alpha-Beta Search
* Monte Carlo Tree Search (MCTS)

The objective is to compare different search techniques used in Artificial Intelligence for decision making in adversarial games.

---

## Algorithms Implemented

### 1. Minimax Search

Minimax explores the complete game tree and assumes both players play optimally. The algorithm chooses the move that maximizes the utility for the current player while minimizing the opponent's utility.

### 2. Alpha-Beta Search

Alpha-Beta Search is an optimization of Minimax. It prunes branches that cannot affect the final decision, reducing the number of states explored while producing the same result as Minimax.

### 3. Heuristic Alpha-Beta Search

This algorithm combines Alpha-Beta pruning with a heuristic evaluation function. Instead of exploring the entire game tree, the search is limited to a specified depth and non-terminal positions are evaluated using a heuristic score.

### 4. Monte Carlo Tree Search (MCTS)

MCTS uses random simulations to estimate the strength of moves. The algorithm consists of four phases:

1. Selection
2. Expansion
3. Simulation
4. Backpropagation

The move with the best statistical performance is selected.

---

## Game Representation

The game used in this project is Tic-Tac-Toe.

* X is the maximizing player.
* O is the minimizing player.
* Empty cells represent legal moves.

The board positions are numbered as:

## 0 | 1 | 2

## 3 | 4 | 5

## 6 | 7 | 8

---

## Test Cases

The implementation was tested using multiple board configurations.

### Test Case 1: Winning Move

Board:

## X | O | X

## O | X | O

## O | X |

Expected Result:

* Minimax selects the winning move.
* Alpha-Beta selects the same move.
* Heuristic Alpha-Beta selects the same move.
* MCTS identifies the winning move.

### Test Case 2: Blocking the Opponent

Board:

## O | X | X

## X | O |

## | | O

Expected Result:

* The algorithms block the opponent's winning opportunity.

### Test Case 3: Empty Board

Expected Result:

* A valid opening move is selected.
* Minimax and Alpha-Beta evaluate the position as a draw with optimal play.

### Test Case 4: Algorithm Comparison

* Alpha-Beta vs Minimax
* Alpha-Beta vs MCTS

These tests verify consistency and correctness of the implementations.

---

## Results

All test cases passed successfully.

Total Tests: 24

Passed: 24

Failed: 0

The results confirm the correctness of the implementations and demonstrate the expected behavior of all four algorithms.

---

## Running the Program

Requirements:

* Python 3.x

Execute:

```bash
python game_search.py
```

The program will:

1. Run the complete test suite.
2. Display the test results.
3. Demonstrate the behavior of all four algorithms on a sample Tic-Tac-Toe board.

---

## Conclusion

This project successfully implements and evaluates Minimax, Alpha-Beta Search, Heuristic Alpha-Beta Search, and Monte Carlo Tree Search for Tic-Tac-Toe. The algorithms were verified using multiple test cases and produced correct results across all evaluations.
