import cards
import db_con
import hand_strength


db = db_con.DB_Con()


# Base class. 
class Player():

  _raise_limit = 30

  def __init__(self, name, money, play_style):
    self.money = money
    self.name = name
    self.sum_pot_in = 0
    self.is_blind = False
    self.last_bet = 0
    self.raise_count = 0
    self.play_style = play_style
    self.last_action = ""
    self.total_fold = 0
    self.total_call = 0
    self.total_check = 0
    self.total_raise = 0
    self.total_showdown_tie = 0
    self.total_showdown_win = 0
    self.total_showdown_loss = 0
    self.total_pre_showdown_win = 0

    self.calculated_opponent_models = {} # only used by phase 3 player


  def set_cards(self, cards):
    self.cards = cards

  def show_cards(self):
    return self.cards
  
  def new_round(self, is_small = False, is_big = False):
    self.sum_pot_in = 0
    self.is_blind = is_big or is_small
    self.raise_count = 0

    self.modeling = []

    if (is_big):
      print("Big blind:", self.name, "puts", float(self._raise_limit), "in the pot")
      return self.bet_action(self._raise_limit)
    elif (is_small):
      print("Small blind:", self.name, "puts", (self._raise_limit/2), "in the pot")
      return self.bet_action(self._raise_limit/2)
    else:
      return 0

  def fold_action(self):
    print("Player", self.name, "folded")
    self.total_fold += 1
    self.sum_pot_in = 0
    return False

  def call_action(self, highest_bet):
    deducted = highest_bet - self.sum_pot_in
    self.sum_pot_in += deducted
    # self.sum_pot_in = 0
    self.money -= deducted
    print("Player", self.name, "called" if deducted > 0 else "checked", "with", deducted, "and has a total of", self.sum_pot_in, "in the pot")
    if deducted > 0:
      # This is a call
      self.total_call += 1
      return [0, deducted]
    else:
      # This is a check
      self.total_check += 1
      return [2, deducted]

  def raise_action(self, highest_bet):
    print("Player", self.name, "has", self.money, "BEFORE raising")
    self.raise_count += 1
    print("raise_limit: ", self._raise_limit, " highest_bet:", highest_bet, " sum_pot_in:", self.sum_pot_in)
    print("raise_count: ", self.raise_count)
    deducted = self._raise_limit + highest_bet - self.sum_pot_in
    self.sum_pot_in += deducted
    self.money -= deducted
    self.last_bet = self.sum_pot_in
    # Uncomment after testing - self.last_bet = deducted
    # self.sum_pot_in = 0
    print("Player", self.name, "raised  with", deducted, "and has a total of", self.sum_pot_in, "in the pot")
    # Put this between "raised with" and deducted. If needed
    # deducted-self._raise_limit if highest_bet > 0 else
    print("Player", self.name, "has", self.money, "AFTER raising, and last bet is", self.last_bet)
    self.total_raise += 1
    return [1, deducted]

  def bet_action(self, bet):
    self.sum_pot_in += bet
    self.money -= bet
    self.last_bet = bet
    return bet

  def win(self, pot):
    self.money += pot
    self.sum_pot_in = 0
    self.total_pre_showdown_win += 1

  def showdown_loss(self):
    self.total_showdown_loss += 1
    self.sum_pot_in = 0

  def showdown_tie(self, pot):
    self.total_showdown_tie += 1
    self.money += pot
    self.sum_pot_in = 0

  def showdown_win(self, pot):
    self.total_showdown_win += 1
    self.money += pot
    self.sum_pot_in = 0

  # Update model each time a player makes an action!
  def update_modeling (self, betting_round, players_remaining, total_raises, pot_odds, action):

    # returns a context based on what round, num players remaining, number of total raises in game
    # and the pot odds (C/(C+P))
    self.modeling.append([db.generate_context(betting_round, players_remaining, total_raises, pot_odds), action])

  # Save modeling after showdown is presented. (all shared cards)
  def save_modeling(self, num_players, shared_cards):
    
    hand = hand_strength.HandStrength(num_players)
    strength = hand.calculate(self.cards, shared_cards)

    # in form of [[context, action], [context, action], ... ] and player, strength
    db.insert_data(self.modeling, self.name, strength)


  def take_action_super(self, highest_bet, pot, players, position, shared_cards, state, total_raises, action):

    # pot_odds = use highest_bet and pot
    # players_remaining = players
    # betting_round = state
    # total_raises
    pot_odds = (float(highest_bet)/(float(highest_bet)+float(pot)))
    self.update_modeling(state, players, total_raises, pot_odds, action)







  def print_info(self, shared_cards):
    print(self.name, "- play style: "+self.play_style, "(", self.money, "credits):", cards.card_names(self.cards), cards.calc_cards_power(self.cards + shared_cards))
  
  def print_action_info(self, shared_cards):
    print(self.name, "- play style: "+self.play_style, "(", self.money, "credits):", cards.card_names(self.cards), cards.calc_cards_power(self.cards + shared_cards))
    print("Total wins before showdown: ", self.total_pre_showdown_win)
    print("Total wins at showdown: ", self.total_showdown_win)
    print("Total ties at showdown: ", self.total_showdown_tie)
    print("Total losses at showdown: ", self.total_showdown_loss)
    print("Total calls: ", self.total_call)
    print("Total checks: ", self.total_check)
    print("Total raises: ", self.total_raise)
    print("Total folds: ", self.total_fold)
    print("\n")