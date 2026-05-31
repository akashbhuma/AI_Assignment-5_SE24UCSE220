import math
import random
import time


class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def clone(self):
        g = TicTacToe()
        g.board = self.board[:]
        g.current_player = self.current_player
        return g

    def get_legal_moves(self):
        return [i for i, v in enumerate(self.board) if v == " "]

    def make_move(self, move):
        self.board[move] = self.current_player
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None

    def is_terminal(self):
        return self.check_winner() is not None or not self.get_legal_moves()

    def get_result(self, player):
        winner = self.check_winner()
        if winner is None:
            return 0
        return 1 if winner == player else -1

    def display(self):
        b = self.board
        print(f" {b[0]} | {b[1]} | {b[2]} ")
        print("---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]} ")
        print("---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]} ")


def minimax(state, maximizing, original_player):
    if state.is_terminal():
        return state.get_result(original_player)

    if maximizing:
        best = -math.inf
        for move in state.get_legal_moves():
            child = state.clone()
            child.make_move(move)
            val = minimax(child, False, original_player)
            best = max(best, val)
        return best
    else:
        best = math.inf
        for move in state.get_legal_moves():
            child = state.clone()
            child.make_move(move)
            val = minimax(child, True, original_player)
            best = min(best, val)
        return best


def minimax_best_move(state):
    original_player = state.current_player
    best_val = -math.inf
    best_move = None
    for move in state.get_legal_moves():
        child = state.clone()
        child.make_move(move)
        val = minimax(child, False, original_player)
        if val > best_val:
            best_val = val
            best_move = move
    return best_move, best_val


def alpha_beta(state, alpha, beta, maximizing, original_player):
    if state.is_terminal():
        return state.get_result(original_player)

    if maximizing:
        val = -math.inf
        for move in state.get_legal_moves():
            child = state.clone()
            child.make_move(move)
            val = max(val, alpha_beta(child, alpha, beta, False, original_player))
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        return val
    else:
        val = math.inf
        for move in state.get_legal_moves():
            child = state.clone()
            child.make_move(move)
            val = min(val, alpha_beta(child, alpha, beta, True, original_player))
            beta = min(beta, val)
            if beta <= alpha:
                break
        return val


def alpha_beta_best_move(state):
    original_player = state.current_player
    best_val = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for move in state.get_legal_moves():
        child = state.clone()
        child.make_move(move)
        val = alpha_beta(child, alpha, beta, False, original_player)
        if val > best_val:
            best_val = val
            best_move = move
        alpha = max(alpha, best_val)
    return best_move, best_val


def tictactoe_heuristic(state, player):
    winner = state.check_winner()
    if winner == player:
        return 100
    if winner is not None:
        return -100
    if not state.get_legal_moves():
        return 0

    opponent = "O" if player == "X" else "X"
    score = 0
    lines = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a, b, c in lines:
        cells = [state.board[a], state.board[b], state.board[c]]
        p_count = cells.count(player)
        o_count = cells.count(opponent)
        if o_count == 0:
            score += 10 ** p_count
        if p_count == 0:
            score -= 10 ** o_count
    return score


def heuristic_alpha_beta(state, depth, alpha, beta, maximizing, original_player, heuristic_fn):
    if state.is_terminal():
        return state.get_result(original_player) * 1000

    if depth == 0:
        return heuristic_fn(state, original_player)

    if maximizing:
        val = -math.inf
        for move in state.get_legal_moves():
            child = state.clone()
            child.make_move(move)
            val = max(val, heuristic_alpha_beta(child, depth - 1, alpha, beta, False, original_player, heuristic_fn))
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        return val
    else:
        val = math.inf
        for move in state.get_legal_moves():
            child = state.clone()
            child.make_move(move)
            val = min(val, heuristic_alpha_beta(child, depth - 1, alpha, beta, True, original_player, heuristic_fn))
            beta = min(beta, val)
            if beta <= alpha:
                break
        return val


