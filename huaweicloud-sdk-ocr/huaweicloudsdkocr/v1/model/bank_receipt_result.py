# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BankReceiptResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bank_receipt_count': 'int',
        'bank_receipt_list': 'list[BankReceiptDict]'
    }

    attribute_map = {
        'bank_receipt_count': 'bank_receipt_count',
        'bank_receipt_list': 'bank_receipt_list'
    }

    def __init__(self, bank_receipt_count=None, bank_receipt_list=None):
        r"""BankReceiptResult

        The model defined in huaweicloud sdk

        :param bank_receipt_count: 银行回单数量 
        :type bank_receipt_count: int
        :param bank_receipt_list: 银行回单键值对提取结果。 
        :type bank_receipt_list: list[:class:`huaweicloudsdkocr.v1.BankReceiptDict`]
        """
        
        

        self._bank_receipt_count = None
        self._bank_receipt_list = None
        self.discriminator = None

        if bank_receipt_count is not None:
            self.bank_receipt_count = bank_receipt_count
        if bank_receipt_list is not None:
            self.bank_receipt_list = bank_receipt_list

    @property
    def bank_receipt_count(self):
        r"""Gets the bank_receipt_count of this BankReceiptResult.

        银行回单数量 

        :return: The bank_receipt_count of this BankReceiptResult.
        :rtype: int
        """
        return self._bank_receipt_count

    @bank_receipt_count.setter
    def bank_receipt_count(self, bank_receipt_count):
        r"""Sets the bank_receipt_count of this BankReceiptResult.

        银行回单数量 

        :param bank_receipt_count: The bank_receipt_count of this BankReceiptResult.
        :type bank_receipt_count: int
        """
        self._bank_receipt_count = bank_receipt_count

    @property
    def bank_receipt_list(self):
        r"""Gets the bank_receipt_list of this BankReceiptResult.

        银行回单键值对提取结果。 

        :return: The bank_receipt_list of this BankReceiptResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.BankReceiptDict`]
        """
        return self._bank_receipt_list

    @bank_receipt_list.setter
    def bank_receipt_list(self, bank_receipt_list):
        r"""Sets the bank_receipt_list of this BankReceiptResult.

        银行回单键值对提取结果。 

        :param bank_receipt_list: The bank_receipt_list of this BankReceiptResult.
        :type bank_receipt_list: list[:class:`huaweicloudsdkocr.v1.BankReceiptDict`]
        """
        self._bank_receipt_list = bank_receipt_list

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
        if not isinstance(other, BankReceiptResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
