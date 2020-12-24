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
        'code': 'str',
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
        'item_list': 'list[RecognizeVatInvoiceItemsResponse]'
    }

    attribute_map = {
        'type': 'type',
        'code': 'code',
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
        'item_list': 'item_list'
    }

    def __init__(self, type=None, code=None, check_code=None, number=None, issue_date=None, encryption_block=None, buyer_name=None, buyer_id=None, buyer_address=None, buyer_bank=None, seller_name=None, seller_id=None, seller_address=None, seller_bank=None, subtotal_amount=None, subtotal_tax=None, total=None, item_list=None):
        """RecognizeVatInvoiceResultResponse - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._code = None
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
        self._item_list = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if code is not None:
            self.code = code
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
        if item_list is not None:
            self.item_list = item_list

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
    def item_list(self):
        """Gets the item_list of this RecognizeVatInvoiceResultResponse.

        货物或应税劳务列表。 

        :return: The item_list of this RecognizeVatInvoiceResultResponse.
        :rtype: list[RecognizeVatInvoiceItemsResponse]
        """
        return self._item_list

    @item_list.setter
    def item_list(self, item_list):
        """Sets the item_list of this RecognizeVatInvoiceResultResponse.

        货物或应税劳务列表。 

        :param item_list: The item_list of this RecognizeVatInvoiceResultResponse.
        :type: list[RecognizeVatInvoiceItemsResponse]
        """
        self._item_list = item_list

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
