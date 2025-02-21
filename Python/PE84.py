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

# Trial 2
# Using Markov Chains again, but this time defining the state differently
# By defining it as (space, double_count) instead of (space) which includes (space, double_count) as data in it

# Another change is in how we calculate the dice probabilities. We use both dice now

from fractions import Fraction as F
import numpy as np
from time import time as t

strt = t()

dice_vals = []

# Rolling 2 dice
for die1 in range(1, 5):
    for die2 in range(1, 5):
        die_sum = die1 + die2
        is_double = (die1 == die2)
        dice_vals.append([die_sum, is_double])

# We know it's going to be a 120 x 120 matrix, because there are 40 x 3 = 120 iterations

# Ok, this part involves some " folding the probabilities " for doubles which went over my head
# Have to look at this again later
# Code courtesy (only this part) - ChatGPT

# Create two matrices: N (ending outcomes) and D (double outcomes for extra roll)
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

            dist = outcome[0]
            roll_is_double = outcome[1]

            # Use the current double_count from the outer loop
            if roll_is_double:
                new_doubles = double_count + 1
            else:
                new_doubles = 0

            # If triple doubles, send to Jail
            if roll_is_double and new_doubles == 3:
                new_space = 10
                new_doubles = 0

            else:
                # Update board position (use 'space', not the full state index)
                new_space = (space + dist) % 40

            new_state = [new_space, new_doubles]
            new_state_index = (new_state[0] * 3) + new_state[1]

            # Each outcome has probability 1/36.

            if roll_is_double and new_doubles != 0:
                # Roll is a double that doesn't trigger jail -> extra roll (contribute to D)
                D[current_state, new_state_index] += F(1, 36)

            else:
                # Either not a double or triple-double (sending to jail) -> turn ends (contribute to N)
                N[current_state, new_state_index] += F(1, 36)

# Now build the identity matrix I (as Fractions)
I = np.empty((120, 120), dtype=object)
for i in range(120):
    for j in range(120):
        I[i, j] = F(1) if i == j else F(0)

# Convert I, D, and N to float for inversion.
I_float = np.array([[float(I[i, j]) for j in range(120)] for i in range(120)])
D_float = np.array([[float(D[i, j]) for j in range(120)] for i in range(120)])
N_float = np.array([[float(N[i, j]) for j in range(120)] for i in range(120)])

composite_dice = np.dot(np.linalg.inv(I_float - D_float), N_float)


# Now for the card matrix
card_matrix = np.zeros((120, 120), dtype=object)

# Only Community cards (CC) and Chance cards (CH) affect movement

CH_spaces = [7, 22, 36]
CC_spaces = [2, 17, 33]

RR = [5, 15, 25, 35]
UT = [12, 28]


def nearest_rail(state: int) -> int:
    for rail in RR:
        if rail > state:
            return rail

    return 5


def nearest_ut(state: int) -> int:

    for utility in UT:
        if utility > state:
            return utility

    return 12

# A list of functions to which we are going to pass each CH space
# Each function represents an instruction from the chance pile
# Nearest Rail is included twice because there are 2 cards with the same instructions


chance_moves = [lambda space: 0,
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

# Now we need to loop through all the chance spaces and pass each one to the functions in the list
for space in CH_spaces:

    # This loops through the moving cards
    for move in chance_moves:

        # Our new space, i.e. new position
        land = move(space) % 40

        for double_count in range(3):

            current_state_index = (space * 3) + double_count
            new_state_index = (land * 3) + double_count

            card_matrix[current_state_index, new_state_index] += F(1, 16)

    # The non - movement cards' probability being added
    #  Probability of non - moving cards = 6/16

    for double_count in range(3):
        current_state_index = (space * 3) + double_count

        card_matrix[current_state_index, current_state_index] += F(6, 16)

community_moves = [lambda space: 0,
                   lambda space: 10]

for space in CC_spaces:

    # This is for looping through the moving cards
    for move in community_moves:

        land = move(space) % 40

        for double_count in range(3):

            current_state_index = (space * 3) + double_count
            new_state_index = (land * 3) + double_count

            card_matrix[current_state_index, new_state_index] += F(1, 16)

    # The non - movement cards' probability being added
    # Probability of non - moving cards = 14/16

    for double_count in range(3):
        current_state_index = (space * 3) + double_count

        card_matrix[current_state_index, current_state_index] += F(14, 16)


for space in range(40):
    if space not in (CC_spaces + CH_spaces):

        for double_count in range(3):

            current_state_index = (space * 3) + double_count

            card_matrix[current_state_index, current_state_index] += F(1)

card_matrix_float = np.array([[float(card_matrix[i, j]) for j in range(120)] for i in range(120)])

transition_matrix = np.dot(composite_dice, card_matrix_float)


for state_index in range(120):
    board_position = state_index // 3
    if board_position == 30:
        # Set the entire row to 0.
        transition_matrix[state_index, :] = 0
        # Force the move to Jail: board position 10, double count 0 (state index 30).
        transition_matrix[state_index, 30] = 1.0

# Now calculating steady state distribution using iterative method
n = transition_matrix.shape[0]
pi = np.ones(n) / n

final_matrix = np.array(transition_matrix, dtype=float)

MAX_ITERATIONS = 1_000_000
TOLERANCE = 1e-12

for _ in range(MAX_ITERATIONS):
    new_pi = np.dot(pi, final_matrix)
    if np.linalg.norm(new_pi - pi, ord=1) < TOLERANCE:
        break
    pi = new_pi

board_probs = np.zeros(40)

# Sum the probabilities over the 3 states for each board position
for pos in range(40):
    board_probs[pos] = np.sum(pi[pos*3:(pos+1)*3])

# Now finding the top 3 positions
dup = board_probs.copy()
dup.sort()
top3 = dup[-3:][::-1]
squares = []

for i in top3:
    squares.append(np.where(board_probs == i)[0][0])

ans = ''
for i in squares:
    ans += str(i)

print(ans)
end = t()
print('------- %s seconds -------' % (end - strt))
