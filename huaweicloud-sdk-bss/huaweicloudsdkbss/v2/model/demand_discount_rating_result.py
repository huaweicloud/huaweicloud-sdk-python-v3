# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DemandDiscountRatingResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'discount_id': 'str',
        'discount_type': 'int',
        'amount': 'decimal.Decimal',
        'measure_id': 'int',
        'discount_name': 'str'
    }

    attribute_map = {
        'discount_id': 'discount_id',
        'discount_type': 'discount_type',
        'amount': 'amount',
        'measure_id': 'measure_id',
        'discount_name': 'discount_name'
    }

    def __init__(self, discount_id=None, discount_type=None, amount=None, measure_id=None, discount_name=None):
        """DemandDiscountRatingResult

        The model defined in huaweicloud sdk

        :param discount_id: 优惠标识ID。
        :type discount_id: str
        :param discount_type: 折扣优惠类型。 合同商务折扣：605：华为云BE场景下的合同商务折扣606：分销商BE场景下的合同商务折扣 伙伴授予折扣：607：合作伙伴授予折扣-折扣率
        :type discount_type: int
        :param amount: 折扣的金额。
        :type amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param measure_id: 度量单位标识。 1：元
        :type measure_id: int
        :param discount_name: 折扣名称。
        :type discount_name: str
        """
        
        

        self._discount_id = None
        self._discount_type = None
        self._amount = None
        self._measure_id = None
        self._discount_name = None
        self.discriminator = None

        if discount_id is not None:
            self.discount_id = discount_id
        if discount_type is not None:
            self.discount_type = discount_type
        if amount is not None:
            self.amount = amount
        if measure_id is not None:
            self.measure_id = measure_id
        if discount_name is not None:
            self.discount_name = discount_name

    @property
    def discount_id(self):
        """Gets the discount_id of this DemandDiscountRatingResult.

        优惠标识ID。

        :return: The discount_id of this DemandDiscountRatingResult.
        :rtype: str
        """
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        """Sets the discount_id of this DemandDiscountRatingResult.

        优惠标识ID。

        :param discount_id: The discount_id of this DemandDiscountRatingResult.
        :type discount_id: str
        """
        self._discount_id = discount_id

    @property
    def discount_type(self):
        """Gets the discount_type of this DemandDiscountRatingResult.

        折扣优惠类型。 合同商务折扣：605：华为云BE场景下的合同商务折扣606：分销商BE场景下的合同商务折扣 伙伴授予折扣：607：合作伙伴授予折扣-折扣率

        :return: The discount_type of this DemandDiscountRatingResult.
        :rtype: int
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this DemandDiscountRatingResult.

        折扣优惠类型。 合同商务折扣：605：华为云BE场景下的合同商务折扣606：分销商BE场景下的合同商务折扣 伙伴授予折扣：607：合作伙伴授予折扣-折扣率

        :param discount_type: The discount_type of this DemandDiscountRatingResult.
        :type discount_type: int
        """
        self._discount_type = discount_type

    @property
    def amount(self):
        """Gets the amount of this DemandDiscountRatingResult.

        折扣的金额。

        :return: The amount of this DemandDiscountRatingResult.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this DemandDiscountRatingResult.

        折扣的金额。

        :param amount: The amount of this DemandDiscountRatingResult.
        :type amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._amount = amount

    @property
    def measure_id(self):
        """Gets the measure_id of this DemandDiscountRatingResult.

        度量单位标识。 1：元

        :return: The measure_id of this DemandDiscountRatingResult.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this DemandDiscountRatingResult.

        度量单位标识。 1：元

        :param measure_id: The measure_id of this DemandDiscountRatingResult.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def discount_name(self):
        """Gets the discount_name of this DemandDiscountRatingResult.

        折扣名称。

        :return: The discount_name of this DemandDiscountRatingResult.
        :rtype: str
        """
        return self._discount_name

    @discount_name.setter
    def discount_name(self, discount_name):
        """Sets the discount_name of this DemandDiscountRatingResult.

        折扣名称。

        :param discount_name: The discount_name of this DemandDiscountRatingResult.
        :type discount_name: str
        """
        self._discount_name = discount_name

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
        if not isinstance(other, DemandDiscountRatingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
