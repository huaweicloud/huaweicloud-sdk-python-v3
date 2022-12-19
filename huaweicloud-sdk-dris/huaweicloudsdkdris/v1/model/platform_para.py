# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlatformPara:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address': 'str',
        'username': 'str',
        'passwd': 'str'
    }

    attribute_map = {
        'address': 'address',
        'username': 'username',
        'passwd': 'passwd'
    }

    def __init__(self, address=None, username=None, passwd=None):
        """PlatformPara

        The model defined in huaweicloud sdk

        :param address: **参数说明**：第三方业务平台的ip地址和端口。
        :type address: str
        :param username: **参数说明**：鉴权用户名。
        :type username: str
        :param passwd: **参数说明**：鉴权密码，ITS800或者ATLAS500的密码
        :type passwd: str
        """
        
        

        self._address = None
        self._username = None
        self._passwd = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if username is not None:
            self.username = username
        if passwd is not None:
            self.passwd = passwd

    @property
    def address(self):
        """Gets the address of this PlatformPara.

        **参数说明**：第三方业务平台的ip地址和端口。

        :return: The address of this PlatformPara.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PlatformPara.

        **参数说明**：第三方业务平台的ip地址和端口。

        :param address: The address of this PlatformPara.
        :type address: str
        """
        self._address = address

    @property
    def username(self):
        """Gets the username of this PlatformPara.

        **参数说明**：鉴权用户名。

        :return: The username of this PlatformPara.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this PlatformPara.

        **参数说明**：鉴权用户名。

        :param username: The username of this PlatformPara.
        :type username: str
        """
        self._username = username

    @property
    def passwd(self):
        """Gets the passwd of this PlatformPara.

        **参数说明**：鉴权密码，ITS800或者ATLAS500的密码

        :return: The passwd of this PlatformPara.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        """Sets the passwd of this PlatformPara.

        **参数说明**：鉴权密码，ITS800或者ATLAS500的密码

        :param passwd: The passwd of this PlatformPara.
        :type passwd: str
        """
        self._passwd = passwd

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
        if not isinstance(other, PlatformPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
