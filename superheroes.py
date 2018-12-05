import random
from pprint import pprint


class Hero:

    def __init__(self, name, health=100):
        # Initialize starting values
        self.abilities = list()
        self.name = name

        self.armors = list()
        self.starting_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    # def __str__(self):
    #     print("{}'s current health is {} and has killed {} opponents and has died {} times. Has armors: {}, abilities: {}".format(
    #         self.name, self.health, self.kills, self.deaths, self.armors, self.abilities,
    #     ))

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''
        This method will append the weapon object passed in as an argument to the list of abilities that already exists -- self.abilities.

        This means that self.abilities will be a list of abilities and weapons.
        '''
        self.abilities.append(weapon)


    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        """
        Calculates damage from list of abilities.

        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        """
        total_attack = 0

        for the_ability in self.abilities:
            total_attack += the_ability.attack()
        return total_attack

    def defend(self):
        """
        Implement the defend method so that it returns a random integer between 0 and the full defend strength.
        This method should run the defend method on each piece of armor and calculate the total defense.
        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """

        total_defend = 0

        for armor in self.armors:
            total_defend += armor.defend

        if total_defend <= 0:
            return #"The total is 0 and {} is dead".format(self.name)
        else:
            return total_defend

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.

        If the hero dies update number of deaths.
        """

        self.health = self.health - damage_amt
        if self.health <= 0:
            self.deaths += 1

    def add_kill(self):
        """
        This method should add the number of kills to self.kills
        """

        self.kills += 1


    def add_death(self):
        self.deaths += 1


    def is_alive(self):
        """
         This function will
         return true if the hero is alive
         or false if they are not.
         """
        # if self.health == 0:
        #     return False
        # else:
        #     return True
        # # alternate way:
        # if self.health != 0:
        #     return True
        # else:
        #     return False
        # a shorter way:
        # return self.health > 0

        if self.health > 0:
            print("{} Has died in battle".format(self.name))
            return True
        else:
            return False

    def fight(self, opponent):
        # loop until someone dies
        while self.is_alive() and opponent.is_alive():
            # self attacks opponent
            damage = self.attack()
            opponent.take_damage(damage)
            # print("damage:", damage)
            # print("opponent health:", opponent.health)

            # opponent attacks self
            retaliation = opponent.attack()
            self.take_damage(retaliation)
            # print("retaliation:", retaliation)
            # print("self(main) health:", self.health)

        if self.is_alive() == False :
            opponent.add_death()
            opponent.add_kill()
            print("{} died".format(self.name))
        elif opponent.is_alive() == False:
            self.add_death()
            self.add_kill()
            print("{} died".format(opponent.name))



class Ability:
    # Initialize starting values
    def __init__(self, name, attack_strength):
        # Set ability name
        # Set attack strength
        self.name = name
        self.attack_strength = int(attack_strength)

    # Return attack value
    def attack(self):
        # Calculate lowest attack value as an integer.
        max_attack = self.attack_strength
        min_attack = self.attack_strength // 2
        # Use random.randint(a, b) to select a random attack value.
        print('max attack: {}'.format(max_attack))
        print('min attack: {}'.format(min_attack))
        random_value = random.randint(min_attack, max_attack)
        print('random value: {}'.format(random_value))
        # Return attack value between min and the full attack.
        return random_value

    # Update attack value
    def update_attack(self, new_attack_strength):
        self.attack_strength = new_attack_strength

class Weapon(Ability):

    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """

        return random.randint(self.attack_strength // 2, self.attack_strength)


class Armor:
    def __init__(self, name, defend):
        """Instantiate name and defense strength."""
        self.name = name
        self.defend = defend

    def block(self):
        """
        Return a random value between 0 and the
        initialized defend strength.
        """
        return random.randint(0, self.defend)


class Team:
    # Keep all your current code, but add these methods

    def __init__(self, team_name):
        self.name = team_name
        self.heroes = []


    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                the_hero = self.heroes.index(hero)
                #del keyword is used to delete objects in python
                #https://www.w3schools.com/python/ref_keyword_del.asp
                del self.heroes[the_hero]
                return
        print("Hero not found")
        return 0

    def view_all_heroes(self):
        #prints all heroes in console
        for hero in self.heroes:
            print(hero.name)

    def alive_heroes(self):

        alive_list = list()
        #find out if team one has hereos alive
        for hero in self.heroes:
            if hero.is_alive():
                alive_list.append(hero)
        return alive_list


    def attack(self, other_team):
        '''
        This function should randomly select
        a living hero from each team and have
        them fight until one or both teams
        have no surviving heroes.

        Hint: Use the fight method in the Hero
        class.
        '''

        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            random_hero_one = random.choice(self.alive_heroes())
            random_hero_two = random.choice(other_team.alive_heroes())

            random_hero_one.fight(random_hero_two)




    def revive_heroes(self, health=100):
        '''
        This method should reset all heroes
        health to their
        original starting value.
        '''
        for hero in self.heroes:
            if hero.health <= 0:
                hero.health = health

    def stats(self):
        '''
        This method should print the ratio of
        kills/deaths for each member of the
        team to the screen.

        This data must be output to the console.
        '''
        for hero in self.heroes:
            print("{} Kills: Total Hero Killed: {} / Total Times Died: {}".format(hero.name, hero.kills, hero.deaths))



class Arena:
    def __init__(self):
        '''
        Declare variables
        '''
        team_name1 = input("Choose your name for team 1: ")
        team_name2 = input("Choose your name for team 2: ")
        self.team_one = Team(team_name1)
        self.team_two = Team(team_name2)


    #Creating Validations for inputs
    def weapon_name_validation():

        weapons_list = [
            "Flower Raygun"
            "Unicorn Wand"
            "Glitter Sash"
            "Lolipop Sword"
            "Peppermint Staff"
            "Shooting Star"
            "Diamond Knuckles"
            "Rainbow Ring"
            ]

        pass

    def hero_name_validation():

        heroes_list = [
            "Tooth Fairy"
            "Unicorn"
            "Rainbow Warrior"
            "Galatic Snowflake"
            "Candy Winter"
            "Sugar Queen"
            "Night Swan"
            "Chocolate Surfer"
            "Pinky Berry"
            ]

        pass

    def ability_name_validation(self):

        abilities_list = [
            "Unicorn Magic",
            "Pony Syndrome",
            "Glitter Mirage",
            "Neon Rainbow",
            "Shooting Star",
            "Flower Power",
            "Flower Explosion",
            "Team Spirit",
            "Joy",
            "Energy Bomb",
            "Beauty",
            "Charisma",
            ]

        # print("List of abilities:")
        bracketless_abilities= ''.join(abilities_list)

        # print("The list of all abilities to choose from: {}".format(bracketless_abilities))
        num_abilities_list = len(abilities_list)

        # print("The number of the list of abilities: {}".format(num_abilities_list))
        range_abilities_list = list(range(num_abilities_list))

        # print("Range of the list of Abilities: {}".format(range_abilities_list))

        Words = dict(enumerate(abilities_list, 0))

        # print("Dictionary List: {}".format(Words))

        pprint(Words)

        ability_input = input("Choose one ability from list of abilities abouve: ")

        for ability in abilities_list:
            for number in range_abilities_list:
                if (ability == ability_input) | (number == int(ability_input)) :
                    power = random.randint(10, 50)
                    return Ability(ability_input, power)
        print("Unknown error try again")


    #Methods to create hero and deck them out in armor, gear, abilities
    def create_hero(self):
        '''
        This method should allow a user to create a hero.

        User should be able to specify if they want armors, weapons, and abilites. Call the methods you made above and use the return values to build your hero.

        return the new hero object
        '''
        heroes = [
            "Tooth Fairy"
            "Unicorn"
            "Rainbow Warrior"
            "Galatic Snowflake"
            "Candy Winter"
            "Sugar Queen"
            "Night Swan"
            "Chocolate Surfer"
            "Pink Berry"
            ]
        name = input("Choose hero from list abouve:")
        print(name)
        power = random.randint(10, 30)
        print(power)
        hero = Hero(name, power)
        # print(hero)
        hero.abilities.append(self.create_ability())
        hero.armors.append(self.create_armor())
        hero.abilities.append(self.create_weapon())
        return hero

    def create_ability(self):
        '''
        This method will allow a user to create an ability.

        Prompt the user for the necessary information to create a new ability object.

        return the new ability object.
        '''

        power = random.randint(10, 50)
        return Ability(ability_input, power)

    def create_weapon(self):
        '''
        This method will allow a user to create a weapon.

        Prompt the user for the necessary information to create a new weapon object.

        return the new weapon object.
        '''
        weapons_list = [
            "Flower Raygun"
            "Unicorn Wand"
            "Glitter Sash"
            "Lolipop Sword"
            "Peppermint Staff"
            "Shooting Star"
            "Diamond Knuckles"
            "Rainbow Ring"
            ]
        name = input("Choose weapon from list abouve:")
        power = random.randint(20, 40)
        return Weapon(name, power)

    def create_armor(self):
        '''
        This method will allow a user to create a piece of armor.

        Prompt the user for the necessary information to create a new armor object.

        return the new armor object.
        '''


        name = input("Choose armor from list abouve:")
        power = random.randint(50, 100)
        return Armor(name, power)

    def build_team_one(self):
        '''
        This method should allow a user to create team one.
        Prompt the user for the number of Heroes on team one and
        call self.create_hero() for every hero that the user wants to add to team one.

        Add the created hero to team one.
        '''
        print("Time to build 3 your warriors for {}".format(self.team_one.name))
        total_heroes = 3
        while total_heroes > 0:
            hero = self.create_hero()
            total_heroes -= 1
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''
        This method should allow a user to create team two.
        Prompt the user for the number of Heroes on team two and
        call self.create_hero() for every hero that the user wants to add to team two.

        Add the created hero to team two.
        '''

        print("Time to build 3 your warriors for {}".format(self.team_two.name))
        total_heroes = 3
        while total_heroes > 0:
            hero = self.create_hero()
            total_heroes -= 1
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''
        This method should battle the teams together.
        Call the attack method that exists in your team objects to do that battle functionality.
        '''
        while self.team_one.alive_heroes() and self.team_two.alive_heroes():
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
        if len(self.team_one.heroes) <= 0:
            print(self.team_one.name, " won the battle!")
            return "Team one won"
        else:
            print(self.team_two.name, " won the battle!")
            return "Team two won!"

    def show_stats(self):
        '''
        This method should print out battle statistics
        including each team's average kill/death ratio.

        Required Stats:
        Declare winning team
        Show both teams average kill/death ratio.
        Show surviving heroes.
        '''
        print("Stats")
        self.team_one.stats()
        self.team_two.stats()
        # print(self.team_battle())


# if __name__ == "__main__":
#
#     #naming hero one and commanding to attack
#     hero = Hero("Wonder Woman")
#     print(hero.attack())
#
#     #adding ability to hero one
#     ability = Ability("Divine Speed", 40)
#     hero.add_ability(ability)
#
#     #having hero attack and then defining a new ability
#     print(hero.attack())
#     new_ability = Ability("Super Human Strength", 30)
#
#     #adding new ability to hero attack then having hero attack
#     hero.add_ability(new_ability)
#     print(hero.attack())
#
#     #defining hero two
#     hero2 = Hero("Jodie Foster")
#     ability2 = Ability("Science", 50)
#     hero2.add_ability(ability2)
#
#     print(hero)
#     print(hero2)
#
#     hero.fight(hero2)
#     print(hero)
#     print(hero2)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()


# test
def test():
    if __name__ == "__main__":
        arena = Arena()
        arena.build_team_one()
        arena.build_team_two()
        arena.team_battle()
        arena.show_stats()
