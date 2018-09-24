# -*- coding: utf-8 -*-
#
# Module Odoo URB.
# Copyright (C) 2018  Auneor-Conseil
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


from openerp import models, fields


class Formation(models.Model):
    _name = "formation.formation"

    name = fields.Char(string="Nom")
    type_formation = fields.Selection([
        ('convention', 'Convention'),
        ('contract', 'Contrat')],
        string='Type de document')
    objet_formation = fields.Char(string="Object Convention / Contrat")
    objectifs_pedagogiques = fields.Html(string="Objectifs pédagogiques")
    contenu = fields.Html(string="Contenu")
    methodes_moyens_pedagogique = fields.Html(string="Méthodes et moyens pédagogiques")
    modalite_validation = fields.Html(string="Modalités de suivi et validation des acquis")
    date_et_duree = fields.Html(string="Date et durée")
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    lieu = fields.Char(string="Lieu")
    niveau_connaissances = fields.Html(string="Niveau de connaissances préalables nécessaire")
    organisation = fields.Char(string="Organisation de l’action de formation")
    formateurs = fields.Many2many('res.partner', string="formateurs")
    effectifs = fields.Many2many(comodel_name='res.partner',
                                 relation='effectifs',
                                 column1='effectif_formation',
                                 column2='effectif_res_partner')
    modalites_reglement = fields.Html(string="Modalités de règlement")
    date_contrat = fields.Date("Date signature du contrat")
    cotractant = fields.Many2one('res.partner', 'Cotractant')

    urb_logo = fields.Binary("Logo", attachment=True)
    urb_tampon = fields.Binary("Tampon", attachment=True)
