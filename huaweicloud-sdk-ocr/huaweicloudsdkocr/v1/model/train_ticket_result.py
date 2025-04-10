# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrainTicketResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_id': 'str',
        'check_port': 'str',
        'train_number': 'str',
        'departure_station': 'str',
        'destination_station': 'str',
        'departure_station_en': 'str',
        'destination_station_en': 'str',
        'departure_time': 'str',
        'seat_number': 'str',
        'ticket_price': 'str',
        'sale_method': 'str',
        'seat_category': 'str',
        'ticket_changing': 'str',
        'id_number': 'str',
        'name': 'str',
        'log_id': 'str',
        'sale_location': 'str',
        'invoice_style': 'str',
        'issue_date': 'str',
        'discount_mark': 'str',
        'serial_number': 'str',
        'tax_amount': 'str',
        'tax_rate': 'str',
        'air_conditioning': 'str',
        'original_invoice_number': 'str',
        'unified_social_credit_code': 'str',
        'buyer_name': 'str',
        'total_amount_excluding_tax': 'str',
        'invoice_number': 'str',
        'seal_mark': 'bool',
        'title': 'str',
        'area': 'str',
        'receipt_number': 'str',
        'amount_in_figures': 'str',
        'amount_in_words': 'str',
        'confidence': 'object',
        'text_location': 'object'
    }

    attribute_map = {
        'ticket_id': 'ticket_id',
        'check_port': 'check_port',
        'train_number': 'train_number',
        'departure_station': 'departure_station',
        'destination_station': 'destination_station',
        'departure_station_en': 'departure_station_en',
        'destination_station_en': 'destination_station_en',
        'departure_time': 'departure_time',
        'seat_number': 'seat_number',
        'ticket_price': 'ticket_price',
        'sale_method': 'sale_method',
        'seat_category': 'seat_category',
        'ticket_changing': 'ticket_changing',
        'id_number': 'id_number',
        'name': 'name',
        'log_id': 'log_id',
        'sale_location': 'sale_location',
        'invoice_style': 'invoice_style',
        'issue_date': 'issue_date',
        'discount_mark': 'discount_mark',
        'serial_number': 'serial_number',
        'tax_amount': 'tax_amount',
        'tax_rate': 'tax_rate',
        'air_conditioning': 'air_conditioning',
        'original_invoice_number': 'original_invoice_number',
        'unified_social_credit_code': 'unified_social_credit_code',
        'buyer_name': 'buyer_name',
        'total_amount_excluding_tax': 'total_amount_excluding_tax',
        'invoice_number': 'invoice_number',
        'seal_mark': 'seal_mark',
        'title': 'title',
        'area': 'area',
        'receipt_number': 'receipt_number',
        'amount_in_figures': 'amount_in_figures',
        'amount_in_words': 'amount_in_words',
        'confidence': 'confidence',
        'text_location': 'text_location'
    }

    def __init__(self, ticket_id=None, check_port=None, train_number=None, departure_station=None, destination_station=None, departure_station_en=None, destination_station_en=None, departure_time=None, seat_number=None, ticket_price=None, sale_method=None, seat_category=None, ticket_changing=None, id_number=None, name=None, log_id=None, sale_location=None, invoice_style=None, issue_date=None, discount_mark=None, serial_number=None, tax_amount=None, tax_rate=None, air_conditioning=None, original_invoice_number=None, unified_social_credit_code=None, buyer_name=None, total_amount_excluding_tax=None, invoice_number=None, seal_mark=None, title=None, area=None, receipt_number=None, amount_in_figures=None, amount_in_words=None, confidence=None, text_location=None):
        r"""TrainTicketResult

        The model defined in huaweicloud sdk

        :param ticket_id: 火车票左上角的车票ID。 
        :type ticket_id: str
        :param check_port: 检票口信息。 
        :type check_port: str
        :param train_number: 车次。 
        :type train_number: str
        :param departure_station: 始发站。 
        :type departure_station: str
        :param destination_station: 终点站。 
        :type destination_station: str
        :param departure_station_en: 始发站拼音。 
        :type departure_station_en: str
        :param destination_station_en: 终点站拼音。 
        :type destination_station_en: str
        :param departure_time: 开车时间。 
        :type departure_time: str
        :param seat_number: 座位号。 
        :type seat_number: str
        :param ticket_price: 票价，当为退票凭证时，表示退票费。 
        :type ticket_price: str
        :param sale_method: 售票方式。 
        :type sale_method: str
        :param seat_category: 座位类别。 
        :type seat_category: str
        :param ticket_changing: 标识信息，包含始发改签、退票、差额退票等。 
        :type ticket_changing: str
        :param id_number: 车票持有人的身份证号。 
        :type id_number: str
        :param name: 车票持有人姓名。 
        :type name: str
        :param log_id: 车票最下方的序列号。 
        :type log_id: str
        :param sale_location: 车票售票地点。 
        :type sale_location: str
        :param invoice_style: 类型。包含以下几种类型： - paper：纸质火车票 - electronic：铁路电子客票 - refund_old：退票费报销凭证 - refund_new：纸质火车票退票凭证  - refund_electronic：铁路电子客票退票凭证 
        :type invoice_style: str
        :param issue_date: 开票时间 
        :type issue_date: str
        :param discount_mark: 打折标识 
        :type discount_mark: str
        :param serial_number: 电子客票号 
        :type serial_number: str
        :param tax_amount: 税金价格 
        :type tax_amount: str
        :param tax_rate: 税率 
        :type tax_rate: str
        :param air_conditioning: 是否是空调车厢 
        :type air_conditioning: str
        :param original_invoice_number: 原发票号码 
        :type original_invoice_number: str
        :param unified_social_credit_code: 统一社会信用号码 
        :type unified_social_credit_code: str
        :param buyer_name: 购买方名称 
        :type buyer_name: str
        :param total_amount_excluding_tax: 不含税价格 
        :type total_amount_excluding_tax: str
        :param invoice_number: 发票号码 
        :type invoice_number: str
        :param seal_mark: 是否有印章，True表示有印章，False表示不含印章，字段默认为False 
        :type seal_mark: bool
        :param title: 标题 
        :type title: str
        :param area: 地区 
        :type area: str
        :param receipt_number: 收据编码 
        :type receipt_number: str
        :param amount_in_figures: 小写票据金额 
        :type amount_in_figures: str
        :param amount_in_words: 大写票据金额 
        :type amount_in_words: str
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。
        :type confidence: object
        :param text_location: 对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。  &gt; 说明：输入数据格式是OFD时，返回的字段坐标为空列表。 
        :type text_location: object
        """
        
        

        self._ticket_id = None
        self._check_port = None
        self._train_number = None
        self._departure_station = None
        self._destination_station = None
        self._departure_station_en = None
        self._destination_station_en = None
        self._departure_time = None
        self._seat_number = None
        self._ticket_price = None
        self._sale_method = None
        self._seat_category = None
        self._ticket_changing = None
        self._id_number = None
        self._name = None
        self._log_id = None
        self._sale_location = None
        self._invoice_style = None
        self._issue_date = None
        self._discount_mark = None
        self._serial_number = None
        self._tax_amount = None
        self._tax_rate = None
        self._air_conditioning = None
        self._original_invoice_number = None
        self._unified_social_credit_code = None
        self._buyer_name = None
        self._total_amount_excluding_tax = None
        self._invoice_number = None
        self._seal_mark = None
        self._title = None
        self._area = None
        self._receipt_number = None
        self._amount_in_figures = None
        self._amount_in_words = None
        self._confidence = None
        self._text_location = None
        self.discriminator = None

        if ticket_id is not None:
            self.ticket_id = ticket_id
        if check_port is not None:
            self.check_port = check_port
        if train_number is not None:
            self.train_number = train_number
        if departure_station is not None:
            self.departure_station = departure_station
        if destination_station is not None:
            self.destination_station = destination_station
        if departure_station_en is not None:
            self.departure_station_en = departure_station_en
        if destination_station_en is not None:
            self.destination_station_en = destination_station_en
        if departure_time is not None:
            self.departure_time = departure_time
        if seat_number is not None:
            self.seat_number = seat_number
        if ticket_price is not None:
            self.ticket_price = ticket_price
        if sale_method is not None:
            self.sale_method = sale_method
        if seat_category is not None:
            self.seat_category = seat_category
        if ticket_changing is not None:
            self.ticket_changing = ticket_changing
        if id_number is not None:
            self.id_number = id_number
        if name is not None:
            self.name = name
        if log_id is not None:
            self.log_id = log_id
        if sale_location is not None:
            self.sale_location = sale_location
        if invoice_style is not None:
            self.invoice_style = invoice_style
        if issue_date is not None:
            self.issue_date = issue_date
        if discount_mark is not None:
            self.discount_mark = discount_mark
        if serial_number is not None:
            self.serial_number = serial_number
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if air_conditioning is not None:
            self.air_conditioning = air_conditioning
        if original_invoice_number is not None:
            self.original_invoice_number = original_invoice_number
        if unified_social_credit_code is not None:
            self.unified_social_credit_code = unified_social_credit_code
        if buyer_name is not None:
            self.buyer_name = buyer_name
        if total_amount_excluding_tax is not None:
            self.total_amount_excluding_tax = total_amount_excluding_tax
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if seal_mark is not None:
            self.seal_mark = seal_mark
        if title is not None:
            self.title = title
        if area is not None:
            self.area = area
        if receipt_number is not None:
            self.receipt_number = receipt_number
        if amount_in_figures is not None:
            self.amount_in_figures = amount_in_figures
        if amount_in_words is not None:
            self.amount_in_words = amount_in_words
        if confidence is not None:
            self.confidence = confidence
        if text_location is not None:
            self.text_location = text_location

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this TrainTicketResult.

        火车票左上角的车票ID。 

        :return: The ticket_id of this TrainTicketResult.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this TrainTicketResult.

        火车票左上角的车票ID。 

        :param ticket_id: The ticket_id of this TrainTicketResult.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def check_port(self):
        r"""Gets the check_port of this TrainTicketResult.

        检票口信息。 

        :return: The check_port of this TrainTicketResult.
        :rtype: str
        """
        return self._check_port

    @check_port.setter
    def check_port(self, check_port):
        r"""Sets the check_port of this TrainTicketResult.

        检票口信息。 

        :param check_port: The check_port of this TrainTicketResult.
        :type check_port: str
        """
        self._check_port = check_port

    @property
    def train_number(self):
        r"""Gets the train_number of this TrainTicketResult.

        车次。 

        :return: The train_number of this TrainTicketResult.
        :rtype: str
        """
        return self._train_number

    @train_number.setter
    def train_number(self, train_number):
        r"""Sets the train_number of this TrainTicketResult.

        车次。 

        :param train_number: The train_number of this TrainTicketResult.
        :type train_number: str
        """
        self._train_number = train_number

    @property
    def departure_station(self):
        r"""Gets the departure_station of this TrainTicketResult.

        始发站。 

        :return: The departure_station of this TrainTicketResult.
        :rtype: str
        """
        return self._departure_station

    @departure_station.setter
    def departure_station(self, departure_station):
        r"""Sets the departure_station of this TrainTicketResult.

        始发站。 

        :param departure_station: The departure_station of this TrainTicketResult.
        :type departure_station: str
        """
        self._departure_station = departure_station

    @property
    def destination_station(self):
        r"""Gets the destination_station of this TrainTicketResult.

        终点站。 

        :return: The destination_station of this TrainTicketResult.
        :rtype: str
        """
        return self._destination_station

    @destination_station.setter
    def destination_station(self, destination_station):
        r"""Sets the destination_station of this TrainTicketResult.

        终点站。 

        :param destination_station: The destination_station of this TrainTicketResult.
        :type destination_station: str
        """
        self._destination_station = destination_station

    @property
    def departure_station_en(self):
        r"""Gets the departure_station_en of this TrainTicketResult.

        始发站拼音。 

        :return: The departure_station_en of this TrainTicketResult.
        :rtype: str
        """
        return self._departure_station_en

    @departure_station_en.setter
    def departure_station_en(self, departure_station_en):
        r"""Sets the departure_station_en of this TrainTicketResult.

        始发站拼音。 

        :param departure_station_en: The departure_station_en of this TrainTicketResult.
        :type departure_station_en: str
        """
        self._departure_station_en = departure_station_en

    @property
    def destination_station_en(self):
        r"""Gets the destination_station_en of this TrainTicketResult.

        终点站拼音。 

        :return: The destination_station_en of this TrainTicketResult.
        :rtype: str
        """
        return self._destination_station_en

    @destination_station_en.setter
    def destination_station_en(self, destination_station_en):
        r"""Sets the destination_station_en of this TrainTicketResult.

        终点站拼音。 

        :param destination_station_en: The destination_station_en of this TrainTicketResult.
        :type destination_station_en: str
        """
        self._destination_station_en = destination_station_en

    @property
    def departure_time(self):
        r"""Gets the departure_time of this TrainTicketResult.

        开车时间。 

        :return: The departure_time of this TrainTicketResult.
        :rtype: str
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        r"""Sets the departure_time of this TrainTicketResult.

        开车时间。 

        :param departure_time: The departure_time of this TrainTicketResult.
        :type departure_time: str
        """
        self._departure_time = departure_time

    @property
    def seat_number(self):
        r"""Gets the seat_number of this TrainTicketResult.

        座位号。 

        :return: The seat_number of this TrainTicketResult.
        :rtype: str
        """
        return self._seat_number

    @seat_number.setter
    def seat_number(self, seat_number):
        r"""Sets the seat_number of this TrainTicketResult.

        座位号。 

        :param seat_number: The seat_number of this TrainTicketResult.
        :type seat_number: str
        """
        self._seat_number = seat_number

    @property
    def ticket_price(self):
        r"""Gets the ticket_price of this TrainTicketResult.

        票价，当为退票凭证时，表示退票费。 

        :return: The ticket_price of this TrainTicketResult.
        :rtype: str
        """
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, ticket_price):
        r"""Sets the ticket_price of this TrainTicketResult.

        票价，当为退票凭证时，表示退票费。 

        :param ticket_price: The ticket_price of this TrainTicketResult.
        :type ticket_price: str
        """
        self._ticket_price = ticket_price

    @property
    def sale_method(self):
        r"""Gets the sale_method of this TrainTicketResult.

        售票方式。 

        :return: The sale_method of this TrainTicketResult.
        :rtype: str
        """
        return self._sale_method

    @sale_method.setter
    def sale_method(self, sale_method):
        r"""Sets the sale_method of this TrainTicketResult.

        售票方式。 

        :param sale_method: The sale_method of this TrainTicketResult.
        :type sale_method: str
        """
        self._sale_method = sale_method

    @property
    def seat_category(self):
        r"""Gets the seat_category of this TrainTicketResult.

        座位类别。 

        :return: The seat_category of this TrainTicketResult.
        :rtype: str
        """
        return self._seat_category

    @seat_category.setter
    def seat_category(self, seat_category):
        r"""Sets the seat_category of this TrainTicketResult.

        座位类别。 

        :param seat_category: The seat_category of this TrainTicketResult.
        :type seat_category: str
        """
        self._seat_category = seat_category

    @property
    def ticket_changing(self):
        r"""Gets the ticket_changing of this TrainTicketResult.

        标识信息，包含始发改签、退票、差额退票等。 

        :return: The ticket_changing of this TrainTicketResult.
        :rtype: str
        """
        return self._ticket_changing

    @ticket_changing.setter
    def ticket_changing(self, ticket_changing):
        r"""Sets the ticket_changing of this TrainTicketResult.

        标识信息，包含始发改签、退票、差额退票等。 

        :param ticket_changing: The ticket_changing of this TrainTicketResult.
        :type ticket_changing: str
        """
        self._ticket_changing = ticket_changing

    @property
    def id_number(self):
        r"""Gets the id_number of this TrainTicketResult.

        车票持有人的身份证号。 

        :return: The id_number of this TrainTicketResult.
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        r"""Sets the id_number of this TrainTicketResult.

        车票持有人的身份证号。 

        :param id_number: The id_number of this TrainTicketResult.
        :type id_number: str
        """
        self._id_number = id_number

    @property
    def name(self):
        r"""Gets the name of this TrainTicketResult.

        车票持有人姓名。 

        :return: The name of this TrainTicketResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TrainTicketResult.

        车票持有人姓名。 

        :param name: The name of this TrainTicketResult.
        :type name: str
        """
        self._name = name

    @property
    def log_id(self):
        r"""Gets the log_id of this TrainTicketResult.

        车票最下方的序列号。 

        :return: The log_id of this TrainTicketResult.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        r"""Sets the log_id of this TrainTicketResult.

        车票最下方的序列号。 

        :param log_id: The log_id of this TrainTicketResult.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def sale_location(self):
        r"""Gets the sale_location of this TrainTicketResult.

        车票售票地点。 

        :return: The sale_location of this TrainTicketResult.
        :rtype: str
        """
        return self._sale_location

    @sale_location.setter
    def sale_location(self, sale_location):
        r"""Sets the sale_location of this TrainTicketResult.

        车票售票地点。 

        :param sale_location: The sale_location of this TrainTicketResult.
        :type sale_location: str
        """
        self._sale_location = sale_location

    @property
    def invoice_style(self):
        r"""Gets the invoice_style of this TrainTicketResult.

        类型。包含以下几种类型： - paper：纸质火车票 - electronic：铁路电子客票 - refund_old：退票费报销凭证 - refund_new：纸质火车票退票凭证  - refund_electronic：铁路电子客票退票凭证 

        :return: The invoice_style of this TrainTicketResult.
        :rtype: str
        """
        return self._invoice_style

    @invoice_style.setter
    def invoice_style(self, invoice_style):
        r"""Sets the invoice_style of this TrainTicketResult.

        类型。包含以下几种类型： - paper：纸质火车票 - electronic：铁路电子客票 - refund_old：退票费报销凭证 - refund_new：纸质火车票退票凭证  - refund_electronic：铁路电子客票退票凭证 

        :param invoice_style: The invoice_style of this TrainTicketResult.
        :type invoice_style: str
        """
        self._invoice_style = invoice_style

    @property
    def issue_date(self):
        r"""Gets the issue_date of this TrainTicketResult.

        开票时间 

        :return: The issue_date of this TrainTicketResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this TrainTicketResult.

        开票时间 

        :param issue_date: The issue_date of this TrainTicketResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def discount_mark(self):
        r"""Gets the discount_mark of this TrainTicketResult.

        打折标识 

        :return: The discount_mark of this TrainTicketResult.
        :rtype: str
        """
        return self._discount_mark

    @discount_mark.setter
    def discount_mark(self, discount_mark):
        r"""Sets the discount_mark of this TrainTicketResult.

        打折标识 

        :param discount_mark: The discount_mark of this TrainTicketResult.
        :type discount_mark: str
        """
        self._discount_mark = discount_mark

    @property
    def serial_number(self):
        r"""Gets the serial_number of this TrainTicketResult.

        电子客票号 

        :return: The serial_number of this TrainTicketResult.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this TrainTicketResult.

        电子客票号 

        :param serial_number: The serial_number of this TrainTicketResult.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def tax_amount(self):
        r"""Gets the tax_amount of this TrainTicketResult.

        税金价格 

        :return: The tax_amount of this TrainTicketResult.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        r"""Sets the tax_amount of this TrainTicketResult.

        税金价格 

        :param tax_amount: The tax_amount of this TrainTicketResult.
        :type tax_amount: str
        """
        self._tax_amount = tax_amount

    @property
    def tax_rate(self):
        r"""Gets the tax_rate of this TrainTicketResult.

        税率 

        :return: The tax_rate of this TrainTicketResult.
        :rtype: str
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        r"""Sets the tax_rate of this TrainTicketResult.

        税率 

        :param tax_rate: The tax_rate of this TrainTicketResult.
        :type tax_rate: str
        """
        self._tax_rate = tax_rate

    @property
    def air_conditioning(self):
        r"""Gets the air_conditioning of this TrainTicketResult.

        是否是空调车厢 

        :return: The air_conditioning of this TrainTicketResult.
        :rtype: str
        """
        return self._air_conditioning

    @air_conditioning.setter
    def air_conditioning(self, air_conditioning):
        r"""Sets the air_conditioning of this TrainTicketResult.

        是否是空调车厢 

        :param air_conditioning: The air_conditioning of this TrainTicketResult.
        :type air_conditioning: str
        """
        self._air_conditioning = air_conditioning

    @property
    def original_invoice_number(self):
        r"""Gets the original_invoice_number of this TrainTicketResult.

        原发票号码 

        :return: The original_invoice_number of this TrainTicketResult.
        :rtype: str
        """
        return self._original_invoice_number

    @original_invoice_number.setter
    def original_invoice_number(self, original_invoice_number):
        r"""Sets the original_invoice_number of this TrainTicketResult.

        原发票号码 

        :param original_invoice_number: The original_invoice_number of this TrainTicketResult.
        :type original_invoice_number: str
        """
        self._original_invoice_number = original_invoice_number

    @property
    def unified_social_credit_code(self):
        r"""Gets the unified_social_credit_code of this TrainTicketResult.

        统一社会信用号码 

        :return: The unified_social_credit_code of this TrainTicketResult.
        :rtype: str
        """
        return self._unified_social_credit_code

    @unified_social_credit_code.setter
    def unified_social_credit_code(self, unified_social_credit_code):
        r"""Sets the unified_social_credit_code of this TrainTicketResult.

        统一社会信用号码 

        :param unified_social_credit_code: The unified_social_credit_code of this TrainTicketResult.
        :type unified_social_credit_code: str
        """
        self._unified_social_credit_code = unified_social_credit_code

    @property
    def buyer_name(self):
        r"""Gets the buyer_name of this TrainTicketResult.

        购买方名称 

        :return: The buyer_name of this TrainTicketResult.
        :rtype: str
        """
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, buyer_name):
        r"""Sets the buyer_name of this TrainTicketResult.

        购买方名称 

        :param buyer_name: The buyer_name of this TrainTicketResult.
        :type buyer_name: str
        """
        self._buyer_name = buyer_name

    @property
    def total_amount_excluding_tax(self):
        r"""Gets the total_amount_excluding_tax of this TrainTicketResult.

        不含税价格 

        :return: The total_amount_excluding_tax of this TrainTicketResult.
        :rtype: str
        """
        return self._total_amount_excluding_tax

    @total_amount_excluding_tax.setter
    def total_amount_excluding_tax(self, total_amount_excluding_tax):
        r"""Sets the total_amount_excluding_tax of this TrainTicketResult.

        不含税价格 

        :param total_amount_excluding_tax: The total_amount_excluding_tax of this TrainTicketResult.
        :type total_amount_excluding_tax: str
        """
        self._total_amount_excluding_tax = total_amount_excluding_tax

    @property
    def invoice_number(self):
        r"""Gets the invoice_number of this TrainTicketResult.

        发票号码 

        :return: The invoice_number of this TrainTicketResult.
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        r"""Sets the invoice_number of this TrainTicketResult.

        发票号码 

        :param invoice_number: The invoice_number of this TrainTicketResult.
        :type invoice_number: str
        """
        self._invoice_number = invoice_number

    @property
    def seal_mark(self):
        r"""Gets the seal_mark of this TrainTicketResult.

        是否有印章，True表示有印章，False表示不含印章，字段默认为False 

        :return: The seal_mark of this TrainTicketResult.
        :rtype: bool
        """
        return self._seal_mark

    @seal_mark.setter
    def seal_mark(self, seal_mark):
        r"""Sets the seal_mark of this TrainTicketResult.

        是否有印章，True表示有印章，False表示不含印章，字段默认为False 

        :param seal_mark: The seal_mark of this TrainTicketResult.
        :type seal_mark: bool
        """
        self._seal_mark = seal_mark

    @property
    def title(self):
        r"""Gets the title of this TrainTicketResult.

        标题 

        :return: The title of this TrainTicketResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this TrainTicketResult.

        标题 

        :param title: The title of this TrainTicketResult.
        :type title: str
        """
        self._title = title

    @property
    def area(self):
        r"""Gets the area of this TrainTicketResult.

        地区 

        :return: The area of this TrainTicketResult.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        r"""Sets the area of this TrainTicketResult.

        地区 

        :param area: The area of this TrainTicketResult.
        :type area: str
        """
        self._area = area

    @property
    def receipt_number(self):
        r"""Gets the receipt_number of this TrainTicketResult.

        收据编码 

        :return: The receipt_number of this TrainTicketResult.
        :rtype: str
        """
        return self._receipt_number

    @receipt_number.setter
    def receipt_number(self, receipt_number):
        r"""Sets the receipt_number of this TrainTicketResult.

        收据编码 

        :param receipt_number: The receipt_number of this TrainTicketResult.
        :type receipt_number: str
        """
        self._receipt_number = receipt_number

    @property
    def amount_in_figures(self):
        r"""Gets the amount_in_figures of this TrainTicketResult.

        小写票据金额 

        :return: The amount_in_figures of this TrainTicketResult.
        :rtype: str
        """
        return self._amount_in_figures

    @amount_in_figures.setter
    def amount_in_figures(self, amount_in_figures):
        r"""Sets the amount_in_figures of this TrainTicketResult.

        小写票据金额 

        :param amount_in_figures: The amount_in_figures of this TrainTicketResult.
        :type amount_in_figures: str
        """
        self._amount_in_figures = amount_in_figures

    @property
    def amount_in_words(self):
        r"""Gets the amount_in_words of this TrainTicketResult.

        大写票据金额 

        :return: The amount_in_words of this TrainTicketResult.
        :rtype: str
        """
        return self._amount_in_words

    @amount_in_words.setter
    def amount_in_words(self, amount_in_words):
        r"""Sets the amount_in_words of this TrainTicketResult.

        大写票据金额 

        :param amount_in_words: The amount_in_words of this TrainTicketResult.
        :type amount_in_words: str
        """
        self._amount_in_words = amount_in_words

    @property
    def confidence(self):
        r"""Gets the confidence of this TrainTicketResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。

        :return: The confidence of this TrainTicketResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this TrainTicketResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。

        :param confidence: The confidence of this TrainTicketResult.
        :type confidence: object
        """
        self._confidence = confidence

    @property
    def text_location(self):
        r"""Gets the text_location of this TrainTicketResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。  > 说明：输入数据格式是OFD时，返回的字段坐标为空列表。 

        :return: The text_location of this TrainTicketResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        r"""Sets the text_location of this TrainTicketResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。  > 说明：输入数据格式是OFD时，返回的字段坐标为空列表。 

        :param text_location: The text_location of this TrainTicketResult.
        :type text_location: object
        """
        self._text_location = text_location

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
        if not isinstance(other, TrainTicketResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
