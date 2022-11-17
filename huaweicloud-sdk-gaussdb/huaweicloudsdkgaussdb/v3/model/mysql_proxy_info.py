# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlProxyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'name': 'str',
        'address': 'str'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'name': 'name',
        'address': 'address'
    }

    def __init__(self, pool_id=None, name=None, address=None):
        """MysqlProxyInfo

        The model defined in huaweicloud sdk

        :param pool_id: Proxy实例id。
        :type pool_id: str
        :param name: Proxy实例名称。
        :type name: str
        :param address: Proxy读写分离地址。
        :type address: str
        """
        
        

        self._pool_id = None
        self._name = None
        self._address = None
        self.discriminator = None

        if pool_id is not None:
            self.pool_id = pool_id
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address

    @property
    def pool_id(self):
        """Gets the pool_id of this MysqlProxyInfo.

        Proxy实例id。

        :return: The pool_id of this MysqlProxyInfo.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this MysqlProxyInfo.

        Proxy实例id。

        :param pool_id: The pool_id of this MysqlProxyInfo.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def name(self):
        """Gets the name of this MysqlProxyInfo.

        Proxy实例名称。

        :return: The name of this MysqlProxyInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MysqlProxyInfo.

        Proxy实例名称。

        :param name: The name of this MysqlProxyInfo.
        :type name: str
        """
        self._name = name

    @property
    def address(self):
        """Gets the address of this MysqlProxyInfo.

        Proxy读写分离地址。

        :return: The address of this MysqlProxyInfo.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MysqlProxyInfo.

        Proxy读写分离地址。

        :param address: The address of this MysqlProxyInfo.
        :type address: str
        """
        self._address = address

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
        if not isinstance(other, MysqlProxyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
