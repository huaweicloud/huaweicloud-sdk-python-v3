# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowlogItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'command': 'str',
        'start_time': 'str',
        'duration': 'str',
        'shard_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'command': 'command',
        'start_time': 'start_time',
        'duration': 'duration',
        'shard_name': 'shard_name'
    }

    def __init__(self, id=None, command=None, start_time=None, duration=None, shard_name=None):
        """SlowlogItem

        The model defined in huaweicloud sdk

        :param id: 慢日志的唯一标识
        :type id: int
        :param command: 慢命令
        :type command: str
        :param start_time: 执行开始时间,格式为“2020-06-19T07:06:07Z”
        :type start_time: str
        :param duration: 持续时间，单位是ms
        :type duration: str
        :param shard_name: 慢命令所在的分片名称，仅在实例类型为集群时支持
        :type shard_name: str
        """
        
        

        self._id = None
        self._command = None
        self._start_time = None
        self._duration = None
        self._shard_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if command is not None:
            self.command = command
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if shard_name is not None:
            self.shard_name = shard_name

    @property
    def id(self):
        """Gets the id of this SlowlogItem.

        慢日志的唯一标识

        :return: The id of this SlowlogItem.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlowlogItem.

        慢日志的唯一标识

        :param id: The id of this SlowlogItem.
        :type id: int
        """
        self._id = id

    @property
    def command(self):
        """Gets the command of this SlowlogItem.

        慢命令

        :return: The command of this SlowlogItem.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this SlowlogItem.

        慢命令

        :param command: The command of this SlowlogItem.
        :type command: str
        """
        self._command = command

    @property
    def start_time(self):
        """Gets the start_time of this SlowlogItem.

        执行开始时间,格式为“2020-06-19T07:06:07Z”

        :return: The start_time of this SlowlogItem.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SlowlogItem.

        执行开始时间,格式为“2020-06-19T07:06:07Z”

        :param start_time: The start_time of this SlowlogItem.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this SlowlogItem.

        持续时间，单位是ms

        :return: The duration of this SlowlogItem.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SlowlogItem.

        持续时间，单位是ms

        :param duration: The duration of this SlowlogItem.
        :type duration: str
        """
        self._duration = duration

    @property
    def shard_name(self):
        """Gets the shard_name of this SlowlogItem.

        慢命令所在的分片名称，仅在实例类型为集群时支持

        :return: The shard_name of this SlowlogItem.
        :rtype: str
        """
        return self._shard_name

    @shard_name.setter
    def shard_name(self, shard_name):
        """Sets the shard_name of this SlowlogItem.

        慢命令所在的分片名称，仅在实例类型为集群时支持

        :param shard_name: The shard_name of this SlowlogItem.
        :type shard_name: str
        """
        self._shard_name = shard_name

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
        if not isinstance(other, SlowlogItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
