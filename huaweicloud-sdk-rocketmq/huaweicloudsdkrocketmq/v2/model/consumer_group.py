# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsumerGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'broadcast': 'bool',
        'brokers': 'list[str]',
        'name': 'str',
        'group_desc': 'str',
        'retry_max_time': 'int',
        'created_at': 'int',
        'permissions': 'list[str]',
        'consume_orderly': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'broadcast': 'broadcast',
        'brokers': 'brokers',
        'name': 'name',
        'group_desc': 'group_desc',
        'retry_max_time': 'retry_max_time',
        'created_at': 'createdAt',
        'permissions': 'permissions',
        'consume_orderly': 'consume_orderly'
    }

    def __init__(self, enabled=None, broadcast=None, brokers=None, name=None, group_desc=None, retry_max_time=None, created_at=None, permissions=None, consume_orderly=None):
        """ConsumerGroup

        The model defined in huaweicloud sdk

        :param enabled: 是否可以消费。
        :type enabled: bool
        :param broadcast: 是否广播。
        :type broadcast: bool
        :param brokers: 关联的代理列表。
        :type brokers: list[str]
        :param name: 消费组名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。
        :type name: str
        :param group_desc: 消费组描述，长度0~200个字符。
        :type group_desc: str
        :param retry_max_time: 最大重试次数，取值范围为1~16。
        :type retry_max_time: int
        :param created_at: 创建时间戳。
        :type created_at: int
        :param permissions: 权限集。
        :type permissions: list[str]
        :param consume_orderly: 是否按顺序消费。
        :type consume_orderly: bool
        """
        
        

        self._enabled = None
        self._broadcast = None
        self._brokers = None
        self._name = None
        self._group_desc = None
        self._retry_max_time = None
        self._created_at = None
        self._permissions = None
        self._consume_orderly = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if broadcast is not None:
            self.broadcast = broadcast
        if brokers is not None:
            self.brokers = brokers
        if name is not None:
            self.name = name
        if group_desc is not None:
            self.group_desc = group_desc
        if retry_max_time is not None:
            self.retry_max_time = retry_max_time
        if created_at is not None:
            self.created_at = created_at
        if permissions is not None:
            self.permissions = permissions
        if consume_orderly is not None:
            self.consume_orderly = consume_orderly

    @property
    def enabled(self):
        """Gets the enabled of this ConsumerGroup.

        是否可以消费。

        :return: The enabled of this ConsumerGroup.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConsumerGroup.

        是否可以消费。

        :param enabled: The enabled of this ConsumerGroup.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def broadcast(self):
        """Gets the broadcast of this ConsumerGroup.

        是否广播。

        :return: The broadcast of this ConsumerGroup.
        :rtype: bool
        """
        return self._broadcast

    @broadcast.setter
    def broadcast(self, broadcast):
        """Sets the broadcast of this ConsumerGroup.

        是否广播。

        :param broadcast: The broadcast of this ConsumerGroup.
        :type broadcast: bool
        """
        self._broadcast = broadcast

    @property
    def brokers(self):
        """Gets the brokers of this ConsumerGroup.

        关联的代理列表。

        :return: The brokers of this ConsumerGroup.
        :rtype: list[str]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this ConsumerGroup.

        关联的代理列表。

        :param brokers: The brokers of this ConsumerGroup.
        :type brokers: list[str]
        """
        self._brokers = brokers

    @property
    def name(self):
        """Gets the name of this ConsumerGroup.

        消费组名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。

        :return: The name of this ConsumerGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConsumerGroup.

        消费组名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。

        :param name: The name of this ConsumerGroup.
        :type name: str
        """
        self._name = name

    @property
    def group_desc(self):
        """Gets the group_desc of this ConsumerGroup.

        消费组描述，长度0~200个字符。

        :return: The group_desc of this ConsumerGroup.
        :rtype: str
        """
        return self._group_desc

    @group_desc.setter
    def group_desc(self, group_desc):
        """Sets the group_desc of this ConsumerGroup.

        消费组描述，长度0~200个字符。

        :param group_desc: The group_desc of this ConsumerGroup.
        :type group_desc: str
        """
        self._group_desc = group_desc

    @property
    def retry_max_time(self):
        """Gets the retry_max_time of this ConsumerGroup.

        最大重试次数，取值范围为1~16。

        :return: The retry_max_time of this ConsumerGroup.
        :rtype: int
        """
        return self._retry_max_time

    @retry_max_time.setter
    def retry_max_time(self, retry_max_time):
        """Sets the retry_max_time of this ConsumerGroup.

        最大重试次数，取值范围为1~16。

        :param retry_max_time: The retry_max_time of this ConsumerGroup.
        :type retry_max_time: int
        """
        self._retry_max_time = retry_max_time

    @property
    def created_at(self):
        """Gets the created_at of this ConsumerGroup.

        创建时间戳。

        :return: The created_at of this ConsumerGroup.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConsumerGroup.

        创建时间戳。

        :param created_at: The created_at of this ConsumerGroup.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def permissions(self):
        """Gets the permissions of this ConsumerGroup.

        权限集。

        :return: The permissions of this ConsumerGroup.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ConsumerGroup.

        权限集。

        :param permissions: The permissions of this ConsumerGroup.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def consume_orderly(self):
        """Gets the consume_orderly of this ConsumerGroup.

        是否按顺序消费。

        :return: The consume_orderly of this ConsumerGroup.
        :rtype: bool
        """
        return self._consume_orderly

    @consume_orderly.setter
    def consume_orderly(self, consume_orderly):
        """Sets the consume_orderly of this ConsumerGroup.

        是否按顺序消费。

        :param consume_orderly: The consume_orderly of this ConsumerGroup.
        :type consume_orderly: bool
        """
        self._consume_orderly = consume_orderly

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
        if not isinstance(other, ConsumerGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
