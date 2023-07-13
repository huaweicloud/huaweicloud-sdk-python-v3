# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLeftQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quantity': 'int',
        'cpu': 'int',
        'ram': 'int'
    }

    attribute_map = {
        'quantity': 'quantity',
        'cpu': 'cpu',
        'ram': 'ram'
    }

    def __init__(self, quantity=None, cpu=None, ram=None):
        """ShowLeftQuotaResponse

        The model defined in huaweicloud sdk

        :param quantity: 剩余服务器数
        :type quantity: int
        :param cpu: 剩余CPU
        :type cpu: int
        :param ram: 剩余内存
        :type ram: int
        """
        
        super(ShowLeftQuotaResponse, self).__init__()

        self._quantity = None
        self._cpu = None
        self._ram = None
        self.discriminator = None

        if quantity is not None:
            self.quantity = quantity
        if cpu is not None:
            self.cpu = cpu
        if ram is not None:
            self.ram = ram

    @property
    def quantity(self):
        """Gets the quantity of this ShowLeftQuotaResponse.

        剩余服务器数

        :return: The quantity of this ShowLeftQuotaResponse.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ShowLeftQuotaResponse.

        剩余服务器数

        :param quantity: The quantity of this ShowLeftQuotaResponse.
        :type quantity: int
        """
        self._quantity = quantity

    @property
    def cpu(self):
        """Gets the cpu of this ShowLeftQuotaResponse.

        剩余CPU

        :return: The cpu of this ShowLeftQuotaResponse.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ShowLeftQuotaResponse.

        剩余CPU

        :param cpu: The cpu of this ShowLeftQuotaResponse.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def ram(self):
        """Gets the ram of this ShowLeftQuotaResponse.

        剩余内存

        :return: The ram of this ShowLeftQuotaResponse.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this ShowLeftQuotaResponse.

        剩余内存

        :param ram: The ram of this ShowLeftQuotaResponse.
        :type ram: int
        """
        self._ram = ram

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
        if not isinstance(other, ShowLeftQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
