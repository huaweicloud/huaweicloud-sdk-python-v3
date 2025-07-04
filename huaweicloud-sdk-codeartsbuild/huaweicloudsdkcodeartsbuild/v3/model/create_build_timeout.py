# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBuildTimeout:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'unit': 'unit'
    }

    def __init__(self, limit=None, unit=None):
        r"""CreateBuildTimeout

        The model defined in huaweicloud sdk

        :param limit: 超时时间数值
        :type limit: str
        :param unit: 超时时间单位
        :type unit: str
        """
        
        

        self._limit = None
        self._unit = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if unit is not None:
            self.unit = unit

    @property
    def limit(self):
        r"""Gets the limit of this CreateBuildTimeout.

        超时时间数值

        :return: The limit of this CreateBuildTimeout.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this CreateBuildTimeout.

        超时时间数值

        :param limit: The limit of this CreateBuildTimeout.
        :type limit: str
        """
        self._limit = limit

    @property
    def unit(self):
        r"""Gets the unit of this CreateBuildTimeout.

        超时时间单位

        :return: The unit of this CreateBuildTimeout.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this CreateBuildTimeout.

        超时时间单位

        :param unit: The unit of this CreateBuildTimeout.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, CreateBuildTimeout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
