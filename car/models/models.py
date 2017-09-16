# -*- coding: utf-8 -*-

from odoo import models, fields, api
# from scrapy_data import main

# class car(models.Model):
#     _name = 'car.car'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class brand(models.Model):
    _name = 'car.brand'

    name = fields.Char(string=u"名称", required=True)
    name_e = fields.Char(string=u"英文名称")
    first = fields.Char(string=u"首字母")
    code_guazi = fields.Char(string=u"瓜子网编码")


class car(models.Model):
    _name = 'car.car'

    name = fields.Char(string=u"名称", required=True)
    brand_id = fields.Many2one('car.brand', string=u"品牌")
    code_guazi = fields.Char(string=u"瓜子网编码")
    type = fields.Selection([('two', u"两厢"), ('three', u"三厢"), ('sport', u"跑车"), ('suv', u"SUV"),
                             ('mpv', u"MPV"), ('pickup', u"皮卡"), ('van', u"面包车"), ('other', u"其他")],
                            string=u"类型")


class model(models.Model):
    _name = 'car.model'

    name = fields.Char(string=u"名称", required=True)
    car_id = fields.Many2one('car.car', string=u"车系")
    price_new = fields.Char(string=u"新车指导价(含税)")

class temp1(models.Model):
    _name = 'car.temp1'

    brand_id = fields.Char(string=u"品牌id")
    brand_name = fields.Char(string=u"品牌名称")
    brand_first = fields.Char(string=u"品牌首字母")
    car_id = fields.Char(string=u"车系id")
    car_name = fields.Char(string=u"车系名称")
    car_type = fields.Char(string=u"类别")
    model_id = fields.Char(string=u"型号id")
    model_name = fields.Char(string=u"型号名称")


class sale(models.Model):
    _name = 'car.sale'

    brand_name = fields.Char(string=u"品牌名称")
    brand_first = fields.Char(string=u"品牌首字母")
    car_name = fields.Char(string=u"车系名称")
    car_type = fields.Char(string=u"类别")
    model_name = fields.Char(string=u"型号名称")

    url = fields.Char(string=u"链接地址")
    shangpai_date = fields.Char(string=u"上牌时间")
    address = fields.Char(string=u"上牌地点")
    xingshi = fields.Char(string=u"行驶里程")
    price = fields.Char(string=u"挂牌销售价格")
    price_new = fields.Char(string=u"新车指导价格")

class area(models.Model):
    _name = 'car.area'

    province_id = fields.Char(string=u"省份id")
    province_name = fields.Char(string=u"省份名称")
    city_id = fields.Char(string=u"城市id")
    city_name = fields.Char(string=u"城市名称")

class tf(models.Model):
    _name = 'car.tf'

    model_id = fields.Char(string=u"型号id")
    city_id = fields.Char(string=u"城市id")
    used_months = fields.Char(string=u"使用时间月")
    xingshi = fields.Char(string=u"行驶里程")
    price_new = fields.Char(string=u"新车指导价格")
    price = fields.Char(string=u"挂牌销售价格")

class Wizard(models.TransientModel):
    _name = 'car.wizard'

    @api.multi
    def catch_guazi(self):
        # main.run()
        pass

