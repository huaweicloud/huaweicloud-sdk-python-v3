# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedisConnectionParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'password': 'str',
        'id': 'str',
        'addrs': 'str',
        'name': 'str'
    }

    attribute_map = {
        'password': 'password',
        'id': 'id',
        'addrs': 'addrs',
        'name': 'name'
    }

    def __init__(self, password=None, id=None, addrs=None, name=None):
        """RedisConnectionParam

        The model defined in huaweicloud sdk

        :param password: 密码
        :type password: str
        :param id: 实例id
        :type id: str
        :param addrs: 地址
        :type addrs: str
        :param name: 实例名称
        :type name: str
        """
        
        

        self._password = None
        self._id = None
        self._addrs = None
        self._name = None
        self.discriminator = None

        if password is not None:
            self.password = password
        if id is not None:
            self.id = id
        if addrs is not None:
            self.addrs = addrs
        if name is not None:
            self.name = name

    @property
    def password(self):
        """Gets the password of this RedisConnectionParam.

        密码

        :return: The password of this RedisConnectionParam.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RedisConnectionParam.

        密码

        :param password: The password of this RedisConnectionParam.
        :type password: str
        """
        self._password = password

    @property
    def id(self):
        """Gets the id of this RedisConnectionParam.

        实例id

        :return: The id of this RedisConnectionParam.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RedisConnectionParam.

        实例id

        :param id: The id of this RedisConnectionParam.
        :type id: str
        """
        self._id = id

    @property
    def addrs(self):
        """Gets the addrs of this RedisConnectionParam.

        地址

        :return: The addrs of this RedisConnectionParam.
        :rtype: str
        """
        return self._addrs

    @addrs.setter
    def addrs(self, addrs):
        """Sets the addrs of this RedisConnectionParam.

        地址

        :param addrs: The addrs of this RedisConnectionParam.
        :type addrs: str
        """
        self._addrs = addrs

    @property
    def name(self):
        """Gets the name of this RedisConnectionParam.

        实例名称

        :return: The name of this RedisConnectionParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RedisConnectionParam.

        实例名称

        :param name: The name of this RedisConnectionParam.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, RedisConnectionParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
