# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'start_app_name': 'str',
        'stream_name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'start_app_name': 'start_app_name',
        'stream_name': 'stream_name'
    }

    def __init__(self, limit=None, start_app_name=None, stream_name=None):
        """ListAppRequest

        The model defined in huaweicloud sdk

        :param limit: 单次请求返回APP列表的最大数量。
        :type limit: int
        :param start_app_name: 从该app名称开始返回app列表，返回的app列表不包括此app名称。
        :type start_app_name: str
        :param stream_name: 返回该通道下的app列表。
        :type stream_name: str
        """
        
        

        self._limit = None
        self._start_app_name = None
        self._stream_name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if start_app_name is not None:
            self.start_app_name = start_app_name
        if stream_name is not None:
            self.stream_name = stream_name

    @property
    def limit(self):
        """Gets the limit of this ListAppRequest.

        单次请求返回APP列表的最大数量。

        :return: The limit of this ListAppRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppRequest.

        单次请求返回APP列表的最大数量。

        :param limit: The limit of this ListAppRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_app_name(self):
        """Gets the start_app_name of this ListAppRequest.

        从该app名称开始返回app列表，返回的app列表不包括此app名称。

        :return: The start_app_name of this ListAppRequest.
        :rtype: str
        """
        return self._start_app_name

    @start_app_name.setter
    def start_app_name(self, start_app_name):
        """Sets the start_app_name of this ListAppRequest.

        从该app名称开始返回app列表，返回的app列表不包括此app名称。

        :param start_app_name: The start_app_name of this ListAppRequest.
        :type start_app_name: str
        """
        self._start_app_name = start_app_name

    @property
    def stream_name(self):
        """Gets the stream_name of this ListAppRequest.

        返回该通道下的app列表。

        :return: The stream_name of this ListAppRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this ListAppRequest.

        返回该通道下的app列表。

        :param stream_name: The stream_name of this ListAppRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

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
        if not isinstance(other, ListAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
