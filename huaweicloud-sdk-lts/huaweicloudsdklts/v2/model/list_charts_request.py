# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListChartsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, log_group_id=None, log_stream_id=None, offset=None, limit=None):
        """ListChartsRequest

        The model defined in huaweicloud sdk

        :param log_group_id: 日志组ID
        :type log_group_id: str
        :param log_stream_id: 日志流ID
        :type log_stream_id: str
        :param offset: 查询游标，初始传入0，后续从上一次的返回值中获取
        :type offset: int
        :param limit: 每页数据量，最大值为100
        :type limit: int
        """
        
        

        self._log_group_id = None
        self._log_stream_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.log_group_id = log_group_id
        self.log_stream_id = log_stream_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def log_group_id(self):
        """Gets the log_group_id of this ListChartsRequest.

        日志组ID

        :return: The log_group_id of this ListChartsRequest.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this ListChartsRequest.

        日志组ID

        :param log_group_id: The log_group_id of this ListChartsRequest.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this ListChartsRequest.

        日志流ID

        :return: The log_stream_id of this ListChartsRequest.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this ListChartsRequest.

        日志流ID

        :param log_stream_id: The log_stream_id of this ListChartsRequest.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def offset(self):
        """Gets the offset of this ListChartsRequest.

        查询游标，初始传入0，后续从上一次的返回值中获取

        :return: The offset of this ListChartsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListChartsRequest.

        查询游标，初始传入0，后续从上一次的返回值中获取

        :param offset: The offset of this ListChartsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListChartsRequest.

        每页数据量，最大值为100

        :return: The limit of this ListChartsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListChartsRequest.

        每页数据量，最大值为100

        :param limit: The limit of this ListChartsRequest.
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
        if not isinstance(other, ListChartsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
