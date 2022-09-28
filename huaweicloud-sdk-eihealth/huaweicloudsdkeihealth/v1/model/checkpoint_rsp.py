# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckpointRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'timestamp': 'str',
        'message': 'str'
    }

    attribute_map = {
        'source': 'source',
        'timestamp': 'timestamp',
        'message': 'message'
    }

    def __init__(self, source=None, timestamp=None, message=None):
        """CheckpointRsp

        The model defined in huaweicloud sdk

        :param source: 数据名称
        :type source: str
        :param timestamp: 日志时间戳
        :type timestamp: str
        :param message: 执行信息
        :type message: str
        """
        
        

        self._source = None
        self._timestamp = None
        self._message = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if timestamp is not None:
            self.timestamp = timestamp
        if message is not None:
            self.message = message

    @property
    def source(self):
        """Gets the source of this CheckpointRsp.

        数据名称

        :return: The source of this CheckpointRsp.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CheckpointRsp.

        数据名称

        :param source: The source of this CheckpointRsp.
        :type source: str
        """
        self._source = source

    @property
    def timestamp(self):
        """Gets the timestamp of this CheckpointRsp.

        日志时间戳

        :return: The timestamp of this CheckpointRsp.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CheckpointRsp.

        日志时间戳

        :param timestamp: The timestamp of this CheckpointRsp.
        :type timestamp: str
        """
        self._timestamp = timestamp

    @property
    def message(self):
        """Gets the message of this CheckpointRsp.

        执行信息

        :return: The message of this CheckpointRsp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CheckpointRsp.

        执行信息

        :param message: The message of this CheckpointRsp.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, CheckpointRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
