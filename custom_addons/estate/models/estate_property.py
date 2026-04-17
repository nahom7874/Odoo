from odoo import models,fields
class EstateProperty(models.Model):
    _name= "estate.property"
    _description = "Real Estate Property"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    name=fields.Char(string="Title", required=True, tracking=True)
    postcode=fields.Char(string="Postcode")
    description=fields.Text(string="Description")
    date_availability=fields.Date(string="Available from", default=fields.Date.today, copy=False)
    expected_price=fields.Float(string="Expected Price",required=True, tracking=True)
    selling_price=fields.Float(string="Selling Price",readonly=True,copy=False )
    bedrooms=fields.Integer(string="Bedrooms",default=2)
    living_area=fields.Integer(string="Living Area (sqm)", help="Total living area in square meters")
    facades=fields.Integer(string="Facades")
    garage=fields.Boolean(string="Garage")
    garden=fields.Boolean(string="Garden", default=False )
    garden_area=fields.Integer(string="Garden Area (sqm)",default=0)
    garden_orientation=fields.Selection([
        ("north","North"),("south","South"),("east","East"), ("west","West")
    ])
    state=fields.Selection([
        ("new","New"),("offer_received","Offer Received"),("offer_accepted","Offer Accepted"),("sold","Sold"),("canceled","Canceled")
    ], default="new", tracking=True, required=True)
    property_type_id=fields.Many2one("estate.property.type", string="Property Type", required=True)
    salesman_id=fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user) 
    buyer_id=fields.Many2one("res.partner", string="Buyer", copy=False)
    tag_ids=fields.Many2many("estate.property.tag", string="Tags")
    offer_ids=fields.One2many("estate.property.offer", "property_id", string="Offers")

    

   
   








    


