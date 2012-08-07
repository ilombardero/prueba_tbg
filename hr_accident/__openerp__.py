
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Accident",
    "version": "1.0",
    "depends" : [
             'hr',
             'mgmtsystem_action',
             'wiki_procedure',
    ],
    "author": "Digital5, S.L.",
    "website" : "http://www.digital5.es",
    "category" : "Human Resources",
    "init_xml" : [],
    "update_xml" : [
            'hr_accident_view.xml',
            'hr_accident_sequence.xml',
            'hr_accident_board.xml'
    ],
    'demo_xml': [],
    'installable': True,
}