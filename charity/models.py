from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from dictatorupf.models import Constants as DConstants

doc = """
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'charity'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'charity/Instructions.html'

    # Initial amount allocated to the dictator
    endowment = c(5)


class Subsession(BaseSubsession):
    def creating_session(self):
        num_d_rounds = DConstants.num_rounds
        tot_rounds = num_d_rounds + Constants.num_rounds
        if self.round_number == 1:
            for p in self.session.get_participants():
                p.vars['paying_round'] = random.randint(1, tot_rounds)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    final_payoff = models.CurrencyField()
    paying_round = models.IntegerField()
    donate = models.CurrencyField(
        doc="""Amount of donation""",
        min=0, max=Constants.endowment,
        verbose_name='I will donate (from 0 to %i)' % Constants.endowment
    )

    def set_payoff(self):
        self.payoff = Constants.endowment - self.donate
        self.paying_round = self.participant.vars['paying_round']
        if self.paying_round > DConstants.num_rounds:
            self.final_payoff = self.payoff
        else:
            self.final_payoff = self.participant.dictatorupf_player.filter(round_number=self.paying_round).first().payoff
