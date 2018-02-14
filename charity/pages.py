from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Offer(Page):
    form_model = 'player'
    form_fields = ['donate']


class Results(Page):
    def vars_for_template(self):
        return {
            'keep': Constants.endowment - self.player.donate,
        }

    def before_next_page(self):
        self.player.set_payoff()


class ResultsSummary(Page):
    def vars_for_template(self):
        rounds = self.participant.dictatorupf_player.all()
        nrounds = rounds.count()

        return {
            'rounds': rounds,
            'nrounds': nrounds,
        }


page_sequence = [
    Introduction,
    Offer,
    Results,
    ResultsSummary
]
