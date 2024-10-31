# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceDemand:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min': 'int',
        'max': 'int',
        'spec_code': 'str'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max',
        'spec_code': 'spec_code'
    }

    def __init__(self, min=None, max=None, spec_code=None):
        """ResourceDemand

        The model defined in huaweicloud sdk

        :param min: 最小数
        :type min: int
        :param max: 最大数，最小值为1，最大值为1000。
        :type max: int
        :param spec_code: 资源规格，从规格列表查询获取。
        :type spec_code: str
        """
        
        

        self._min = None
        self._max = None
        self._spec_code = None
        self.discriminator = None

        self.min = min
        self.max = max
        self.spec_code = spec_code

    @property
    def min(self):
        """Gets the min of this ResourceDemand.

        最小数

        :return: The min of this ResourceDemand.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ResourceDemand.

        最小数

        :param min: The min of this ResourceDemand.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this ResourceDemand.

        最大数，最小值为1，最大值为1000。

        :return: The max of this ResourceDemand.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ResourceDemand.

        最大数，最小值为1，最大值为1000。

        :param max: The max of this ResourceDemand.
        :type max: int
        """
        self._max = max

    @property
    def spec_code(self):
        """Gets the spec_code of this ResourceDemand.

        资源规格，从规格列表查询获取。

        :return: The spec_code of this ResourceDemand.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ResourceDemand.

        资源规格，从规格列表查询获取。

        :param spec_code: The spec_code of this ResourceDemand.
        :type spec_code: str
        """
        self._spec_code = spec_code

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
        if not isinstance(other, ResourceDemand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
