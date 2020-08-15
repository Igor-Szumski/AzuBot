import random

# var = [x1, y1, x2, y2]
previous_stage = [44, 482, 89, 572]
previous_stage_x = random.randint(previous_stage[0], previous_stage[2])
previous_stage_y = random.randint(previous_stage[1], previous_stage[3])

next_stage = [1540, 482, 1590, 572]
next_stage_x = random.randint(next_stage[0], next_stage[2])
next_stage_y = random.randint(next_stage[1], next_stage[3])

start_combat = [1085, 658, 1340, 740]
random_start_combat_x = random.randint(start_combat[0], start_combat[2])
random_start_combat_y = random.randint(start_combat[1], start_combat[3])
random_start_combat = [random_start_combat_x, random_start_combat_y]

confirm_combat = [1276, 780, 1475, 843]
random_confirm_combat_x = random.randint(confirm_combat[0], confirm_combat[2])
random_confirm_combat_y = random.randint(confirm_combat[1], confirm_combat[3])
random_confirm_combat = [random_confirm_combat_x, random_confirm_combat_y]
