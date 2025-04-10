# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionManagement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'driver_management': 'DriverManagement'
    }

    attribute_map = {
        'driver_management': 'driver_management'
    }

    def __init__(self, driver_management=None):
        r"""ConnectionManagement

        The model defined in huaweicloud sdk

        :param driver_management: 
        :type driver_management: :class:`huaweicloudsdkdrs.v5.DriverManagement`
        """
        
        

        self._driver_management = None
        self.discriminator = None

        if driver_management is not None:
            self.driver_management = driver_management

    @property
    def driver_management(self):
        r"""Gets the driver_management of this ConnectionManagement.

        :return: The driver_management of this ConnectionManagement.
        :rtype: :class:`huaweicloudsdkdrs.v5.DriverManagement`
        """
        return self._driver_management

    @driver_management.setter
    def driver_management(self, driver_management):
        r"""Sets the driver_management of this ConnectionManagement.

        :param driver_management: The driver_management of this ConnectionManagement.
        :type driver_management: :class:`huaweicloudsdkdrs.v5.DriverManagement`
        """
        self._driver_management = driver_management

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
        if not isinstance(other, ConnectionManagement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
