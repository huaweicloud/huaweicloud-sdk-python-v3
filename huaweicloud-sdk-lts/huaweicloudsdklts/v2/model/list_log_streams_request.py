# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogStreamsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_group_name': 'str',
        'log_stream_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'log_group_name': 'log_group_name',
        'log_stream_name': 'log_stream_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, log_group_name=None, log_stream_name=None, offset=None, limit=None):
        """ListLogStreamsRequest

        The model defined in huaweicloud sdk

        :param log_group_name: 日志组名称
        :type log_group_name: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        :param offset: 查询游标，初始传入0，后续从上一次的返回值中获取
        :type offset: int
        :param limit: 每页数据量，最大值为100
        :type limit: int
        """
        
        

        self._log_group_name = None
        self._log_stream_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if log_group_name is not None:
            self.log_group_name = log_group_name
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def log_group_name(self):
        """Gets the log_group_name of this ListLogStreamsRequest.

        日志组名称

        :return: The log_group_name of this ListLogStreamsRequest.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """Sets the log_group_name of this ListLogStreamsRequest.

        日志组名称

        :param log_group_name: The log_group_name of this ListLogStreamsRequest.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this ListLogStreamsRequest.

        日志流名称

        :return: The log_stream_name of this ListLogStreamsRequest.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this ListLogStreamsRequest.

        日志流名称

        :param log_stream_name: The log_stream_name of this ListLogStreamsRequest.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def offset(self):
        """Gets the offset of this ListLogStreamsRequest.

        查询游标，初始传入0，后续从上一次的返回值中获取

        :return: The offset of this ListLogStreamsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListLogStreamsRequest.

        查询游标，初始传入0，后续从上一次的返回值中获取

        :param offset: The offset of this ListLogStreamsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListLogStreamsRequest.

        每页数据量，最大值为100

        :return: The limit of this ListLogStreamsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListLogStreamsRequest.

        每页数据量，最大值为100

        :param limit: The limit of this ListLogStreamsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListLogStreamsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
