##############################################################################
#
#    OmniaSolutions, Open Source Management Solution    
#    Copyright (C) 2010-2011 OmniaSolutions (<http://www.omniasolutions.eu>). All Rights Reserved
#    $Id$
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'PLM Spare',
    'version': '1.1',
    'author': 'OmniaSolutions',
    'website': 'http://www.omniasolutions.eu',
    'category': 'Product Lifecycle Management',
    'sequence': 15,
    'summary': '',
    'images': [],
    'depends': ['plm'],
    'description': """
Add obsolete status to the work flow
==============================================
    """,
    'data': [
        # views
        'views/plm_product_view.xml',
        'views/plm_document_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
