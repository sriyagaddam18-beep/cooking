import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)  # Faster speed for smoother gameplay
    print("\n")

def cook_burger():
    print_slow("\n🍔 --- RECIPE: THE PERFECT BURGER --- 🍔")
    score = 0
    
    # Step 1
    print("1. Beef Patty\n2. Plant-based Patty\n3. An old boot")
    choice = input("Select your protein (1-3): ")
    score += 20 if choice in ["1", "2"] else -10

    # Step 2
    print("\n1. Rare (30s)\n2. Medium (3 mins)\n3. Charcoal (30 mins)")
    choice = input("How long do you grill it? (1-3): ")
    if choice == "2": score += 30
    elif choice == "1": score += 10
    else: score -= 20

    # Step 3
    print("\n1. Cheese & Lettuce\n2. Only Ketchup\n3. Chocolate Sauce")
    choice = input("Choose toppings (1-3): ")
    score += 30 if choice == "1" else (15 if choice == "2" else -30)
    
    return score

def cook_pizza():
    print_slow("\n🍕 --- RECIPE: WOODFIRED PIZZA --- 🍕")
    score = 0
    
    # Step 1
    print("1. Hand-tossed Neapolitan\n2. Pre-made frozen crust\n3. Cardboard box")
    choice = input("Select your dough base (1-3): ")
    score += 30 if choice == "1" else (10 if choice == "2" else -20)

    # Step 2
    print("\n1. San Marzano Tomato Sauce\n2. Spicy BBQ Sauce\n3. Mayonnaise")
    choice = input("Select your sauce base (1-3): ")
    score += 20 if choice == "1" else (15 if choice == "2" else -15)

    # Step 3
    print("\n1. Fresh Mozzarella & Basil\n2. Pineapple & Ham\n3. Jellybeans")
    choice = input("Choose toppings (1-3): ")
    score += 30 if choice == "1" else (20 if choice == "2" else -30)
    
    return score

def cook_sushi():
    print_slow("\n🍣 --- RECIPE: TRADITIONAL SUSHI --- 🍣")
    score = 0
    
    # Step 1
    print("1. Seasoned Short-grain Rice\n2. Long-grain Basmati Rice\n3. Leftover sticky rice")
    choice = input("Prepare your rice (1-3): ")
    score += 30 if choice == "1" else (5 if choice == "2" else -10)

    # Step 2
    print("\n1. Fresh Sashimi-grade Tuna\n2. Smoked Salmon\n3. Raw Hot Dog slices")
    choice = input("Select the seafood fill (1-3): ")
    score += 30 if choice == "1" else (20 if choice == "2" else -25)

    # Step 3
    print("\n1. Tight cylinder roll (with Bamboo mat)\n2. Loose roll using bare hands\n3. Squished into a ball")
    choice = input("How do you roll the Nori? (1-3): ")
    score += 20 if choice == "1" else (10 if choice == "2" else 0)
    
    return score

def cooking_game():
    print_slow("🍳 Welcome back to GitChef: The Multi-Recipe Challenge! 🍳")
    print("1. Classic Burger 🍔\n2. Woodfired Pizza 🍕\n3. Traditional Sushi 🍣")
    recipe_choice = input("Which recipe would you like to cook? (1-3): ")
    
    if recipe_choice == "1":
        final_score = cook_burger()
    elif recipe_choice == "2":
        final_score = cook_pizza()
    elif recipe_choice == "3":
        final_score = cook_sushi()
    else:
        print_slow("❌ Invalid menu choice. The restaurant closed early.")
        return

    # Final Score Screen
    print_slow("\n⭐ --- FINAL EVALUATION --- ⭐")
    print(f"Your final score: {final_score}/80")
    if final_score >= 70:
        print_slow("🎉 3 Michelin Stars! Master Chef level! 🎉")
    elif final_score >= 40:
        print_slow("👍 Good job! Tasty enough to sell in a cafe.")
    else:
        print_slow("💀 Back to culinary school for you!")

if __name__ == "__main__":
    cooking_game()
