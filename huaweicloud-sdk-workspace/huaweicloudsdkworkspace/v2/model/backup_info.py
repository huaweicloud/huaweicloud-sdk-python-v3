# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'priority': 'int',
        'address': 'str',
        'address_custom': 'str'
    }

    attribute_map = {
        'priority': 'priority',
        'address': 'address',
        'address_custom': 'address_custom'
    }

    def __init__(self, priority=None, address=None, address_custom=None):
        r"""BackupInfo

        The model defined in huaweicloud sdk

        :param priority: 优先级，数字越小，优先级越高，取值1-255。
        :type priority: int
        :param address: 接入备份地址。
        :type address: str
        :param address_custom: 租户自定义接入备份地址。
        :type address_custom: str
        """
        
        

        self._priority = None
        self._address = None
        self._address_custom = None
        self.discriminator = None

        self.priority = priority
        self.address = address
        if address_custom is not None:
            self.address_custom = address_custom

    @property
    def priority(self):
        r"""Gets the priority of this BackupInfo.

        优先级，数字越小，优先级越高，取值1-255。

        :return: The priority of this BackupInfo.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this BackupInfo.

        优先级，数字越小，优先级越高，取值1-255。

        :param priority: The priority of this BackupInfo.
        :type priority: int
        """
        self._priority = priority

    @property
    def address(self):
        r"""Gets the address of this BackupInfo.

        接入备份地址。

        :return: The address of this BackupInfo.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this BackupInfo.

        接入备份地址。

        :param address: The address of this BackupInfo.
        :type address: str
        """
        self._address = address

    @property
    def address_custom(self):
        r"""Gets the address_custom of this BackupInfo.

        租户自定义接入备份地址。

        :return: The address_custom of this BackupInfo.
        :rtype: str
        """
        return self._address_custom

    @address_custom.setter
    def address_custom(self, address_custom):
        r"""Sets the address_custom of this BackupInfo.

        租户自定义接入备份地址。

        :param address_custom: The address_custom of this BackupInfo.
        :type address_custom: str
        """
        self._address_custom = address_custom

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
        if not isinstance(other, BackupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