def heuristic_alpha_beta_best_move(state, depth, heuristic_fn):
    original_player = state.current_player
    best_val = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for move in state.get_legal_moves():
        child = state.clone()
        child.make_move(move)
        val = heuristic_alpha_beta(child, depth - 1, alpha, beta, False, original_player, heuristic_fn)
        if val > best_val:
            best_val = val
            best_move = move
        alpha = max(alpha, best_val)
    return best_move, best_val


class MCTSNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.wins = 0
        self.untried_moves = state.get_legal_moves()

    def is_fully_expanded(self):
        return len(self.untried_moves) == 0

    def is_terminal(self):
        return self.state.is_terminal()

    def ucb1(self, c=1.414):
        if self.visits == 0:
            return math.inf
        return self.wins / self.visits + c * math.sqrt(math.log(self.parent.visits) / self.visits)

    def best_child(self, c=1.414):
        return max(self.children, key=lambda n: n.ucb1(c))

    def expand(self):
        move = self.untried_moves.pop(random.randrange(len(self.untried_moves)))
        child_state = self.state.clone()
        child_state.make_move(move)
        child = MCTSNode(child_state, parent=self, move=move)
        self.children.append(child)
        return child

    def rollout(self):
        sim = self.state.clone()
        while not sim.is_terminal():
            moves = sim.get_legal_moves()
            sim.make_move(random.choice(moves))
        return sim

    def backpropagate(self, result_state, root_player):
        self.visits += 1
        self.wins += result_state.get_result(root_player)
        if self.parent:
            self.parent.backpropagate(result_state, root_player)


def mcts_best_move(state, iterations=1000):
    root_player = state.current_player
    root = MCTSNode(state.clone())

    for _ in range(iterations):
        node = root

        while node.is_fully_expanded() and not node.is_terminal():
            node = node.best_child()

        if not node.is_terminal():
            node = node.expand()

        result_state = node.rollout()
        node.backpropagate(result_state, root_player)

    if not root.children:
        moves = state.get_legal_moves()
        return (random.choice(moves) if moves else None), 0
    best = max(root.children, key=lambda n: n.visits)
    return best.move, best.wins / best.visits if best.visits else 0


