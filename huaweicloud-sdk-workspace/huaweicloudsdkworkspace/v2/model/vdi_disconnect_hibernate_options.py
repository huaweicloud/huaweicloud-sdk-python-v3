# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VdiDisconnectHibernateOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disconnect_hibernate_minutes': 'int'
    }

    attribute_map = {
        'disconnect_hibernate_minutes': 'disconnect_hibernate_minutes'
    }

    def __init__(self, disconnect_hibernate_minutes=None):
        r"""VdiDisconnectHibernateOptions

        The model defined in huaweicloud sdk

        :param disconnect_hibernate_minutes: 断连休眠时间。
        :type disconnect_hibernate_minutes: int
        """
        
        

        self._disconnect_hibernate_minutes = None
        self.discriminator = None

        if disconnect_hibernate_minutes is not None:
            self.disconnect_hibernate_minutes = disconnect_hibernate_minutes

    @property
    def disconnect_hibernate_minutes(self):
        r"""Gets the disconnect_hibernate_minutes of this VdiDisconnectHibernateOptions.

        断连休眠时间。

        :return: The disconnect_hibernate_minutes of this VdiDisconnectHibernateOptions.
        :rtype: int
        """
        return self._disconnect_hibernate_minutes

    @disconnect_hibernate_minutes.setter
    def disconnect_hibernate_minutes(self, disconnect_hibernate_minutes):
        r"""Sets the disconnect_hibernate_minutes of this VdiDisconnectHibernateOptions.

        断连休眠时间。

        :param disconnect_hibernate_minutes: The disconnect_hibernate_minutes of this VdiDisconnectHibernateOptions.
        :type disconnect_hibernate_minutes: int
        """
        self._disconnect_hibernate_minutes = disconnect_hibernate_minutes

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
        if not isinstance(other, VdiDisconnectHibernateOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
