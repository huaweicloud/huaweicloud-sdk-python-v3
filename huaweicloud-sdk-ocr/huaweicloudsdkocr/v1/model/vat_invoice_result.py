# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VatInvoiceResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'type': 'str',
        'invoice_tag': 'str',
        'sum_amount': 'str',
        'sum_tax': 'str',
        'serial_number': 'str',
        'attribution': 'str',
        'supervision_seal': 'list[str]',
        'code': 'str',
        'print_code': 'str',
        'machine_number': 'str',
        'print_number': 'str',
        'check_code': 'str',
        'number': 'str',
        'issue_date': 'str',
        'encryption_block': 'str',
        'buyer_name': 'str',
        'buyer_id': 'str',
        'buyer_address': 'str',
        'buyer_bank': 'str',
        'seller_name': 'str',
        'seller_id': 'str',
        'seller_address': 'str',
        'seller_bank': 'str',
        'subtotal_amount': 'str',
        'subtotal_tax': 'str',
        'total': 'str',
        'total_in_words': 'str',
        'remarks': 'str',
        'receiver': 'str',
        'reviewer': 'str',
        'issuer': 'str',
        'seller_seal': 'list[str]',
        'item_list': 'list[ItemList]',
        'province': 'str',
        'city': 'str',
        'confidence': 'object',
        'text_location': 'object',
        'belong_buyer_name': 'str',
        'belong_seller_name': 'str',
        'belong_vat_code': 'str',
        'belong_number': 'str',
        'belong_pages': 'str',
        'belong_current_page': 'str',
        'belong_remarks': 'str',
        'belong_issue_date': 'str',
        'sales_mark': 'bool',
        'belong_sum_amount': 'str',
        'belong_sum_tax': 'str',
        'belong_subtotal_amount': 'str',
        'belong_subtotal_tax': 'str',
        'belong_discount_amount': 'str',
        'belong_discount_tax': 'str',
        'belong_item_list': 'list[BelongItemList]',
        'passenger_travel_item_list': 'list[PassengerTravelItemList]'
    }

    attribute_map = {
        'title': 'title',
        'type': 'type',
        'invoice_tag': 'invoice_tag',
        'sum_amount': 'sum_amount',
        'sum_tax': 'sum_tax',
        'serial_number': 'serial_number',
        'attribution': 'attribution',
        'supervision_seal': 'supervision_seal',
        'code': 'code',
        'print_code': 'print_code',
        'machine_number': 'machine_number',
        'print_number': 'print_number',
        'check_code': 'check_code',
        'number': 'number',
        'issue_date': 'issue_date',
        'encryption_block': 'encryption_block',
        'buyer_name': 'buyer_name',
        'buyer_id': 'buyer_id',
        'buyer_address': 'buyer_address',
        'buyer_bank': 'buyer_bank',
        'seller_name': 'seller_name',
        'seller_id': 'seller_id',
        'seller_address': 'seller_address',
        'seller_bank': 'seller_bank',
        'subtotal_amount': 'subtotal_amount',
        'subtotal_tax': 'subtotal_tax',
        'total': 'total',
        'total_in_words': 'total_in_words',
        'remarks': 'remarks',
        'receiver': 'receiver',
        'reviewer': 'reviewer',
        'issuer': 'issuer',
        'seller_seal': 'seller_seal',
        'item_list': 'item_list',
        'province': 'province',
        'city': 'city',
        'confidence': 'confidence',
        'text_location': 'text_location',
        'belong_buyer_name': 'belong_buyer_name',
        'belong_seller_name': 'belong_seller_name',
        'belong_vat_code': 'belong_vat_code',
        'belong_number': 'belong_number',
        'belong_pages': 'belong_pages',
        'belong_current_page': 'belong_current_page',
        'belong_remarks': 'belong_remarks',
        'belong_issue_date': 'belong_issue_date',
        'sales_mark': 'sales_mark',
        'belong_sum_amount': 'belong_sum_amount',
        'belong_sum_tax': 'belong_sum_tax',
        'belong_subtotal_amount': 'belong_subtotal_amount',
        'belong_subtotal_tax': 'belong_subtotal_tax',
        'belong_discount_amount': 'belong_discount_amount',
        'belong_discount_tax': 'belong_discount_tax',
        'belong_item_list': 'belong_item_list',
        'passenger_travel_item_list': 'passenger_travel_item_list'
    }

    def __init__(self, title=None, type=None, invoice_tag=None, sum_amount=None, sum_tax=None, serial_number=None, attribution=None, supervision_seal=None, code=None, print_code=None, machine_number=None, print_number=None, check_code=None, number=None, issue_date=None, encryption_block=None, buyer_name=None, buyer_id=None, buyer_address=None, buyer_bank=None, seller_name=None, seller_id=None, seller_address=None, seller_bank=None, subtotal_amount=None, subtotal_tax=None, total=None, total_in_words=None, remarks=None, receiver=None, reviewer=None, issuer=None, seller_seal=None, item_list=None, province=None, city=None, confidence=None, text_location=None, belong_buyer_name=None, belong_seller_name=None, belong_vat_code=None, belong_number=None, belong_pages=None, belong_current_page=None, belong_remarks=None, belong_issue_date=None, sales_mark=None, belong_sum_amount=None, belong_sum_tax=None, belong_subtotal_amount=None, belong_subtotal_tax=None, belong_discount_amount=None, belong_discount_tax=None, belong_item_list=None, passenger_travel_item_list=None):
        r"""VatInvoiceResult

        The model defined in huaweicloud sdk

        :param title: 增值税发票标题 
        :type title: str
        :param type: 增值税发票类型，取值包括： - special: 增值税专用发票  - normal: 增值税普通发票  - electronic: 增值税电子普通发票  - special_electronic: 增值税电子专用发票  - toll: 增值税电子普通发票（通行费）  - roll: 增值税普通发票（卷票）  - fully_digitalized_special_electronic: 全电专用发票  - fully_digitalized_normal_electronic: 全电普通发票 
        :type type: str
        :param invoice_tag: 增值税发票左上角标志。取值包含：通行费、代开、成品油、收购、机动车、旅客运输服务。 当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type invoice_tag: str
        :param sum_amount: 小计金额，当传入为全电发票时返回此字段。 
        :type sum_amount: str
        :param sum_tax: 小计税额，当传入为全电发票时返回此字段。 
        :type sum_tax: str
        :param serial_number: 发票联次。  当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type serial_number: str
        :param attribution: 发票归属地。  当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type attribution: str
        :param supervision_seal: 发票监制章。  当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type supervision_seal: list[str]
        :param code: 发票代码。 
        :type code: str
        :param print_code: 机打代码。 当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type print_code: str
        :param machine_number: 机器编号。  当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type machine_number: str
        :param print_number: 机打号码。  当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type print_number: str
        :param check_code: 发票校验码，特定类型增值税发票内不存在该信息时返回空字符串。 
        :type check_code: str
        :param number: 发票号码。 
        :type number: str
        :param issue_date: 开票日期。 
        :type issue_date: str
        :param encryption_block: 密码区。 
        :type encryption_block: str
        :param buyer_name: 购买方名称。 
        :type buyer_name: str
        :param buyer_id: 购买方纳税人识别号。 
        :type buyer_id: str
        :param buyer_address: 购买方地址、电话。 
        :type buyer_address: str
        :param buyer_bank: 购买方开户行及帐号。 
        :type buyer_bank: str
        :param seller_name: 销售方名称。 
        :type seller_name: str
        :param seller_id: 销售方纳税人识别号。 
        :type seller_id: str
        :param seller_address: 销售方地址、电话。 
        :type seller_address: str
        :param seller_bank: 销售方开户行及帐号。 
        :type seller_bank: str
        :param subtotal_amount: 合计金额。 
        :type subtotal_amount: str
        :param subtotal_tax: 合计税额。 
        :type subtotal_tax: str
        :param total: 价税合计。 
        :type total: str
        :param total_in_words: 价税合计（大写）。  当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type total_in_words: str
        :param remarks: 备注。  当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type remarks: str
        :param receiver: 收款人。  当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type receiver: str
        :param reviewer: 复核。  当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type reviewer: str
        :param issuer: 开票人。  当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type issuer: str
        :param seller_seal: 销售方发票专用章。  当\&quot;advanced_mode\&quot;设置为\&quot;true\&quot;时才返回。 
        :type seller_seal: list[str]
        :param item_list: 货物或应税劳务列表。 
        :type item_list: list[:class:`huaweicloudsdkocr.v1.ItemList`]
        :param province: 省。 
        :type province: str
        :param city: 市。 
        :type city: str
        :param confidence: 各个字段的置信度。 当“advanced_mode”设置为“true”时才返回。 
        :type confidence: object
        :param text_location: 文本框在原图位置。输出左上、右上、右下、左下四个点坐标。当\&quot;return_text_location\&quot;设置为“true”时才返回。 
        :type text_location: object
        :param belong_buyer_name: 销货清单的购买方名称。 当传入图片为发票销货清单时返回此字段。 
        :type belong_buyer_name: str
        :param belong_seller_name: 销货清单的销售方名称。 当传入图片为发票销货清单时返回此字段。 
        :type belong_seller_name: str
        :param belong_vat_code: 所属的增值税发票代码。 当传入图片为发票销货清单时返回此字段。 
        :type belong_vat_code: str
        :param belong_number: 销货清单的开票号码。 当传入图片为发票销货清单时返回此字段。 
        :type belong_number: str
        :param belong_pages: 销货清单的总页码数。 当传入图片为发票销货清单时返回此字段。 
        :type belong_pages: str
        :param belong_current_page: 销货清单的当前页码。 当传入图片为发票销货清单时返回此字段。 
        :type belong_current_page: str
        :param belong_remarks: 销货清单的备注。 当传入图片为发票销货清单时返回此字段。 
        :type belong_remarks: str
        :param belong_issue_date: 销货清单的填开日期。 当传入图片为发票销货清单时返回此字段。 
        :type belong_issue_date: str
        :param sales_mark: 是否是销货清单，可选值为： - true：输入图片是销货清单。 - false：输入图片不是销货清单。 
        :type sales_mark: bool
        :param belong_sum_amount: 销货清单的小计金额。 当传入图片为发票销货清单时返回此字段。 
        :type belong_sum_amount: str
        :param belong_sum_tax: 销货清单的小计税额。 当传入图片为发票销货清单时返回此字段。 
        :type belong_sum_tax: str
        :param belong_subtotal_amount: 销货清单的总计或者合计金额。 当传入图片为发票销货清单时返回此字段。 
        :type belong_subtotal_amount: str
        :param belong_subtotal_tax: 销货清单的总计税额。 当传入图片为发票销货清单时返回此字段。 
        :type belong_subtotal_tax: str
        :param belong_discount_amount: 销货清单的折扣金额。 当传入图片为发票销货清单时返回此字段。 
        :type belong_discount_amount: str
        :param belong_discount_tax: 销货清单的折扣税额。 当传入图片为发票销货清单时返回此字段。 
        :type belong_discount_tax: str
        :param belong_item_list: 销货清单的货物（劳务）名称列表。 当传入图片为发票销货清单时返回此字段。 
        :type belong_item_list: list[:class:`huaweicloudsdkocr.v1.BelongItemList`]
        :param passenger_travel_item_list: 旅客运输服务的出行信息列表。 当传入图片为旅客运输服务发票时返回此字段。 
        :type passenger_travel_item_list: list[:class:`huaweicloudsdkocr.v1.PassengerTravelItemList`]
        """
        
        

        self._title = None
        self._type = None
        self._invoice_tag = None
        self._sum_amount = None
        self._sum_tax = None
        self._serial_number = None
        self._attribution = None
        self._supervision_seal = None
        self._code = None
        self._print_code = None
        self._machine_number = None
        self._print_number = None
        self._check_code = None
        self._number = None
        self._issue_date = None
        self._encryption_block = None
        self._buyer_name = None
        self._buyer_id = None
        self._buyer_address = None
        self._buyer_bank = None
        self._seller_name = None
        self._seller_id = None
        self._seller_address = None
        self._seller_bank = None
        self._subtotal_amount = None
        self._subtotal_tax = None
        self._total = None
        self._total_in_words = None
        self._remarks = None
        self._receiver = None
        self._reviewer = None
        self._issuer = None
        self._seller_seal = None
        self._item_list = None
        self._province = None
        self._city = None
        self._confidence = None
        self._text_location = None
        self._belong_buyer_name = None
        self._belong_seller_name = None
        self._belong_vat_code = None
        self._belong_number = None
        self._belong_pages = None
        self._belong_current_page = None
        self._belong_remarks = None
        self._belong_issue_date = None
        self._sales_mark = None
        self._belong_sum_amount = None
        self._belong_sum_tax = None
        self._belong_subtotal_amount = None
        self._belong_subtotal_tax = None
        self._belong_discount_amount = None
        self._belong_discount_tax = None
        self._belong_item_list = None
        self._passenger_travel_item_list = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if invoice_tag is not None:
            self.invoice_tag = invoice_tag
        if sum_amount is not None:
            self.sum_amount = sum_amount
        if sum_tax is not None:
            self.sum_tax = sum_tax
        if serial_number is not None:
            self.serial_number = serial_number
        if attribution is not None:
            self.attribution = attribution
        if supervision_seal is not None:
            self.supervision_seal = supervision_seal
        if code is not None:
            self.code = code
        if print_code is not None:
            self.print_code = print_code
        if machine_number is not None:
            self.machine_number = machine_number
        if print_number is not None:
            self.print_number = print_number
        if check_code is not None:
            self.check_code = check_code
        if number is not None:
            self.number = number
        if issue_date is not None:
            self.issue_date = issue_date
        if encryption_block is not None:
            self.encryption_block = encryption_block
        if buyer_name is not None:
            self.buyer_name = buyer_name
        if buyer_id is not None:
            self.buyer_id = buyer_id
        if buyer_address is not None:
            self.buyer_address = buyer_address
        if buyer_bank is not None:
            self.buyer_bank = buyer_bank
        if seller_name is not None:
            self.seller_name = seller_name
        if seller_id is not None:
            self.seller_id = seller_id
        if seller_address is not None:
            self.seller_address = seller_address
        if seller_bank is not None:
            self.seller_bank = seller_bank
        if subtotal_amount is not None:
            self.subtotal_amount = subtotal_amount
        if subtotal_tax is not None:
            self.subtotal_tax = subtotal_tax
        if total is not None:
            self.total = total
        if total_in_words is not None:
            self.total_in_words = total_in_words
        if remarks is not None:
            self.remarks = remarks
        if receiver is not None:
            self.receiver = receiver
        if reviewer is not None:
            self.reviewer = reviewer
        if issuer is not None:
            self.issuer = issuer
        if seller_seal is not None:
            self.seller_seal = seller_seal
        if item_list is not None:
            self.item_list = item_list
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if confidence is not None:
            self.confidence = confidence
        if text_location is not None:
            self.text_location = text_location
        if belong_buyer_name is not None:
            self.belong_buyer_name = belong_buyer_name
        if belong_seller_name is not None:
            self.belong_seller_name = belong_seller_name
        if belong_vat_code is not None:
            self.belong_vat_code = belong_vat_code
        if belong_number is not None:
            self.belong_number = belong_number
        if belong_pages is not None:
            self.belong_pages = belong_pages
        if belong_current_page is not None:
            self.belong_current_page = belong_current_page
        if belong_remarks is not None:
            self.belong_remarks = belong_remarks
        if belong_issue_date is not None:
            self.belong_issue_date = belong_issue_date
        if sales_mark is not None:
            self.sales_mark = sales_mark
        if belong_sum_amount is not None:
            self.belong_sum_amount = belong_sum_amount
        if belong_sum_tax is not None:
            self.belong_sum_tax = belong_sum_tax
        if belong_subtotal_amount is not None:
            self.belong_subtotal_amount = belong_subtotal_amount
        if belong_subtotal_tax is not None:
            self.belong_subtotal_tax = belong_subtotal_tax
        if belong_discount_amount is not None:
            self.belong_discount_amount = belong_discount_amount
        if belong_discount_tax is not None:
            self.belong_discount_tax = belong_discount_tax
        if belong_item_list is not None:
            self.belong_item_list = belong_item_list
        if passenger_travel_item_list is not None:
            self.passenger_travel_item_list = passenger_travel_item_list

    @property
    def title(self):
        r"""Gets the title of this VatInvoiceResult.

        增值税发票标题 

        :return: The title of this VatInvoiceResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this VatInvoiceResult.

        增值税发票标题 

        :param title: The title of this VatInvoiceResult.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this VatInvoiceResult.

        增值税发票类型，取值包括： - special: 增值税专用发票  - normal: 增值税普通发票  - electronic: 增值税电子普通发票  - special_electronic: 增值税电子专用发票  - toll: 增值税电子普通发票（通行费）  - roll: 增值税普通发票（卷票）  - fully_digitalized_special_electronic: 全电专用发票  - fully_digitalized_normal_electronic: 全电普通发票 

        :return: The type of this VatInvoiceResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VatInvoiceResult.

        增值税发票类型，取值包括： - special: 增值税专用发票  - normal: 增值税普通发票  - electronic: 增值税电子普通发票  - special_electronic: 增值税电子专用发票  - toll: 增值税电子普通发票（通行费）  - roll: 增值税普通发票（卷票）  - fully_digitalized_special_electronic: 全电专用发票  - fully_digitalized_normal_electronic: 全电普通发票 

        :param type: The type of this VatInvoiceResult.
        :type type: str
        """
        self._type = type

    @property
    def invoice_tag(self):
        r"""Gets the invoice_tag of this VatInvoiceResult.

        增值税发票左上角标志。取值包含：通行费、代开、成品油、收购、机动车、旅客运输服务。 当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The invoice_tag of this VatInvoiceResult.
        :rtype: str
        """
        return self._invoice_tag

    @invoice_tag.setter
    def invoice_tag(self, invoice_tag):
        r"""Sets the invoice_tag of this VatInvoiceResult.

        增值税发票左上角标志。取值包含：通行费、代开、成品油、收购、机动车、旅客运输服务。 当\"advanced_mode\"设置为\"true\"时才返回。 

        :param invoice_tag: The invoice_tag of this VatInvoiceResult.
        :type invoice_tag: str
        """
        self._invoice_tag = invoice_tag

    @property
    def sum_amount(self):
        r"""Gets the sum_amount of this VatInvoiceResult.

        小计金额，当传入为全电发票时返回此字段。 

        :return: The sum_amount of this VatInvoiceResult.
        :rtype: str
        """
        return self._sum_amount

    @sum_amount.setter
    def sum_amount(self, sum_amount):
        r"""Sets the sum_amount of this VatInvoiceResult.

        小计金额，当传入为全电发票时返回此字段。 

        :param sum_amount: The sum_amount of this VatInvoiceResult.
        :type sum_amount: str
        """
        self._sum_amount = sum_amount

    @property
    def sum_tax(self):
        r"""Gets the sum_tax of this VatInvoiceResult.

        小计税额，当传入为全电发票时返回此字段。 

        :return: The sum_tax of this VatInvoiceResult.
        :rtype: str
        """
        return self._sum_tax

    @sum_tax.setter
    def sum_tax(self, sum_tax):
        r"""Sets the sum_tax of this VatInvoiceResult.

        小计税额，当传入为全电发票时返回此字段。 

        :param sum_tax: The sum_tax of this VatInvoiceResult.
        :type sum_tax: str
        """
        self._sum_tax = sum_tax

    @property
    def serial_number(self):
        r"""Gets the serial_number of this VatInvoiceResult.

        发票联次。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The serial_number of this VatInvoiceResult.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this VatInvoiceResult.

        发票联次。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :param serial_number: The serial_number of this VatInvoiceResult.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def attribution(self):
        r"""Gets the attribution of this VatInvoiceResult.

        发票归属地。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The attribution of this VatInvoiceResult.
        :rtype: str
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        r"""Sets the attribution of this VatInvoiceResult.

        发票归属地。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :param attribution: The attribution of this VatInvoiceResult.
        :type attribution: str
        """
        self._attribution = attribution

    @property
    def supervision_seal(self):
        r"""Gets the supervision_seal of this VatInvoiceResult.

        发票监制章。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The supervision_seal of this VatInvoiceResult.
        :rtype: list[str]
        """
        return self._supervision_seal

    @supervision_seal.setter
    def supervision_seal(self, supervision_seal):
        r"""Sets the supervision_seal of this VatInvoiceResult.

        发票监制章。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :param supervision_seal: The supervision_seal of this VatInvoiceResult.
        :type supervision_seal: list[str]
        """
        self._supervision_seal = supervision_seal

    @property
    def code(self):
        r"""Gets the code of this VatInvoiceResult.

        发票代码。 

        :return: The code of this VatInvoiceResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this VatInvoiceResult.

        发票代码。 

        :param code: The code of this VatInvoiceResult.
        :type code: str
        """
        self._code = code

    @property
    def print_code(self):
        r"""Gets the print_code of this VatInvoiceResult.

        机打代码。 当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The print_code of this VatInvoiceResult.
        :rtype: str
        """
        return self._print_code

    @print_code.setter
    def print_code(self, print_code):
        r"""Sets the print_code of this VatInvoiceResult.

        机打代码。 当\"advanced_mode\"设置为\"true\"时才返回。 

        :param print_code: The print_code of this VatInvoiceResult.
        :type print_code: str
        """
        self._print_code = print_code

    @property
    def machine_number(self):
        r"""Gets the machine_number of this VatInvoiceResult.

        机器编号。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The machine_number of this VatInvoiceResult.
        :rtype: str
        """
        return self._machine_number

    @machine_number.setter
    def machine_number(self, machine_number):
        r"""Sets the machine_number of this VatInvoiceResult.

        机器编号。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :param machine_number: The machine_number of this VatInvoiceResult.
        :type machine_number: str
        """
        self._machine_number = machine_number

    @property
    def print_number(self):
        r"""Gets the print_number of this VatInvoiceResult.

        机打号码。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The print_number of this VatInvoiceResult.
        :rtype: str
        """
        return self._print_number

    @print_number.setter
    def print_number(self, print_number):
        r"""Sets the print_number of this VatInvoiceResult.

        机打号码。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :param print_number: The print_number of this VatInvoiceResult.
        :type print_number: str
        """
        self._print_number = print_number

    @property
    def check_code(self):
        r"""Gets the check_code of this VatInvoiceResult.

        发票校验码，特定类型增值税发票内不存在该信息时返回空字符串。 

        :return: The check_code of this VatInvoiceResult.
        :rtype: str
        """
        return self._check_code

    @check_code.setter
    def check_code(self, check_code):
        r"""Sets the check_code of this VatInvoiceResult.

        发票校验码，特定类型增值税发票内不存在该信息时返回空字符串。 

        :param check_code: The check_code of this VatInvoiceResult.
        :type check_code: str
        """
        self._check_code = check_code

    @property
    def number(self):
        r"""Gets the number of this VatInvoiceResult.

        发票号码。 

        :return: The number of this VatInvoiceResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this VatInvoiceResult.

        发票号码。 

        :param number: The number of this VatInvoiceResult.
        :type number: str
        """
        self._number = number

    @property
    def issue_date(self):
        r"""Gets the issue_date of this VatInvoiceResult.

        开票日期。 

        :return: The issue_date of this VatInvoiceResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this VatInvoiceResult.

        开票日期。 

        :param issue_date: The issue_date of this VatInvoiceResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def encryption_block(self):
        r"""Gets the encryption_block of this VatInvoiceResult.

        密码区。 

        :return: The encryption_block of this VatInvoiceResult.
        :rtype: str
        """
        return self._encryption_block

    @encryption_block.setter
    def encryption_block(self, encryption_block):
        r"""Sets the encryption_block of this VatInvoiceResult.

        密码区。 

        :param encryption_block: The encryption_block of this VatInvoiceResult.
        :type encryption_block: str
        """
        self._encryption_block = encryption_block

    @property
    def buyer_name(self):
        r"""Gets the buyer_name of this VatInvoiceResult.

        购买方名称。 

        :return: The buyer_name of this VatInvoiceResult.
        :rtype: str
        """
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, buyer_name):
        r"""Sets the buyer_name of this VatInvoiceResult.

        购买方名称。 

        :param buyer_name: The buyer_name of this VatInvoiceResult.
        :type buyer_name: str
        """
        self._buyer_name = buyer_name

    @property
    def buyer_id(self):
        r"""Gets the buyer_id of this VatInvoiceResult.

        购买方纳税人识别号。 

        :return: The buyer_id of this VatInvoiceResult.
        :rtype: str
        """
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, buyer_id):
        r"""Sets the buyer_id of this VatInvoiceResult.

        购买方纳税人识别号。 

        :param buyer_id: The buyer_id of this VatInvoiceResult.
        :type buyer_id: str
        """
        self._buyer_id = buyer_id

    @property
    def buyer_address(self):
        r"""Gets the buyer_address of this VatInvoiceResult.

        购买方地址、电话。 

        :return: The buyer_address of this VatInvoiceResult.
        :rtype: str
        """
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, buyer_address):
        r"""Sets the buyer_address of this VatInvoiceResult.

        购买方地址、电话。 

        :param buyer_address: The buyer_address of this VatInvoiceResult.
        :type buyer_address: str
        """
        self._buyer_address = buyer_address

    @property
    def buyer_bank(self):
        r"""Gets the buyer_bank of this VatInvoiceResult.

        购买方开户行及帐号。 

        :return: The buyer_bank of this VatInvoiceResult.
        :rtype: str
        """
        return self._buyer_bank

    @buyer_bank.setter
    def buyer_bank(self, buyer_bank):
        r"""Sets the buyer_bank of this VatInvoiceResult.

        购买方开户行及帐号。 

        :param buyer_bank: The buyer_bank of this VatInvoiceResult.
        :type buyer_bank: str
        """
        self._buyer_bank = buyer_bank

    @property
    def seller_name(self):
        r"""Gets the seller_name of this VatInvoiceResult.

        销售方名称。 

        :return: The seller_name of this VatInvoiceResult.
        :rtype: str
        """
        return self._seller_name

    @seller_name.setter
    def seller_name(self, seller_name):
        r"""Sets the seller_name of this VatInvoiceResult.

        销售方名称。 

        :param seller_name: The seller_name of this VatInvoiceResult.
        :type seller_name: str
        """
        self._seller_name = seller_name

    @property
    def seller_id(self):
        r"""Gets the seller_id of this VatInvoiceResult.

        销售方纳税人识别号。 

        :return: The seller_id of this VatInvoiceResult.
        :rtype: str
        """
        return self._seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        r"""Sets the seller_id of this VatInvoiceResult.

        销售方纳税人识别号。 

        :param seller_id: The seller_id of this VatInvoiceResult.
        :type seller_id: str
        """
        self._seller_id = seller_id

    @property
    def seller_address(self):
        r"""Gets the seller_address of this VatInvoiceResult.

        销售方地址、电话。 

        :return: The seller_address of this VatInvoiceResult.
        :rtype: str
        """
        return self._seller_address

    @seller_address.setter
    def seller_address(self, seller_address):
        r"""Sets the seller_address of this VatInvoiceResult.

        销售方地址、电话。 

        :param seller_address: The seller_address of this VatInvoiceResult.
        :type seller_address: str
        """
        self._seller_address = seller_address

    @property
    def seller_bank(self):
        r"""Gets the seller_bank of this VatInvoiceResult.

        销售方开户行及帐号。 

        :return: The seller_bank of this VatInvoiceResult.
        :rtype: str
        """
        return self._seller_bank

    @seller_bank.setter
    def seller_bank(self, seller_bank):
        r"""Sets the seller_bank of this VatInvoiceResult.

        销售方开户行及帐号。 

        :param seller_bank: The seller_bank of this VatInvoiceResult.
        :type seller_bank: str
        """
        self._seller_bank = seller_bank

    @property
    def subtotal_amount(self):
        r"""Gets the subtotal_amount of this VatInvoiceResult.

        合计金额。 

        :return: The subtotal_amount of this VatInvoiceResult.
        :rtype: str
        """
        return self._subtotal_amount

    @subtotal_amount.setter
    def subtotal_amount(self, subtotal_amount):
        r"""Sets the subtotal_amount of this VatInvoiceResult.

        合计金额。 

        :param subtotal_amount: The subtotal_amount of this VatInvoiceResult.
        :type subtotal_amount: str
        """
        self._subtotal_amount = subtotal_amount

    @property
    def subtotal_tax(self):
        r"""Gets the subtotal_tax of this VatInvoiceResult.

        合计税额。 

        :return: The subtotal_tax of this VatInvoiceResult.
        :rtype: str
        """
        return self._subtotal_tax

    @subtotal_tax.setter
    def subtotal_tax(self, subtotal_tax):
        r"""Sets the subtotal_tax of this VatInvoiceResult.

        合计税额。 

        :param subtotal_tax: The subtotal_tax of this VatInvoiceResult.
        :type subtotal_tax: str
        """
        self._subtotal_tax = subtotal_tax

    @property
    def total(self):
        r"""Gets the total of this VatInvoiceResult.

        价税合计。 

        :return: The total of this VatInvoiceResult.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this VatInvoiceResult.

        价税合计。 

        :param total: The total of this VatInvoiceResult.
        :type total: str
        """
        self._total = total

    @property
    def total_in_words(self):
        r"""Gets the total_in_words of this VatInvoiceResult.

        价税合计（大写）。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The total_in_words of this VatInvoiceResult.
        :rtype: str
        """
        return self._total_in_words

    @total_in_words.setter
    def total_in_words(self, total_in_words):
        r"""Sets the total_in_words of this VatInvoiceResult.

        价税合计（大写）。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :param total_in_words: The total_in_words of this VatInvoiceResult.
        :type total_in_words: str
        """
        self._total_in_words = total_in_words

    @property
    def remarks(self):
        r"""Gets the remarks of this VatInvoiceResult.

        备注。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The remarks of this VatInvoiceResult.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this VatInvoiceResult.

        备注。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :param remarks: The remarks of this VatInvoiceResult.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def receiver(self):
        r"""Gets the receiver of this VatInvoiceResult.

        收款人。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The receiver of this VatInvoiceResult.
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        r"""Sets the receiver of this VatInvoiceResult.

        收款人。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :param receiver: The receiver of this VatInvoiceResult.
        :type receiver: str
        """
        self._receiver = receiver

    @property
    def reviewer(self):
        r"""Gets the reviewer of this VatInvoiceResult.

        复核。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The reviewer of this VatInvoiceResult.
        :rtype: str
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        r"""Sets the reviewer of this VatInvoiceResult.

        复核。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :param reviewer: The reviewer of this VatInvoiceResult.
        :type reviewer: str
        """
        self._reviewer = reviewer

    @property
    def issuer(self):
        r"""Gets the issuer of this VatInvoiceResult.

        开票人。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The issuer of this VatInvoiceResult.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        r"""Sets the issuer of this VatInvoiceResult.

        开票人。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :param issuer: The issuer of this VatInvoiceResult.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def seller_seal(self):
        r"""Gets the seller_seal of this VatInvoiceResult.

        销售方发票专用章。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :return: The seller_seal of this VatInvoiceResult.
        :rtype: list[str]
        """
        return self._seller_seal

    @seller_seal.setter
    def seller_seal(self, seller_seal):
        r"""Sets the seller_seal of this VatInvoiceResult.

        销售方发票专用章。  当\"advanced_mode\"设置为\"true\"时才返回。 

        :param seller_seal: The seller_seal of this VatInvoiceResult.
        :type seller_seal: list[str]
        """
        self._seller_seal = seller_seal

    @property
    def item_list(self):
        r"""Gets the item_list of this VatInvoiceResult.

        货物或应税劳务列表。 

        :return: The item_list of this VatInvoiceResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.ItemList`]
        """
        return self._item_list

    @item_list.setter
    def item_list(self, item_list):
        r"""Sets the item_list of this VatInvoiceResult.

        货物或应税劳务列表。 

        :param item_list: The item_list of this VatInvoiceResult.
        :type item_list: list[:class:`huaweicloudsdkocr.v1.ItemList`]
        """
        self._item_list = item_list

    @property
    def province(self):
        r"""Gets the province of this VatInvoiceResult.

        省。 

        :return: The province of this VatInvoiceResult.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this VatInvoiceResult.

        省。 

        :param province: The province of this VatInvoiceResult.
        :type province: str
        """
        self._province = province

    @property
    def city(self):
        r"""Gets the city of this VatInvoiceResult.

        市。 

        :return: The city of this VatInvoiceResult.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this VatInvoiceResult.

        市。 

        :param city: The city of this VatInvoiceResult.
        :type city: str
        """
        self._city = city

    @property
    def confidence(self):
        r"""Gets the confidence of this VatInvoiceResult.

        各个字段的置信度。 当“advanced_mode”设置为“true”时才返回。 

        :return: The confidence of this VatInvoiceResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this VatInvoiceResult.

        各个字段的置信度。 当“advanced_mode”设置为“true”时才返回。 

        :param confidence: The confidence of this VatInvoiceResult.
        :type confidence: object
        """
        self._confidence = confidence

    @property
    def text_location(self):
        r"""Gets the text_location of this VatInvoiceResult.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。当\"return_text_location\"设置为“true”时才返回。 

        :return: The text_location of this VatInvoiceResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        r"""Sets the text_location of this VatInvoiceResult.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。当\"return_text_location\"设置为“true”时才返回。 

        :param text_location: The text_location of this VatInvoiceResult.
        :type text_location: object
        """
        self._text_location = text_location

    @property
    def belong_buyer_name(self):
        r"""Gets the belong_buyer_name of this VatInvoiceResult.

        销货清单的购买方名称。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_buyer_name of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_buyer_name

    @belong_buyer_name.setter
    def belong_buyer_name(self, belong_buyer_name):
        r"""Sets the belong_buyer_name of this VatInvoiceResult.

        销货清单的购买方名称。 当传入图片为发票销货清单时返回此字段。 

        :param belong_buyer_name: The belong_buyer_name of this VatInvoiceResult.
        :type belong_buyer_name: str
        """
        self._belong_buyer_name = belong_buyer_name

    @property
    def belong_seller_name(self):
        r"""Gets the belong_seller_name of this VatInvoiceResult.

        销货清单的销售方名称。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_seller_name of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_seller_name

    @belong_seller_name.setter
    def belong_seller_name(self, belong_seller_name):
        r"""Sets the belong_seller_name of this VatInvoiceResult.

        销货清单的销售方名称。 当传入图片为发票销货清单时返回此字段。 

        :param belong_seller_name: The belong_seller_name of this VatInvoiceResult.
        :type belong_seller_name: str
        """
        self._belong_seller_name = belong_seller_name

    @property
    def belong_vat_code(self):
        r"""Gets the belong_vat_code of this VatInvoiceResult.

        所属的增值税发票代码。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_vat_code of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_vat_code

    @belong_vat_code.setter
    def belong_vat_code(self, belong_vat_code):
        r"""Sets the belong_vat_code of this VatInvoiceResult.

        所属的增值税发票代码。 当传入图片为发票销货清单时返回此字段。 

        :param belong_vat_code: The belong_vat_code of this VatInvoiceResult.
        :type belong_vat_code: str
        """
        self._belong_vat_code = belong_vat_code

    @property
    def belong_number(self):
        r"""Gets the belong_number of this VatInvoiceResult.

        销货清单的开票号码。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_number of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_number

    @belong_number.setter
    def belong_number(self, belong_number):
        r"""Sets the belong_number of this VatInvoiceResult.

        销货清单的开票号码。 当传入图片为发票销货清单时返回此字段。 

        :param belong_number: The belong_number of this VatInvoiceResult.
        :type belong_number: str
        """
        self._belong_number = belong_number

    @property
    def belong_pages(self):
        r"""Gets the belong_pages of this VatInvoiceResult.

        销货清单的总页码数。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_pages of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_pages

    @belong_pages.setter
    def belong_pages(self, belong_pages):
        r"""Sets the belong_pages of this VatInvoiceResult.

        销货清单的总页码数。 当传入图片为发票销货清单时返回此字段。 

        :param belong_pages: The belong_pages of this VatInvoiceResult.
        :type belong_pages: str
        """
        self._belong_pages = belong_pages

    @property
    def belong_current_page(self):
        r"""Gets the belong_current_page of this VatInvoiceResult.

        销货清单的当前页码。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_current_page of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_current_page

    @belong_current_page.setter
    def belong_current_page(self, belong_current_page):
        r"""Sets the belong_current_page of this VatInvoiceResult.

        销货清单的当前页码。 当传入图片为发票销货清单时返回此字段。 

        :param belong_current_page: The belong_current_page of this VatInvoiceResult.
        :type belong_current_page: str
        """
        self._belong_current_page = belong_current_page

    @property
    def belong_remarks(self):
        r"""Gets the belong_remarks of this VatInvoiceResult.

        销货清单的备注。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_remarks of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_remarks

    @belong_remarks.setter
    def belong_remarks(self, belong_remarks):
        r"""Sets the belong_remarks of this VatInvoiceResult.

        销货清单的备注。 当传入图片为发票销货清单时返回此字段。 

        :param belong_remarks: The belong_remarks of this VatInvoiceResult.
        :type belong_remarks: str
        """
        self._belong_remarks = belong_remarks

    @property
    def belong_issue_date(self):
        r"""Gets the belong_issue_date of this VatInvoiceResult.

        销货清单的填开日期。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_issue_date of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_issue_date

    @belong_issue_date.setter
    def belong_issue_date(self, belong_issue_date):
        r"""Sets the belong_issue_date of this VatInvoiceResult.

        销货清单的填开日期。 当传入图片为发票销货清单时返回此字段。 

        :param belong_issue_date: The belong_issue_date of this VatInvoiceResult.
        :type belong_issue_date: str
        """
        self._belong_issue_date = belong_issue_date

    @property
    def sales_mark(self):
        r"""Gets the sales_mark of this VatInvoiceResult.

        是否是销货清单，可选值为： - true：输入图片是销货清单。 - false：输入图片不是销货清单。 

        :return: The sales_mark of this VatInvoiceResult.
        :rtype: bool
        """
        return self._sales_mark

    @sales_mark.setter
    def sales_mark(self, sales_mark):
        r"""Sets the sales_mark of this VatInvoiceResult.

        是否是销货清单，可选值为： - true：输入图片是销货清单。 - false：输入图片不是销货清单。 

        :param sales_mark: The sales_mark of this VatInvoiceResult.
        :type sales_mark: bool
        """
        self._sales_mark = sales_mark

    @property
    def belong_sum_amount(self):
        r"""Gets the belong_sum_amount of this VatInvoiceResult.

        销货清单的小计金额。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_sum_amount of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_sum_amount

    @belong_sum_amount.setter
    def belong_sum_amount(self, belong_sum_amount):
        r"""Sets the belong_sum_amount of this VatInvoiceResult.

        销货清单的小计金额。 当传入图片为发票销货清单时返回此字段。 

        :param belong_sum_amount: The belong_sum_amount of this VatInvoiceResult.
        :type belong_sum_amount: str
        """
        self._belong_sum_amount = belong_sum_amount

    @property
    def belong_sum_tax(self):
        r"""Gets the belong_sum_tax of this VatInvoiceResult.

        销货清单的小计税额。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_sum_tax of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_sum_tax

    @belong_sum_tax.setter
    def belong_sum_tax(self, belong_sum_tax):
        r"""Sets the belong_sum_tax of this VatInvoiceResult.

        销货清单的小计税额。 当传入图片为发票销货清单时返回此字段。 

        :param belong_sum_tax: The belong_sum_tax of this VatInvoiceResult.
        :type belong_sum_tax: str
        """
        self._belong_sum_tax = belong_sum_tax

    @property
    def belong_subtotal_amount(self):
        r"""Gets the belong_subtotal_amount of this VatInvoiceResult.

        销货清单的总计或者合计金额。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_subtotal_amount of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_subtotal_amount

    @belong_subtotal_amount.setter
    def belong_subtotal_amount(self, belong_subtotal_amount):
        r"""Sets the belong_subtotal_amount of this VatInvoiceResult.

        销货清单的总计或者合计金额。 当传入图片为发票销货清单时返回此字段。 

        :param belong_subtotal_amount: The belong_subtotal_amount of this VatInvoiceResult.
        :type belong_subtotal_amount: str
        """
        self._belong_subtotal_amount = belong_subtotal_amount

    @property
    def belong_subtotal_tax(self):
        r"""Gets the belong_subtotal_tax of this VatInvoiceResult.

        销货清单的总计税额。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_subtotal_tax of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_subtotal_tax

    @belong_subtotal_tax.setter
    def belong_subtotal_tax(self, belong_subtotal_tax):
        r"""Sets the belong_subtotal_tax of this VatInvoiceResult.

        销货清单的总计税额。 当传入图片为发票销货清单时返回此字段。 

        :param belong_subtotal_tax: The belong_subtotal_tax of this VatInvoiceResult.
        :type belong_subtotal_tax: str
        """
        self._belong_subtotal_tax = belong_subtotal_tax

    @property
    def belong_discount_amount(self):
        r"""Gets the belong_discount_amount of this VatInvoiceResult.

        销货清单的折扣金额。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_discount_amount of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_discount_amount

    @belong_discount_amount.setter
    def belong_discount_amount(self, belong_discount_amount):
        r"""Sets the belong_discount_amount of this VatInvoiceResult.

        销货清单的折扣金额。 当传入图片为发票销货清单时返回此字段。 

        :param belong_discount_amount: The belong_discount_amount of this VatInvoiceResult.
        :type belong_discount_amount: str
        """
        self._belong_discount_amount = belong_discount_amount

    @property
    def belong_discount_tax(self):
        r"""Gets the belong_discount_tax of this VatInvoiceResult.

        销货清单的折扣税额。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_discount_tax of this VatInvoiceResult.
        :rtype: str
        """
        return self._belong_discount_tax

    @belong_discount_tax.setter
    def belong_discount_tax(self, belong_discount_tax):
        r"""Sets the belong_discount_tax of this VatInvoiceResult.

        销货清单的折扣税额。 当传入图片为发票销货清单时返回此字段。 

        :param belong_discount_tax: The belong_discount_tax of this VatInvoiceResult.
        :type belong_discount_tax: str
        """
        self._belong_discount_tax = belong_discount_tax

    @property
    def belong_item_list(self):
        r"""Gets the belong_item_list of this VatInvoiceResult.

        销货清单的货物（劳务）名称列表。 当传入图片为发票销货清单时返回此字段。 

        :return: The belong_item_list of this VatInvoiceResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.BelongItemList`]
        """
        return self._belong_item_list

    @belong_item_list.setter
    def belong_item_list(self, belong_item_list):
        r"""Sets the belong_item_list of this VatInvoiceResult.

        销货清单的货物（劳务）名称列表。 当传入图片为发票销货清单时返回此字段。 

        :param belong_item_list: The belong_item_list of this VatInvoiceResult.
        :type belong_item_list: list[:class:`huaweicloudsdkocr.v1.BelongItemList`]
        """
        self._belong_item_list = belong_item_list

    @property
    def passenger_travel_item_list(self):
        r"""Gets the passenger_travel_item_list of this VatInvoiceResult.

        旅客运输服务的出行信息列表。 当传入图片为旅客运输服务发票时返回此字段。 

        :return: The passenger_travel_item_list of this VatInvoiceResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.PassengerTravelItemList`]
        """
        return self._passenger_travel_item_list

    @passenger_travel_item_list.setter
    def passenger_travel_item_list(self, passenger_travel_item_list):
        r"""Sets the passenger_travel_item_list of this VatInvoiceResult.

        旅客运输服务的出行信息列表。 当传入图片为旅客运输服务发票时返回此字段。 

        :param passenger_travel_item_list: The passenger_travel_item_list of this VatInvoiceResult.
        :type passenger_travel_item_list: list[:class:`huaweicloudsdkocr.v1.PassengerTravelItemList`]
        """
        self._passenger_travel_item_list = passenger_travel_item_list

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
        if not isinstance(other, VatInvoiceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
