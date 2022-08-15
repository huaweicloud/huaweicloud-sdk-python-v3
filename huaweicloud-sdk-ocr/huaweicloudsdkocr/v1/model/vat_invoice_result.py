# coding: utf-8

import re
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
        'confidence': 'object',
        'text_location': 'object'
    }

    attribute_map = {
        'title': 'title',
        'type': 'type',
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
        'confidence': 'confidence',
        'text_location': 'text_location'
    }

    def __init__(self, title=None, type=None, serial_number=None, attribution=None, supervision_seal=None, code=None, print_code=None, machine_number=None, print_number=None, check_code=None, number=None, issue_date=None, encryption_block=None, buyer_name=None, buyer_id=None, buyer_address=None, buyer_bank=None, seller_name=None, seller_id=None, seller_address=None, seller_bank=None, subtotal_amount=None, subtotal_tax=None, total=None, total_in_words=None, remarks=None, receiver=None, reviewer=None, issuer=None, seller_seal=None, item_list=None, confidence=None, text_location=None):
        """VatInvoiceResult

        The model defined in huaweicloud sdk

        :param title: 增值税发票标题 
        :type title: str
        :param type: 增值税发票类型，可选值包括：  - special: 增值税专用发票  - normal: 增值税普通发票  - electronic: 增值税电子普通发票  - special_electronic: 增值税电子专用发票  - toll: 增值税电子普通发票（通行费）  - roll: 增值税普通发票（卷票） 
        :type type: str
        :param serial_number: 发票联次。 当“advanced_mode”设置为“true”时才返回。 
        :type serial_number: str
        :param attribution: 发票归属地。 当“advanced_mode”设置为“true”时才返回。 
        :type attribution: str
        :param supervision_seal: 发票监制章。 当“advanced_mode”设置为“true”时才返回。 
        :type supervision_seal: list[str]
        :param code: 发票代码。 
        :type code: str
        :param print_code: 机打代码。当“advanced_mode”设置为“true”时才返回。 
        :type print_code: str
        :param machine_number: 机器编号。 当“advanced_mode”设置为“true”时才返回。 
        :type machine_number: str
        :param print_number: 机打号码。 当“advanced_mode”设置为“true”时才返回 
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
        :param total_in_words: 价税合计（大写）。 当“advanced_mode”设置为“true”时才返回。 
        :type total_in_words: str
        :param remarks: 备注。 当“advanced_mode”设置为“true”时才返回。 
        :type remarks: str
        :param receiver: 收款人。 当“advanced_mode”设置为“true”时才返回。 
        :type receiver: str
        :param reviewer: 复核。 当“advanced_mode”设置为“true”时才返回。 
        :type reviewer: str
        :param issuer: 开票人。 当“advanced_mode”设置为“true”时才返回。 
        :type issuer: str
        :param seller_seal: 销售方发票专用章。 当“advanced_mode”设置为“true”时才返回。 
        :type seller_seal: list[str]
        :param item_list: 货物或应税劳务列表。 
        :type item_list: list[:class:`huaweicloudsdkocr.v1.ItemList`]
        :param confidence: 各个字段的置信度。 当“advanced_mode”设置为“true”时才返回。 
        :type confidence: object
        :param text_location: 文本框在原图位置。输出左上、右上、右下、左下四个点坐标。当“return_text_location”设置为“true”时才返回。 
        :type text_location: object
        """
        
        

        self._title = None
        self._type = None
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
        self._confidence = None
        self._text_location = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
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
        if confidence is not None:
            self.confidence = confidence
        if text_location is not None:
            self.text_location = text_location

    @property
    def title(self):
        """Gets the title of this VatInvoiceResult.

        增值税发票标题 

        :return: The title of this VatInvoiceResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this VatInvoiceResult.

        增值税发票标题 

        :param title: The title of this VatInvoiceResult.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        """Gets the type of this VatInvoiceResult.

        增值税发票类型，可选值包括：  - special: 增值税专用发票  - normal: 增值税普通发票  - electronic: 增值税电子普通发票  - special_electronic: 增值税电子专用发票  - toll: 增值税电子普通发票（通行费）  - roll: 增值税普通发票（卷票） 

        :return: The type of this VatInvoiceResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VatInvoiceResult.

        增值税发票类型，可选值包括：  - special: 增值税专用发票  - normal: 增值税普通发票  - electronic: 增值税电子普通发票  - special_electronic: 增值税电子专用发票  - toll: 增值税电子普通发票（通行费）  - roll: 增值税普通发票（卷票） 

        :param type: The type of this VatInvoiceResult.
        :type type: str
        """
        self._type = type

    @property
    def serial_number(self):
        """Gets the serial_number of this VatInvoiceResult.

        发票联次。 当“advanced_mode”设置为“true”时才返回。 

        :return: The serial_number of this VatInvoiceResult.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this VatInvoiceResult.

        发票联次。 当“advanced_mode”设置为“true”时才返回。 

        :param serial_number: The serial_number of this VatInvoiceResult.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def attribution(self):
        """Gets the attribution of this VatInvoiceResult.

        发票归属地。 当“advanced_mode”设置为“true”时才返回。 

        :return: The attribution of this VatInvoiceResult.
        :rtype: str
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """Sets the attribution of this VatInvoiceResult.

        发票归属地。 当“advanced_mode”设置为“true”时才返回。 

        :param attribution: The attribution of this VatInvoiceResult.
        :type attribution: str
        """
        self._attribution = attribution

    @property
    def supervision_seal(self):
        """Gets the supervision_seal of this VatInvoiceResult.

        发票监制章。 当“advanced_mode”设置为“true”时才返回。 

        :return: The supervision_seal of this VatInvoiceResult.
        :rtype: list[str]
        """
        return self._supervision_seal

    @supervision_seal.setter
    def supervision_seal(self, supervision_seal):
        """Sets the supervision_seal of this VatInvoiceResult.

        发票监制章。 当“advanced_mode”设置为“true”时才返回。 

        :param supervision_seal: The supervision_seal of this VatInvoiceResult.
        :type supervision_seal: list[str]
        """
        self._supervision_seal = supervision_seal

    @property
    def code(self):
        """Gets the code of this VatInvoiceResult.

        发票代码。 

        :return: The code of this VatInvoiceResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this VatInvoiceResult.

        发票代码。 

        :param code: The code of this VatInvoiceResult.
        :type code: str
        """
        self._code = code

    @property
    def print_code(self):
        """Gets the print_code of this VatInvoiceResult.

        机打代码。当“advanced_mode”设置为“true”时才返回。 

        :return: The print_code of this VatInvoiceResult.
        :rtype: str
        """
        return self._print_code

    @print_code.setter
    def print_code(self, print_code):
        """Sets the print_code of this VatInvoiceResult.

        机打代码。当“advanced_mode”设置为“true”时才返回。 

        :param print_code: The print_code of this VatInvoiceResult.
        :type print_code: str
        """
        self._print_code = print_code

    @property
    def machine_number(self):
        """Gets the machine_number of this VatInvoiceResult.

        机器编号。 当“advanced_mode”设置为“true”时才返回。 

        :return: The machine_number of this VatInvoiceResult.
        :rtype: str
        """
        return self._machine_number

    @machine_number.setter
    def machine_number(self, machine_number):
        """Sets the machine_number of this VatInvoiceResult.

        机器编号。 当“advanced_mode”设置为“true”时才返回。 

        :param machine_number: The machine_number of this VatInvoiceResult.
        :type machine_number: str
        """
        self._machine_number = machine_number

    @property
    def print_number(self):
        """Gets the print_number of this VatInvoiceResult.

        机打号码。 当“advanced_mode”设置为“true”时才返回 

        :return: The print_number of this VatInvoiceResult.
        :rtype: str
        """
        return self._print_number

    @print_number.setter
    def print_number(self, print_number):
        """Sets the print_number of this VatInvoiceResult.

        机打号码。 当“advanced_mode”设置为“true”时才返回 

        :param print_number: The print_number of this VatInvoiceResult.
        :type print_number: str
        """
        self._print_number = print_number

    @property
    def check_code(self):
        """Gets the check_code of this VatInvoiceResult.

        发票校验码，特定类型增值税发票内不存在该信息时返回空字符串。 

        :return: The check_code of this VatInvoiceResult.
        :rtype: str
        """
        return self._check_code

    @check_code.setter
    def check_code(self, check_code):
        """Sets the check_code of this VatInvoiceResult.

        发票校验码，特定类型增值税发票内不存在该信息时返回空字符串。 

        :param check_code: The check_code of this VatInvoiceResult.
        :type check_code: str
        """
        self._check_code = check_code

    @property
    def number(self):
        """Gets the number of this VatInvoiceResult.

        发票号码。 

        :return: The number of this VatInvoiceResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this VatInvoiceResult.

        发票号码。 

        :param number: The number of this VatInvoiceResult.
        :type number: str
        """
        self._number = number

    @property
    def issue_date(self):
        """Gets the issue_date of this VatInvoiceResult.

        开票日期。 

        :return: The issue_date of this VatInvoiceResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this VatInvoiceResult.

        开票日期。 

        :param issue_date: The issue_date of this VatInvoiceResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def encryption_block(self):
        """Gets the encryption_block of this VatInvoiceResult.

        密码区。 

        :return: The encryption_block of this VatInvoiceResult.
        :rtype: str
        """
        return self._encryption_block

    @encryption_block.setter
    def encryption_block(self, encryption_block):
        """Sets the encryption_block of this VatInvoiceResult.

        密码区。 

        :param encryption_block: The encryption_block of this VatInvoiceResult.
        :type encryption_block: str
        """
        self._encryption_block = encryption_block

    @property
    def buyer_name(self):
        """Gets the buyer_name of this VatInvoiceResult.

        购买方名称。 

        :return: The buyer_name of this VatInvoiceResult.
        :rtype: str
        """
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, buyer_name):
        """Sets the buyer_name of this VatInvoiceResult.

        购买方名称。 

        :param buyer_name: The buyer_name of this VatInvoiceResult.
        :type buyer_name: str
        """
        self._buyer_name = buyer_name

    @property
    def buyer_id(self):
        """Gets the buyer_id of this VatInvoiceResult.

        购买方纳税人识别号。 

        :return: The buyer_id of this VatInvoiceResult.
        :rtype: str
        """
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, buyer_id):
        """Sets the buyer_id of this VatInvoiceResult.

        购买方纳税人识别号。 

        :param buyer_id: The buyer_id of this VatInvoiceResult.
        :type buyer_id: str
        """
        self._buyer_id = buyer_id

    @property
    def buyer_address(self):
        """Gets the buyer_address of this VatInvoiceResult.

        购买方地址、电话。 

        :return: The buyer_address of this VatInvoiceResult.
        :rtype: str
        """
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, buyer_address):
        """Sets the buyer_address of this VatInvoiceResult.

        购买方地址、电话。 

        :param buyer_address: The buyer_address of this VatInvoiceResult.
        :type buyer_address: str
        """
        self._buyer_address = buyer_address

    @property
    def buyer_bank(self):
        """Gets the buyer_bank of this VatInvoiceResult.

        购买方开户行及帐号。 

        :return: The buyer_bank of this VatInvoiceResult.
        :rtype: str
        """
        return self._buyer_bank

    @buyer_bank.setter
    def buyer_bank(self, buyer_bank):
        """Sets the buyer_bank of this VatInvoiceResult.

        购买方开户行及帐号。 

        :param buyer_bank: The buyer_bank of this VatInvoiceResult.
        :type buyer_bank: str
        """
        self._buyer_bank = buyer_bank

    @property
    def seller_name(self):
        """Gets the seller_name of this VatInvoiceResult.

        销售方名称。 

        :return: The seller_name of this VatInvoiceResult.
        :rtype: str
        """
        return self._seller_name

    @seller_name.setter
    def seller_name(self, seller_name):
        """Sets the seller_name of this VatInvoiceResult.

        销售方名称。 

        :param seller_name: The seller_name of this VatInvoiceResult.
        :type seller_name: str
        """
        self._seller_name = seller_name

    @property
    def seller_id(self):
        """Gets the seller_id of this VatInvoiceResult.

        销售方纳税人识别号。 

        :return: The seller_id of this VatInvoiceResult.
        :rtype: str
        """
        return self._seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        """Sets the seller_id of this VatInvoiceResult.

        销售方纳税人识别号。 

        :param seller_id: The seller_id of this VatInvoiceResult.
        :type seller_id: str
        """
        self._seller_id = seller_id

    @property
    def seller_address(self):
        """Gets the seller_address of this VatInvoiceResult.

        销售方地址、电话。 

        :return: The seller_address of this VatInvoiceResult.
        :rtype: str
        """
        return self._seller_address

    @seller_address.setter
    def seller_address(self, seller_address):
        """Sets the seller_address of this VatInvoiceResult.

        销售方地址、电话。 

        :param seller_address: The seller_address of this VatInvoiceResult.
        :type seller_address: str
        """
        self._seller_address = seller_address

    @property
    def seller_bank(self):
        """Gets the seller_bank of this VatInvoiceResult.

        销售方开户行及帐号。 

        :return: The seller_bank of this VatInvoiceResult.
        :rtype: str
        """
        return self._seller_bank

    @seller_bank.setter
    def seller_bank(self, seller_bank):
        """Sets the seller_bank of this VatInvoiceResult.

        销售方开户行及帐号。 

        :param seller_bank: The seller_bank of this VatInvoiceResult.
        :type seller_bank: str
        """
        self._seller_bank = seller_bank

    @property
    def subtotal_amount(self):
        """Gets the subtotal_amount of this VatInvoiceResult.

        合计金额。 

        :return: The subtotal_amount of this VatInvoiceResult.
        :rtype: str
        """
        return self._subtotal_amount

    @subtotal_amount.setter
    def subtotal_amount(self, subtotal_amount):
        """Sets the subtotal_amount of this VatInvoiceResult.

        合计金额。 

        :param subtotal_amount: The subtotal_amount of this VatInvoiceResult.
        :type subtotal_amount: str
        """
        self._subtotal_amount = subtotal_amount

    @property
    def subtotal_tax(self):
        """Gets the subtotal_tax of this VatInvoiceResult.

        合计税额。 

        :return: The subtotal_tax of this VatInvoiceResult.
        :rtype: str
        """
        return self._subtotal_tax

    @subtotal_tax.setter
    def subtotal_tax(self, subtotal_tax):
        """Sets the subtotal_tax of this VatInvoiceResult.

        合计税额。 

        :param subtotal_tax: The subtotal_tax of this VatInvoiceResult.
        :type subtotal_tax: str
        """
        self._subtotal_tax = subtotal_tax

    @property
    def total(self):
        """Gets the total of this VatInvoiceResult.

        价税合计。 

        :return: The total of this VatInvoiceResult.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this VatInvoiceResult.

        价税合计。 

        :param total: The total of this VatInvoiceResult.
        :type total: str
        """
        self._total = total

    @property
    def total_in_words(self):
        """Gets the total_in_words of this VatInvoiceResult.

        价税合计（大写）。 当“advanced_mode”设置为“true”时才返回。 

        :return: The total_in_words of this VatInvoiceResult.
        :rtype: str
        """
        return self._total_in_words

    @total_in_words.setter
    def total_in_words(self, total_in_words):
        """Sets the total_in_words of this VatInvoiceResult.

        价税合计（大写）。 当“advanced_mode”设置为“true”时才返回。 

        :param total_in_words: The total_in_words of this VatInvoiceResult.
        :type total_in_words: str
        """
        self._total_in_words = total_in_words

    @property
    def remarks(self):
        """Gets the remarks of this VatInvoiceResult.

        备注。 当“advanced_mode”设置为“true”时才返回。 

        :return: The remarks of this VatInvoiceResult.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this VatInvoiceResult.

        备注。 当“advanced_mode”设置为“true”时才返回。 

        :param remarks: The remarks of this VatInvoiceResult.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def receiver(self):
        """Gets the receiver of this VatInvoiceResult.

        收款人。 当“advanced_mode”设置为“true”时才返回。 

        :return: The receiver of this VatInvoiceResult.
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this VatInvoiceResult.

        收款人。 当“advanced_mode”设置为“true”时才返回。 

        :param receiver: The receiver of this VatInvoiceResult.
        :type receiver: str
        """
        self._receiver = receiver

    @property
    def reviewer(self):
        """Gets the reviewer of this VatInvoiceResult.

        复核。 当“advanced_mode”设置为“true”时才返回。 

        :return: The reviewer of this VatInvoiceResult.
        :rtype: str
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        """Sets the reviewer of this VatInvoiceResult.

        复核。 当“advanced_mode”设置为“true”时才返回。 

        :param reviewer: The reviewer of this VatInvoiceResult.
        :type reviewer: str
        """
        self._reviewer = reviewer

    @property
    def issuer(self):
        """Gets the issuer of this VatInvoiceResult.

        开票人。 当“advanced_mode”设置为“true”时才返回。 

        :return: The issuer of this VatInvoiceResult.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this VatInvoiceResult.

        开票人。 当“advanced_mode”设置为“true”时才返回。 

        :param issuer: The issuer of this VatInvoiceResult.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def seller_seal(self):
        """Gets the seller_seal of this VatInvoiceResult.

        销售方发票专用章。 当“advanced_mode”设置为“true”时才返回。 

        :return: The seller_seal of this VatInvoiceResult.
        :rtype: list[str]
        """
        return self._seller_seal

    @seller_seal.setter
    def seller_seal(self, seller_seal):
        """Sets the seller_seal of this VatInvoiceResult.

        销售方发票专用章。 当“advanced_mode”设置为“true”时才返回。 

        :param seller_seal: The seller_seal of this VatInvoiceResult.
        :type seller_seal: list[str]
        """
        self._seller_seal = seller_seal

    @property
    def item_list(self):
        """Gets the item_list of this VatInvoiceResult.

        货物或应税劳务列表。 

        :return: The item_list of this VatInvoiceResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.ItemList`]
        """
        return self._item_list

    @item_list.setter
    def item_list(self, item_list):
        """Sets the item_list of this VatInvoiceResult.

        货物或应税劳务列表。 

        :param item_list: The item_list of this VatInvoiceResult.
        :type item_list: list[:class:`huaweicloudsdkocr.v1.ItemList`]
        """
        self._item_list = item_list

    @property
    def confidence(self):
        """Gets the confidence of this VatInvoiceResult.

        各个字段的置信度。 当“advanced_mode”设置为“true”时才返回。 

        :return: The confidence of this VatInvoiceResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this VatInvoiceResult.

        各个字段的置信度。 当“advanced_mode”设置为“true”时才返回。 

        :param confidence: The confidence of this VatInvoiceResult.
        :type confidence: object
        """
        self._confidence = confidence

    @property
    def text_location(self):
        """Gets the text_location of this VatInvoiceResult.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。当“return_text_location”设置为“true”时才返回。 

        :return: The text_location of this VatInvoiceResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        """Sets the text_location of this VatInvoiceResult.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。当“return_text_location”设置为“true”时才返回。 

        :param text_location: The text_location of this VatInvoiceResult.
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
        if not isinstance(other, VatInvoiceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
