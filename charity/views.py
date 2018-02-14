from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Offer(Page):
    form_model = models.Player
    form_fields = ['donate']



class Results(Page):
    def keep(self):
        return Constants.endowment - self.player.donate

    def vars_for_template(self):
        return {
            'keep': Constants.endowment - self.player.donate,
        }

class ResultsSummary(Page):
    def vars_for_template(self):
        return {
            'paying_round': self.session.vars['paying_round'],
            'payoff':  self.participant.vars['keep'],
        }

page_sequence = [
    Introduction,
    Offer,
    Results,
    ResultsSummary
]
