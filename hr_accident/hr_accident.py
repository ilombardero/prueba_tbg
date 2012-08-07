# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from osv import fields, osv
import time

class hr_accident_cause(osv.osv):
    """
    Cause of the accident
    """
    _name = "hr.accident.cause"
    _description = "Cause of the accident"
    _columns = {
        'name': fields.char('Cause', size=50, required=True),
        'description': fields.text('Description')
    }

hr_accident_cause()

class hr_accident_origin(osv.osv):
    """
    Origin of the accident
    """
    _name = "hr.accident.origin"
    _description = "Origin of the accident"
    _columns = {
        'name': fields.char('Origin', size=50, required=True),
        'description': fields.text('Description')
    }

hr_accident_origin()

class hr_accident(osv.osv):
    """
    Management System - Accident 
    """
    _name = "hr.accident"
    _description = "Accident"
    _columns = {
        'name': fields.char('Reference', size=64, required=True, readonly=True),
        'title': fields.char('Title', size=50),
        'date': fields.date('Date', required=True),
        'partner_id': fields.many2one('res.partner', 'Partner'),
        
        'type' : fields.selection([('discharge', 'With Discharge'), ('nodischarge', 'Without Discharge')], 'Type', required=True),
        'date_discharge': fields.date('Date of Discharge'),
        'analytic_account_id' : fields.many2one('account.analytic.account', 'Account', ondelete='cascade', required=True),
        
        'affected_employee': fields.many2one('hr.employee','Affected', required=True),
        'manager_employee': fields.many2one('hr.employee','Manager', required=True),
        'author_user_id': fields.many2one('res.users','Author', required=True),
        
        'origin_ids': fields.many2many('hr.accident.origin','hr_accident_origin_rel', 'hr_accident_id', 'origin_id', 'Origins', required=True),
        'cause_ids': fields.many2many('hr.accident.cause','hr_accident_cause_rel', 'hr_accident_id', 'cause_id', 'Causes'),
        
        'procedure_ids': fields.many2many('wiki.wiki','hr_accident_wiki_rel', 'hr_accident_id', 'procedure_id', 'Procedure'),
        'description': fields.text('Description', required=True),
        'analysis': fields.text('Analysis'),
        
        'immediate_action_id': fields.many2one('mgmtsystem.action', 'Immediate Action'),
        'efficiency_immediate': fields.text('Efficiency of the Immediate Action'),
        'corrective_action_id': fields.many2one('mgmtsystem.action', 'Corrective Action'),
        'efficiency_corrective': fields.text('Efficiency of the Corrective Action'),
        'preventive_action_id': fields.many2one('mgmtsystem.action', 'Preventive Action'),
        'efficiency_preventive': fields.text('Efficiency of the Preventive Action'),
        'state': fields.selection((('o','Open'),('c','Closed')), 'State', size=16, readonly=True),
    }
    _defaults = {
        'date': lambda *a: time.strftime('%Y-%m-%d'),
        'state': 'o',
        'type': 'nodischarge',
        'author_user_id': lambda cr, uid, id, c={}: id,
        'name': 'NEW',
    }
    
    def create(self, cr, uid, vals, context=None):
        vals.update({
            'name': self.pool.get('ir.sequence').get(cr, uid, 'hr.accident')
        })
        return super(hr_accident, self).create(cr, uid, vals, context)


    def button_close(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'c'})
    
hr_accident()

class hr_employee(osv.osv):
    _name = "hr.employee"
    _inherit = 'hr.employee'
    _columns = {
        'accident_ids' : fields.one2many('hr.accident', 'affected_employee', 'Accidents'),
    }

hr_employee()