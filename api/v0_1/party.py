# -*- coding: utf-8 -*-

from api.view import ApiView
from popong_models.party import Party


class PartyApi(ApiView):
    model = Party

