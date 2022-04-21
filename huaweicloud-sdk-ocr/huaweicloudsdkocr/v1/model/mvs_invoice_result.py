# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MvsInvoiceResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'number': 'str',
        'machine_printed_code': 'str',
        'machine_printed_number': 'str',
        'issue_date': 'str',
        'machine_number': 'str',
        'buyer_name': 'str',
        'buyer_organization_number': 'str',
        'buyer_id': 'str',
        'seller_name': 'str',
        'seller_phone': 'str',
        'seller_id': 'str',
        'seller_account': 'str',
        'seller_address': 'str',
        'seller_bank': 'str',
        'vehicle_type': 'str',
        'brand_model': 'str',
        'manufacturing_location': 'str',
        'quality_certificate': 'str',
        'import_certificate': 'str',
        'inspection_number': 'str',
        'engine_number': 'str',
        'vehicle_identification_number': 'str',
        'tonnage': 'str',
        'seating_capacity': 'str',
        'tax_authority': 'str',
        'tax_authority_code': 'str',
        'tax_payment_receipt': 'str',
        'tax_rate': 'str',
        'tax': 'str',
        'tax_exclusive_price': 'str',
        'total': 'str',
        'total_chinese': 'str',
        'fiscal_code': 'str'
    }

    attribute_map = {
        'code': 'code',
        'number': 'number',
        'machine_printed_code': 'machine_printed_code',
        'machine_printed_number': 'machine_printed_number',
        'issue_date': 'issue_date',
        'machine_number': 'machine_number',
        'buyer_name': 'buyer_name',
        'buyer_organization_number': 'buyer_organization_number',
        'buyer_id': 'buyer_id',
        'seller_name': 'seller_name',
        'seller_phone': 'seller_phone',
        'seller_id': 'seller_id',
        'seller_account': 'seller_account',
        'seller_address': 'seller_address',
        'seller_bank': 'seller_bank',
        'vehicle_type': 'vehicle_type',
        'brand_model': 'brand_model',
        'manufacturing_location': 'manufacturing_location',
        'quality_certificate': 'quality_certificate',
        'import_certificate': 'import_certificate',
        'inspection_number': 'inspection_number',
        'engine_number': 'engine_number',
        'vehicle_identification_number': 'vehicle_identification_number',
        'tonnage': 'tonnage',
        'seating_capacity': 'seating_capacity',
        'tax_authority': 'tax_authority',
        'tax_authority_code': 'tax_authority_code',
        'tax_payment_receipt': 'tax_payment_receipt',
        'tax_rate': 'tax_rate',
        'tax': 'tax',
        'tax_exclusive_price': 'tax_exclusive_price',
        'total': 'total',
        'total_chinese': 'total_chinese',
        'fiscal_code': 'fiscal_code'
    }

    def __init__(self, code=None, number=None, machine_printed_code=None, machine_printed_number=None, issue_date=None, machine_number=None, buyer_name=None, buyer_organization_number=None, buyer_id=None, seller_name=None, seller_phone=None, seller_id=None, seller_account=None, seller_address=None, seller_bank=None, vehicle_type=None, brand_model=None, manufacturing_location=None, quality_certificate=None, import_certificate=None, inspection_number=None, engine_number=None, vehicle_identification_number=None, tonnage=None, seating_capacity=None, tax_authority=None, tax_authority_code=None, tax_payment_receipt=None, tax_rate=None, tax=None, tax_exclusive_price=None, total=None, total_chinese=None, fiscal_code=None):
        """MvsInvoiceResult

        The model defined in huaweicloud sdk

        :param code: 发票代码。 
        :type code: str
        :param number: 发票号码。 
        :type number: str
        :param machine_printed_code: 机打代码。 
        :type machine_printed_code: str
        :param machine_printed_number: 机打号码。 
        :type machine_printed_number: str
        :param issue_date: 开票日期。 
        :type issue_date: str
        :param machine_number: 机器编号。 
        :type machine_number: str
        :param buyer_name: 购买方名称。 
        :type buyer_name: str
        :param buyer_organization_number: 购买方身份证号码/组织机构代码。 
        :type buyer_organization_number: str
        :param buyer_id: 购买方纳税人识别号。 
        :type buyer_id: str
        :param seller_name: 销货单位名称。 
        :type seller_name: str
        :param seller_phone: 销售方电话。 
        :type seller_phone: str
        :param seller_id: 销售方纳税人识别号。 
        :type seller_id: str
        :param seller_account: 销售方账号。 
        :type seller_account: str
        :param seller_address: 销售方地址。 
        :type seller_address: str
        :param seller_bank: 销售方开户行。 
        :type seller_bank: str
        :param vehicle_type: 车辆类型。 
        :type vehicle_type: str
        :param brand_model: 厂牌型号。 
        :type brand_model: str
        :param manufacturing_location: 产地。 
        :type manufacturing_location: str
        :param quality_certificate: 合格证号。 
        :type quality_certificate: str
        :param import_certificate: 进口证明书号。 
        :type import_certificate: str
        :param inspection_number: 商检单号。 
        :type inspection_number: str
        :param engine_number: 发动机号码。 
        :type engine_number: str
        :param vehicle_identification_number: 车辆识别代号/车架号码。 
        :type vehicle_identification_number: str
        :param tonnage: 吨位。 
        :type tonnage: str
        :param seating_capacity: 限乘人数。 
        :type seating_capacity: str
        :param tax_authority: 主管税务机关。 
        :type tax_authority: str
        :param tax_authority_code: 主管税务机关代码。 
        :type tax_authority_code: str
        :param tax_payment_receipt: 完税凭证号码。 
        :type tax_payment_receipt: str
        :param tax_rate: 增值税税率或征收率。 
        :type tax_rate: str
        :param tax: 增值税税额。 
        :type tax: str
        :param tax_exclusive_price: 不含税价。 
        :type tax_exclusive_price: str
        :param total: 价税合计。 
        :type total: str
        :param total_chinese: 价税合计大写。 
        :type total_chinese: str
        :param fiscal_code: 税控码。 
        :type fiscal_code: str
        """
        
        

        self._code = None
        self._number = None
        self._machine_printed_code = None
        self._machine_printed_number = None
        self._issue_date = None
        self._machine_number = None
        self._buyer_name = None
        self._buyer_organization_number = None
        self._buyer_id = None
        self._seller_name = None
        self._seller_phone = None
        self._seller_id = None
        self._seller_account = None
        self._seller_address = None
        self._seller_bank = None
        self._vehicle_type = None
        self._brand_model = None
        self._manufacturing_location = None
        self._quality_certificate = None
        self._import_certificate = None
        self._inspection_number = None
        self._engine_number = None
        self._vehicle_identification_number = None
        self._tonnage = None
        self._seating_capacity = None
        self._tax_authority = None
        self._tax_authority_code = None
        self._tax_payment_receipt = None
        self._tax_rate = None
        self._tax = None
        self._tax_exclusive_price = None
        self._total = None
        self._total_chinese = None
        self._fiscal_code = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if number is not None:
            self.number = number
        if machine_printed_code is not None:
            self.machine_printed_code = machine_printed_code
        if machine_printed_number is not None:
            self.machine_printed_number = machine_printed_number
        if issue_date is not None:
            self.issue_date = issue_date
        if machine_number is not None:
            self.machine_number = machine_number
        if buyer_name is not None:
            self.buyer_name = buyer_name
        if buyer_organization_number is not None:
            self.buyer_organization_number = buyer_organization_number
        if buyer_id is not None:
            self.buyer_id = buyer_id
        if seller_name is not None:
            self.seller_name = seller_name
        if seller_phone is not None:
            self.seller_phone = seller_phone
        if seller_id is not None:
            self.seller_id = seller_id
        if seller_account is not None:
            self.seller_account = seller_account
        if seller_address is not None:
            self.seller_address = seller_address
        if seller_bank is not None:
            self.seller_bank = seller_bank
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type
        if brand_model is not None:
            self.brand_model = brand_model
        if manufacturing_location is not None:
            self.manufacturing_location = manufacturing_location
        if quality_certificate is not None:
            self.quality_certificate = quality_certificate
        if import_certificate is not None:
            self.import_certificate = import_certificate
        if inspection_number is not None:
            self.inspection_number = inspection_number
        if engine_number is not None:
            self.engine_number = engine_number
        if vehicle_identification_number is not None:
            self.vehicle_identification_number = vehicle_identification_number
        if tonnage is not None:
            self.tonnage = tonnage
        if seating_capacity is not None:
            self.seating_capacity = seating_capacity
        if tax_authority is not None:
            self.tax_authority = tax_authority
        if tax_authority_code is not None:
            self.tax_authority_code = tax_authority_code
        if tax_payment_receipt is not None:
            self.tax_payment_receipt = tax_payment_receipt
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if tax is not None:
            self.tax = tax
        if tax_exclusive_price is not None:
            self.tax_exclusive_price = tax_exclusive_price
        if total is not None:
            self.total = total
        if total_chinese is not None:
            self.total_chinese = total_chinese
        if fiscal_code is not None:
            self.fiscal_code = fiscal_code

    @property
    def code(self):
        """Gets the code of this MvsInvoiceResult.

        发票代码。 

        :return: The code of this MvsInvoiceResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this MvsInvoiceResult.

        发票代码。 

        :param code: The code of this MvsInvoiceResult.
        :type code: str
        """
        self._code = code

    @property
    def number(self):
        """Gets the number of this MvsInvoiceResult.

        发票号码。 

        :return: The number of this MvsInvoiceResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this MvsInvoiceResult.

        发票号码。 

        :param number: The number of this MvsInvoiceResult.
        :type number: str
        """
        self._number = number

    @property
    def machine_printed_code(self):
        """Gets the machine_printed_code of this MvsInvoiceResult.

        机打代码。 

        :return: The machine_printed_code of this MvsInvoiceResult.
        :rtype: str
        """
        return self._machine_printed_code

    @machine_printed_code.setter
    def machine_printed_code(self, machine_printed_code):
        """Sets the machine_printed_code of this MvsInvoiceResult.

        机打代码。 

        :param machine_printed_code: The machine_printed_code of this MvsInvoiceResult.
        :type machine_printed_code: str
        """
        self._machine_printed_code = machine_printed_code

    @property
    def machine_printed_number(self):
        """Gets the machine_printed_number of this MvsInvoiceResult.

        机打号码。 

        :return: The machine_printed_number of this MvsInvoiceResult.
        :rtype: str
        """
        return self._machine_printed_number

    @machine_printed_number.setter
    def machine_printed_number(self, machine_printed_number):
        """Sets the machine_printed_number of this MvsInvoiceResult.

        机打号码。 

        :param machine_printed_number: The machine_printed_number of this MvsInvoiceResult.
        :type machine_printed_number: str
        """
        self._machine_printed_number = machine_printed_number

    @property
    def issue_date(self):
        """Gets the issue_date of this MvsInvoiceResult.

        开票日期。 

        :return: The issue_date of this MvsInvoiceResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this MvsInvoiceResult.

        开票日期。 

        :param issue_date: The issue_date of this MvsInvoiceResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def machine_number(self):
        """Gets the machine_number of this MvsInvoiceResult.

        机器编号。 

        :return: The machine_number of this MvsInvoiceResult.
        :rtype: str
        """
        return self._machine_number

    @machine_number.setter
    def machine_number(self, machine_number):
        """Sets the machine_number of this MvsInvoiceResult.

        机器编号。 

        :param machine_number: The machine_number of this MvsInvoiceResult.
        :type machine_number: str
        """
        self._machine_number = machine_number

    @property
    def buyer_name(self):
        """Gets the buyer_name of this MvsInvoiceResult.

        购买方名称。 

        :return: The buyer_name of this MvsInvoiceResult.
        :rtype: str
        """
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, buyer_name):
        """Sets the buyer_name of this MvsInvoiceResult.

        购买方名称。 

        :param buyer_name: The buyer_name of this MvsInvoiceResult.
        :type buyer_name: str
        """
        self._buyer_name = buyer_name

    @property
    def buyer_organization_number(self):
        """Gets the buyer_organization_number of this MvsInvoiceResult.

        购买方身份证号码/组织机构代码。 

        :return: The buyer_organization_number of this MvsInvoiceResult.
        :rtype: str
        """
        return self._buyer_organization_number

    @buyer_organization_number.setter
    def buyer_organization_number(self, buyer_organization_number):
        """Sets the buyer_organization_number of this MvsInvoiceResult.

        购买方身份证号码/组织机构代码。 

        :param buyer_organization_number: The buyer_organization_number of this MvsInvoiceResult.
        :type buyer_organization_number: str
        """
        self._buyer_organization_number = buyer_organization_number

    @property
    def buyer_id(self):
        """Gets the buyer_id of this MvsInvoiceResult.

        购买方纳税人识别号。 

        :return: The buyer_id of this MvsInvoiceResult.
        :rtype: str
        """
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, buyer_id):
        """Sets the buyer_id of this MvsInvoiceResult.

        购买方纳税人识别号。 

        :param buyer_id: The buyer_id of this MvsInvoiceResult.
        :type buyer_id: str
        """
        self._buyer_id = buyer_id

    @property
    def seller_name(self):
        """Gets the seller_name of this MvsInvoiceResult.

        销货单位名称。 

        :return: The seller_name of this MvsInvoiceResult.
        :rtype: str
        """
        return self._seller_name

    @seller_name.setter
    def seller_name(self, seller_name):
        """Sets the seller_name of this MvsInvoiceResult.

        销货单位名称。 

        :param seller_name: The seller_name of this MvsInvoiceResult.
        :type seller_name: str
        """
        self._seller_name = seller_name

    @property
    def seller_phone(self):
        """Gets the seller_phone of this MvsInvoiceResult.

        销售方电话。 

        :return: The seller_phone of this MvsInvoiceResult.
        :rtype: str
        """
        return self._seller_phone

    @seller_phone.setter
    def seller_phone(self, seller_phone):
        """Sets the seller_phone of this MvsInvoiceResult.

        销售方电话。 

        :param seller_phone: The seller_phone of this MvsInvoiceResult.
        :type seller_phone: str
        """
        self._seller_phone = seller_phone

    @property
    def seller_id(self):
        """Gets the seller_id of this MvsInvoiceResult.

        销售方纳税人识别号。 

        :return: The seller_id of this MvsInvoiceResult.
        :rtype: str
        """
        return self._seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        """Sets the seller_id of this MvsInvoiceResult.

        销售方纳税人识别号。 

        :param seller_id: The seller_id of this MvsInvoiceResult.
        :type seller_id: str
        """
        self._seller_id = seller_id

    @property
    def seller_account(self):
        """Gets the seller_account of this MvsInvoiceResult.

        销售方账号。 

        :return: The seller_account of this MvsInvoiceResult.
        :rtype: str
        """
        return self._seller_account

    @seller_account.setter
    def seller_account(self, seller_account):
        """Sets the seller_account of this MvsInvoiceResult.

        销售方账号。 

        :param seller_account: The seller_account of this MvsInvoiceResult.
        :type seller_account: str
        """
        self._seller_account = seller_account

    @property
    def seller_address(self):
        """Gets the seller_address of this MvsInvoiceResult.

        销售方地址。 

        :return: The seller_address of this MvsInvoiceResult.
        :rtype: str
        """
        return self._seller_address

    @seller_address.setter
    def seller_address(self, seller_address):
        """Sets the seller_address of this MvsInvoiceResult.

        销售方地址。 

        :param seller_address: The seller_address of this MvsInvoiceResult.
        :type seller_address: str
        """
        self._seller_address = seller_address

    @property
    def seller_bank(self):
        """Gets the seller_bank of this MvsInvoiceResult.

        销售方开户行。 

        :return: The seller_bank of this MvsInvoiceResult.
        :rtype: str
        """
        return self._seller_bank

    @seller_bank.setter
    def seller_bank(self, seller_bank):
        """Sets the seller_bank of this MvsInvoiceResult.

        销售方开户行。 

        :param seller_bank: The seller_bank of this MvsInvoiceResult.
        :type seller_bank: str
        """
        self._seller_bank = seller_bank

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this MvsInvoiceResult.

        车辆类型。 

        :return: The vehicle_type of this MvsInvoiceResult.
        :rtype: str
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this MvsInvoiceResult.

        车辆类型。 

        :param vehicle_type: The vehicle_type of this MvsInvoiceResult.
        :type vehicle_type: str
        """
        self._vehicle_type = vehicle_type

    @property
    def brand_model(self):
        """Gets the brand_model of this MvsInvoiceResult.

        厂牌型号。 

        :return: The brand_model of this MvsInvoiceResult.
        :rtype: str
        """
        return self._brand_model

    @brand_model.setter
    def brand_model(self, brand_model):
        """Sets the brand_model of this MvsInvoiceResult.

        厂牌型号。 

        :param brand_model: The brand_model of this MvsInvoiceResult.
        :type brand_model: str
        """
        self._brand_model = brand_model

    @property
    def manufacturing_location(self):
        """Gets the manufacturing_location of this MvsInvoiceResult.

        产地。 

        :return: The manufacturing_location of this MvsInvoiceResult.
        :rtype: str
        """
        return self._manufacturing_location

    @manufacturing_location.setter
    def manufacturing_location(self, manufacturing_location):
        """Sets the manufacturing_location of this MvsInvoiceResult.

        产地。 

        :param manufacturing_location: The manufacturing_location of this MvsInvoiceResult.
        :type manufacturing_location: str
        """
        self._manufacturing_location = manufacturing_location

    @property
    def quality_certificate(self):
        """Gets the quality_certificate of this MvsInvoiceResult.

        合格证号。 

        :return: The quality_certificate of this MvsInvoiceResult.
        :rtype: str
        """
        return self._quality_certificate

    @quality_certificate.setter
    def quality_certificate(self, quality_certificate):
        """Sets the quality_certificate of this MvsInvoiceResult.

        合格证号。 

        :param quality_certificate: The quality_certificate of this MvsInvoiceResult.
        :type quality_certificate: str
        """
        self._quality_certificate = quality_certificate

    @property
    def import_certificate(self):
        """Gets the import_certificate of this MvsInvoiceResult.

        进口证明书号。 

        :return: The import_certificate of this MvsInvoiceResult.
        :rtype: str
        """
        return self._import_certificate

    @import_certificate.setter
    def import_certificate(self, import_certificate):
        """Sets the import_certificate of this MvsInvoiceResult.

        进口证明书号。 

        :param import_certificate: The import_certificate of this MvsInvoiceResult.
        :type import_certificate: str
        """
        self._import_certificate = import_certificate

    @property
    def inspection_number(self):
        """Gets the inspection_number of this MvsInvoiceResult.

        商检单号。 

        :return: The inspection_number of this MvsInvoiceResult.
        :rtype: str
        """
        return self._inspection_number

    @inspection_number.setter
    def inspection_number(self, inspection_number):
        """Sets the inspection_number of this MvsInvoiceResult.

        商检单号。 

        :param inspection_number: The inspection_number of this MvsInvoiceResult.
        :type inspection_number: str
        """
        self._inspection_number = inspection_number

    @property
    def engine_number(self):
        """Gets the engine_number of this MvsInvoiceResult.

        发动机号码。 

        :return: The engine_number of this MvsInvoiceResult.
        :rtype: str
        """
        return self._engine_number

    @engine_number.setter
    def engine_number(self, engine_number):
        """Sets the engine_number of this MvsInvoiceResult.

        发动机号码。 

        :param engine_number: The engine_number of this MvsInvoiceResult.
        :type engine_number: str
        """
        self._engine_number = engine_number

    @property
    def vehicle_identification_number(self):
        """Gets the vehicle_identification_number of this MvsInvoiceResult.

        车辆识别代号/车架号码。 

        :return: The vehicle_identification_number of this MvsInvoiceResult.
        :rtype: str
        """
        return self._vehicle_identification_number

    @vehicle_identification_number.setter
    def vehicle_identification_number(self, vehicle_identification_number):
        """Sets the vehicle_identification_number of this MvsInvoiceResult.

        车辆识别代号/车架号码。 

        :param vehicle_identification_number: The vehicle_identification_number of this MvsInvoiceResult.
        :type vehicle_identification_number: str
        """
        self._vehicle_identification_number = vehicle_identification_number

    @property
    def tonnage(self):
        """Gets the tonnage of this MvsInvoiceResult.

        吨位。 

        :return: The tonnage of this MvsInvoiceResult.
        :rtype: str
        """
        return self._tonnage

    @tonnage.setter
    def tonnage(self, tonnage):
        """Sets the tonnage of this MvsInvoiceResult.

        吨位。 

        :param tonnage: The tonnage of this MvsInvoiceResult.
        :type tonnage: str
        """
        self._tonnage = tonnage

    @property
    def seating_capacity(self):
        """Gets the seating_capacity of this MvsInvoiceResult.

        限乘人数。 

        :return: The seating_capacity of this MvsInvoiceResult.
        :rtype: str
        """
        return self._seating_capacity

    @seating_capacity.setter
    def seating_capacity(self, seating_capacity):
        """Sets the seating_capacity of this MvsInvoiceResult.

        限乘人数。 

        :param seating_capacity: The seating_capacity of this MvsInvoiceResult.
        :type seating_capacity: str
        """
        self._seating_capacity = seating_capacity

    @property
    def tax_authority(self):
        """Gets the tax_authority of this MvsInvoiceResult.

        主管税务机关。 

        :return: The tax_authority of this MvsInvoiceResult.
        :rtype: str
        """
        return self._tax_authority

    @tax_authority.setter
    def tax_authority(self, tax_authority):
        """Sets the tax_authority of this MvsInvoiceResult.

        主管税务机关。 

        :param tax_authority: The tax_authority of this MvsInvoiceResult.
        :type tax_authority: str
        """
        self._tax_authority = tax_authority

    @property
    def tax_authority_code(self):
        """Gets the tax_authority_code of this MvsInvoiceResult.

        主管税务机关代码。 

        :return: The tax_authority_code of this MvsInvoiceResult.
        :rtype: str
        """
        return self._tax_authority_code

    @tax_authority_code.setter
    def tax_authority_code(self, tax_authority_code):
        """Sets the tax_authority_code of this MvsInvoiceResult.

        主管税务机关代码。 

        :param tax_authority_code: The tax_authority_code of this MvsInvoiceResult.
        :type tax_authority_code: str
        """
        self._tax_authority_code = tax_authority_code

    @property
    def tax_payment_receipt(self):
        """Gets the tax_payment_receipt of this MvsInvoiceResult.

        完税凭证号码。 

        :return: The tax_payment_receipt of this MvsInvoiceResult.
        :rtype: str
        """
        return self._tax_payment_receipt

    @tax_payment_receipt.setter
    def tax_payment_receipt(self, tax_payment_receipt):
        """Sets the tax_payment_receipt of this MvsInvoiceResult.

        完税凭证号码。 

        :param tax_payment_receipt: The tax_payment_receipt of this MvsInvoiceResult.
        :type tax_payment_receipt: str
        """
        self._tax_payment_receipt = tax_payment_receipt

    @property
    def tax_rate(self):
        """Gets the tax_rate of this MvsInvoiceResult.

        增值税税率或征收率。 

        :return: The tax_rate of this MvsInvoiceResult.
        :rtype: str
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this MvsInvoiceResult.

        增值税税率或征收率。 

        :param tax_rate: The tax_rate of this MvsInvoiceResult.
        :type tax_rate: str
        """
        self._tax_rate = tax_rate

    @property
    def tax(self):
        """Gets the tax of this MvsInvoiceResult.

        增值税税额。 

        :return: The tax of this MvsInvoiceResult.
        :rtype: str
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this MvsInvoiceResult.

        增值税税额。 

        :param tax: The tax of this MvsInvoiceResult.
        :type tax: str
        """
        self._tax = tax

    @property
    def tax_exclusive_price(self):
        """Gets the tax_exclusive_price of this MvsInvoiceResult.

        不含税价。 

        :return: The tax_exclusive_price of this MvsInvoiceResult.
        :rtype: str
        """
        return self._tax_exclusive_price

    @tax_exclusive_price.setter
    def tax_exclusive_price(self, tax_exclusive_price):
        """Sets the tax_exclusive_price of this MvsInvoiceResult.

        不含税价。 

        :param tax_exclusive_price: The tax_exclusive_price of this MvsInvoiceResult.
        :type tax_exclusive_price: str
        """
        self._tax_exclusive_price = tax_exclusive_price

    @property
    def total(self):
        """Gets the total of this MvsInvoiceResult.

        价税合计。 

        :return: The total of this MvsInvoiceResult.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this MvsInvoiceResult.

        价税合计。 

        :param total: The total of this MvsInvoiceResult.
        :type total: str
        """
        self._total = total

    @property
    def total_chinese(self):
        """Gets the total_chinese of this MvsInvoiceResult.

        价税合计大写。 

        :return: The total_chinese of this MvsInvoiceResult.
        :rtype: str
        """
        return self._total_chinese

    @total_chinese.setter
    def total_chinese(self, total_chinese):
        """Sets the total_chinese of this MvsInvoiceResult.

        价税合计大写。 

        :param total_chinese: The total_chinese of this MvsInvoiceResult.
        :type total_chinese: str
        """
        self._total_chinese = total_chinese

    @property
    def fiscal_code(self):
        """Gets the fiscal_code of this MvsInvoiceResult.

        税控码。 

        :return: The fiscal_code of this MvsInvoiceResult.
        :rtype: str
        """
        return self._fiscal_code

    @fiscal_code.setter
    def fiscal_code(self, fiscal_code):
        """Sets the fiscal_code of this MvsInvoiceResult.

        税控码。 

        :param fiscal_code: The fiscal_code of this MvsInvoiceResult.
        :type fiscal_code: str
        """
        self._fiscal_code = fiscal_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MvsInvoiceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
