from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'charity'
    players_per_group =None
    num_rounds = 1

    instructions_template = 'charity/Instructions.html'

    # Initial amount allocated to the dictator
    endowment = c(5)


class Subsession(BaseSubsession):
    def creating_session(self):
        payoff = Constants.endowment - self.player.donate
        self.participant.vars['keep'] = payoff
        paying_round = random.randint(1, Constants.num_rounds)
        self.session.vars['paying_round'] = paying_round

class Group(BaseGroup):
   pass

class Player(BasePlayer):
    donate = models.CurrencyField(
        doc="""Amount of donation""",
        min=0, max=Constants.endowment,
        verbose_name='I will donate (from 0 to %i)' % Constants.endowment
    )


