# -*- coding: utf-8 -*-

import json

from api.view import ApiView
from popong_models.statement import Statement


class StatementApi(ApiView):
    model = Statement
    kind_single = 'statement'
    kind_list = 'statements'

    def _search(self):
        return super(StatementApi, self)._search(fieldname='content')

    def to_dict(self, statement):
        d = {
            'id': statement.id,
            'meeting_id': statement.meeting_id,
            'person_id': statement.person_id,
            'sequence': statement.sequence,
            'speaker': statement.speaker,
            'content': statement.content,
            'date': statement.date,
        }
        return d

