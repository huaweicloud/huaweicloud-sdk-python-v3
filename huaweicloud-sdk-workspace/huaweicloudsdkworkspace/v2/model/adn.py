# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Adn:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'str',
        'bandwidth_size': 'int'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'bandwidth_size': 'bandwidth_size'
    }

    def __init__(self, charge_mode=None, bandwidth_size=None):
        """Adn

        The model defined in huaweicloud sdk

        :param charge_mode: adn带宽计费模式 - free：不计费。
        :type charge_mode: str
        :param bandwidth_size: 带宽大小，charge_mode为free时，不支持配置。
        :type bandwidth_size: int
        """
        
        

        self._charge_mode = None
        self._bandwidth_size = None
        self.discriminator = None

        self.charge_mode = charge_mode
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size

    @property
    def charge_mode(self):
        """Gets the charge_mode of this Adn.

        adn带宽计费模式 - free：不计费。

        :return: The charge_mode of this Adn.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this Adn.

        adn带宽计费模式 - free：不计费。

        :param charge_mode: The charge_mode of this Adn.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this Adn.

        带宽大小，charge_mode为free时，不支持配置。

        :return: The bandwidth_size of this Adn.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this Adn.

        带宽大小，charge_mode为free时，不支持配置。

        :param bandwidth_size: The bandwidth_size of this Adn.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

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
        if not isinstance(other, Adn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
