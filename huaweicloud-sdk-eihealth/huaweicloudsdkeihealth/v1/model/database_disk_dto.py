# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseDiskDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'space': 'int',
        'encrypt': 'bool',
        'used': 'float'
    }

    attribute_map = {
        'type': 'type',
        'space': 'space',
        'encrypt': 'encrypt',
        'used': 'used'
    }

    def __init__(self, type=None, space=None, encrypt=None, used=None):
        """DatabaseDiskDto

        The model defined in huaweicloud sdk

        :param type: 磁盘类型
        :type type: str
        :param space: 磁盘大小，单位GB
        :type space: int
        :param encrypt: 是否加密
        :type encrypt: bool
        :param used: 磁盘已使用量，单位GB
        :type used: float
        """
        
        

        self._type = None
        self._space = None
        self._encrypt = None
        self._used = None
        self.discriminator = None

        self.type = type
        self.space = space
        self.encrypt = encrypt
        self.used = used

    @property
    def type(self):
        """Gets the type of this DatabaseDiskDto.

        磁盘类型

        :return: The type of this DatabaseDiskDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DatabaseDiskDto.

        磁盘类型

        :param type: The type of this DatabaseDiskDto.
        :type type: str
        """
        self._type = type

    @property
    def space(self):
        """Gets the space of this DatabaseDiskDto.

        磁盘大小，单位GB

        :return: The space of this DatabaseDiskDto.
        :rtype: int
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this DatabaseDiskDto.

        磁盘大小，单位GB

        :param space: The space of this DatabaseDiskDto.
        :type space: int
        """
        self._space = space

    @property
    def encrypt(self):
        """Gets the encrypt of this DatabaseDiskDto.

        是否加密

        :return: The encrypt of this DatabaseDiskDto.
        :rtype: bool
        """
        return self._encrypt

    @encrypt.setter
    def encrypt(self, encrypt):
        """Sets the encrypt of this DatabaseDiskDto.

        是否加密

        :param encrypt: The encrypt of this DatabaseDiskDto.
        :type encrypt: bool
        """
        self._encrypt = encrypt

    @property
    def used(self):
        """Gets the used of this DatabaseDiskDto.

        磁盘已使用量，单位GB

        :return: The used of this DatabaseDiskDto.
        :rtype: float
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this DatabaseDiskDto.

        磁盘已使用量，单位GB

        :param used: The used of this DatabaseDiskDto.
        :type used: float
        """
        self._used = used

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
        if not isinstance(other, DatabaseDiskDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
