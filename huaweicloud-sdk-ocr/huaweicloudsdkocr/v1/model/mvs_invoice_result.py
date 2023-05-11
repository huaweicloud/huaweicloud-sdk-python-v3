# coding: utf-8

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
        'buyer_address': 'str',
        'buyer_phone': 'str',
        'seller_name': 'str',
        'seller_phone': 'str',
        'seller_id': 'str',
        'seller_account': 'str',
        'seller_address': 'str',
        'licence_plate_number': 'str',
        'registration_number': 'str',
        'dept_motor_vehicles': 'str',
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
        'fiscal_code': 'str',
        'auction_org_name': 'str',
        'auction_org_address': 'str',
        'auction_org_id': 'str',
        'auction_org_bank_account': 'str',
        'auction_org_phone': 'str',
        'used_vehicle_market_name': 'str',
        'used_vehicle_market_id': 'str',
        'used_vehicle_market_address': 'str',
        'used_vehicle_market_bank_account': 'str',
        'used_vehicle_market_phone': 'str',
        'remark': 'str',
        'drawer_name': 'str',
        'type': 'str',
        'text_location': 'object',
        'confidence': 'object'
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
        'buyer_address': 'buyer_address',
        'buyer_phone': 'buyer_phone',
        'seller_name': 'seller_name',
        'seller_phone': 'seller_phone',
        'seller_id': 'seller_id',
        'seller_account': 'seller_account',
        'seller_address': 'seller_address',
        'licence_plate_number': 'licence_plate_number',
        'registration_number': 'registration_number',
        'dept_motor_vehicles': 'dept_motor_vehicles',
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
        'fiscal_code': 'fiscal_code',
        'auction_org_name': 'auction_org_name',
        'auction_org_address': 'auction_org_address',
        'auction_org_id': 'auction_org_id',
        'auction_org_bank_account': 'auction_org_bank_account',
        'auction_org_phone': 'auction_org_phone',
        'used_vehicle_market_name': 'used_vehicle_market_name',
        'used_vehicle_market_id': 'used_vehicle_market_id',
        'used_vehicle_market_address': 'used_vehicle_market_address',
        'used_vehicle_market_bank_account': 'used_vehicle_market_bank_account',
        'used_vehicle_market_phone': 'used_vehicle_market_phone',
        'remark': 'remark',
        'drawer_name': 'drawer_name',
        'type': 'type',
        'text_location': 'text_location',
        'confidence': 'confidence'
    }

    def __init__(self, code=None, number=None, machine_printed_code=None, machine_printed_number=None, issue_date=None, machine_number=None, buyer_name=None, buyer_organization_number=None, buyer_id=None, buyer_address=None, buyer_phone=None, seller_name=None, seller_phone=None, seller_id=None, seller_account=None, seller_address=None, licence_plate_number=None, registration_number=None, dept_motor_vehicles=None, seller_bank=None, vehicle_type=None, brand_model=None, manufacturing_location=None, quality_certificate=None, import_certificate=None, inspection_number=None, engine_number=None, vehicle_identification_number=None, tonnage=None, seating_capacity=None, tax_authority=None, tax_authority_code=None, tax_payment_receipt=None, tax_rate=None, tax=None, tax_exclusive_price=None, total=None, total_chinese=None, fiscal_code=None, auction_org_name=None, auction_org_address=None, auction_org_id=None, auction_org_bank_account=None, auction_org_phone=None, used_vehicle_market_name=None, used_vehicle_market_id=None, used_vehicle_market_address=None, used_vehicle_market_bank_account=None, used_vehicle_market_phone=None, remark=None, drawer_name=None, type=None, text_location=None, confidence=None):
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
        :param buyer_name: 购买方名称、二手车买方单位/个人 
        :type buyer_name: str
        :param buyer_organization_number: 购买方身份证号码/组织机构代码。 
        :type buyer_organization_number: str
        :param buyer_id: 购买方纳税人识别号、二手车买方单位代码/身份证号 
        :type buyer_id: str
        :param buyer_address: 二手车买方单位/个人住址。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type buyer_address: str
        :param buyer_phone: 二手车买方单位/个人电话。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type buyer_phone: str
        :param seller_name: 销货单位名称、二手车卖方单位/个人 
        :type seller_name: str
        :param seller_phone: 销售方电话、二手车卖方电话 
        :type seller_phone: str
        :param seller_id: 销售方纳税人识别号、二手车卖方单位代码/身份证号 
        :type seller_id: str
        :param seller_account: 销售方账号。 
        :type seller_account: str
        :param seller_address: 销售方地址、二手车卖方单位/个人地址 
        :type seller_address: str
        :param licence_plate_number: 二手车车牌照号。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type licence_plate_number: str
        :param registration_number: 二手车登记证号。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type registration_number: str
        :param dept_motor_vehicles: 二手车转入地车管所名称。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type dept_motor_vehicles: str
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
        :param total: 价税合计、二手车车价合计（小写） 
        :type total: str
        :param total_chinese: 价税合计大写、二手车车价合计（大写） 
        :type total_chinese: str
        :param fiscal_code: 税控码。 
        :type fiscal_code: str
        :param auction_org_name: 二手车经营拍卖单位名称。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type auction_org_name: str
        :param auction_org_address: 二手车经营拍卖单位地址。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type auction_org_address: str
        :param auction_org_id: 二手车经营拍卖单位纳税人识别号。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type auction_org_id: str
        :param auction_org_bank_account: 二手车经营拍卖单位银行和账号。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type auction_org_bank_account: str
        :param auction_org_phone: 二手车经营拍卖单位电话。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type auction_org_phone: str
        :param used_vehicle_market_name: 二手车市场名称。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type used_vehicle_market_name: str
        :param used_vehicle_market_id: 二手车市场纳税人识别号。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type used_vehicle_market_id: str
        :param used_vehicle_market_address: 二手车市场地址。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type used_vehicle_market_address: str
        :param used_vehicle_market_bank_account: 二手车市场银行和账号。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type used_vehicle_market_bank_account: str
        :param used_vehicle_market_phone: 二手车市场电话。 当请求参数\&quot;type\&quot;设置为\&quot;auto\&quot;或\&quot;used\&quot;时才返回。 
        :type used_vehicle_market_phone: str
        :param remark: 备注 
        :type remark: str
        :param drawer_name: 开票人 
        :type drawer_name: str
        :param type: 枚举值，机动车销售统一发票或者二手车销售统一发票。 当入参中包含type时返回。 
        :type type: str
        :param text_location: 检测框对象，内部为字段-框坐标对。如 code:[[x0, y0],[x1,y1],[x2,y2],[x3,y3]], 点的顺序是左上角、右上角、右下角、左下角。如果原图找不到字段，返回空列表。 
        :type text_location: object
        :param confidence: 字段文字内容置信度，内容为字段-字符置信度对,如code:0.9999。这个数值为字段中每个字符置信度，格式为fp32，保留四位。若字段不存在则返回0.0。 
        :type confidence: object
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
        self._buyer_address = None
        self._buyer_phone = None
        self._seller_name = None
        self._seller_phone = None
        self._seller_id = None
        self._seller_account = None
        self._seller_address = None
        self._licence_plate_number = None
        self._registration_number = None
        self._dept_motor_vehicles = None
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
        self._auction_org_name = None
        self._auction_org_address = None
        self._auction_org_id = None
        self._auction_org_bank_account = None
        self._auction_org_phone = None
        self._used_vehicle_market_name = None
        self._used_vehicle_market_id = None
        self._used_vehicle_market_address = None
        self._used_vehicle_market_bank_account = None
        self._used_vehicle_market_phone = None
        self._remark = None
        self._drawer_name = None
        self._type = None
        self._text_location = None
        self._confidence = None
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
        if buyer_address is not None:
            self.buyer_address = buyer_address
        if buyer_phone is not None:
            self.buyer_phone = buyer_phone
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
        if licence_plate_number is not None:
            self.licence_plate_number = licence_plate_number
        if registration_number is not None:
            self.registration_number = registration_number
        if dept_motor_vehicles is not None:
            self.dept_motor_vehicles = dept_motor_vehicles
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
        if auction_org_name is not None:
            self.auction_org_name = auction_org_name
        if auction_org_address is not None:
            self.auction_org_address = auction_org_address
        if auction_org_id is not None:
            self.auction_org_id = auction_org_id
        if auction_org_bank_account is not None:
            self.auction_org_bank_account = auction_org_bank_account
        if auction_org_phone is not None:
            self.auction_org_phone = auction_org_phone
        if used_vehicle_market_name is not None:
            self.used_vehicle_market_name = used_vehicle_market_name
        if used_vehicle_market_id is not None:
            self.used_vehicle_market_id = used_vehicle_market_id
        if used_vehicle_market_address is not None:
            self.used_vehicle_market_address = used_vehicle_market_address
        if used_vehicle_market_bank_account is not None:
            self.used_vehicle_market_bank_account = used_vehicle_market_bank_account
        if used_vehicle_market_phone is not None:
            self.used_vehicle_market_phone = used_vehicle_market_phone
        if remark is not None:
            self.remark = remark
        if drawer_name is not None:
            self.drawer_name = drawer_name
        if type is not None:
            self.type = type
        if text_location is not None:
            self.text_location = text_location
        if confidence is not None:
            self.confidence = confidence

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

        购买方名称、二手车买方单位/个人 

        :return: The buyer_name of this MvsInvoiceResult.
        :rtype: str
        """
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, buyer_name):
        """Sets the buyer_name of this MvsInvoiceResult.

        购买方名称、二手车买方单位/个人 

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

        购买方纳税人识别号、二手车买方单位代码/身份证号 

        :return: The buyer_id of this MvsInvoiceResult.
        :rtype: str
        """
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, buyer_id):
        """Sets the buyer_id of this MvsInvoiceResult.

        购买方纳税人识别号、二手车买方单位代码/身份证号 

        :param buyer_id: The buyer_id of this MvsInvoiceResult.
        :type buyer_id: str
        """
        self._buyer_id = buyer_id

    @property
    def buyer_address(self):
        """Gets the buyer_address of this MvsInvoiceResult.

        二手车买方单位/个人住址。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The buyer_address of this MvsInvoiceResult.
        :rtype: str
        """
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, buyer_address):
        """Sets the buyer_address of this MvsInvoiceResult.

        二手车买方单位/个人住址。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param buyer_address: The buyer_address of this MvsInvoiceResult.
        :type buyer_address: str
        """
        self._buyer_address = buyer_address

    @property
    def buyer_phone(self):
        """Gets the buyer_phone of this MvsInvoiceResult.

        二手车买方单位/个人电话。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The buyer_phone of this MvsInvoiceResult.
        :rtype: str
        """
        return self._buyer_phone

    @buyer_phone.setter
    def buyer_phone(self, buyer_phone):
        """Sets the buyer_phone of this MvsInvoiceResult.

        二手车买方单位/个人电话。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param buyer_phone: The buyer_phone of this MvsInvoiceResult.
        :type buyer_phone: str
        """
        self._buyer_phone = buyer_phone

    @property
    def seller_name(self):
        """Gets the seller_name of this MvsInvoiceResult.

        销货单位名称、二手车卖方单位/个人 

        :return: The seller_name of this MvsInvoiceResult.
        :rtype: str
        """
        return self._seller_name

    @seller_name.setter
    def seller_name(self, seller_name):
        """Sets the seller_name of this MvsInvoiceResult.

        销货单位名称、二手车卖方单位/个人 

        :param seller_name: The seller_name of this MvsInvoiceResult.
        :type seller_name: str
        """
        self._seller_name = seller_name

    @property
    def seller_phone(self):
        """Gets the seller_phone of this MvsInvoiceResult.

        销售方电话、二手车卖方电话 

        :return: The seller_phone of this MvsInvoiceResult.
        :rtype: str
        """
        return self._seller_phone

    @seller_phone.setter
    def seller_phone(self, seller_phone):
        """Sets the seller_phone of this MvsInvoiceResult.

        销售方电话、二手车卖方电话 

        :param seller_phone: The seller_phone of this MvsInvoiceResult.
        :type seller_phone: str
        """
        self._seller_phone = seller_phone

    @property
    def seller_id(self):
        """Gets the seller_id of this MvsInvoiceResult.

        销售方纳税人识别号、二手车卖方单位代码/身份证号 

        :return: The seller_id of this MvsInvoiceResult.
        :rtype: str
        """
        return self._seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        """Sets the seller_id of this MvsInvoiceResult.

        销售方纳税人识别号、二手车卖方单位代码/身份证号 

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

        销售方地址、二手车卖方单位/个人地址 

        :return: The seller_address of this MvsInvoiceResult.
        :rtype: str
        """
        return self._seller_address

    @seller_address.setter
    def seller_address(self, seller_address):
        """Sets the seller_address of this MvsInvoiceResult.

        销售方地址、二手车卖方单位/个人地址 

        :param seller_address: The seller_address of this MvsInvoiceResult.
        :type seller_address: str
        """
        self._seller_address = seller_address

    @property
    def licence_plate_number(self):
        """Gets the licence_plate_number of this MvsInvoiceResult.

        二手车车牌照号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The licence_plate_number of this MvsInvoiceResult.
        :rtype: str
        """
        return self._licence_plate_number

    @licence_plate_number.setter
    def licence_plate_number(self, licence_plate_number):
        """Sets the licence_plate_number of this MvsInvoiceResult.

        二手车车牌照号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param licence_plate_number: The licence_plate_number of this MvsInvoiceResult.
        :type licence_plate_number: str
        """
        self._licence_plate_number = licence_plate_number

    @property
    def registration_number(self):
        """Gets the registration_number of this MvsInvoiceResult.

        二手车登记证号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The registration_number of this MvsInvoiceResult.
        :rtype: str
        """
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number):
        """Sets the registration_number of this MvsInvoiceResult.

        二手车登记证号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param registration_number: The registration_number of this MvsInvoiceResult.
        :type registration_number: str
        """
        self._registration_number = registration_number

    @property
    def dept_motor_vehicles(self):
        """Gets the dept_motor_vehicles of this MvsInvoiceResult.

        二手车转入地车管所名称。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The dept_motor_vehicles of this MvsInvoiceResult.
        :rtype: str
        """
        return self._dept_motor_vehicles

    @dept_motor_vehicles.setter
    def dept_motor_vehicles(self, dept_motor_vehicles):
        """Sets the dept_motor_vehicles of this MvsInvoiceResult.

        二手车转入地车管所名称。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param dept_motor_vehicles: The dept_motor_vehicles of this MvsInvoiceResult.
        :type dept_motor_vehicles: str
        """
        self._dept_motor_vehicles = dept_motor_vehicles

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

        价税合计、二手车车价合计（小写） 

        :return: The total of this MvsInvoiceResult.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this MvsInvoiceResult.

        价税合计、二手车车价合计（小写） 

        :param total: The total of this MvsInvoiceResult.
        :type total: str
        """
        self._total = total

    @property
    def total_chinese(self):
        """Gets the total_chinese of this MvsInvoiceResult.

        价税合计大写、二手车车价合计（大写） 

        :return: The total_chinese of this MvsInvoiceResult.
        :rtype: str
        """
        return self._total_chinese

    @total_chinese.setter
    def total_chinese(self, total_chinese):
        """Sets the total_chinese of this MvsInvoiceResult.

        价税合计大写、二手车车价合计（大写） 

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

    @property
    def auction_org_name(self):
        """Gets the auction_org_name of this MvsInvoiceResult.

        二手车经营拍卖单位名称。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The auction_org_name of this MvsInvoiceResult.
        :rtype: str
        """
        return self._auction_org_name

    @auction_org_name.setter
    def auction_org_name(self, auction_org_name):
        """Sets the auction_org_name of this MvsInvoiceResult.

        二手车经营拍卖单位名称。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param auction_org_name: The auction_org_name of this MvsInvoiceResult.
        :type auction_org_name: str
        """
        self._auction_org_name = auction_org_name

    @property
    def auction_org_address(self):
        """Gets the auction_org_address of this MvsInvoiceResult.

        二手车经营拍卖单位地址。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The auction_org_address of this MvsInvoiceResult.
        :rtype: str
        """
        return self._auction_org_address

    @auction_org_address.setter
    def auction_org_address(self, auction_org_address):
        """Sets the auction_org_address of this MvsInvoiceResult.

        二手车经营拍卖单位地址。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param auction_org_address: The auction_org_address of this MvsInvoiceResult.
        :type auction_org_address: str
        """
        self._auction_org_address = auction_org_address

    @property
    def auction_org_id(self):
        """Gets the auction_org_id of this MvsInvoiceResult.

        二手车经营拍卖单位纳税人识别号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The auction_org_id of this MvsInvoiceResult.
        :rtype: str
        """
        return self._auction_org_id

    @auction_org_id.setter
    def auction_org_id(self, auction_org_id):
        """Sets the auction_org_id of this MvsInvoiceResult.

        二手车经营拍卖单位纳税人识别号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param auction_org_id: The auction_org_id of this MvsInvoiceResult.
        :type auction_org_id: str
        """
        self._auction_org_id = auction_org_id

    @property
    def auction_org_bank_account(self):
        """Gets the auction_org_bank_account of this MvsInvoiceResult.

        二手车经营拍卖单位银行和账号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The auction_org_bank_account of this MvsInvoiceResult.
        :rtype: str
        """
        return self._auction_org_bank_account

    @auction_org_bank_account.setter
    def auction_org_bank_account(self, auction_org_bank_account):
        """Sets the auction_org_bank_account of this MvsInvoiceResult.

        二手车经营拍卖单位银行和账号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param auction_org_bank_account: The auction_org_bank_account of this MvsInvoiceResult.
        :type auction_org_bank_account: str
        """
        self._auction_org_bank_account = auction_org_bank_account

    @property
    def auction_org_phone(self):
        """Gets the auction_org_phone of this MvsInvoiceResult.

        二手车经营拍卖单位电话。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The auction_org_phone of this MvsInvoiceResult.
        :rtype: str
        """
        return self._auction_org_phone

    @auction_org_phone.setter
    def auction_org_phone(self, auction_org_phone):
        """Sets the auction_org_phone of this MvsInvoiceResult.

        二手车经营拍卖单位电话。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param auction_org_phone: The auction_org_phone of this MvsInvoiceResult.
        :type auction_org_phone: str
        """
        self._auction_org_phone = auction_org_phone

    @property
    def used_vehicle_market_name(self):
        """Gets the used_vehicle_market_name of this MvsInvoiceResult.

        二手车市场名称。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The used_vehicle_market_name of this MvsInvoiceResult.
        :rtype: str
        """
        return self._used_vehicle_market_name

    @used_vehicle_market_name.setter
    def used_vehicle_market_name(self, used_vehicle_market_name):
        """Sets the used_vehicle_market_name of this MvsInvoiceResult.

        二手车市场名称。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param used_vehicle_market_name: The used_vehicle_market_name of this MvsInvoiceResult.
        :type used_vehicle_market_name: str
        """
        self._used_vehicle_market_name = used_vehicle_market_name

    @property
    def used_vehicle_market_id(self):
        """Gets the used_vehicle_market_id of this MvsInvoiceResult.

        二手车市场纳税人识别号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The used_vehicle_market_id of this MvsInvoiceResult.
        :rtype: str
        """
        return self._used_vehicle_market_id

    @used_vehicle_market_id.setter
    def used_vehicle_market_id(self, used_vehicle_market_id):
        """Sets the used_vehicle_market_id of this MvsInvoiceResult.

        二手车市场纳税人识别号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param used_vehicle_market_id: The used_vehicle_market_id of this MvsInvoiceResult.
        :type used_vehicle_market_id: str
        """
        self._used_vehicle_market_id = used_vehicle_market_id

    @property
    def used_vehicle_market_address(self):
        """Gets the used_vehicle_market_address of this MvsInvoiceResult.

        二手车市场地址。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The used_vehicle_market_address of this MvsInvoiceResult.
        :rtype: str
        """
        return self._used_vehicle_market_address

    @used_vehicle_market_address.setter
    def used_vehicle_market_address(self, used_vehicle_market_address):
        """Sets the used_vehicle_market_address of this MvsInvoiceResult.

        二手车市场地址。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param used_vehicle_market_address: The used_vehicle_market_address of this MvsInvoiceResult.
        :type used_vehicle_market_address: str
        """
        self._used_vehicle_market_address = used_vehicle_market_address

    @property
    def used_vehicle_market_bank_account(self):
        """Gets the used_vehicle_market_bank_account of this MvsInvoiceResult.

        二手车市场银行和账号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The used_vehicle_market_bank_account of this MvsInvoiceResult.
        :rtype: str
        """
        return self._used_vehicle_market_bank_account

    @used_vehicle_market_bank_account.setter
    def used_vehicle_market_bank_account(self, used_vehicle_market_bank_account):
        """Sets the used_vehicle_market_bank_account of this MvsInvoiceResult.

        二手车市场银行和账号。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param used_vehicle_market_bank_account: The used_vehicle_market_bank_account of this MvsInvoiceResult.
        :type used_vehicle_market_bank_account: str
        """
        self._used_vehicle_market_bank_account = used_vehicle_market_bank_account

    @property
    def used_vehicle_market_phone(self):
        """Gets the used_vehicle_market_phone of this MvsInvoiceResult.

        二手车市场电话。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :return: The used_vehicle_market_phone of this MvsInvoiceResult.
        :rtype: str
        """
        return self._used_vehicle_market_phone

    @used_vehicle_market_phone.setter
    def used_vehicle_market_phone(self, used_vehicle_market_phone):
        """Sets the used_vehicle_market_phone of this MvsInvoiceResult.

        二手车市场电话。 当请求参数\"type\"设置为\"auto\"或\"used\"时才返回。 

        :param used_vehicle_market_phone: The used_vehicle_market_phone of this MvsInvoiceResult.
        :type used_vehicle_market_phone: str
        """
        self._used_vehicle_market_phone = used_vehicle_market_phone

    @property
    def remark(self):
        """Gets the remark of this MvsInvoiceResult.

        备注 

        :return: The remark of this MvsInvoiceResult.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this MvsInvoiceResult.

        备注 

        :param remark: The remark of this MvsInvoiceResult.
        :type remark: str
        """
        self._remark = remark

    @property
    def drawer_name(self):
        """Gets the drawer_name of this MvsInvoiceResult.

        开票人 

        :return: The drawer_name of this MvsInvoiceResult.
        :rtype: str
        """
        return self._drawer_name

    @drawer_name.setter
    def drawer_name(self, drawer_name):
        """Sets the drawer_name of this MvsInvoiceResult.

        开票人 

        :param drawer_name: The drawer_name of this MvsInvoiceResult.
        :type drawer_name: str
        """
        self._drawer_name = drawer_name

    @property
    def type(self):
        """Gets the type of this MvsInvoiceResult.

        枚举值，机动车销售统一发票或者二手车销售统一发票。 当入参中包含type时返回。 

        :return: The type of this MvsInvoiceResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MvsInvoiceResult.

        枚举值，机动车销售统一发票或者二手车销售统一发票。 当入参中包含type时返回。 

        :param type: The type of this MvsInvoiceResult.
        :type type: str
        """
        self._type = type

    @property
    def text_location(self):
        """Gets the text_location of this MvsInvoiceResult.

        检测框对象，内部为字段-框坐标对。如 code:[[x0, y0],[x1,y1],[x2,y2],[x3,y3]], 点的顺序是左上角、右上角、右下角、左下角。如果原图找不到字段，返回空列表。 

        :return: The text_location of this MvsInvoiceResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        """Sets the text_location of this MvsInvoiceResult.

        检测框对象，内部为字段-框坐标对。如 code:[[x0, y0],[x1,y1],[x2,y2],[x3,y3]], 点的顺序是左上角、右上角、右下角、左下角。如果原图找不到字段，返回空列表。 

        :param text_location: The text_location of this MvsInvoiceResult.
        :type text_location: object
        """
        self._text_location = text_location

    @property
    def confidence(self):
        """Gets the confidence of this MvsInvoiceResult.

        字段文字内容置信度，内容为字段-字符置信度对,如code:0.9999。这个数值为字段中每个字符置信度，格式为fp32，保留四位。若字段不存在则返回0.0。 

        :return: The confidence of this MvsInvoiceResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this MvsInvoiceResult.

        字段文字内容置信度，内容为字段-字符置信度对,如code:0.9999。这个数值为字段中每个字符置信度，格式为fp32，保留四位。若字段不存在则返回0.0。 

        :param confidence: The confidence of this MvsInvoiceResult.
        :type confidence: object
        """
        self._confidence = confidence

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
