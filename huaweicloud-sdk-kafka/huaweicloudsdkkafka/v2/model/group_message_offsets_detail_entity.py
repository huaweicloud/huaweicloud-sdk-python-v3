# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupMessageOffsetsDetailEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partition': 'str',
        'message_current_offset': 'str',
        'message_log_start_offset': 'int',
        'message_log_end_offset': 'int',
        'consumer_id': 'str',
        'host': 'str',
        'client_id': 'str'
    }

    attribute_map = {
        'partition': 'partition',
        'message_current_offset': 'message_current_offset',
        'message_log_start_offset': 'message_log_start_offset',
        'message_log_end_offset': 'message_log_end_offset',
        'consumer_id': 'consumer_id',
        'host': 'host',
        'client_id': 'client_id'
    }

    def __init__(self, partition=None, message_current_offset=None, message_log_start_offset=None, message_log_end_offset=None, consumer_id=None, host=None, client_id=None):
        r"""GroupMessageOffsetsDetailEntity

        The model defined in huaweicloud sdk

        :param partition: 分区
        :type partition: str
        :param message_current_offset: 消息当前位点
        :type message_current_offset: str
        :param message_log_start_offset: 消息开始位点
        :type message_log_start_offset: int
        :param message_log_end_offset: 消息结束位点
        :type message_log_end_offset: int
        :param consumer_id: 消费者Id
        :type consumer_id: str
        :param host: host名称
        :type host: str
        :param client_id: 客户端Id
        :type client_id: str
        """
        
        

        self._partition = None
        self._message_current_offset = None
        self._message_log_start_offset = None
        self._message_log_end_offset = None
        self._consumer_id = None
        self._host = None
        self._client_id = None
        self.discriminator = None

        if partition is not None:
            self.partition = partition
        if message_current_offset is not None:
            self.message_current_offset = message_current_offset
        if message_log_start_offset is not None:
            self.message_log_start_offset = message_log_start_offset
        if message_log_end_offset is not None:
            self.message_log_end_offset = message_log_end_offset
        if consumer_id is not None:
            self.consumer_id = consumer_id
        if host is not None:
            self.host = host
        if client_id is not None:
            self.client_id = client_id

    @property
    def partition(self):
        r"""Gets the partition of this GroupMessageOffsetsDetailEntity.

        分区

        :return: The partition of this GroupMessageOffsetsDetailEntity.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this GroupMessageOffsetsDetailEntity.

        分区

        :param partition: The partition of this GroupMessageOffsetsDetailEntity.
        :type partition: str
        """
        self._partition = partition

    @property
    def message_current_offset(self):
        r"""Gets the message_current_offset of this GroupMessageOffsetsDetailEntity.

        消息当前位点

        :return: The message_current_offset of this GroupMessageOffsetsDetailEntity.
        :rtype: str
        """
        return self._message_current_offset

    @message_current_offset.setter
    def message_current_offset(self, message_current_offset):
        r"""Sets the message_current_offset of this GroupMessageOffsetsDetailEntity.

        消息当前位点

        :param message_current_offset: The message_current_offset of this GroupMessageOffsetsDetailEntity.
        :type message_current_offset: str
        """
        self._message_current_offset = message_current_offset

    @property
    def message_log_start_offset(self):
        r"""Gets the message_log_start_offset of this GroupMessageOffsetsDetailEntity.

        消息开始位点

        :return: The message_log_start_offset of this GroupMessageOffsetsDetailEntity.
        :rtype: int
        """
        return self._message_log_start_offset

    @message_log_start_offset.setter
    def message_log_start_offset(self, message_log_start_offset):
        r"""Sets the message_log_start_offset of this GroupMessageOffsetsDetailEntity.

        消息开始位点

        :param message_log_start_offset: The message_log_start_offset of this GroupMessageOffsetsDetailEntity.
        :type message_log_start_offset: int
        """
        self._message_log_start_offset = message_log_start_offset

    @property
    def message_log_end_offset(self):
        r"""Gets the message_log_end_offset of this GroupMessageOffsetsDetailEntity.

        消息结束位点

        :return: The message_log_end_offset of this GroupMessageOffsetsDetailEntity.
        :rtype: int
        """
        return self._message_log_end_offset

    @message_log_end_offset.setter
    def message_log_end_offset(self, message_log_end_offset):
        r"""Sets the message_log_end_offset of this GroupMessageOffsetsDetailEntity.

        消息结束位点

        :param message_log_end_offset: The message_log_end_offset of this GroupMessageOffsetsDetailEntity.
        :type message_log_end_offset: int
        """
        self._message_log_end_offset = message_log_end_offset

    @property
    def consumer_id(self):
        r"""Gets the consumer_id of this GroupMessageOffsetsDetailEntity.

        消费者Id

        :return: The consumer_id of this GroupMessageOffsetsDetailEntity.
        :rtype: str
        """
        return self._consumer_id

    @consumer_id.setter
    def consumer_id(self, consumer_id):
        r"""Sets the consumer_id of this GroupMessageOffsetsDetailEntity.

        消费者Id

        :param consumer_id: The consumer_id of this GroupMessageOffsetsDetailEntity.
        :type consumer_id: str
        """
        self._consumer_id = consumer_id

    @property
    def host(self):
        r"""Gets the host of this GroupMessageOffsetsDetailEntity.

        host名称

        :return: The host of this GroupMessageOffsetsDetailEntity.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this GroupMessageOffsetsDetailEntity.

        host名称

        :param host: The host of this GroupMessageOffsetsDetailEntity.
        :type host: str
        """
        self._host = host

    @property
    def client_id(self):
        r"""Gets the client_id of this GroupMessageOffsetsDetailEntity.

        客户端Id

        :return: The client_id of this GroupMessageOffsetsDetailEntity.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this GroupMessageOffsetsDetailEntity.

        客户端Id

        :param client_id: The client_id of this GroupMessageOffsetsDetailEntity.
        :type client_id: str
        """
        self._client_id = client_id

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
        if not isinstance(other, GroupMessageOffsetsDetailEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
