# -*- coding: utf-8 -*-

import json

from api.view import ApiView
from popong_models.person import Person


class PersonApi(ApiView):
    model = Person
    kind_single = 'person'
    kind_list = 'people'

    def to_dict(self, person):
        extra_vars = json.loads(person.extra_vars)
        d = {
            'id': person.id,
            'name': person.name,
            'name_en': person.name_en,
            'name_cn': person.name_cn,
            'gender': person.gender,
            'birthday': person.birthday_date.isoformat(),
            'education': extra_vars.get('education'),
            'address': extra_vars.get('address'),
            'image': person.image,
            'twitter': person.twitter,
            'facebook': person.facebook,
            'homepage': person.homepage,
            'wiki': person.wiki,
        }
        return d

