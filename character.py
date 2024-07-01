import random

class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        

    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):
    enemies_to_defeat = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.health = 100
        Enemy.enemies_to_defeat += 1

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def set_health(self, health):
        self.health = health

    def decrease_health(self, amount):
        self.health -= amount
        print(f"{self.name}'s health is now {self.health}.")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            Enemy.enemies_to_defeat -= 1
            return True
        return False

    def perform_random_attack(self, character):
        attack_value = random.randint(5, 15)
        character.decrease_health(attack_value)
        print(f"{character.name} loses {attack_value} health points!")

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("\nYou fend " + self.name + " off with the " + combat_item)
            return self.decrease_health(100)
        else:
            self.perform_random_attack(self)
            if self.health > 0:
                print(self.name + " swallows you, little wimp")
                return False
            return True

    def steal(self):
        print("You steal from " + self.name)


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
        self.health = 100

    def set_health(self, health):
        self.health = health

    def hug(self):
        print(self.name + " hugs you back!")

    def receive_gift(self, gift):
        print(self.name + " receives your gift and feels happier!")
    


class Bystander(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
