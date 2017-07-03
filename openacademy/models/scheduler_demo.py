# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import logging
from datetime import datetime
_logger = logging.getLogger(__name__)

class scheduler_demo(models.Model):
    _name = 'scheduler.demo'
    name = fields.Char(required=True)
    numberOfUpdates = fields.Integer('Number of updates')
    lastModified = fields.Datetime('Last updated')

    def process_demo_scheduler_queue(self):
        scheduler_line_ids = self.env['scheduler.demo'].search([])
        for scheduler_line in scheduler_line_ids:
            _logger.info('line:' + scheduler_line.name)
            scheduler_line.numberOfUpdates += 1
            scheduler_line.lastModified = datetime.utcnow()

