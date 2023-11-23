# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDriverReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'driver_name': 'str'
    }

    attribute_map = {
        'driver_name': 'driver_name'
    }

    def __init__(self, driver_name=None):
        """UpdateDriverReq

        The model defined in huaweicloud sdk

        :param driver_name: jdbc驱动文件名称，name的长度5-64，结尾以.jar结尾。
        :type driver_name: str
        """
        
        

        self._driver_name = None
        self.discriminator = None

        self.driver_name = driver_name

    @property
    def driver_name(self):
        """Gets the driver_name of this UpdateDriverReq.

        jdbc驱动文件名称，name的长度5-64，结尾以.jar结尾。

        :return: The driver_name of this UpdateDriverReq.
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        """Sets the driver_name of this UpdateDriverReq.

        jdbc驱动文件名称，name的长度5-64，结尾以.jar结尾。

        :param driver_name: The driver_name of this UpdateDriverReq.
        :type driver_name: str
        """
        self._driver_name = driver_name

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
        if not isinstance(other, UpdateDriverReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
