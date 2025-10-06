import math

def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:   # leaf node
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:   # prune
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:   # prune
                break
        return best

# Example values
values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Optimal value:", alpha_beta(0, 0, True, values, -math.inf, math.inf))
