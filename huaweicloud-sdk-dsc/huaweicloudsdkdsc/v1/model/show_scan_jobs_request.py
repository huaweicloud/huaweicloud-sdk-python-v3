# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowScanJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'content': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'content': 'content',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, offset=None, limit=None, content=None, start_time=None, end_time=None):
        """ShowScanJobsRequest

        The model defined in huaweicloud sdk

        :param offset: 页码
        :type offset: int
        :param limit: 分页大小
        :type limit: int
        :param content: 内容
        :type content: str
        :param start_time: 预留，待启用
        :type start_time: str
        :param end_time: 预留，待启用
        :type end_time: str
        """
        
        

        self._offset = None
        self._limit = None
        self._content = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if content is not None:
            self.content = content
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this ShowScanJobsRequest.

        页码

        :return: The offset of this ShowScanJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowScanJobsRequest.

        页码

        :param offset: The offset of this ShowScanJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowScanJobsRequest.

        分页大小

        :return: The limit of this ShowScanJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowScanJobsRequest.

        分页大小

        :param limit: The limit of this ShowScanJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def content(self):
        """Gets the content of this ShowScanJobsRequest.

        内容

        :return: The content of this ShowScanJobsRequest.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ShowScanJobsRequest.

        内容

        :param content: The content of this ShowScanJobsRequest.
        :type content: str
        """
        self._content = content

    @property
    def start_time(self):
        """Gets the start_time of this ShowScanJobsRequest.

        预留，待启用

        :return: The start_time of this ShowScanJobsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowScanJobsRequest.

        预留，待启用

        :param start_time: The start_time of this ShowScanJobsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowScanJobsRequest.

        预留，待启用

        :return: The end_time of this ShowScanJobsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowScanJobsRequest.

        预留，待启用

        :param end_time: The end_time of this ShowScanJobsRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowScanJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
