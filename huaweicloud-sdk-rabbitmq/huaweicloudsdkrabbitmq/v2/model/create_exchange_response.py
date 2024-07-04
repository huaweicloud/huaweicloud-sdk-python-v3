# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExchangeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'durable': 'bool',
        'default': 'bool',
        'internal': 'bool',
        'name': 'str',
        'auto_delete': 'bool',
        'type': 'str',
        'vhost': 'str'
    }

    attribute_map = {
        'durable': 'durable',
        'default': 'default',
        'internal': 'internal',
        'name': 'name',
        'auto_delete': 'auto_delete',
        'type': 'type',
        'vhost': 'vhost'
    }

    def __init__(self, durable=None, default=None, internal=None, name=None, auto_delete=None, type=None, vhost=None):
        """CreateExchangeResponse

        The model defined in huaweicloud sdk

        :param durable: 是否持久化
        :type durable: bool
        :param default: 是否是默认Exchange
        :type default: bool
        :param internal: 是否是内部Exchange
        :type internal: bool
        :param name: Exchange名称
        :type name: str
        :param auto_delete: 是否自动删除
        :type auto_delete: bool
        :param type: Exchange类型
        :type type: str
        :param vhost: 所属Vhost
        :type vhost: str
        """
        
        super(CreateExchangeResponse, self).__init__()

        self._durable = None
        self._default = None
        self._internal = None
        self._name = None
        self._auto_delete = None
        self._type = None
        self._vhost = None
        self.discriminator = None

        if durable is not None:
            self.durable = durable
        if default is not None:
            self.default = default
        if internal is not None:
            self.internal = internal
        if name is not None:
            self.name = name
        if auto_delete is not None:
            self.auto_delete = auto_delete
        if type is not None:
            self.type = type
        if vhost is not None:
            self.vhost = vhost

    @property
    def durable(self):
        """Gets the durable of this CreateExchangeResponse.

        是否持久化

        :return: The durable of this CreateExchangeResponse.
        :rtype: bool
        """
        return self._durable

    @durable.setter
    def durable(self, durable):
        """Sets the durable of this CreateExchangeResponse.

        是否持久化

        :param durable: The durable of this CreateExchangeResponse.
        :type durable: bool
        """
        self._durable = durable

    @property
    def default(self):
        """Gets the default of this CreateExchangeResponse.

        是否是默认Exchange

        :return: The default of this CreateExchangeResponse.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this CreateExchangeResponse.

        是否是默认Exchange

        :param default: The default of this CreateExchangeResponse.
        :type default: bool
        """
        self._default = default

    @property
    def internal(self):
        """Gets the internal of this CreateExchangeResponse.

        是否是内部Exchange

        :return: The internal of this CreateExchangeResponse.
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this CreateExchangeResponse.

        是否是内部Exchange

        :param internal: The internal of this CreateExchangeResponse.
        :type internal: bool
        """
        self._internal = internal

    @property
    def name(self):
        """Gets the name of this CreateExchangeResponse.

        Exchange名称

        :return: The name of this CreateExchangeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateExchangeResponse.

        Exchange名称

        :param name: The name of this CreateExchangeResponse.
        :type name: str
        """
        self._name = name

    @property
    def auto_delete(self):
        """Gets the auto_delete of this CreateExchangeResponse.

        是否自动删除

        :return: The auto_delete of this CreateExchangeResponse.
        :rtype: bool
        """
        return self._auto_delete

    @auto_delete.setter
    def auto_delete(self, auto_delete):
        """Sets the auto_delete of this CreateExchangeResponse.

        是否自动删除

        :param auto_delete: The auto_delete of this CreateExchangeResponse.
        :type auto_delete: bool
        """
        self._auto_delete = auto_delete

    @property
    def type(self):
        """Gets the type of this CreateExchangeResponse.

        Exchange类型

        :return: The type of this CreateExchangeResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateExchangeResponse.

        Exchange类型

        :param type: The type of this CreateExchangeResponse.
        :type type: str
        """
        self._type = type

    @property
    def vhost(self):
        """Gets the vhost of this CreateExchangeResponse.

        所属Vhost

        :return: The vhost of this CreateExchangeResponse.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        """Sets the vhost of this CreateExchangeResponse.

        所属Vhost

        :param vhost: The vhost of this CreateExchangeResponse.
        :type vhost: str
        """
        self._vhost = vhost

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
        if not isinstance(other, CreateExchangeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
