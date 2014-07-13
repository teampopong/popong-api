# -*- coding: utf-8 -*-

from flask import request

from api.view import ApiView
from popong_models.bill import Bill


class BillApi(ApiView):
    model = Bill

    def _search(self):
        query = super(BillApi, self)._search()

        s = request.args.get('s', '')
        query = query.filter(self.model.sponsor.like(u'%{s}%'.format(s=s)))

        return query

