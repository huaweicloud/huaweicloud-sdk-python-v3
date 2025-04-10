# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMqsInstanceTopicReq:

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
        'app_id': 'str',
        'partition': 'int',
        'replication': 'int',
        'access_policy': 'str',
        'sync_message_flush': 'bool',
        'sync_replication': 'bool',
        'retention_time': 'int',
        'tag': 'str',
        'description': 'str',
        'sensitive_word': 'str'
    }

    attribute_map = {
        'name': 'name',
        'app_id': 'app_id',
        'partition': 'partition',
        'replication': 'replication',
        'access_policy': 'access_policy',
        'sync_message_flush': 'sync_message_flush',
        'sync_replication': 'sync_replication',
        'retention_time': 'retention_time',
        'tag': 'tag',
        'description': 'description',
        'sensitive_word': 'sensitive_word'
    }

    def __init__(self, name=None, app_id=None, partition=None, replication=None, access_policy=None, sync_message_flush=None, sync_replication=None, retention_time=None, tag=None, description=None, sensitive_word=None):
        r"""CreateMqsInstanceTopicReq

        The model defined in huaweicloud sdk

        :param name: topic名称，以字母开头，仅能包含数字,字母,下划线(_)，中划线（-）,长度3-200字符。
        :type name: str
        :param app_id: 集成应用key。
        :type app_id: str
        :param partition: topic分区数，设置消费的并发数。  取值范围：1-50。  默认值：3。
        :type partition: int
        :param replication: 副本数，配置数据的可靠性。  取值范围：1-3。  默认值：3。  &gt; 体验版实例的副本数只能为1。
        :type replication: int
        :param access_policy: 权限类型。   - all：发布+订阅   - pub：发布   - sub：订阅
        :type access_policy: str
        :param sync_message_flush: 是否使用同步落盘。默认值为false。同步落盘会导致性能降低。
        :type sync_message_flush: bool
        :param sync_replication: 是否开启同步复制，开启后，客户端生产消息时相应的也要设置acks&#x3D;-1，否则不生效,默认关闭。
        :type sync_replication: bool
        :param retention_time: 消息老化时间。默认值为72。取值范围1~720，单位小时。
        :type retention_time: int
        :param tag: 权限类型对应的标签。  当权限类型是all时，发布和订阅的标签用符号“&amp;”隔开。  当有多个标签时，标签用符号“||”隔开。
        :type tag: str
        :param description: 描述。长度0-1000字符。
        :type description: str
        :param sensitive_word: 敏感字段。  当有多个敏感字段时，敏感字段用符号“||”隔开。
        :type sensitive_word: str
        """
        
        

        self._name = None
        self._app_id = None
        self._partition = None
        self._replication = None
        self._access_policy = None
        self._sync_message_flush = None
        self._sync_replication = None
        self._retention_time = None
        self._tag = None
        self._description = None
        self._sensitive_word = None
        self.discriminator = None

        self.name = name
        self.app_id = app_id
        if partition is not None:
            self.partition = partition
        if replication is not None:
            self.replication = replication
        self.access_policy = access_policy
        if sync_message_flush is not None:
            self.sync_message_flush = sync_message_flush
        if sync_replication is not None:
            self.sync_replication = sync_replication
        if retention_time is not None:
            self.retention_time = retention_time
        if tag is not None:
            self.tag = tag
        if description is not None:
            self.description = description
        if sensitive_word is not None:
            self.sensitive_word = sensitive_word

    @property
    def name(self):
        r"""Gets the name of this CreateMqsInstanceTopicReq.

        topic名称，以字母开头，仅能包含数字,字母,下划线(_)，中划线（-）,长度3-200字符。

        :return: The name of this CreateMqsInstanceTopicReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateMqsInstanceTopicReq.

        topic名称，以字母开头，仅能包含数字,字母,下划线(_)，中划线（-）,长度3-200字符。

        :param name: The name of this CreateMqsInstanceTopicReq.
        :type name: str
        """
        self._name = name

    @property
    def app_id(self):
        r"""Gets the app_id of this CreateMqsInstanceTopicReq.

        集成应用key。

        :return: The app_id of this CreateMqsInstanceTopicReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CreateMqsInstanceTopicReq.

        集成应用key。

        :param app_id: The app_id of this CreateMqsInstanceTopicReq.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def partition(self):
        r"""Gets the partition of this CreateMqsInstanceTopicReq.

        topic分区数，设置消费的并发数。  取值范围：1-50。  默认值：3。

        :return: The partition of this CreateMqsInstanceTopicReq.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this CreateMqsInstanceTopicReq.

        topic分区数，设置消费的并发数。  取值范围：1-50。  默认值：3。

        :param partition: The partition of this CreateMqsInstanceTopicReq.
        :type partition: int
        """
        self._partition = partition

    @property
    def replication(self):
        r"""Gets the replication of this CreateMqsInstanceTopicReq.

        副本数，配置数据的可靠性。  取值范围：1-3。  默认值：3。  > 体验版实例的副本数只能为1。

        :return: The replication of this CreateMqsInstanceTopicReq.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        r"""Sets the replication of this CreateMqsInstanceTopicReq.

        副本数，配置数据的可靠性。  取值范围：1-3。  默认值：3。  > 体验版实例的副本数只能为1。

        :param replication: The replication of this CreateMqsInstanceTopicReq.
        :type replication: int
        """
        self._replication = replication

    @property
    def access_policy(self):
        r"""Gets the access_policy of this CreateMqsInstanceTopicReq.

        权限类型。   - all：发布+订阅   - pub：发布   - sub：订阅

        :return: The access_policy of this CreateMqsInstanceTopicReq.
        :rtype: str
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        r"""Sets the access_policy of this CreateMqsInstanceTopicReq.

        权限类型。   - all：发布+订阅   - pub：发布   - sub：订阅

        :param access_policy: The access_policy of this CreateMqsInstanceTopicReq.
        :type access_policy: str
        """
        self._access_policy = access_policy

    @property
    def sync_message_flush(self):
        r"""Gets the sync_message_flush of this CreateMqsInstanceTopicReq.

        是否使用同步落盘。默认值为false。同步落盘会导致性能降低。

        :return: The sync_message_flush of this CreateMqsInstanceTopicReq.
        :rtype: bool
        """
        return self._sync_message_flush

    @sync_message_flush.setter
    def sync_message_flush(self, sync_message_flush):
        r"""Sets the sync_message_flush of this CreateMqsInstanceTopicReq.

        是否使用同步落盘。默认值为false。同步落盘会导致性能降低。

        :param sync_message_flush: The sync_message_flush of this CreateMqsInstanceTopicReq.
        :type sync_message_flush: bool
        """
        self._sync_message_flush = sync_message_flush

    @property
    def sync_replication(self):
        r"""Gets the sync_replication of this CreateMqsInstanceTopicReq.

        是否开启同步复制，开启后，客户端生产消息时相应的也要设置acks=-1，否则不生效,默认关闭。

        :return: The sync_replication of this CreateMqsInstanceTopicReq.
        :rtype: bool
        """
        return self._sync_replication

    @sync_replication.setter
    def sync_replication(self, sync_replication):
        r"""Sets the sync_replication of this CreateMqsInstanceTopicReq.

        是否开启同步复制，开启后，客户端生产消息时相应的也要设置acks=-1，否则不生效,默认关闭。

        :param sync_replication: The sync_replication of this CreateMqsInstanceTopicReq.
        :type sync_replication: bool
        """
        self._sync_replication = sync_replication

    @property
    def retention_time(self):
        r"""Gets the retention_time of this CreateMqsInstanceTopicReq.

        消息老化时间。默认值为72。取值范围1~720，单位小时。

        :return: The retention_time of this CreateMqsInstanceTopicReq.
        :rtype: int
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        r"""Sets the retention_time of this CreateMqsInstanceTopicReq.

        消息老化时间。默认值为72。取值范围1~720，单位小时。

        :param retention_time: The retention_time of this CreateMqsInstanceTopicReq.
        :type retention_time: int
        """
        self._retention_time = retention_time

    @property
    def tag(self):
        r"""Gets the tag of this CreateMqsInstanceTopicReq.

        权限类型对应的标签。  当权限类型是all时，发布和订阅的标签用符号“&”隔开。  当有多个标签时，标签用符号“||”隔开。

        :return: The tag of this CreateMqsInstanceTopicReq.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this CreateMqsInstanceTopicReq.

        权限类型对应的标签。  当权限类型是all时，发布和订阅的标签用符号“&”隔开。  当有多个标签时，标签用符号“||”隔开。

        :param tag: The tag of this CreateMqsInstanceTopicReq.
        :type tag: str
        """
        self._tag = tag

    @property
    def description(self):
        r"""Gets the description of this CreateMqsInstanceTopicReq.

        描述。长度0-1000字符。

        :return: The description of this CreateMqsInstanceTopicReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateMqsInstanceTopicReq.

        描述。长度0-1000字符。

        :param description: The description of this CreateMqsInstanceTopicReq.
        :type description: str
        """
        self._description = description

    @property
    def sensitive_word(self):
        r"""Gets the sensitive_word of this CreateMqsInstanceTopicReq.

        敏感字段。  当有多个敏感字段时，敏感字段用符号“||”隔开。

        :return: The sensitive_word of this CreateMqsInstanceTopicReq.
        :rtype: str
        """
        return self._sensitive_word

    @sensitive_word.setter
    def sensitive_word(self, sensitive_word):
        r"""Sets the sensitive_word of this CreateMqsInstanceTopicReq.

        敏感字段。  当有多个敏感字段时，敏感字段用符号“||”隔开。

        :param sensitive_word: The sensitive_word of this CreateMqsInstanceTopicReq.
        :type sensitive_word: str
        """
        self._sensitive_word = sensitive_word

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
        if not isinstance(other, CreateMqsInstanceTopicReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
