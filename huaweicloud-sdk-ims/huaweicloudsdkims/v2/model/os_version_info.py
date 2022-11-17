# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OsVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'platform': 'str',
        'os_version_key': 'str',
        'os_version': 'str',
        'os_bit': 'int',
        'os_type': 'str'
    }

    attribute_map = {
        'platform': 'platform',
        'os_version_key': 'os_version_key',
        'os_version': 'os_version',
        'os_bit': 'os_bit',
        'os_type': 'os_type'
    }

    def __init__(self, platform=None, os_version_key=None, os_version=None, os_bit=None, os_type=None):
        """OsVersionInfo

        The model defined in huaweicloud sdk

        :param platform: 操作系统的平台值
        :type platform: str
        :param os_version_key: os_version的key值，和os_version值相同
        :type os_version_key: str
        :param os_version: 操作系统的版本
        :type os_version: str
        :param os_bit: 操作系统的位数
        :type os_bit: int
        :param os_type: 操作系统的类型，Linux或Windows
        :type os_type: str
        """
        
        

        self._platform = None
        self._os_version_key = None
        self._os_version = None
        self._os_bit = None
        self._os_type = None
        self.discriminator = None

        self.platform = platform
        self.os_version_key = os_version_key
        self.os_version = os_version
        self.os_bit = os_bit
        self.os_type = os_type

    @property
    def platform(self):
        """Gets the platform of this OsVersionInfo.

        操作系统的平台值

        :return: The platform of this OsVersionInfo.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this OsVersionInfo.

        操作系统的平台值

        :param platform: The platform of this OsVersionInfo.
        :type platform: str
        """
        self._platform = platform

    @property
    def os_version_key(self):
        """Gets the os_version_key of this OsVersionInfo.

        os_version的key值，和os_version值相同

        :return: The os_version_key of this OsVersionInfo.
        :rtype: str
        """
        return self._os_version_key

    @os_version_key.setter
    def os_version_key(self, os_version_key):
        """Sets the os_version_key of this OsVersionInfo.

        os_version的key值，和os_version值相同

        :param os_version_key: The os_version_key of this OsVersionInfo.
        :type os_version_key: str
        """
        self._os_version_key = os_version_key

    @property
    def os_version(self):
        """Gets the os_version of this OsVersionInfo.

        操作系统的版本

        :return: The os_version of this OsVersionInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this OsVersionInfo.

        操作系统的版本

        :param os_version: The os_version of this OsVersionInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def os_bit(self):
        """Gets the os_bit of this OsVersionInfo.

        操作系统的位数

        :return: The os_bit of this OsVersionInfo.
        :rtype: int
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        """Sets the os_bit of this OsVersionInfo.

        操作系统的位数

        :param os_bit: The os_bit of this OsVersionInfo.
        :type os_bit: int
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        """Gets the os_type of this OsVersionInfo.

        操作系统的类型，Linux或Windows

        :return: The os_type of this OsVersionInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this OsVersionInfo.

        操作系统的类型，Linux或Windows

        :param os_type: The os_type of this OsVersionInfo.
        :type os_type: str
        """
        self._os_type = os_type

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
        if not isinstance(other, OsVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