def run_tests():
    print("=" * 60)
    print("TEST SUITE: GAME SEARCH ALGORITHMS")
    print("=" * 60)

    total_passed = 0
    total_failed = 0

    def check(name, condition, detail=""):
        nonlocal total_passed, total_failed
        status = "PASS" if condition else "FAIL"
        tag = "✓" if condition else "✗"
        print(f"  [{status}] {tag} {name}" + (f" — {detail}" if detail else ""))
        if condition:
            total_passed += 1
        else:
            total_failed += 1

    print("\n--- Minimax ---")

    g = TicTacToe()
    g.board = ["X","O","X", "O","X","O", " "," ","X"]
    g.current_player = "O"
    winner = g.check_winner()
    check("Terminal: X wins diagonal", winner == "X")

    g = TicTacToe()
    g.board = ["X","O","X", "O","X","O", "O","X"," "]
    g.current_player = "X"
    move, val = minimax_best_move(g)
    check("Minimax: wins immediately", move == 8 and val == 1, f"move={move}, val={val}")

    g = TicTacToe()
    g.board = ["O","X","X", "X","O"," ", " "," ","O"]
    g.current_player = "X"
    move, val = minimax_best_move(g)
    check("Minimax: blocks O win (pos 5)", move == 5, f"move={move}")

    g = TicTacToe()
    move, val = minimax_best_move(g)
    check("Minimax: empty board returns valid move", move in range(9), f"move={move}")
    check("Minimax: empty board val is 0 (draw)", val == 0, f"val={val}")

    g = TicTacToe()
    g.board = ["X","O","X", "O","O","X", "X","X","O"]
    g.current_player = "X"
    check("Terminal: full board no winner", g.is_terminal() and g.check_winner() is None)
    check("Terminal: get_result draw = 0", g.get_result("X") == 0)

    print("\n--- Alpha-Beta ---")

    g = TicTacToe()
    g.board = ["X","O","X", "O","X","O", "O","X"," "]
    g.current_player = "X"
    ab_move, ab_val = alpha_beta_best_move(g)
    check("Alpha-Beta: wins immediately", ab_move == 8 and ab_val == 1, f"move={ab_move}, val={ab_val}")

    g = TicTacToe()
    g.board = ["O","X","X", "X","O"," ", " "," ","O"]
    g.current_player = "X"
    ab_move, _ = alpha_beta_best_move(g)
    check("Alpha-Beta: blocks O win (pos 5)", ab_move == 5, f"move={ab_move}")

    g = TicTacToe()
    mm_move, mm_val = minimax_best_move(g)
    ab_move, ab_val = alpha_beta_best_move(g)
    check("Alpha-Beta == Minimax on empty board (val)", mm_val == ab_val, f"mm={mm_val}, ab={ab_val}")

    for _ in range(10):
        g = TicTacToe()
        moves = random.sample(range(9), random.randint(0, 4))
        for m in moves:
            if not g.is_terminal():
                g.make_move(m)
        if not g.is_terminal():
            mm_move, mm_val = minimax_best_move(g)
            ab_move, ab_val = alpha_beta_best_move(g)
            if mm_val != ab_val:
                check("Alpha-Beta == Minimax on random board", False, f"mm={mm_val}, ab={ab_val}")
                break
    else:
        check("Alpha-Beta == Minimax on 10 random boards", True)

    g = TicTacToe()
    start = time.perf_counter()
    minimax_best_move(g)
    mm_time = time.perf_counter() - start

    start = time.perf_counter()
    alpha_beta_best_move(g)
    ab_time = time.perf_counter() - start

    check("Alpha-Beta faster than Minimax on empty board", ab_time <= mm_time * 2,
          f"mm={mm_time:.4f}s ab={ab_time:.4f}s")

    print("\n--- Heuristic Alpha-Beta ---")

    g = TicTacToe()
    g.board = ["X","O","X", "O","X","O", "O","X"," "]
    g.current_player = "X"
    h_move, _ = heuristic_alpha_beta_best_move(g, depth=4, heuristic_fn=tictactoe_heuristic)
    check("Heuristic AB: wins immediately at depth 4", h_move == 8, f"move={h_move}")

    g = TicTacToe()
    g.board = ["O","X","X", "X","O"," ", " "," ","O"]
    g.current_player = "X"
    h_move, _ = heuristic_alpha_beta_best_move(g, depth=4, heuristic_fn=tictactoe_heuristic)
    check("Heuristic AB: blocks O win at depth 4", h_move == 5, f"move={h_move}")

    g = TicTacToe()
    h_move, _ = heuristic_alpha_beta_best_move(g, depth=2, heuristic_fn=tictactoe_heuristic)
    check("Heuristic AB depth=2: returns valid move", h_move in range(9), f"move={h_move}")

    g = TicTacToe()
    h_move_d6, _ = heuristic_alpha_beta_best_move(g, depth=9, heuristic_fn=tictactoe_heuristic)
    ab_move_full, ab_val = alpha_beta_best_move(g)
    h_move_d6, h_val_d6 = heuristic_alpha_beta_best_move(
    g,
    depth=9,
    heuristic_fn=tictactoe_heuristic
)

    ab_move_full, ab_val = alpha_beta_best_move(g)

    check(
        "Heuristic AB depth=9 == full AB",
        h_move_d6 == ab_move_full and h_val_d6 == ab_val,
        f"hab=({h_move_d6},{h_val_d6}), ab=({ab_move_full},{ab_val})"
    )

    g2 = TicTacToe()
    g2.board = [" "," "," ", " ","X"," ", " "," "," "]
    g2.current_player = "O"
    score = tictactoe_heuristic(g2, "X")
    check("Heuristic: center X gives positive score for X", score > 0, f"score={score}")

    print("\n--- Monte Carlo Tree Search ---")

    g = TicTacToe()
    g.board = ["X","O","X", "O","X","O", "O","X"," "]
    g.current_player = "X"
    mc_move, win_rate = mcts_best_move(g, iterations=500)
    check("MCTS: wins immediately", mc_move == 8, f"move={mc_move}, win_rate={win_rate:.2f}")

    g = TicTacToe()
    g.board = [" ","O","O", "X","X"," ", " "," "," "]
    g.current_player = "X"
    mc_move, _ = mcts_best_move(g, iterations=2000)
    check("MCTS: X takes winning move (pos 5, 2000 iter)", mc_move == 5, f"move={mc_move}")

    g = TicTacToe()
    mc_move, _ = mcts_best_move(g, iterations=1000)
    check("MCTS: empty board returns valid move", mc_move in range(9), f"move={mc_move}")

    wins_as_x = 0
    for _ in range(20):
        g = TicTacToe()
        while not g.is_terminal():
            if g.current_player == "X":
                move, _ = mcts_best_move(g, iterations=300)
            else:
                move = random.choice(g.get_legal_moves())
            g.make_move(move)
        result = g.get_result("X")
        if result == 1:
            wins_as_x += 1
    check("MCTS X vs Random O: X wins majority (>=10/20)", wins_as_x >= 10,
          f"X won {wins_as_x}/20")

    root = MCTSNode(TicTacToe())
    child = root.expand()
    result_state = child.rollout()
    child.backpropagate(result_state, "X")
    check("MCTS: backpropagation increments visits", root.visits == 1 and child.visits == 1,
          f"root.visits={root.visits}, child.visits={child.visits}")

    print("\n--- Algorithm vs Algorithm ---")

    ab_wins = mm_wins = draws = 0
    for _ in range(10):
        g = TicTacToe()
        while not g.is_terminal():
            if g.current_player == "X":
                move, _ = alpha_beta_best_move(g)
            else:
                move, _ = minimax_best_move(g)
            g.make_move(move)
        r = g.get_result("X")
        if r == 1: ab_wins += 1
        elif r == -1: mm_wins += 1
        else: draws += 1
    check("AlphaBeta(X) vs Minimax(O): all draws", draws == 10,
          f"draws={draws}, ab_wins={ab_wins}, mm_wins={mm_wins}")

    mc_wins = ab_wins_vs_mc = draws2 = 0
    for _ in range(20):
        g = TicTacToe()
        while not g.is_terminal():
            if g.current_player == "X":
                move, _ = alpha_beta_best_move(g)
            else:
                move, _ = mcts_best_move(g, iterations=500)
            g.make_move(move)
        r = g.get_result("X")
        if r == 1: ab_wins_vs_mc += 1
        elif r == -1: mc_wins += 1
        else: draws2 += 1
    check("AlphaBeta(X) vs MCTS(O): X not losing majority",
          ab_wins_vs_mc + draws2 >= mc_wins,
          f"ab_wins={ab_wins_vs_mc}, draws={draws2}, mc_wins={mc_wins}")

    print("\n" + "=" * 60)
    print(f"RESULTS: {total_passed} passed, {total_failed} failed out of {total_passed+total_failed} tests")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()

    print("\n\n--- DEMO: Minimax vs Alpha-Beta on a mid-game board ---")
    g = TicTacToe()
    g.board = ["X"," ","O", " ","O"," ", " "," ","X"]
    g.current_player = "X"
    g.display()
    mm_move, mm_val = minimax_best_move(g)
    ab_move, ab_val = alpha_beta_best_move(g)
    h_move, h_val = heuristic_alpha_beta_best_move(g, depth=6, heuristic_fn=tictactoe_heuristic)
    mc_move, mc_wr = mcts_best_move(g, iterations=3000)
    print(f"\nMinimax best move:           {mm_move}  (val={mm_val})")
    print(f"Alpha-Beta best move:        {ab_move}  (val={ab_val})")
    print(f"Heuristic AB best move:      {h_move}  (val={h_val})")
    print(f"MCTS best move:              {mc_move}  (win_rate={mc_wr:.2f})")
