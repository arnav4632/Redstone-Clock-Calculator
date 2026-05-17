#assuming that time is defined as the time between the start of one pulse and the start of the next pulse of the output
#method for checking model was by these command blocks, with arrows pointing into eachother:
#   Impulse/Unconditional/Needs Redstone. connected to output, as shown in setup.png; /scoreboard players add #toggle click_count 1
#   Chain/Unconditional/Always Active; /execute if score #toggle click_count matches 1 store result score last_time timer run time query gametime
#   Chain/Unconditional/Always Active; /execute if score #toggle click_count matches 2 store result score current_time timer run time query gametime
#   Chain/Unconditional/Always Active; /execute if score #toggle click_count matches 2 run scoreboard players operation current_time timer -= last_time timer
#   Chain/Unconditional/Always Active; /execute if score #toggle click_count matches 2 run tellraw @a [{"text":"Ticks between impulses: ","color":"green"},{"score":{"name":"current_time","objective":"timer"}}]
#   Chain/Unconditional/Always Active; /execute if score #toggle click_count matches 2 run scoreboard players set #toggle click_count 0


