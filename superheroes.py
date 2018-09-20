import random


class Ability:
    # Initialize starting values
    def __init__(self, name, attack_strength):
        # Set ability name
        # Set attack strength
        self.name = name
        self.attack_strength = attack_strength

    # Return attack value
    def attack(self):
        # Calculate lowest attack value as an integer.
        max_attack = self.attack_strength
        min_attack = self.attack_strength // 2
        # Use random.randint(a, b) to select a random attack value.
        random_value = random.randint(min_attack, max_attack)
        # Return attack value between min and the full attack.
        return random_value

    # Update attack value
    def update_attack(self, new_attack_strength):
        self.attack_strength = new_attack_strength


class Hero:

    def __init__(self, name, health=100):
        # Initialize starting values
        self.abilities = list()
        self.name = name

        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0


    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)


    def attack(self):
        total_attack = 0
        # Run attack() on every ability hero has
        # Call the attack method on every ability in our ability list
        # Add up and return the total of all attacks
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
        for defend in Armour.defend:
            defend += total_defend
            return total_defend
            if total_defend <= 0:
                return 0


    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.

        If the hero dies update number of deaths.
        """

        self.health = self.start_health - damage_amt
        if start_health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """

        self.kills += 1

class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """

        random_attack = random.randint(0, int(Ability.attack(self)))
        return random_attack


class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the
        initialized defend strength.
        """
        random_defend = random.randint(0,self.defense)
        return random_defend

class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)


    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        index = 0
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.pop(index)
                return
            index += 1
        return 0

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """

        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0


    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
        total_team_attack = 0
        for hero in self.heroes:
            hero.attack += total_team_attack
            other_team.defend(total_team_attack)
        for hero in self.heroes:
            hero.add_kill()


    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """
        total_team_defense = 0


    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        total_damage = damage // len(self.heroes)
        for hero in self.heroes:
            hero.take_damage(total_damage)
        return self.update_kills()

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for hero in self.heroes:
            if hero.health <= 0:
                hero.health = hero.start_health


    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """
        for hero in self.heroes:
            print(hero.kills/hero.deaths)


    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """
        dead_heros= 0
        for hero in self.heroes:
            if hero.health <= 0:
                hero += 1

class Arena:
    def __init__(self):
        """
        self.team_one = None
        self.team_two = None
        """

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        

#if __name__ == "__main__":
