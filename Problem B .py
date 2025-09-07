flour, sugar = 550, 250

cake = min(flour//100, sugar//50)
remaining_flour = flour - cake*100
remaining_sugar = sugar - cake*50

print(cake)
print(remaining_flour)
print(remaining_sugar)


# Description:
# The baker can bake 5 cakes because flour is the limiting ingredient.
# After baking, 50 units of flour and 70 units of sugar remain.
# The algorithm ensures resources are used optimally.
# Complexity: O(1) — constant time calculations
