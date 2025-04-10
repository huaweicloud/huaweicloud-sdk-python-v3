# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConsumerGroupOrBatchDeleteConsumerGroupReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'groups': 'list[str]',
        'name': 'str',
        'brokers': 'list[str]',
        'broadcast': 'bool',
        'retry_max_time': 'int',
        'enabled': 'bool',
        'consume_orderly': 'bool',
        'group_desc': 'str'
    }

    attribute_map = {
        'groups': 'groups',
        'name': 'name',
        'brokers': 'brokers',
        'broadcast': 'broadcast',
        'retry_max_time': 'retry_max_time',
        'enabled': 'enabled',
        'consume_orderly': 'consume_orderly',
        'group_desc': 'group_desc'
    }

    def __init__(self, groups=None, name=None, brokers=None, broadcast=None, retry_max_time=None, enabled=None, consume_orderly=None, group_desc=None):
        r"""CreateConsumerGroupOrBatchDeleteConsumerGroupReq

        The model defined in huaweicloud sdk

        :param groups: 待删除的消费组列表。
        :type groups: list[str]
        :param name: 消费组名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。
        :type name: str
        :param brokers: 关联的代理列表（仅RocketMQ实例4.8.0版本需要填写此参数）。
        :type brokers: list[str]
        :param broadcast: 是否广播。
        :type broadcast: bool
        :param retry_max_time: 最大重试次数，取值范围为1~16。
        :type retry_max_time: int
        :param enabled: 是否可以消费。
        :type enabled: bool
        :param consume_orderly: 是否按顺序消费（仅RocketMQ实例5.x版本需要填写此参数）。
        :type consume_orderly: bool
        :param group_desc: 消费组描述，长度0~200个字符。
        :type group_desc: str
        """
        
        

        self._groups = None
        self._name = None
        self._brokers = None
        self._broadcast = None
        self._retry_max_time = None
        self._enabled = None
        self._consume_orderly = None
        self._group_desc = None
        self.discriminator = None

        if groups is not None:
            self.groups = groups
        if name is not None:
            self.name = name
        if brokers is not None:
            self.brokers = brokers
        if broadcast is not None:
            self.broadcast = broadcast
        if retry_max_time is not None:
            self.retry_max_time = retry_max_time
        if enabled is not None:
            self.enabled = enabled
        if consume_orderly is not None:
            self.consume_orderly = consume_orderly
        if group_desc is not None:
            self.group_desc = group_desc

    @property
    def groups(self):
        r"""Gets the groups of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        待删除的消费组列表。

        :return: The groups of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        待删除的消费组列表。

        :param groups: The groups of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :type groups: list[str]
        """
        self._groups = groups

    @property
    def name(self):
        r"""Gets the name of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        消费组名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。

        :return: The name of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        消费组名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。

        :param name: The name of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :type name: str
        """
        self._name = name

    @property
    def brokers(self):
        r"""Gets the brokers of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        关联的代理列表（仅RocketMQ实例4.8.0版本需要填写此参数）。

        :return: The brokers of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :rtype: list[str]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        r"""Sets the brokers of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        关联的代理列表（仅RocketMQ实例4.8.0版本需要填写此参数）。

        :param brokers: The brokers of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :type brokers: list[str]
        """
        self._brokers = brokers

    @property
    def broadcast(self):
        r"""Gets the broadcast of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        是否广播。

        :return: The broadcast of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :rtype: bool
        """
        return self._broadcast

    @broadcast.setter
    def broadcast(self, broadcast):
        r"""Sets the broadcast of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        是否广播。

        :param broadcast: The broadcast of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :type broadcast: bool
        """
        self._broadcast = broadcast

    @property
    def retry_max_time(self):
        r"""Gets the retry_max_time of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        最大重试次数，取值范围为1~16。

        :return: The retry_max_time of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :rtype: int
        """
        return self._retry_max_time

    @retry_max_time.setter
    def retry_max_time(self, retry_max_time):
        r"""Sets the retry_max_time of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        最大重试次数，取值范围为1~16。

        :param retry_max_time: The retry_max_time of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :type retry_max_time: int
        """
        self._retry_max_time = retry_max_time

    @property
    def enabled(self):
        r"""Gets the enabled of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        是否可以消费。

        :return: The enabled of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        是否可以消费。

        :param enabled: The enabled of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def consume_orderly(self):
        r"""Gets the consume_orderly of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        是否按顺序消费（仅RocketMQ实例5.x版本需要填写此参数）。

        :return: The consume_orderly of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :rtype: bool
        """
        return self._consume_orderly

    @consume_orderly.setter
    def consume_orderly(self, consume_orderly):
        r"""Sets the consume_orderly of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        是否按顺序消费（仅RocketMQ实例5.x版本需要填写此参数）。

        :param consume_orderly: The consume_orderly of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :type consume_orderly: bool
        """
        self._consume_orderly = consume_orderly

    @property
    def group_desc(self):
        r"""Gets the group_desc of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        消费组描述，长度0~200个字符。

        :return: The group_desc of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :rtype: str
        """
        return self._group_desc

    @group_desc.setter
    def group_desc(self, group_desc):
        r"""Sets the group_desc of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.

        消费组描述，长度0~200个字符。

        :param group_desc: The group_desc of this CreateConsumerGroupOrBatchDeleteConsumerGroupReq.
        :type group_desc: str
        """
        self._group_desc = group_desc

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
        if not isinstance(other, CreateConsumerGroupOrBatchDeleteConsumerGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
