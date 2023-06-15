# Growtopia Wooden Platform Mass Calculator
# Data https://www.desmos.com/calculator/1vqfxdrqx7

print("Wooden Platform Mass Calculator made by fevo (c) 2023")
print("=====================================================================")

x = int(input("Number of blocks to be obtained: ")) # No. blocks to be obtained

#plat_block = ( 774 / 200 ) * x
#y = plat_yield / x

plat_block = ( 200 / 774 ) * x # No. seeds required
#plat_seed = ( 200 / 267 ) * x -> Finding no. seeds to be obtained

#print(str(plat_block))
#print(str(x) + " Wooden Platform (Tier 3) requires planting " + str(round(plat_block, 3)) + " Grass Seed (Tier 2) and Wood Block Seed (tier 2)")

grass_yield = ( 200 / 381 ) * plat_block
#print(str(grass_yield))
#print(str(round(plat_block, 3)) + " Grass Seed (Tier 2) requires splicing " + str(round(grass_yield, 3)) + " Dirt Seed (Tier 1) and Rock Seed (Tier 1)")

wood_yield = ( 136 / 206 ) * plat_block
#print(str(wood_yield))

#print(str(round(plat_block, 3)) + " Wood Block Seed (Tier 2) requires " + str(round(wood_yield, 3)) + " Dirt Seed (Tier 1) and Lava Seed (Tier 1)")

dirt_required = grass_yield + wood_yield # Total dirt seed required for mass
plat_seed = ( 51 / 200 ) * ( 200 / 774 ) * x
#print(str(plat_seed))
total_plat = plat_block * ( 774 / 200 )
#print(str(round(total_plat, )))


print("Objective: Obtain " + str(x) + " Wooden Platform blocks")
print(" ")
print("Seeds required:")
print("- " + str(round(dirt_required, )) + " Dirt Seed (+- 3 seeds)")
print('- ' + str(round(grass_yield, )) + " Rock Seed (+- 3 seeds)")
print("- " + str(round(wood_yield, )) + " Lava Seed (+- 3 seeds)")
print(" ")
print("Step 1:")
print("- Splice " + str(round(grass_yield, )) + " Dirt Seed (+- 3 seeds) and Rock Seed (+- 3 seeds) to make Grass")
print("- Harvest the Grass trees and you will get " + str(round(plat_block, )) + " Grass Seed after breaking them")
print(" ")
print("Step 2:")
print("- Splice " + str(round(wood_yield)) + " Dirt Seed (+- 3 seeds) and Lava Seed (+- 3 seeds) to make Wood Block")
print("- Harvest the Wood Block trees and you will get " + str(round(plat_block, )) + " Wood Block Seed after breaking them")
print(" ")
print("Step 3 (Final):")
print("- Splice " + str(round(plat_block, )) + " Grass Seed (+- 3 seeds) and Wood Block Seed (+- 3 seeds) to make Wooden Platform")
print("- Harvest the Wooden Platform trees and you will get approximately " + str(x) + " blocks and " + str(round(plat_seed, )) + " seeds")

