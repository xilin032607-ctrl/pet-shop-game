# pet-shop-game
import random
import time

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.health = 50
        self.alive = True
    
    def feed(self):
        if self.hunger > 10:
            self.hunger -= 20
            self.health += 5
            print(f"🍖 {self.name} has been fed! Hunger: {self.hunger}")
        else:
            print(f"{self.name} is not hungry right now!")
    
    def play(self):
        if self.energy > 20:
            self.happiness += 15
            self.energy -= 20
            self.hunger += 10
            print(f"🎾 {self.name} played! Happiness: {self.happiness}")
        else:
            print(f"{self.name} is too tired to play!")
    
    def sleep(self):
        self.energy = 100
        self.health += 10
        print(f"😴 {self.name} slept well! Energy: {self.energy}")
    
    def pet(self):
        self.happiness += 10
        print(f"🤗 You petted {self.name}! Happiness: {self.happiness}")
    
    def check_status(self):
        print(f"\n{'='*40}")
        print(f"Pet: {self.name} ({self.species})")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Energy: {self.energy}/100")
        print(f"Health: {self.health}/100")
        print(f"{'='*40}\n")
    
    def update_status(self):
        """Update status every turn"""
        self.hunger += random.randint(1, 3)
        self.energy -= random.randint(1, 2)
        self.happiness -= random.randint(0, 2)
        
        if self.hunger > 100:
            self.hunger = 100
        
        if self.hunger > 80:
            self.health -= 5
        
        if self.happiness < 20:
            self.health -= 3
        
        if self.health <= 0:
            self.alive = False
            print(f"💀 Oh no! {self.name} has passed away!")
    
    def is_alive(self):
        return self.alive

class PetShop:
    def __init__(self):
        self.pet = None
        self.day = 1
        self.money = 100
    
    def buy_pet(self):
        print("\n🐕 Welcome to Pet Shop! 🐈")
        print("Available pets:")
        pets = [
            ("Dog", "🐕"),
            ("Cat", "🐈"),
            ("Rabbit", "🐰"),
            ("Hamster", "🐹")
        ]
        
        for i, (species, emoji) in enumerate(pets, 1):
            print(f"{i}. {emoji} {species} - $50")
        
        choice = input("Choose a pet (1-4): ")
        species = pets[int(choice) - 1][0]
        name = input("What would you like to name your pet? ")
        
        if self.money >= 50:
            self.pet = Pet(name, species)
            self.money -= 50
            print(f"\n🎉 Welcome {name} the {species}!")
        else:
            print("Not enough money!")
    
    def play_game(self):
        if not self.pet:
            print("You need to buy a pet first!")
            return
        
        while self.pet.is_alive():
            self.pet.check_status()
            print(f"Day: {self.day} | Money: ${self.money}")
            print("\nWhat would you like to do?")
            print("1. Feed")
            print("2. Play")
            print("3. Sleep")
            print("4. Pet")
            print("5. Check Status")
            print("6. Next Day")
            print("7. Quit")
            
            choice = input("\nEnter your choice (1-7): ")
            
            if choice == "1":
                self.pet.feed()
            elif choice == "2":
                self.pet.play()
            elif choice == "3":
                self.pet.sleep()
            elif choice == "4":
                self.pet.pet()
            elif choice == "5":
                self.pet.check_status()
            elif choice == "6":
                self.day += 1
                self.money += random.randint(10, 30)
                print(f"\n📅 Day {self.day}! You earned some money!")
                self.pet.update_status()
            elif choice == "7":
                print(f"Final Money: ${self.money}")
                break
    
    def start(self):
        print("🏪 Welcome to Pet Shop Game! 🏪")
        self.buy_pet()
        self.play_game()

if __name__ == "__main__":
    shop = PetShop()
    shop.start()
