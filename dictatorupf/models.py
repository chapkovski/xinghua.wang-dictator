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
    name_in_url = 'dictatorupf'
    players_per_group = 2
    num_rounds = 2

    instructions_template = 'dictatorupf/Instructions.html'
    # Initial amount allocated to the dictator
    endowment = c(5)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 2:
            # reverse the roles
            self.get_group_matrix()
            self.group_randomly(fixed_id_in_group=True)
            matrix = self.get_group_matrix()
            for row in matrix:
                row.reverse()
            self.set_group_matrix(matrix)


class Group(BaseGroup):
    kept = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0, max=Constants.endowment,
        verbose_name='I will keep (from 0 to %i)' % Constants.endowment
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = self.kept
        p2.payoff = Constants.endowment - self.kept


class Player(BasePlayer):
    pass