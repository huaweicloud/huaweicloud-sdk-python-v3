# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExchangeBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'durable': 'bool',
        'auto_delete': 'bool',
        'internal': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'durable': 'durable',
        'auto_delete': 'auto_delete',
        'internal': 'internal'
    }

    def __init__(self, name=None, type=None, durable=None, auto_delete=None, internal=None):
        """CreateExchangeBody

        The model defined in huaweicloud sdk

        :param name: Exchange名称
        :type name: str
        :param type: 类型（direct、fanout、topic、headers）
        :type type: str
        :param durable: 是否持久化[（AMQP版本默认持久化，不涉及此参数）](tag:hws,hws_hk)。
        :type durable: bool
        :param auto_delete: 是否自动删除
        :type auto_delete: bool
        :param internal: 内部Exchange[（AMQP版本不支持内部Exchange，不涉及此参数）](tag:hws,hws_hk)。
        :type internal: bool
        """
        
        

        self._name = None
        self._type = None
        self._durable = None
        self._auto_delete = None
        self._internal = None
        self.discriminator = None

        self.name = name
        self.type = type
        if durable is not None:
            self.durable = durable
        self.auto_delete = auto_delete
        if internal is not None:
            self.internal = internal

    @property
    def name(self):
        """Gets the name of this CreateExchangeBody.

        Exchange名称

        :return: The name of this CreateExchangeBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateExchangeBody.

        Exchange名称

        :param name: The name of this CreateExchangeBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateExchangeBody.

        类型（direct、fanout、topic、headers）

        :return: The type of this CreateExchangeBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateExchangeBody.

        类型（direct、fanout、topic、headers）

        :param type: The type of this CreateExchangeBody.
        :type type: str
        """
        self._type = type

    @property
    def durable(self):
        """Gets the durable of this CreateExchangeBody.

        是否持久化[（AMQP版本默认持久化，不涉及此参数）](tag:hws,hws_hk)。

        :return: The durable of this CreateExchangeBody.
        :rtype: bool
        """
        return self._durable

    @durable.setter
    def durable(self, durable):
        """Sets the durable of this CreateExchangeBody.

        是否持久化[（AMQP版本默认持久化，不涉及此参数）](tag:hws,hws_hk)。

        :param durable: The durable of this CreateExchangeBody.
        :type durable: bool
        """
        self._durable = durable

    @property
    def auto_delete(self):
        """Gets the auto_delete of this CreateExchangeBody.

        是否自动删除

        :return: The auto_delete of this CreateExchangeBody.
        :rtype: bool
        """
        return self._auto_delete

    @auto_delete.setter
    def auto_delete(self, auto_delete):
        """Sets the auto_delete of this CreateExchangeBody.

        是否自动删除

        :param auto_delete: The auto_delete of this CreateExchangeBody.
        :type auto_delete: bool
        """
        self._auto_delete = auto_delete

    @property
    def internal(self):
        """Gets the internal of this CreateExchangeBody.

        内部Exchange[（AMQP版本不支持内部Exchange，不涉及此参数）](tag:hws,hws_hk)。

        :return: The internal of this CreateExchangeBody.
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this CreateExchangeBody.

        内部Exchange[（AMQP版本不支持内部Exchange，不涉及此参数）](tag:hws,hws_hk)。

        :param internal: The internal of this CreateExchangeBody.
        :type internal: bool
        """
        self._internal = internal

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
        if not isinstance(other, CreateExchangeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
