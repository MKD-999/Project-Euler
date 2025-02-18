"""# Trial 1 using Markov Chains

# For the transition from one state to another, we can move either because of
# dice or the cards


from fractions import Fraction as F
import numpy as np

q = 1
frac = F(1, 36)
dice_probabilities = {}

for i in range(2, 13):

    if i < 7:
        dice_probabilities[i] = q * frac
        q += 1

    elif i == 7:
        dice_probabilities[i] = q * frac

    else:
        q -= 1
        dice_probabilities[i] = q * frac

# Filling the transition matrix with the dice probabilities
# Format of each cell is going to be [P(transition), double_count]

dice_matrix = np.empty((40, 40), dtype=object)
for i in range(40):
    for j in range(40):
        dice_matrix[i, j] = np.array([F(0), 0])

# Double count is cumulative; so defined outside the loop
double_count = 0

for start in range(40):
    for dist in range(2, 13):

        # Even -> Doubles is possible
        if dist % 2 == 0:
            double_count += 1

        # If not an even number, a double is not rolled, breaking the chain
        else:
            double_count = 0

        land = (start + dist) % 40
        p_total = dice_probabilities[dist]

        # " 3 consecutive doubles -> JAIL " rule
        if double_count <= 2:
            dice_matrix[start, land] += np.array([p_total, double_count])

        else:
            # Go to JAIL and reset double count
            double_count = 0
            dice_matrix[start, 10] += np.array([F(1, 6), 0])
            continue

# Filling the card matrix with the card probabilities
# For the community cards (CC) and chance cards (CH), only movement inducing cards
# To be considered

# Probability of getting a movement inducing community chest card = 2/16
# Probability of getting a movement inducing chance card = 10/16
# Implementing the card conditions in the card matrix

card_matrix = np.empty((40, 40), dtype=object)
for i in range(40):
    for j in range(40):
        card_matrix[i, j] = np.array([F(0), 0])

double_count = 0
# CC positions
CC = [2, 17, 36]

for start in CC:
    # Probability of non - moving cards = 14/16
    card_matrix[start, start] = card_matrix[start, start] + np.array([F(14, 16), 0])

    # Probability of moving to " GO " square
    card_matrix[start, 0] = card_matrix[start, 0] + np.array([F(1, 16), 0])

    # Probability of moving to " JAIL " square
    card_matrix[start, 10] = card_matrix[start, 10] + np.array([F(1, 16), 0])

# CH positions
CH = [7, 22, 36]

for start in CH:
    # Probability of non - moving cards = 6/16
    card_matrix[start, start] = card_matrix[start, start] + np.array([F(6, 16), 0])

    # The other card conditions -> JAIL, GO, etc
    # Basically -> 0, 10, 11, 24, 39, 5, nearest in [5, 15, 25, 35], nearest in [12, 28], [position - 3]
    card_matrix[start, 0] = card_matrix[start, 0] + np.array([F(1, 16), 0])
    card_matrix[start, 10] = card_matrix[start, 10] + np.array([F(1, 16), 0])
    card_matrix[start, 11] = card_matrix[start, 11] + np.array([F(1, 16), 0])
    card_matrix[start, 24] = card_matrix[start, 24] + np.array([F(1, 16), 0])
    card_matrix[start, 39] = card_matrix[start, 39] + np.array([F(1, 16), 0])
    card_matrix[start, 5] = card_matrix[start, 5] + np.array([F(1, 16), 0])

    next_r = [5, 15, 25, 35]

    # 2 Times because of 2 cards
    for _ in range(2):

        nearest = 40
        for chk in next_r:

            # Can only move front
            if chk > start:
                if chk - start < nearest:
                    nearest = chk - start

            else:
                # This means we have crossed the last R and the nearest R after this is sq 5
                nearest = 5

        card_matrix[start, nearest] = card_matrix[start, nearest] + np.array([F(1, 16), 0])

    next_u = [12, 28]
    nearest = 40
    for chk in next_u:

        if chk > start:
            if chk - start < nearest:
                nearest = chk - start

        else:
            nearest = 12

    card_matrix[start, nearest] = card_matrix[start, nearest] + np.array([F(1, 16), 0])

    card_matrix[start, start - 3] = card_matrix[start, start - 3] + np.array([F(1, 16), 0])

# For non-card positions, make sure the player stays in the same position
for i in range(40):
    if i not in CC and i not in CH:
        card_matrix[i, i] = np.array([F(1), 0])

# Now comes the Transition Matrix, which is the product of the
# Dice Matrix and the Card Matrix
transition_matrix = np.dot(dice_matrix, card_matrix)
"""

from fractions import Fraction as F
import numpy as np
from time import time as t

strt = t()

# Build the Dice Transition Matrices
dice_vals = []
for die1 in range(1, 7):
    for die2 in range(1, 7):
        die_sum = die1 + die2
        is_double = (die1 == die2)
        dice_vals.append([die_sum, is_double])

N = np.zeros((120, 120), dtype=object)
D = np.zeros((120, 120), dtype=object)
for i in range(120):
    for j in range(120):
        N[i, j] = F(0)
        D[i, j] = F(0)

