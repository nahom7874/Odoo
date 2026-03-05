from odoo import models,fields
class EstateProperty(models.Model):
    _name= "estate.property"
    _description = "Real Estate Property"
    name=fields.Char(string="property name", required=True)
    description=fields.Text(string="description")
    postcode=fields.Char(string="postcode")
    date_availability=fields.Date()
    expected_price=fields.Float(string="expected price",required=True, tracking=True)
    selling_price=fields.Float(string="selling price",readonly=True,copy=False)
    bedrooms=fields.Integer(string="bedrooms",default=2)
    living_area=fields.Integer(string="living area (sqm)", help="Total living area in square meters")
    facades=fields.Integer(string="facades")
    garage=fields.Boolean(string="garage")
    garden=fields.Boolean(string="garden", default=False )
    garden_area=fields.Integer(string="garden area (sqm)",default=0)
    garden_orientation=fields.Selection([
        ("north","North"),("south","South"),("east","East"), ("west","West")
    ])
   

   
   








    


