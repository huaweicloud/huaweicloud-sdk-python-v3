# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpenApiCalledRecordsRequest:

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
        'called_url': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'called_url': 'called_url',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'marker': 'marker'
    }

    def __init__(self, limit=None, called_url=None, start_time=None, end_time=None, marker=None):
        """ShowOpenApiCalledRecordsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页大小，默认1000，最大2000。
        :type limit: int
        :param called_url: 需要查询调用记录的URL，例如：/v1/{project_id}/sdg/database/watermark/embed。
        :type called_url: str
        :param start_time: 开始时间（Unix timestamp），单位：毫秒，例如：0
        :type start_time: int
        :param end_time: 结束时间（Unix timestamp），单位：毫秒，例如：1638515803572
        :type end_time: int
        :param marker: 指定一个标识符。获取第一页时不用赋值，获取下一页时取上页查询结果的返回值。
        :type marker: str
        """
        
        

        self._limit = None
        self._called_url = None
        self._start_time = None
        self._end_time = None
        self._marker = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if called_url is not None:
            self.called_url = called_url
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if marker is not None:
            self.marker = marker

    @property
    def limit(self):
        """Gets the limit of this ShowOpenApiCalledRecordsRequest.

        分页大小，默认1000，最大2000。

        :return: The limit of this ShowOpenApiCalledRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowOpenApiCalledRecordsRequest.

        分页大小，默认1000，最大2000。

        :param limit: The limit of this ShowOpenApiCalledRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def called_url(self):
        """Gets the called_url of this ShowOpenApiCalledRecordsRequest.

        需要查询调用记录的URL，例如：/v1/{project_id}/sdg/database/watermark/embed。

        :return: The called_url of this ShowOpenApiCalledRecordsRequest.
        :rtype: str
        """
        return self._called_url

    @called_url.setter
    def called_url(self, called_url):
        """Sets the called_url of this ShowOpenApiCalledRecordsRequest.

        需要查询调用记录的URL，例如：/v1/{project_id}/sdg/database/watermark/embed。

        :param called_url: The called_url of this ShowOpenApiCalledRecordsRequest.
        :type called_url: str
        """
        self._called_url = called_url

    @property
    def start_time(self):
        """Gets the start_time of this ShowOpenApiCalledRecordsRequest.

        开始时间（Unix timestamp），单位：毫秒，例如：0

        :return: The start_time of this ShowOpenApiCalledRecordsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowOpenApiCalledRecordsRequest.

        开始时间（Unix timestamp），单位：毫秒，例如：0

        :param start_time: The start_time of this ShowOpenApiCalledRecordsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowOpenApiCalledRecordsRequest.

        结束时间（Unix timestamp），单位：毫秒，例如：1638515803572

        :return: The end_time of this ShowOpenApiCalledRecordsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowOpenApiCalledRecordsRequest.

        结束时间（Unix timestamp），单位：毫秒，例如：1638515803572

        :param end_time: The end_time of this ShowOpenApiCalledRecordsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def marker(self):
        """Gets the marker of this ShowOpenApiCalledRecordsRequest.

        指定一个标识符。获取第一页时不用赋值，获取下一页时取上页查询结果的返回值。

        :return: The marker of this ShowOpenApiCalledRecordsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ShowOpenApiCalledRecordsRequest.

        指定一个标识符。获取第一页时不用赋值，获取下一页时取上页查询结果的返回值。

        :param marker: The marker of this ShowOpenApiCalledRecordsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ShowOpenApiCalledRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
