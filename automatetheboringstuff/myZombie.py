import zombiedice
import random
# create bots:
# A bot that, after the first roll, randomly decides if it will continue or stop
# A bot that stops rolling after it has rolled two brains
# A bot that stops rolling after it has rolled two shotguns
# A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
# A bot that stops rolling after it has rolled more shotguns than brains

class RandomStopZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        while diceRollResults is not None:
            randomStopOrContinue = random.randint(0,1)

            if randomStopOrContinue == 1:
                diceRollResults = zombiedice.roll()
            else:
                break

class TwoBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        brains = 0

        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class TwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        shotguns = 0

        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class OneToFourZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        brains = 0
        turns = 0

        while diceRollResults is not None:
            turns += 1

            if diceRollResults['shotgun'] == 2:
                break

            if turns <= 4:
                diceRollResults = zombiedice.roll()
            else:
                break

class MoreShotgunsThanBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        brains = 0
        shotguns = 0

        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']

            if not(shotguns > brains):
                diceRollResults = zombiedice.roll()
            else:
                break

zombies = (
#     zombiedice.examples.RandomCoinFlipZombie(name='Random'),
#     zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
#     zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
#     zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    RandomStopZombie(name='Random Stop Zombie'),
    TwoBrainsZombie(name='Until 2 Brains Zombie'),
    TwoShotgunsZombie(name='Until 2 Shotguns Zombie'),
    OneToFourZombie(name='One to Four'),
    MoreShotgunsThanBrainsZombie(name='More Shotguns Than Brain Zombie')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
