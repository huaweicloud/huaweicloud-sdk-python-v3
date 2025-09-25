# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransactionRequestBodyTransactionQueryOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exec_time': 'str',
        'xlog_quantity': 'str',
        'datnames': 'list[str]',
        'usenames': 'list[str]',
        'client_addrs': 'list[str]'
    }

    attribute_map = {
        'exec_time': 'exec_time',
        'xlog_quantity': 'xlog_quantity',
        'datnames': 'datnames',
        'usenames': 'usenames',
        'client_addrs': 'client_addrs'
    }

    def __init__(self, exec_time=None, xlog_quantity=None, datnames=None, usenames=None, client_addrs=None):
        r"""ListTransactionRequestBodyTransactionQueryOption

        The model defined in huaweicloud sdk

        :param exec_time: **参数解释**: 事务执行时长，单位：秒。 **约束限制**: 不涉及。 **取值范围**: 非负整数。 **默认取值**: 0
        :type exec_time: str
        :param xlog_quantity: **参数解释**: 事务xlog日志大小：单位byte。 **约束限制**: 不涉及。 **取值范围**: 非负整数。 **默认取值**: 0
        :type xlog_quantity: str
        :param datnames: **参数解释**: 数据库名。 **约束限制**: 不涉及。
        :type datnames: list[str]
        :param usenames: **参数解释**: 用户名。 **约束限制**: 不涉及。
        :type usenames: list[str]
        :param client_addrs: **参数解释**: 用户发起事务请求的客户端地址。 **约束限制**: 不涉及。
        :type client_addrs: list[str]
        """
        
        

        self._exec_time = None
        self._xlog_quantity = None
        self._datnames = None
        self._usenames = None
        self._client_addrs = None
        self.discriminator = None

        if exec_time is not None:
            self.exec_time = exec_time
        if xlog_quantity is not None:
            self.xlog_quantity = xlog_quantity
        if datnames is not None:
            self.datnames = datnames
        if usenames is not None:
            self.usenames = usenames
        if client_addrs is not None:
            self.client_addrs = client_addrs

    @property
    def exec_time(self):
        r"""Gets the exec_time of this ListTransactionRequestBodyTransactionQueryOption.

        **参数解释**: 事务执行时长，单位：秒。 **约束限制**: 不涉及。 **取值范围**: 非负整数。 **默认取值**: 0

        :return: The exec_time of this ListTransactionRequestBodyTransactionQueryOption.
        :rtype: str
        """
        return self._exec_time

    @exec_time.setter
    def exec_time(self, exec_time):
        r"""Sets the exec_time of this ListTransactionRequestBodyTransactionQueryOption.

        **参数解释**: 事务执行时长，单位：秒。 **约束限制**: 不涉及。 **取值范围**: 非负整数。 **默认取值**: 0

        :param exec_time: The exec_time of this ListTransactionRequestBodyTransactionQueryOption.
        :type exec_time: str
        """
        self._exec_time = exec_time

    @property
    def xlog_quantity(self):
        r"""Gets the xlog_quantity of this ListTransactionRequestBodyTransactionQueryOption.

        **参数解释**: 事务xlog日志大小：单位byte。 **约束限制**: 不涉及。 **取值范围**: 非负整数。 **默认取值**: 0

        :return: The xlog_quantity of this ListTransactionRequestBodyTransactionQueryOption.
        :rtype: str
        """
        return self._xlog_quantity

    @xlog_quantity.setter
    def xlog_quantity(self, xlog_quantity):
        r"""Sets the xlog_quantity of this ListTransactionRequestBodyTransactionQueryOption.

        **参数解释**: 事务xlog日志大小：单位byte。 **约束限制**: 不涉及。 **取值范围**: 非负整数。 **默认取值**: 0

        :param xlog_quantity: The xlog_quantity of this ListTransactionRequestBodyTransactionQueryOption.
        :type xlog_quantity: str
        """
        self._xlog_quantity = xlog_quantity

    @property
    def datnames(self):
        r"""Gets the datnames of this ListTransactionRequestBodyTransactionQueryOption.

        **参数解释**: 数据库名。 **约束限制**: 不涉及。

        :return: The datnames of this ListTransactionRequestBodyTransactionQueryOption.
        :rtype: list[str]
        """
        return self._datnames

    @datnames.setter
    def datnames(self, datnames):
        r"""Sets the datnames of this ListTransactionRequestBodyTransactionQueryOption.

        **参数解释**: 数据库名。 **约束限制**: 不涉及。

        :param datnames: The datnames of this ListTransactionRequestBodyTransactionQueryOption.
        :type datnames: list[str]
        """
        self._datnames = datnames

    @property
    def usenames(self):
        r"""Gets the usenames of this ListTransactionRequestBodyTransactionQueryOption.

        **参数解释**: 用户名。 **约束限制**: 不涉及。

        :return: The usenames of this ListTransactionRequestBodyTransactionQueryOption.
        :rtype: list[str]
        """
        return self._usenames

    @usenames.setter
    def usenames(self, usenames):
        r"""Sets the usenames of this ListTransactionRequestBodyTransactionQueryOption.

        **参数解释**: 用户名。 **约束限制**: 不涉及。

        :param usenames: The usenames of this ListTransactionRequestBodyTransactionQueryOption.
        :type usenames: list[str]
        """
        self._usenames = usenames

    @property
    def client_addrs(self):
        r"""Gets the client_addrs of this ListTransactionRequestBodyTransactionQueryOption.

        **参数解释**: 用户发起事务请求的客户端地址。 **约束限制**: 不涉及。

        :return: The client_addrs of this ListTransactionRequestBodyTransactionQueryOption.
        :rtype: list[str]
        """
        return self._client_addrs

    @client_addrs.setter
    def client_addrs(self, client_addrs):
        r"""Sets the client_addrs of this ListTransactionRequestBodyTransactionQueryOption.

        **参数解释**: 用户发起事务请求的客户端地址。 **约束限制**: 不涉及。

        :param client_addrs: The client_addrs of this ListTransactionRequestBodyTransactionQueryOption.
        :type client_addrs: list[str]
        """
        self._client_addrs = client_addrs

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
        if not isinstance(other, ListTransactionRequestBodyTransactionQueryOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
