# -*- coding: utf-8 -*-

from flask import request

from api.view import ApiView
from popong_models.bill import Bill


class BillApi(ApiView):
    model = Bill
    kind_single = 'bill'
    kind_list = 'bills'

    def _search(self):
        query = super(BillApi, self)._search()

        s = request.args.get('s', '')
        query = query.filter(self.model.sponsor.like(u'%{s}%'.format(s=s)))

        return query

    def to_dict(self, bill):
        d = {
            'id': bill.id,
            'name': bill.name,
            'summary': bill.summary,
            'assembly_id': bill.assembly_id,
            'proposed_date': bill.proposed_date,
            'decision_date': bill.decision_date,
            'document_url': bill.document_url,
            'sponsor': bill.sponsor,
            'status': bill.status,
            'cosponsors': [{ 'id': p.id, 'name': p.name } for p in bill.cosponsors],
        }
        return d

