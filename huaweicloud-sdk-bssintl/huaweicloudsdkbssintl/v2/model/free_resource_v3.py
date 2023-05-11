# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FreeResourceV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'free_resource_id': 'str',
        'usage_type_name': 'str',
        'amount': 'str',
        'original_amount': 'str',
        'measure_id': 'int'
    }

    attribute_map = {
        'free_resource_id': 'free_resource_id',
        'usage_type_name': 'usage_type_name',
        'amount': 'amount',
        'original_amount': 'original_amount',
        'measure_id': 'measure_id'
    }

    def __init__(self, free_resource_id=None, usage_type_name=None, amount=None, original_amount=None, measure_id=None):
        """FreeResourceV3

        The model defined in huaweicloud sdk

        :param free_resource_id: 资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。
        :type free_resource_id: str
        :param usage_type_name: 使用量类型名称。
        :type usage_type_name: str
        :param amount: 资源剩余额度，针对可重置资源包，是指当前重置周期内的剩余量。
        :type amount: str
        :param original_amount: 资源原始额度，针对可重置资源包，是指每个重置周期内的总量。
        :type original_amount: str
        :param measure_id: 度量单位，免费资源套餐额度度量单位。您可以调用查询度量单位列表接口获取。
        :type measure_id: int
        """
        
        

        self._free_resource_id = None
        self._usage_type_name = None
        self._amount = None
        self._original_amount = None
        self._measure_id = None
        self.discriminator = None

        if free_resource_id is not None:
            self.free_resource_id = free_resource_id
        if usage_type_name is not None:
            self.usage_type_name = usage_type_name
        if amount is not None:
            self.amount = amount
        if original_amount is not None:
            self.original_amount = original_amount
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def free_resource_id(self):
        """Gets the free_resource_id of this FreeResourceV3.

        资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。

        :return: The free_resource_id of this FreeResourceV3.
        :rtype: str
        """
        return self._free_resource_id

    @free_resource_id.setter
    def free_resource_id(self, free_resource_id):
        """Sets the free_resource_id of this FreeResourceV3.

        资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。

        :param free_resource_id: The free_resource_id of this FreeResourceV3.
        :type free_resource_id: str
        """
        self._free_resource_id = free_resource_id

    @property
    def usage_type_name(self):
        """Gets the usage_type_name of this FreeResourceV3.

        使用量类型名称。

        :return: The usage_type_name of this FreeResourceV3.
        :rtype: str
        """
        return self._usage_type_name

    @usage_type_name.setter
    def usage_type_name(self, usage_type_name):
        """Sets the usage_type_name of this FreeResourceV3.

        使用量类型名称。

        :param usage_type_name: The usage_type_name of this FreeResourceV3.
        :type usage_type_name: str
        """
        self._usage_type_name = usage_type_name

    @property
    def amount(self):
        """Gets the amount of this FreeResourceV3.

        资源剩余额度，针对可重置资源包，是指当前重置周期内的剩余量。

        :return: The amount of this FreeResourceV3.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FreeResourceV3.

        资源剩余额度，针对可重置资源包，是指当前重置周期内的剩余量。

        :param amount: The amount of this FreeResourceV3.
        :type amount: str
        """
        self._amount = amount

    @property
    def original_amount(self):
        """Gets the original_amount of this FreeResourceV3.

        资源原始额度，针对可重置资源包，是指每个重置周期内的总量。

        :return: The original_amount of this FreeResourceV3.
        :rtype: str
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        """Sets the original_amount of this FreeResourceV3.

        资源原始额度，针对可重置资源包，是指每个重置周期内的总量。

        :param original_amount: The original_amount of this FreeResourceV3.
        :type original_amount: str
        """
        self._original_amount = original_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this FreeResourceV3.

        度量单位，免费资源套餐额度度量单位。您可以调用查询度量单位列表接口获取。

        :return: The measure_id of this FreeResourceV3.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this FreeResourceV3.

        度量单位，免费资源套餐额度度量单位。您可以调用查询度量单位列表接口获取。

        :param measure_id: The measure_id of this FreeResourceV3.
        :type measure_id: int
        """
        self._measure_id = measure_id

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
        if not isinstance(other, FreeResourceV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
