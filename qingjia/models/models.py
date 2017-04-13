# -*- coding: utf-8 -*-

from odoo import models, fields, api


class qingjiadan(models.Model):
    WORKFLOW_STATE_SELECTION = [
        ('draft', '草稿'),
        ('confirm', '待审批'),
        ('complete', '已完成')
    ]

    _name = 'qingjia.qingjiadan'
    name = fields.Char(string="申请人")
    days = fields.Integer(string="天数")
    startdate = fields.Date(string="开始日期")
    reason = fields.Text(string="请假事由")
    state = fields.Selection(WORKFLOW_STATE_SELECTION,
                             default='draft',
                             string='状态',
                             readonly=True)

    @api.multi
    def do_confirm(self):
        self.state = 'confirm'
        return True

    @api.multi
    def do_complete(self):
        self.state = 'complete'
        return True
