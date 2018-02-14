from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Information(Page):
    pass


class Letsgetstarted(Page):
    pass

class Instructions(Page):
    pass


page_sequence = [
   Information,
Letsgetstarted
]
