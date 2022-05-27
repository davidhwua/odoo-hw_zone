# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __openerp__.py file at the root folder of this module.                   #
###############################################################################
import datetime
from odoo import models, fields, api
from odoo.tools.translate import _
from logging import getLogger
from jinja2 import Environment,FileSystemLoader
import os
_logger = getLogger(__name__)

class Province(models.Model):
    _name = 'hw.province'
    _description = u'省份'

    name = fields.Char(string=u'省份')
    

class Contacts(models.Model):
    _name = 'hw.city'
    _rec_name = 'name'
    _description = u'城市'
    
    department_id = fields.Many2one('hw.province', string=u'省份')
    name = fields.Char(string=u'城市')

class County(models.Model):
    _name = 'hw.county'
    _rec_name = 'name'
    _description = u'县区'

    name = fields.Char(string='区/县')
    department_id = fields.Many2one('hw.province', string=u'省份')
    city_id = fields.Many2one('hw.city', string='城市')