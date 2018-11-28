import random


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

    def __str__(self):
        return "{}'s current health is {} and has killed {} opponents and has died {} times".format(
            self.name, self.health, self.kills, self.deaths
        )

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
            print("{} Kills: {} / {}".format(hero.name, hero.kills, hero.deaths))

    def remove_empty_list(self):
        pass


class Arena:

    def __init__(self):

        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """


        # Ask for user input, and return that user user_input
        pass

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        # check out this super kewl short cut command /
        # do the same as team one

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        # here you are going to call team attack and defend methods

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """

#
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


    #game_is_running = True
    #
    # # Instantiate Game arena
    # arena = Arena()
    #
    # # Build teams
    # arena.build_team_one()
    # arena.build_team_two()
    #
    # while game_is_running:
    #     arena.team_battle()
    #     arena.show_stats()
    #     play_again = input("Play Again? Y or N:")
    #
    #     # Check for Player input
    #     if play_again.lower() == "n":
    #         game_is_running = False
    #
    #     else:
    #         # Revive heroes to play Again
    #         arena.team_one.revive_heroes()
    #         arena.team_two.revive_heroes()


# test
def test():
    if __name__ == "__main__":
        arena = Arena()
        arena.build_team_one()
        arena.build_team_two()
        arena.team_battle()
        arena.show_stats()
