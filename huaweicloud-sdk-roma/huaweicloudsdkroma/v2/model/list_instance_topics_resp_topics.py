# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceTopicsRespTopics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policies_only': 'bool',
        'name': 'str',
        'replication': 'int',
        'partition': 'int',
        'retention_time': 'int',
        'sync_message_flush': 'bool',
        'sync_replication': 'bool',
        'app_id': 'str',
        'app_name': 'str',
        'permissions': 'list[str]',
        'external_configs': 'object',
        'description': 'str',
        'sensitive_word': 'str',
        'topic_type': 'int'
    }

    attribute_map = {
        'policies_only': 'policiesOnly',
        'name': 'name',
        'replication': 'replication',
        'partition': 'partition',
        'retention_time': 'retention_time',
        'sync_message_flush': 'sync_message_flush',
        'sync_replication': 'sync_replication',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'permissions': 'permissions',
        'external_configs': 'external_configs',
        'description': 'description',
        'sensitive_word': 'sensitive_word',
        'topic_type': 'topic_type'
    }

    def __init__(self, policies_only=None, name=None, replication=None, partition=None, retention_time=None, sync_message_flush=None, sync_replication=None, app_id=None, app_name=None, permissions=None, external_configs=None, description=None, sensitive_word=None, topic_type=None):
        r"""ListInstanceTopicsRespTopics

        The model defined in huaweicloud sdk

        :param policies_only: 是否只更新策略。
        :type policies_only: bool
        :param name: topic名称。
        :type name: str
        :param replication: 副本数，配置数据的可靠性。
        :type replication: int
        :param partition: topic分区数，设置消费的并发数。
        :type partition: int
        :param retention_time: 消息老化时间。
        :type retention_time: int
        :param sync_message_flush: 是否使用同步落盘。默认值为false。同步落盘会导致性能降低。
        :type sync_message_flush: bool
        :param sync_replication: 是否开启同步复制，开启后，客户端生产消息时相应的也要设置acks&#x3D;-1，否则不生效,默认关闭。
        :type sync_replication: bool
        :param app_id: 应用ID。
        :type app_id: str
        :param app_name: 应用名称。
        :type app_name: str
        :param permissions: 允许操作的权限。
        :type permissions: list[str]
        :param external_configs: 其他配置。
        :type external_configs: object
        :param description: 描述。
        :type description: str
        :param sensitive_word: 敏感字段。
        :type sensitive_word: str
        :param topic_type: topic类型。
        :type topic_type: int
        """
        
        

        self._policies_only = None
        self._name = None
        self._replication = None
        self._partition = None
        self._retention_time = None
        self._sync_message_flush = None
        self._sync_replication = None
        self._app_id = None
        self._app_name = None
        self._permissions = None
        self._external_configs = None
        self._description = None
        self._sensitive_word = None
        self._topic_type = None
        self.discriminator = None

        if policies_only is not None:
            self.policies_only = policies_only
        if name is not None:
            self.name = name
        if replication is not None:
            self.replication = replication
        if partition is not None:
            self.partition = partition
        if retention_time is not None:
            self.retention_time = retention_time
        if sync_message_flush is not None:
            self.sync_message_flush = sync_message_flush
        if sync_replication is not None:
            self.sync_replication = sync_replication
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if permissions is not None:
            self.permissions = permissions
        if external_configs is not None:
            self.external_configs = external_configs
        if description is not None:
            self.description = description
        if sensitive_word is not None:
            self.sensitive_word = sensitive_word
        if topic_type is not None:
            self.topic_type = topic_type

    @property
    def policies_only(self):
        r"""Gets the policies_only of this ListInstanceTopicsRespTopics.

        是否只更新策略。

        :return: The policies_only of this ListInstanceTopicsRespTopics.
        :rtype: bool
        """
        return self._policies_only

    @policies_only.setter
    def policies_only(self, policies_only):
        r"""Sets the policies_only of this ListInstanceTopicsRespTopics.

        是否只更新策略。

        :param policies_only: The policies_only of this ListInstanceTopicsRespTopics.
        :type policies_only: bool
        """
        self._policies_only = policies_only

    @property
    def name(self):
        r"""Gets the name of this ListInstanceTopicsRespTopics.

        topic名称。

        :return: The name of this ListInstanceTopicsRespTopics.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInstanceTopicsRespTopics.

        topic名称。

        :param name: The name of this ListInstanceTopicsRespTopics.
        :type name: str
        """
        self._name = name

    @property
    def replication(self):
        r"""Gets the replication of this ListInstanceTopicsRespTopics.

        副本数，配置数据的可靠性。

        :return: The replication of this ListInstanceTopicsRespTopics.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        r"""Sets the replication of this ListInstanceTopicsRespTopics.

        副本数，配置数据的可靠性。

        :param replication: The replication of this ListInstanceTopicsRespTopics.
        :type replication: int
        """
        self._replication = replication

    @property
    def partition(self):
        r"""Gets the partition of this ListInstanceTopicsRespTopics.

        topic分区数，设置消费的并发数。

        :return: The partition of this ListInstanceTopicsRespTopics.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this ListInstanceTopicsRespTopics.

        topic分区数，设置消费的并发数。

        :param partition: The partition of this ListInstanceTopicsRespTopics.
        :type partition: int
        """
        self._partition = partition

    @property
    def retention_time(self):
        r"""Gets the retention_time of this ListInstanceTopicsRespTopics.

        消息老化时间。

        :return: The retention_time of this ListInstanceTopicsRespTopics.
        :rtype: int
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        r"""Sets the retention_time of this ListInstanceTopicsRespTopics.

        消息老化时间。

        :param retention_time: The retention_time of this ListInstanceTopicsRespTopics.
        :type retention_time: int
        """
        self._retention_time = retention_time

    @property
    def sync_message_flush(self):
        r"""Gets the sync_message_flush of this ListInstanceTopicsRespTopics.

        是否使用同步落盘。默认值为false。同步落盘会导致性能降低。

        :return: The sync_message_flush of this ListInstanceTopicsRespTopics.
        :rtype: bool
        """
        return self._sync_message_flush

    @sync_message_flush.setter
    def sync_message_flush(self, sync_message_flush):
        r"""Sets the sync_message_flush of this ListInstanceTopicsRespTopics.

        是否使用同步落盘。默认值为false。同步落盘会导致性能降低。

        :param sync_message_flush: The sync_message_flush of this ListInstanceTopicsRespTopics.
        :type sync_message_flush: bool
        """
        self._sync_message_flush = sync_message_flush

    @property
    def sync_replication(self):
        r"""Gets the sync_replication of this ListInstanceTopicsRespTopics.

        是否开启同步复制，开启后，客户端生产消息时相应的也要设置acks=-1，否则不生效,默认关闭。

        :return: The sync_replication of this ListInstanceTopicsRespTopics.
        :rtype: bool
        """
        return self._sync_replication

    @sync_replication.setter
    def sync_replication(self, sync_replication):
        r"""Sets the sync_replication of this ListInstanceTopicsRespTopics.

        是否开启同步复制，开启后，客户端生产消息时相应的也要设置acks=-1，否则不生效,默认关闭。

        :param sync_replication: The sync_replication of this ListInstanceTopicsRespTopics.
        :type sync_replication: bool
        """
        self._sync_replication = sync_replication

    @property
    def app_id(self):
        r"""Gets the app_id of this ListInstanceTopicsRespTopics.

        应用ID。

        :return: The app_id of this ListInstanceTopicsRespTopics.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ListInstanceTopicsRespTopics.

        应用ID。

        :param app_id: The app_id of this ListInstanceTopicsRespTopics.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this ListInstanceTopicsRespTopics.

        应用名称。

        :return: The app_name of this ListInstanceTopicsRespTopics.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListInstanceTopicsRespTopics.

        应用名称。

        :param app_name: The app_name of this ListInstanceTopicsRespTopics.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def permissions(self):
        r"""Gets the permissions of this ListInstanceTopicsRespTopics.

        允许操作的权限。

        :return: The permissions of this ListInstanceTopicsRespTopics.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this ListInstanceTopicsRespTopics.

        允许操作的权限。

        :param permissions: The permissions of this ListInstanceTopicsRespTopics.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def external_configs(self):
        r"""Gets the external_configs of this ListInstanceTopicsRespTopics.

        其他配置。

        :return: The external_configs of this ListInstanceTopicsRespTopics.
        :rtype: object
        """
        return self._external_configs

    @external_configs.setter
    def external_configs(self, external_configs):
        r"""Sets the external_configs of this ListInstanceTopicsRespTopics.

        其他配置。

        :param external_configs: The external_configs of this ListInstanceTopicsRespTopics.
        :type external_configs: object
        """
        self._external_configs = external_configs

    @property
    def description(self):
        r"""Gets the description of this ListInstanceTopicsRespTopics.

        描述。

        :return: The description of this ListInstanceTopicsRespTopics.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListInstanceTopicsRespTopics.

        描述。

        :param description: The description of this ListInstanceTopicsRespTopics.
        :type description: str
        """
        self._description = description

    @property
    def sensitive_word(self):
        r"""Gets the sensitive_word of this ListInstanceTopicsRespTopics.

        敏感字段。

        :return: The sensitive_word of this ListInstanceTopicsRespTopics.
        :rtype: str
        """
        return self._sensitive_word

    @sensitive_word.setter
    def sensitive_word(self, sensitive_word):
        r"""Sets the sensitive_word of this ListInstanceTopicsRespTopics.

        敏感字段。

        :param sensitive_word: The sensitive_word of this ListInstanceTopicsRespTopics.
        :type sensitive_word: str
        """
        self._sensitive_word = sensitive_word

    @property
    def topic_type(self):
        r"""Gets the topic_type of this ListInstanceTopicsRespTopics.

        topic类型。

        :return: The topic_type of this ListInstanceTopicsRespTopics.
        :rtype: int
        """
        return self._topic_type

    @topic_type.setter
    def topic_type(self, topic_type):
        r"""Sets the topic_type of this ListInstanceTopicsRespTopics.

        topic类型。

        :param topic_type: The topic_type of this ListInstanceTopicsRespTopics.
        :type topic_type: int
        """
        self._topic_type = topic_type

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
        if not isinstance(other, ListInstanceTopicsRespTopics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
