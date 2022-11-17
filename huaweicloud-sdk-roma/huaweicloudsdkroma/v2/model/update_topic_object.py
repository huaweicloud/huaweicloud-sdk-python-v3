# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTopicObject:

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
        'retention_time': 'int',
        'sync_replication': 'bool',
        'sync_message_flush': 'bool',
        'description': 'str',
        'sensitive_word': 'str'
    }

    attribute_map = {
        'name': 'name',
        'retention_time': 'retention_time',
        'sync_replication': 'sync_replication',
        'sync_message_flush': 'sync_message_flush',
        'description': 'description',
        'sensitive_word': 'sensitive_word'
    }

    def __init__(self, name=None, retention_time=None, sync_replication=None, sync_message_flush=None, description=None, sensitive_word=None):
        """UpdateTopicObject

        The model defined in huaweicloud sdk

        :param name: topic名称。
        :type name: str
        :param retention_time: 消息老化时间。默认值为72。取值范围1~720，单位小时。
        :type retention_time: int
        :param sync_replication: 是否开启同步复制。
        :type sync_replication: bool
        :param sync_message_flush: 是否使用同步落盘。
        :type sync_message_flush: bool
        :param description: 描述。
        :type description: str
        :param sensitive_word: 敏感字段。
        :type sensitive_word: str
        """
        
        

        self._name = None
        self._retention_time = None
        self._sync_replication = None
        self._sync_message_flush = None
        self._description = None
        self._sensitive_word = None
        self.discriminator = None

        self.name = name
        if retention_time is not None:
            self.retention_time = retention_time
        if sync_replication is not None:
            self.sync_replication = sync_replication
        if sync_message_flush is not None:
            self.sync_message_flush = sync_message_flush
        if description is not None:
            self.description = description
        if sensitive_word is not None:
            self.sensitive_word = sensitive_word

    @property
    def name(self):
        """Gets the name of this UpdateTopicObject.

        topic名称。

        :return: The name of this UpdateTopicObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTopicObject.

        topic名称。

        :param name: The name of this UpdateTopicObject.
        :type name: str
        """
        self._name = name

    @property
    def retention_time(self):
        """Gets the retention_time of this UpdateTopicObject.

        消息老化时间。默认值为72。取值范围1~720，单位小时。

        :return: The retention_time of this UpdateTopicObject.
        :rtype: int
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        """Sets the retention_time of this UpdateTopicObject.

        消息老化时间。默认值为72。取值范围1~720，单位小时。

        :param retention_time: The retention_time of this UpdateTopicObject.
        :type retention_time: int
        """
        self._retention_time = retention_time

    @property
    def sync_replication(self):
        """Gets the sync_replication of this UpdateTopicObject.

        是否开启同步复制。

        :return: The sync_replication of this UpdateTopicObject.
        :rtype: bool
        """
        return self._sync_replication

    @sync_replication.setter
    def sync_replication(self, sync_replication):
        """Sets the sync_replication of this UpdateTopicObject.

        是否开启同步复制。

        :param sync_replication: The sync_replication of this UpdateTopicObject.
        :type sync_replication: bool
        """
        self._sync_replication = sync_replication

    @property
    def sync_message_flush(self):
        """Gets the sync_message_flush of this UpdateTopicObject.

        是否使用同步落盘。

        :return: The sync_message_flush of this UpdateTopicObject.
        :rtype: bool
        """
        return self._sync_message_flush

    @sync_message_flush.setter
    def sync_message_flush(self, sync_message_flush):
        """Sets the sync_message_flush of this UpdateTopicObject.

        是否使用同步落盘。

        :param sync_message_flush: The sync_message_flush of this UpdateTopicObject.
        :type sync_message_flush: bool
        """
        self._sync_message_flush = sync_message_flush

    @property
    def description(self):
        """Gets the description of this UpdateTopicObject.

        描述。

        :return: The description of this UpdateTopicObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTopicObject.

        描述。

        :param description: The description of this UpdateTopicObject.
        :type description: str
        """
        self._description = description

    @property
    def sensitive_word(self):
        """Gets the sensitive_word of this UpdateTopicObject.

        敏感字段。

        :return: The sensitive_word of this UpdateTopicObject.
        :rtype: str
        """
        return self._sensitive_word

    @sensitive_word.setter
    def sensitive_word(self, sensitive_word):
        """Sets the sensitive_word of this UpdateTopicObject.

        敏感字段。

        :param sensitive_word: The sensitive_word of this UpdateTopicObject.
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
        if not isinstance(other, UpdateTopicObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
