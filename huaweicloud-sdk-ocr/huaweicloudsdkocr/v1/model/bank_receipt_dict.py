# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BankReceiptDict:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kv_pair_count': 'int',
        'bank_receipt_location': 'list[list[int]]',
        'kv_pair_list': 'list[BankReceiptKvPair]'
    }

    attribute_map = {
        'kv_pair_count': 'kv_pair_count',
        'bank_receipt_location': 'bank_receipt_location',
        'kv_pair_list': 'kv_pair_list'
    }

    def __init__(self, kv_pair_count=None, bank_receipt_location=None, kv_pair_list=None):
        r"""BankReceiptDict

        The model defined in huaweicloud sdk

        :param kv_pair_count: 键值对数量 
        :type kv_pair_count: int
        :param bank_receipt_location: 银行回单的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type bank_receipt_location: list[list[int]]
        :param kv_pair_list: 键值对识别结果列表。 
        :type kv_pair_list: list[:class:`huaweicloudsdkocr.v1.BankReceiptKvPair`]
        """
        
        

        self._kv_pair_count = None
        self._bank_receipt_location = None
        self._kv_pair_list = None
        self.discriminator = None

        if kv_pair_count is not None:
            self.kv_pair_count = kv_pair_count
        if bank_receipt_location is not None:
            self.bank_receipt_location = bank_receipt_location
        if kv_pair_list is not None:
            self.kv_pair_list = kv_pair_list

    @property
    def kv_pair_count(self):
        r"""Gets the kv_pair_count of this BankReceiptDict.

        键值对数量 

        :return: The kv_pair_count of this BankReceiptDict.
        :rtype: int
        """
        return self._kv_pair_count

    @kv_pair_count.setter
    def kv_pair_count(self, kv_pair_count):
        r"""Sets the kv_pair_count of this BankReceiptDict.

        键值对数量 

        :param kv_pair_count: The kv_pair_count of this BankReceiptDict.
        :type kv_pair_count: int
        """
        self._kv_pair_count = kv_pair_count

    @property
    def bank_receipt_location(self):
        r"""Gets the bank_receipt_location of this BankReceiptDict.

        银行回单的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The bank_receipt_location of this BankReceiptDict.
        :rtype: list[list[int]]
        """
        return self._bank_receipt_location

    @bank_receipt_location.setter
    def bank_receipt_location(self, bank_receipt_location):
        r"""Sets the bank_receipt_location of this BankReceiptDict.

        银行回单的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param bank_receipt_location: The bank_receipt_location of this BankReceiptDict.
        :type bank_receipt_location: list[list[int]]
        """
        self._bank_receipt_location = bank_receipt_location

    @property
    def kv_pair_list(self):
        r"""Gets the kv_pair_list of this BankReceiptDict.

        键值对识别结果列表。 

        :return: The kv_pair_list of this BankReceiptDict.
        :rtype: list[:class:`huaweicloudsdkocr.v1.BankReceiptKvPair`]
        """
        return self._kv_pair_list

    @kv_pair_list.setter
    def kv_pair_list(self, kv_pair_list):
        r"""Sets the kv_pair_list of this BankReceiptDict.

        键值对识别结果列表。 

        :param kv_pair_list: The kv_pair_list of this BankReceiptDict.
        :type kv_pair_list: list[:class:`huaweicloudsdkocr.v1.BankReceiptKvPair`]
        """
        self._kv_pair_list = kv_pair_list

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
        if not isinstance(other, BankReceiptDict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
