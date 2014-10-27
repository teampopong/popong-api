# -*- coding: utf-8 -*-

from api.view import ApiView
from popong_models.party import Party


class PartyApi(ApiView):
    model = Party
    kind_single = 'party'
    kind_list = 'parties'

    def to_dict(self, party):
        d = {
            'id': party.id,
            'name': party.name,
            'color': party.color,
            'logo': party.logo,
            'size': party.size,
        }
        return d

