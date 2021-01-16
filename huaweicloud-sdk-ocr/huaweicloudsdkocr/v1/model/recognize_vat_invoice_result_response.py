# coding: utf-8

import pprint
import re

import six





class RecognizeVatInvoiceResultResponse:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'serial_number': 'str',
        'attribution': 'str',
        'supervision_seal': 'list[str]',
        'code': 'str',
        'machine_number': 'str',
        'print_number': 'str',
        'check_code': 'str',
        'number': 'str',
        'issue_id': 'str',
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
        'seller_seal': 'str',
        'item_list': 'list[ItemList]',
        'confidence': 'object'
    }

    attribute_map = {
        'type': 'type',
        'serial_number': 'serial_number',
        'attribution': 'attribution',
        'supervision_seal': 'supervision_seal',
        'code': 'code',
        'machine_number': 'machine_number',
        'print_number': 'print_number',
        'check_code': 'check_code',
        'number': 'number',
        'issue_id': 'issue_id',
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
        'confidence': 'confidence'
    }

    def __init__(self, type=None, serial_number=None, attribution=None, supervision_seal=None, code=None, machine_number=None, print_number=None, check_code=None, number=None, issue_id=None, issue_date=None, encryption_block=None, buyer_name=None, buyer_id=None, buyer_address=None, buyer_bank=None, seller_name=None, seller_id=None, seller_address=None, seller_bank=None, subtotal_amount=None, subtotal_tax=None, total=None, total_in_words=None, remarks=None, receiver=None, reviewer=None, issuer=None, seller_seal=None, item_list=None, confidence=None):
        """RecognizeVatInvoiceResultResponse - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._serial_number = None
        self._attribution = None
        self._supervision_seal = None
        self._code = None
        self._machine_number = None
        self._print_number = None
        self._check_code = None
        self._number = None
        self._issue_id = None
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
        self.discriminator = None

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
        if machine_number is not None:
            self.machine_number = machine_number
        if print_number is not None:
            self.print_number = print_number
        if check_code is not None:
            self.check_code = check_code
        if number is not None:
            self.number = number
        if issue_id is not None:
            self.issue_id = issue_id
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

    @property
    def type(self):
        """Gets the type of this RecognizeVatInvoiceResultResponse.

        增值税发票类型，可选值包括：  - special: 增值税专用发票  - normal: 增值税普通发票  - electronic: 增值税电子普通发票 

        :return: The type of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecognizeVatInvoiceResultResponse.

        增值税发票类型，可选值包括：  - special: 增值税专用发票  - normal: 增值税普通发票  - electronic: 增值税电子普通发票 

        :param type: The type of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._type = type

    @property
    def serial_number(self):
        """Gets the serial_number of this RecognizeVatInvoiceResultResponse.

        发票联次。 当“advanced_mode”设置为“true”时才返回。 

        :return: The serial_number of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this RecognizeVatInvoiceResultResponse.

        发票联次。 当“advanced_mode”设置为“true”时才返回。 

        :param serial_number: The serial_number of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def attribution(self):
        """Gets the attribution of this RecognizeVatInvoiceResultResponse.

        发票归属地。 当“advanced_mode”设置为“true”时才返回。 

        :return: The attribution of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """Sets the attribution of this RecognizeVatInvoiceResultResponse.

        发票归属地。 当“advanced_mode”设置为“true”时才返回。 

        :param attribution: The attribution of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._attribution = attribution

    @property
    def supervision_seal(self):
        """Gets the supervision_seal of this RecognizeVatInvoiceResultResponse.

        发票监制章。 当“advanced_mode”设置为“true”时才返回。 

        :return: The supervision_seal of this RecognizeVatInvoiceResultResponse.
        :rtype: list[str]
        """
        return self._supervision_seal

    @supervision_seal.setter
    def supervision_seal(self, supervision_seal):
        """Sets the supervision_seal of this RecognizeVatInvoiceResultResponse.

        发票监制章。 当“advanced_mode”设置为“true”时才返回。 

        :param supervision_seal: The supervision_seal of this RecognizeVatInvoiceResultResponse.
        :type: list[str]
        """
        self._supervision_seal = supervision_seal

    @property
    def code(self):
        """Gets the code of this RecognizeVatInvoiceResultResponse.

        发票代码。 

        :return: The code of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RecognizeVatInvoiceResultResponse.

        发票代码。 

        :param code: The code of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._code = code

    @property
    def machine_number(self):
        """Gets the machine_number of this RecognizeVatInvoiceResultResponse.

        机器编号。 当“advanced_mode”设置为“true”时才返回。 

        :return: The machine_number of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._machine_number

    @machine_number.setter
    def machine_number(self, machine_number):
        """Sets the machine_number of this RecognizeVatInvoiceResultResponse.

        机器编号。 当“advanced_mode”设置为“true”时才返回。 

        :param machine_number: The machine_number of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._machine_number = machine_number

    @property
    def print_number(self):
        """Gets the print_number of this RecognizeVatInvoiceResultResponse.

        机打号码。 当“advanced_mode”设置为“true”时才返回 

        :return: The print_number of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._print_number

    @print_number.setter
    def print_number(self, print_number):
        """Sets the print_number of this RecognizeVatInvoiceResultResponse.

        机打号码。 当“advanced_mode”设置为“true”时才返回 

        :param print_number: The print_number of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._print_number = print_number

    @property
    def check_code(self):
        """Gets the check_code of this RecognizeVatInvoiceResultResponse.

        发票校验码，特定类型增值税发票内不存在该信息时返回空字符串。 

        :return: The check_code of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._check_code

    @check_code.setter
    def check_code(self, check_code):
        """Sets the check_code of this RecognizeVatInvoiceResultResponse.

        发票校验码，特定类型增值税发票内不存在该信息时返回空字符串。 

        :param check_code: The check_code of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._check_code = check_code

    @property
    def number(self):
        """Gets the number of this RecognizeVatInvoiceResultResponse.

        发票号码。 

        :return: The number of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this RecognizeVatInvoiceResultResponse.

        发票号码。 

        :param number: The number of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._number = number

    @property
    def issue_id(self):
        """Gets the issue_id of this RecognizeVatInvoiceResultResponse.

        发票号码。 

        :return: The issue_id of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this RecognizeVatInvoiceResultResponse.

        发票号码。 

        :param issue_id: The issue_id of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._issue_id = issue_id

    @property
    def issue_date(self):
        """Gets the issue_date of this RecognizeVatInvoiceResultResponse.

        开票日期。 

        :return: The issue_date of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this RecognizeVatInvoiceResultResponse.

        开票日期。 

        :param issue_date: The issue_date of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._issue_date = issue_date

    @property
    def encryption_block(self):
        """Gets the encryption_block of this RecognizeVatInvoiceResultResponse.

        密码区。 

        :return: The encryption_block of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._encryption_block

    @encryption_block.setter
    def encryption_block(self, encryption_block):
        """Sets the encryption_block of this RecognizeVatInvoiceResultResponse.

        密码区。 

        :param encryption_block: The encryption_block of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._encryption_block = encryption_block

    @property
    def buyer_name(self):
        """Gets the buyer_name of this RecognizeVatInvoiceResultResponse.

        购买方名称。 

        :return: The buyer_name of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, buyer_name):
        """Sets the buyer_name of this RecognizeVatInvoiceResultResponse.

        购买方名称。 

        :param buyer_name: The buyer_name of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._buyer_name = buyer_name

    @property
    def buyer_id(self):
        """Gets the buyer_id of this RecognizeVatInvoiceResultResponse.

        购买方纳税人识别号。 

        :return: The buyer_id of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, buyer_id):
        """Sets the buyer_id of this RecognizeVatInvoiceResultResponse.

        购买方纳税人识别号。 

        :param buyer_id: The buyer_id of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._buyer_id = buyer_id

    @property
    def buyer_address(self):
        """Gets the buyer_address of this RecognizeVatInvoiceResultResponse.

        购买方地址、电话。 

        :return: The buyer_address of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, buyer_address):
        """Sets the buyer_address of this RecognizeVatInvoiceResultResponse.

        购买方地址、电话。 

        :param buyer_address: The buyer_address of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._buyer_address = buyer_address

    @property
    def buyer_bank(self):
        """Gets the buyer_bank of this RecognizeVatInvoiceResultResponse.

        购买方开户行及帐号。 

        :return: The buyer_bank of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._buyer_bank

    @buyer_bank.setter
    def buyer_bank(self, buyer_bank):
        """Sets the buyer_bank of this RecognizeVatInvoiceResultResponse.

        购买方开户行及帐号。 

        :param buyer_bank: The buyer_bank of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._buyer_bank = buyer_bank

    @property
    def seller_name(self):
        """Gets the seller_name of this RecognizeVatInvoiceResultResponse.

        销售方名称。 

        :return: The seller_name of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._seller_name

    @seller_name.setter
    def seller_name(self, seller_name):
        """Sets the seller_name of this RecognizeVatInvoiceResultResponse.

        销售方名称。 

        :param seller_name: The seller_name of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._seller_name = seller_name

    @property
    def seller_id(self):
        """Gets the seller_id of this RecognizeVatInvoiceResultResponse.

        销售方纳税人识别号。 

        :return: The seller_id of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        """Sets the seller_id of this RecognizeVatInvoiceResultResponse.

        销售方纳税人识别号。 

        :param seller_id: The seller_id of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._seller_id = seller_id

    @property
    def seller_address(self):
        """Gets the seller_address of this RecognizeVatInvoiceResultResponse.

        销售方地址、电话。 

        :return: The seller_address of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._seller_address

    @seller_address.setter
    def seller_address(self, seller_address):
        """Sets the seller_address of this RecognizeVatInvoiceResultResponse.

        销售方地址、电话。 

        :param seller_address: The seller_address of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._seller_address = seller_address

    @property
    def seller_bank(self):
        """Gets the seller_bank of this RecognizeVatInvoiceResultResponse.

        销售方开户行及帐号。 

        :return: The seller_bank of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._seller_bank

    @seller_bank.setter
    def seller_bank(self, seller_bank):
        """Sets the seller_bank of this RecognizeVatInvoiceResultResponse.

        销售方开户行及帐号。 

        :param seller_bank: The seller_bank of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._seller_bank = seller_bank

    @property
    def subtotal_amount(self):
        """Gets the subtotal_amount of this RecognizeVatInvoiceResultResponse.

        合计金额。 

        :return: The subtotal_amount of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._subtotal_amount

    @subtotal_amount.setter
    def subtotal_amount(self, subtotal_amount):
        """Sets the subtotal_amount of this RecognizeVatInvoiceResultResponse.

        合计金额。 

        :param subtotal_amount: The subtotal_amount of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._subtotal_amount = subtotal_amount

    @property
    def subtotal_tax(self):
        """Gets the subtotal_tax of this RecognizeVatInvoiceResultResponse.

        合计税额。 

        :return: The subtotal_tax of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._subtotal_tax

    @subtotal_tax.setter
    def subtotal_tax(self, subtotal_tax):
        """Sets the subtotal_tax of this RecognizeVatInvoiceResultResponse.

        合计税额。 

        :param subtotal_tax: The subtotal_tax of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._subtotal_tax = subtotal_tax

    @property
    def total(self):
        """Gets the total of this RecognizeVatInvoiceResultResponse.

        价税合计。 

        :return: The total of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this RecognizeVatInvoiceResultResponse.

        价税合计。 

        :param total: The total of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._total = total

    @property
    def total_in_words(self):
        """Gets the total_in_words of this RecognizeVatInvoiceResultResponse.

        价税合计（大写）。 当“advanced_mode”设置为“true”时才返回。 

        :return: The total_in_words of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._total_in_words

    @total_in_words.setter
    def total_in_words(self, total_in_words):
        """Sets the total_in_words of this RecognizeVatInvoiceResultResponse.

        价税合计（大写）。 当“advanced_mode”设置为“true”时才返回。 

        :param total_in_words: The total_in_words of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._total_in_words = total_in_words

    @property
    def remarks(self):
        """Gets the remarks of this RecognizeVatInvoiceResultResponse.

        备注。 当“advanced_mode”设置为“true”时才返回。 

        :return: The remarks of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this RecognizeVatInvoiceResultResponse.

        备注。 当“advanced_mode”设置为“true”时才返回。 

        :param remarks: The remarks of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._remarks = remarks

    @property
    def receiver(self):
        """Gets the receiver of this RecognizeVatInvoiceResultResponse.

        收款人。 当“advanced_mode”设置为“true”时才返回。 

        :return: The receiver of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this RecognizeVatInvoiceResultResponse.

        收款人。 当“advanced_mode”设置为“true”时才返回。 

        :param receiver: The receiver of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._receiver = receiver

    @property
    def reviewer(self):
        """Gets the reviewer of this RecognizeVatInvoiceResultResponse.

        复核。 当“advanced_mode”设置为“true”时才返回。 

        :return: The reviewer of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        """Sets the reviewer of this RecognizeVatInvoiceResultResponse.

        复核。 当“advanced_mode”设置为“true”时才返回。 

        :param reviewer: The reviewer of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._reviewer = reviewer

    @property
    def issuer(self):
        """Gets the issuer of this RecognizeVatInvoiceResultResponse.

        开票人。 当“advanced_mode”设置为“true”时才返回。 

        :return: The issuer of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this RecognizeVatInvoiceResultResponse.

        开票人。 当“advanced_mode”设置为“true”时才返回。 

        :param issuer: The issuer of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._issuer = issuer

    @property
    def seller_seal(self):
        """Gets the seller_seal of this RecognizeVatInvoiceResultResponse.

        销售方发票专用章。 当“advanced_mode”设置为“true”时才返回。 

        :return: The seller_seal of this RecognizeVatInvoiceResultResponse.
        :rtype: str
        """
        return self._seller_seal

    @seller_seal.setter
    def seller_seal(self, seller_seal):
        """Sets the seller_seal of this RecognizeVatInvoiceResultResponse.

        销售方发票专用章。 当“advanced_mode”设置为“true”时才返回。 

        :param seller_seal: The seller_seal of this RecognizeVatInvoiceResultResponse.
        :type: str
        """
        self._seller_seal = seller_seal

    @property
    def item_list(self):
        """Gets the item_list of this RecognizeVatInvoiceResultResponse.

        货物或应税劳务列表。 

        :return: The item_list of this RecognizeVatInvoiceResultResponse.
        :rtype: list[ItemList]
        """
        return self._item_list

    @item_list.setter
    def item_list(self, item_list):
        """Sets the item_list of this RecognizeVatInvoiceResultResponse.

        货物或应税劳务列表。 

        :param item_list: The item_list of this RecognizeVatInvoiceResultResponse.
        :type: list[ItemList]
        """
        self._item_list = item_list

    @property
    def confidence(self):
        """Gets the confidence of this RecognizeVatInvoiceResultResponse.

        各个字段的置信度。 当“advanced_mode”设置为“true”时才返回。 

        :return: The confidence of this RecognizeVatInvoiceResultResponse.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this RecognizeVatInvoiceResultResponse.

        各个字段的置信度。 当“advanced_mode”设置为“true”时才返回。 

        :param confidence: The confidence of this RecognizeVatInvoiceResultResponse.
        :type: object
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecognizeVatInvoiceResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