for space in range(40):
    for double_count in range(3):
        current_state = (space * 3) + double_count
        for outcome in dice_vals:
            dist, roll_is_double = outcome
            new_doubles = double_count + 1 if roll_is_double else 0
            if roll_is_double and new_doubles == 3:
                new_space, new_doubles = 10, 0  # Go to Jail
            else:
                new_space = (space + dist) % 40
            new_state_index = (new_space * 3) + new_doubles
            if roll_is_double and new_doubles != 0:
                D[current_state, new_state_index] += F(1, 36)
            else:
                N[current_state, new_state_index] += F(1, 36)

# Debug: Check transition matrices for dice rolls
print("Dice Transition Matrices (N and D):")
print("N matrix: ", N[:5, :5])  # Show a small portion for inspection
print("D matrix: ", D[:5, :5])  # Show a small portion for inspection

I = np.array([[F(1) if i == j else F(0) for j in range(120)] for i in range(120)], dtype=object)
I_f = np.array([[float(I[i, j]) for j in range(120)] for i in range(120)])
D_f = np.array([[float(D[i, j]) for j in range(120)] for i in range(120)])
N_f = np.array([[float(N[i, j]) for j in range(120)] for i in range(120)])

composite_dice = np.linalg.inv(I_f - D_f) @ N_f

# Debug: Check composite dice matrix
print("Composite Dice Transition Matrix:")
print(composite_dice[:5, :5])  # Check a small portion of the composite dice matrix

# Build the Card Transition Matrix
card_matrix = np.array([[F(0) for _ in range(120)] for _ in range(120)], dtype=object)

CH_spaces = [7, 22, 36]
CC_spaces = [2, 17, 33]
RR = [5, 15, 25, 35]
UT = [12, 28]

def nearest_rail(state: int) -> int:
    return min([r for r in RR if r > state], default=RR[0])

def nearest_ut(state: int) -> int:
    return min([u for u in UT if u > state], default=UT[0])

chance_moves = [
    lambda space: 0,
    lambda space: 10,
    lambda space: 11,
    lambda space: 24,
    lambda space: 39,
    lambda space: 5,
    nearest_rail,
    nearest_rail,
    nearest_ut,
    lambda space: (space - 3) % 40
]

# Debug: Check Chance card transitions
for space in CH_spaces:
    for move in chance_moves:
        land = move(space) % 40
        for double_count in range(3):
            current_state_index = (space * 3) + double_count
            new_state_index = (land * 3) + double_count
            card_matrix[current_state_index, new_state_index] += F(1, 16)
    for double_count in range(3):
        card_matrix[(space * 3) + double_count, (space * 3) + double_count] += F(6, 16)

# Debug: Check card matrix after Chance spaces
print("Card Matrix after Chance spaces:")
print(card_matrix[:5, :5])  # Check a small portion

community_moves = [lambda space: 0, lambda space: 10]
for space in CC_spaces:
    for move in community_moves:
        land = move(space) % 40
        for double_count in range(3):
            card_matrix[(space * 3) + double_count, (land * 3) + double_count] += F(1, 16)
    for double_count in range(3):
        card_matrix[(space * 3) + double_count, (space * 3) + double_count] += F(14, 16)

for space in range(40):
    if space not in (CC_spaces + CH_spaces):
        for double_count in range(3):
            card_matrix[(space * 3) + double_count, (space * 3) + double_count] += F(1)

card_matrix_f = np.array([[float(card_matrix[i, j]) for j in range(120)] for i in range(120)])

# Debug: Check card matrix after all updates
print("Card Matrix after all updates:")
print(card_matrix_f[:5, :5])  # Check a small portion

final_transition_matrix = composite_dice @ card_matrix_f

# Enforce "Go To Jail" rule
for state_index in range(120):
    board_position = state_index // 3
    if board_position == 30:  # Go to Jail (position 30)
        final_transition_matrix[state_index, :] = 0
        final_transition_matrix[state_index, 30] = 1.0  # Go directly to jail (space 30)

# Debug: Check final transition matrix
print("Final Transition Matrix (small portion):")
print(final_transition_matrix[:5, :5])  # Check a small portion of the final matrix

# Compute the Steady-State Distribution
n = final_transition_matrix.shape[0]
pi = np.ones(n) / n
iteration = 0

while True:
    new_pi = np.dot(pi, final_transition_matrix)
    if np.linalg.norm(new_pi - pi) < 1e-10:  # Check for convergence
        break
    pi = new_pi
    iteration += 1
    if iteration % 10 == 0:
        print(f"Iteration {iteration}: Top probabilities so far: {sorted(new_pi, reverse=True)[:5]}")

board_probs = np.array([np.sum(pi[pos * 3:(pos + 1) * 3]) for pos in range(40)])

# Debug: Check board probabilities
print("Board Probabilities:", board_probs[:10])  # Show top 10 for inspection

# Get the top 3 most visited squares
top3 = np.sort(board_probs)[-3:][::-1]
pos = [np.where(board_probs == i)[0][0] for i in top3]

print("\nFinal Results:")
print("Top three squares (in descending order):", pos)
print("Probabilities:", top3)
print("Total time (seconds):", t() - strt)
