from datetime import timedelta

from odoo import models, fields,api
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offers"
    price = fields.Float(string="Offer Price", required=True)
    status = fields.Selection([
        ("accepted", "Accepted"),
        ("refused", "Refused")
    ], string="Status", required=True,readonly=True, copy=False, )
    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    def action_accept(self):
        for record in self:
             if record.property_id.state == "offer_accepted":
                      raise UserError(
                "This property already has an accepted offer."
                )
             record.status = "accepted"
             record.property_id.buyer_id =  record.partner_id
             record.property_id.selling_price = record.price 
             record.property_id.state = "offer_accepted"
            
        
    def action_refuse(self):
        for record in self:
            record.status = 'refused'
                   
    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
         for record in self:
            # If the record is new, use today's date. Otherwise use the creation date.
            base_date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = base_date + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            base_date = record.create_date.date() if record.create_date else fields.Date.today()
            # Calculate the difference in days
            record.validity = (record.date_deadline - base_date).days
      



  