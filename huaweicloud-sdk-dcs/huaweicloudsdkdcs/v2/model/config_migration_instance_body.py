# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigMigrationInstanceBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'addrs': 'str',
        'password': 'str'
    }

    attribute_map = {
        'id': 'id',
        'addrs': 'addrs',
        'password': 'password'
    }

    def __init__(self, id=None, addrs=None, password=None):
        """ConfigMigrationInstanceBody

        The model defined in huaweicloud sdk

        :param id: Redis实例ID。（Redis类型为云服务Redis时必须填写）
        :type id: str
        :param addrs: Redis实例地址。（Redis类型为自建Redis时必须填写）。
        :type addrs: str
        :param password: Redis密码，如果设置了密码，则必须填写。
        :type password: str
        """
        
        

        self._id = None
        self._addrs = None
        self._password = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if addrs is not None:
            self.addrs = addrs
        if password is not None:
            self.password = password

    @property
    def id(self):
        """Gets the id of this ConfigMigrationInstanceBody.

        Redis实例ID。（Redis类型为云服务Redis时必须填写）

        :return: The id of this ConfigMigrationInstanceBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigMigrationInstanceBody.

        Redis实例ID。（Redis类型为云服务Redis时必须填写）

        :param id: The id of this ConfigMigrationInstanceBody.
        :type id: str
        """
        self._id = id

    @property
    def addrs(self):
        """Gets the addrs of this ConfigMigrationInstanceBody.

        Redis实例地址。（Redis类型为自建Redis时必须填写）。

        :return: The addrs of this ConfigMigrationInstanceBody.
        :rtype: str
        """
        return self._addrs

    @addrs.setter
    def addrs(self, addrs):
        """Sets the addrs of this ConfigMigrationInstanceBody.

        Redis实例地址。（Redis类型为自建Redis时必须填写）。

        :param addrs: The addrs of this ConfigMigrationInstanceBody.
        :type addrs: str
        """
        self._addrs = addrs

    @property
    def password(self):
        """Gets the password of this ConfigMigrationInstanceBody.

        Redis密码，如果设置了密码，则必须填写。

        :return: The password of this ConfigMigrationInstanceBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ConfigMigrationInstanceBody.

        Redis密码，如果设置了密码，则必须填写。

        :param password: The password of this ConfigMigrationInstanceBody.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, ConfigMigrationInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
