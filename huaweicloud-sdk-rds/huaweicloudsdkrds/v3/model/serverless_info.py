# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerlessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_cap': 'str',
        'max_cap': 'str'
    }

    attribute_map = {
        'min_cap': 'min_cap',
        'max_cap': 'max_cap'
    }

    def __init__(self, min_cap=None, max_cap=None):
        r"""ServerlessInfo

        The model defined in huaweicloud sdk

        :param min_cap: Serverless型实例的最小算力，单位RCU，范围0.5~8，步进0.5。
        :type min_cap: str
        :param max_cap: Serverless型实例的最大算力，单位RCU，范围0.5~8，步进0.5。
        :type max_cap: str
        """
        
        

        self._min_cap = None
        self._max_cap = None
        self.discriminator = None

        self.min_cap = min_cap
        self.max_cap = max_cap

    @property
    def min_cap(self):
        r"""Gets the min_cap of this ServerlessInfo.

        Serverless型实例的最小算力，单位RCU，范围0.5~8，步进0.5。

        :return: The min_cap of this ServerlessInfo.
        :rtype: str
        """
        return self._min_cap

    @min_cap.setter
    def min_cap(self, min_cap):
        r"""Sets the min_cap of this ServerlessInfo.

        Serverless型实例的最小算力，单位RCU，范围0.5~8，步进0.5。

        :param min_cap: The min_cap of this ServerlessInfo.
        :type min_cap: str
        """
        self._min_cap = min_cap

    @property
    def max_cap(self):
        r"""Gets the max_cap of this ServerlessInfo.

        Serverless型实例的最大算力，单位RCU，范围0.5~8，步进0.5。

        :return: The max_cap of this ServerlessInfo.
        :rtype: str
        """
        return self._max_cap

    @max_cap.setter
    def max_cap(self, max_cap):
        r"""Sets the max_cap of this ServerlessInfo.

        Serverless型实例的最大算力，单位RCU，范围0.5~8，步进0.5。

        :param max_cap: The max_cap of this ServerlessInfo.
        :type max_cap: str
        """
        self._max_cap = max_cap

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
        if not isinstance(other, ServerlessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
