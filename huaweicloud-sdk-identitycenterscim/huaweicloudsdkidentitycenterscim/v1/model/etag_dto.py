# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EtagDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'supported': 'bool'
    }

    attribute_map = {
        'supported': 'supported'
    }

    def __init__(self, supported=None):
        r"""EtagDto

        The model defined in huaweicloud sdk

        :param supported: 一个布尔值，表示服务提供商是否支持这种操作
        :type supported: bool
        """
        
        

        self._supported = None
        self.discriminator = None

        if supported is not None:
            self.supported = supported

    @property
    def supported(self):
        r"""Gets the supported of this EtagDto.

        一个布尔值，表示服务提供商是否支持这种操作

        :return: The supported of this EtagDto.
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        r"""Sets the supported of this EtagDto.

        一个布尔值，表示服务提供商是否支持这种操作

        :param supported: The supported of this EtagDto.
        :type supported: bool
        """
        self._supported = supported

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
        if not isinstance(other, EtagDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
